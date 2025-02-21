import streamlit as st
import os
from dataclasses import dataclass
from typing import Literal
from langchain_community.callbacks.manager import get_openai_callback
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.llms.openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
import streamlit.components.v1 as components
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Kelas untuk melacak pesan chat
@dataclass
class Message:
    origin: Literal["human", "ai"]
    message: str

# Fungsi untuk memuat CSS kustom
def load_css():
    with open("static/styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Fungsi untuk membuat objek MongoDBAtlasVectorSearch
def create_vector_search():
    mongo_uri = os.getenv("MONGO_URI")
    vector_search = MongoDBAtlasVectorSearch.from_connection_string(
        mongo_uri,
        "vectorstores.medibot",
        OpenAIEmbeddings(model='text-embedding-3-small', disallowed_special=())
    )
    return vector_search

# Fungsi untuk menginisialisasi state sesi
def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "token_count" not in st.session_state:
        st.session_state.token_count = 0
    if "limit_reached" not in st.session_state:
        st.session_state.limit_reached = False
    if "conversation" not in st.session_state:
        vector_search = create_vector_search()
        retriever = vector_search.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 1}
        )
        
        # RAG prompt
        prompt_template = """
        system : Anda adalah chatbot medis bernama Medibot yang bertugas untuk menjawab pertanyaan dari pasien hanya seputar medis. Jawablah pertanyaan dengan pasien ramah.
        Gunakan potongan konteks berikut untuk menjawab pertanyaan. Jika konteks yang diberikan tidak sesuai dengan pertanyaan, katakan bahwa Anda tidak memiliki pengetahuan tentang hal terebut.
        
        Context: {context}
        
        Human:{question}
        Medibot:"""
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(max_tokens=200),
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": PROMPT}
        )
        st.session_state.conversation = qa

# Fungsi callback untuk menangani pengiriman formulir
def on_click_callback():
    with get_openai_callback() as cb:
        human_prompt = st.session_state.human_prompt
        
        # Gabungkan semua pesan sebelumnya untuk membentuk histori percakapan
        history = "\n".join([msg.message for msg in st.session_state.history])
        full_prompt = f"{history}\n{human_prompt}"
        
        response = st.session_state.conversation({"query": full_prompt})
        st.session_state.history.extend([
            Message("human", human_prompt),
            Message("ai", response["result"])
        ])
        st.session_state.token_count += cb.total_tokens
        
        # Reset input pesan setelah mengirim
        st.session_state.human_prompt = ""
        
        # Cek apakah token_count melebihi batas
        if st.session_state.token_count >= 1500:
            st.session_state.limit_reached = True

# Fungsi utama untuk menjalankan aplikasi Streamlit
def app():
    load_css()
    initialize_session_state()
    
    # Desain tampilan percakapan
    st.title("Chatbot Kesehatan MediBot 🤖")
    chat_placeholder = st.container()
    prompt_placeholder = st.form("chat-form")
    credit_card_placeholder = st.empty()
    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
    <div class="chat-row {'row-reverse' if chat.origin == 'human' else ''}">
        <img class="chat-icon" src="app/static/{'user_icon.png' if chat.origin == 'human' else 'ai_icon.png'}" width=32 height=32>
        <div class="chat-bubble {'human-bubble' if chat.origin == 'human' else 'ai-bubble'}">
            &#8203;{chat.message}
        </div>
    </div>
            """
            st.markdown(div, unsafe_allow_html=True)
        
        st.markdown("\n" * 3)

    with prompt_placeholder:
        cols = st.columns((6, 1))
        cols[0].text_input("Chat", value="", label_visibility="collapsed", key="human_prompt", disabled=st.session_state.limit_reached)
        cols[1].form_submit_button("Submit", type="primary", on_click=on_click_callback, disabled=st.session_state.limit_reached)

    # Menampilkan jumlah token yang dipakai
    credit_card_placeholder.caption(f"""
    Used {st.session_state.token_count} tokens
    """)
    
    # Menampilkan pesan peringatan jika limit tercapai
    if st.session_state.limit_reached:
        st.warning("Mohon maaf jumlah penggunaan token anda telah mencapai limit sesi percakapan, refresh halaman untuk menggunakanya lagi.")
    
    # Menambahkan fungsi tombol enter pada keyboard untuk mengirim pesan
    components.html("""
    <script>
    const streamlitDoc = window.parent.document;
    const submitButton = Array.from(streamlitDoc.querySelectorAll('.stButton > button')).find(el => el.innerText === 'Submit');
    streamlitDoc.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') submitButton.click();
    });
    </script>
    """, height=0, width=0)
