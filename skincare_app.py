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
    layout="wide"
)

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

def show_home():
    """Tampilan halaman beranda"""
    st.header("Selamat Datang di Pemeriksa Keamanan Skincare")
    st.markdown("Platform terpercaya untuk menganalisis keamanan bahan-bahan dalam produk perawatan kulit Anda")
    
    cols = st.columns(4)
    features = [
        ("🔬", "Analisis Mendalam", "Sistem kami memeriksa berbagai jenis bahan berbahaya"),
        ("⚡", "Hasil Instan", "Dapatkan hasil analisis dalam hitungan detik"),
        ("📚", "Edukasi Komprehensif", "Pelajari tentang bahan berbahaya"),
        ("🛡️", "Keamanan Terjamin", "Berdasarkan regulasi dan penelitian ilmiah")
    ]
    
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.subheader(f"{icon} {title}")
            st.markdown(desc)

def show_analyzer():
    """Tampilan halaman analisis"""
    st.header("📝 Analisis Bahan Skincare")
    
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
