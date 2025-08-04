# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk meniru Vorrath Woodworks
st.markdown("""
<style>
    /* Font dan warna dasar */
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Lato', sans-serif;
        color: #333333;
    }
    
    /* Header */
    .stApp header {
        background-color: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Main container */
    .stApp {
        background-color: #f9f9f9;
    }
    
    /* Judul utama */
    h1 {
        color: #222222 !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Subjudul */
    h2 {
        color: #444444 !important;
        font-weight: 400 !important;
        border-bottom: 1px solid #eeeeee;
        padding-bottom: 0.3rem;
    }
    
    /* Tombol */
    .stButton button {
        background-color: #4a6fa5 !important;
        color: white !important;
        border-radius: 4px !important;
        border: none !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 400 !important;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #3a5a8f !important;
        transform: translateY(-1px);
    }
    
    /* Text area */
    .stTextArea textarea {
        border-radius: 4px !important;
        border: 1px solid #dddddd !important;
    }
    
    /* Tab */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1rem !important;
        background-color: #f0f0f0 !important;
        border-radius: 4px 4px 0 0 !important;
        margin-right: 0 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: white !important;
        font-weight: bold !important;
    }
    
    /* Card fitur */
    .stColumn {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .stColumn:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Hasil analisis */
    .stAlert {
        border-radius: 8px !important;
    }
    
    /* Footer */
    footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        color: #777777;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Database bahan berbahaya
DANGEROUS_INGREDIENTS = {
    'paraben': {
        'description': 'Dapat mengganggu sistem hormon (Regulasi EU No. 1223/2009)',
        'category': 'Pengganggu Endokrin',
        'risk_level': 'Tinggi',
        'common_names': ['methylparaben', 'propylparaben', 'butylparaben'],
        'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik...'
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
        'category': 'Iritan',
        'risk_level': 'Sedang',
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate'],
        'details': 'Sulfate adalah surfaktan yang digunakan untuk membuat busa...'
    },
    # Tambahkan bahan lainnya sesuai kebutuhan
}

def main():
    """Fungsi utama untuk tampilan Streamlit"""
    # Header dengan logo dan navigasi sederhana
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://via.placeholder.com/150x50?text=Skincare+Checker", width=150)
    with col2:
        st.markdown("<div style='text-align: right; padding-top: 1rem;'>"
                    "<a href='#beranda' style='margin: 0 1rem; color: #333; text-decoration: none;'>Beranda</a>"
                    "<a href='#analisis' style='margin: 0 1rem; color: #333; text-decoration: none;'>Analisis</a>"
                    "<a href='#tentang' style='margin: 0 1rem; color: #333; text-decoration: none;'>Tentang</a>"
                    "</div>", unsafe_allow_html=True)
    
    st.title("🧪 Pemeriksa Keamanan Skincare")
    st.markdown("Periksa keamanan produk skincare Anda dengan mudah dan cepat")
    
    # Buat tab navigasi
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Analisis", "ℹ️ Tentang"])
    
    with tab1:
        show_home()
    with tab2:
        show_analyzer()
    with tab3:
        show_about()
    
    # Footer
    st.markdown("---")
    st.markdown("<footer>"
                "© 2023 Pemeriksa Keamanan Skincare. All rights reserved.<br>"
                "Dibuat dengan ❤️ untuk kulit yang lebih sehat"
                "</footer>", unsafe_allow_html=True)

def show_home():
    """Tampilan halaman beranda"""
    st.header("Selamat Datang di Pemeriksa Keamanan Skincare")
    st.markdown("Platform terpercaya untuk menganalisis keamanan bahan-bahan dalam produk perawatan kulit Anda")
    
    # Hero section
    st.image("https://via.placeholder.com/1200x400?text=Periksa+Keamanan+Skincare+Anda", use_column_width=True)
    
    cols = st.columns(4)
    features = [
        ("🔬", "Analisis Mendalam", "Sistem kami memeriksa berbagai jenis bahan berbahaya"),
        ("⚡", "Hasil Instan", "Dapatkan hasil analisis dalam hitungan detik"),
        ("📚", "Edukasi Komprehensif", "Pelajari tentang bahan berbahaya"),
        ("🛡️", "Keamanan Terjamin", "Berdasarkan regulasi dan penelitian ilmiah")
    ]
    
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"<div style='text-align: center;'>"
                        f"<span style='font-size: 2rem;'>{icon}</span>"
                        f"<h3>{title}</h3>"
                        f"<p>{desc}</p>"
                        f"</div>", unsafe_allow_html=True)
    
    # Testimoni
    st.markdown("---")
    st.subheader("Apa Kata Pengguna Kami")
    testimonials = st.columns(3)
    testimoni_data = [
        ("Sangat membantu!", "Sarah - Jakarta"),
        ("Aplikasi wajib untuk pecinta skincare!", "Dani - Bandung"),
        ("Interface yang simpel dan mudah digunakan", "Rina - Surabaya")
    ]
    
    for col, (text, author) in zip(testimonials, testimoni_data):
        with col:
            st.markdown(f"<div style='background: white; padding: 1.5rem; border-radius: 8px;'>"
                        f"<p style='font-style: italic;'>{text}</p>"
                        f"<p style='text-align: right; font-weight: bold;'>{author}</p>"
                        f"</div>", unsafe_allow_html=True)

def show_analyzer():
    """Tampilan halaman analisis"""
    st.header("📝 Analisis Bahan Skincare")
    st.markdown("Masukkan daftar bahan skincare Anda di bawah ini untuk memeriksa keamanannya")
    
    ingredients = st.text_area(
        "Masukkan Daftar Bahan Skincare:",
        placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate",
        height=150
    )
    
    if st.button("🔍 Analisis Bahan", type="primary"):
        if not ingredients.strip():
            st.warning("Silakan masukkan daftar bahan terlebih dahulu")
        else:
            with st.spinner("Sedang menganalisis bahan-bahan..."):
                time.sleep(1)  # Simulasi proses analisis
                results = analyze_ingredients(ingredients)
                display_results(results)

def show_about():
    """Tampilan halaman tentang"""
    st.header("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Pemeriksa Keamanan Skincare adalah alat digital yang dirancang untuk membantu konsumen 
    membuat keputusan yang lebih baik tentang produk perawatan kulit.
    """)
    
    # Tim
    st.subheader("Tim Kami")
    team_cols = st.columns(3)
    team_members = [
        ("Dr. Amanda", "Ahli Dermatologi"),
        ("Rizky", "Pengembang Aplikasi"),
        ("Dewi", "Spesialis Regulasi")
    ]
    
    for col, (name, role) in zip(team_cols, team_members):
        with col:
            st.image(f"https://via.placeholder.com/150?text={name.split()[0]}", width=100)
            st.markdown(f"<div style='text-align: center;'>"
                        f"<h4>{name}</h4>"
                        f"<p>{role}</p>"
                        f"</div>", unsafe_allow_html=True)
    
    with st.expander("📌 Informasi Lengkap"):
        st.markdown("""
        ### 🎯 Tujuan Aplikasi
        Kami berkomitmen untuk meningkatkan kesadaran konsumen tentang bahan-bahan dalam produk skincare.
        
        ### 🔬 Metodologi
        Database kami mencakup berbagai kategori bahan berbahaya berdasarkan:
        - Regulasi Uni Eropa (EU Regulation No. 1223/2009)
        - Penelitian ilmiah terpublikasi
        - Panduan organisasi kesehatan internasional
        """)

def analyze_ingredients(ingredients_text):
    """Fungsi untuk menganalisis bahan-bahan skincare"""
    found_ingredients = []
    text_lower = ingredients_text.lower()
    
    for ing, data in DANGEROUS_INGREDIENTS.items():
        # Cek nama utama dan nama alternatif
        all_names = [ing] + data['common_names']
        if any(name in text_lower for name in all_names):
            found_ingredients.append({
                'name': ing,
                'risk': data['risk_level'],
                'category': data['category'],
                'description': data['description'],
                'details': data['details']
            })
    
    return {
        'is_safe': len(found_ingredients) == 0,
        'dangerous_ingredients': found_ingredients
    }

def display_results(results):
    """Fungsi untuk menampilkan hasil analisis"""
    if results['is_safe']:
        st.success("""
        ## ✅ Produk ini AMAN 
        Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan
        """)
    else:
        st.error(f"""
        ## ⚠️ PERINGATAN: Ditemukan {len(results['dangerous_ingredients'])} bahan berbahaya
        """)
        
        for ing in results['dangerous_ingredients']:
            with st.expander(f"🚨 {ing['name'].title()} (Risiko: {ing['risk']})"):
                st.markdown(f"""
                **Kategori:** {ing['category']}  
                **Deskripsi:** {ing['description']}  
                
                **Detail:**  
                {ing['details']}
                """)

if __name__ == "__main__":
    main()
