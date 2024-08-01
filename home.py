import streamlit as st

def app():
    # Header
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Konsultasi Kesehatan Cepat dan Mudah dengan MediBot</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Chatbot Kesehatan dengan Pengetahuan Medis Terkini</h3>", unsafe_allow_html=True)

    # Banner Image
    st.image("static/Consult_Ilustration.jpeg", use_column_width=True) 

    # Introduction Section
    st.markdown("## Selamat Datang di MediBot!")
    st.markdown('<div style="text-align: justify;">Aplikasi ini menggunakan teknologi chatbot yang didukung oleh OpenAI seperti ChatGPT dan basis pengetahuan yang disimpan dalam vector database Atlas MongoDB. Basis pengetahuan ini mencakup jurnal kesehatan yang dapat diperbarui setiap saat. Dengan metode Retrieval Augmented Generation (RAG), MediBot dapat memberikan informasi dan saran medis yang konsisten sesuai basis pengetahuan yang dimiliki.</div>', unsafe_allow_html=True)

    # How It Works Section
    st.markdown("## Kegunaan Medibot")
    st.markdown("""
    Dengan chatbot ini, Anda dapat:
    1. **Menyampaikan keluhan kesehatan Anda.**
    2. **Mendapatkan diagnosis awal berdasarkan pengetahuan medis terkini yang diambil dari database.**
    3. **Menerima saran pengobatan atau rujukan ke tenaga medis profesional jika diperlukan.**
    """)
    st.image("static/Alur.jpeg", use_column_width=True)

    # Features Section
    st.markdown("## Fitur Unggulan")
    st.markdown("""
    ### Pengetahuan Medis Terpercaya
    Chatbot kami dilengkapi dengan basis data pengetahuan medis yang bisa di cek [disini](https://drive.google.com/file/d/18Ksmk1rkpQ7pVhg9kSqNhawDU28cwjYT/view?usp=drive_link).

    ### Akses 24/7
    Dapatkan konsultasi kapan saja, bahkan di luar jam kerja.

    ### Privasi Terjamin
    Data dan percakapan Anda dijamin kerahasiaannya.
    """)
    st.image("static/Features.jpeg", use_column_width=True) 

    # Footer
    st.markdown("---")
