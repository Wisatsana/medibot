import streamlit as st

def app():
    # Header
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Tentang Kami</h1>", unsafe_allow_html=True)

    # Tentang Pengembang
    st.markdown("## Tentang Pengembang")
    left, right = st.columns([0.80, 0.20])
    left.markdown("""
    <div style="text-align: justify;">
    Saya, Wisatsana Roychan Saefurrochman adalah mahasiswa prodi Statistika Terapan dan Komputasi di Universitas Negeri Semarang. 
    Aplikasi ini merupakan proyek tugas akhir saya yang bertujuan memberikan layanan konsultasi kesehatan yang mudah diakses dan terpercaya melalui teknologi chatbot. 
    Tujuan saya adalah untuk mempermudah masyarakat dalam mendapatkan informasi dan saran medis yang akurat tanpa harus keluar rumah. 
    Aplikasi dibuat dengan mengandalkan referensi yang telah saya kumpulkan dan juga dengan bimbingan dari dosen, saya berharap aplikasi ini dapat bermanfaat bagi penggunanya.
    </div>
    """, unsafe_allow_html=True)
    right.image("static/Fotoku.jpg", use_column_width=True) 

    # Kontak Informasi
    st.markdown("## Kontak Saya")
    st.markdown("""
    Jika Anda memiliki pertanyaan, saran, atau ingin berdiskusi lebih lanjut tentang aplikasi ini, jangan ragu untuk menghubungi saya melalui:
    - Email: wisatsana.saefurrochman@gmail.com
    - Nomor Telepon: 089620291155

    Anda juga dapat mengikuti perkembangan proyek ini melalui media sosial:
    - [LinkedIn](https://www.linkedin.com/in/wisatsana-roychan-s-73b900272?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    - [Github](https://github.com/Wisatsana)
    - [Facebook](https://www.facebook.com/wisatsana.wisatsana.50)
    - [Twitter](https://twitter.com/WisatsanaS?t=53kTniGZkwqGaEEDztryzw&s=09)
    - [Instagram](https://www.instagram.com/wisatsanaroy?igsh=NnM3a2k4MGhpeWg0)
    """)

    # Footer
    st.markdown("""---""")