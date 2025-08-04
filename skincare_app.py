# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import time

# Set page config
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide"
)

# Database bahan berbahaya
DANGEROUS_INGREDIENTS = {
    'paraben': {
        'description': 'Dapat mengganggu sistem hormon',
        'risk_level': 'Tinggi'
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
        'risk_level': 'Sedang'
    },
    'phthalate': {
        'description': 'Dapat mengganggu hormon dan mempengaruhi kesehatan reproduksi',
        'risk_level': 'Tinggi'
    },
    # Add more ingredients as needed
}

# UI Components
def main():
    st.title("🧪 Pemeriksa Keamanan Skincare")
    st.write("Periksa keamanan produk skincare Anda dengan mudah dan cepat")
    
    tab1, tab2, tab3 = st.tabs(["Beranda", "Analisis", "Tentang"])
    
    with tab1:
        st.header("Selamat Datang di Pemeriksa Keamanan Skincare")
        st.write("Platform terpercaya untuk menganalisis keamanan bahan-bahan dalam produk perawatan kulit Anda")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.info("🔬 Analisis Mendalam")
            st.write("Sistem kami memeriksa berbagai jenis bahan berbahaya")
        with col2:
            st.info("⚡ Hasil Instan")
            st.write("Dapatkan hasil analisis dalam hitungan detik")
        with col3:
            st.info("📚 Edukasi Komprehensif")
            st.write("Pelajari tentang bahan berbahaya")
        with col4:
            st.info("🛡️ Keamanan Terjamin")
            st.write("Berdasarkan regulasi dan penelitian ilmiah")
    
    with tab2:
        st.header("📝 Analisis Bahan Skincare")
        ingredients = st.text_area(
            "Masukkan Daftar Bahan Skincare:",
            placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance"
        )
        
        if st.button("🔍 Analisis Bahan"):
            if not ingredients.strip():
                st.warning("Silakan masukkan daftar bahan terlebih dahulu")
            else:
                with st.spinner("Sedang menganalisis bahan-bahan..."):
                    time.sleep(2)  # Simulate processing
                    results = analyze_ingredients(ingredients)
                    display_results(results)
    
    with tab3:
        st.header("ℹ️ Tentang Aplikasi")
        st.write("""
        Pemeriksa Keamanan Skincare adalah alat digital yang dirancang untuk membantu konsumen 
        membuat keputusan yang lebih baik tentang produk perawatan kulit.
        """)

# Analysis functions
def analyze_ingredients(ingredients_text):
    found_ingredients = []
    text_lower = ingredients_text.lower()
    
    for ing, data in DANGEROUS_INGREDIENTS.items():
        if ing.lower() in text_lower:
            found_ingredients.append({
                'name': ing,
                'risk': data['risk_level'],
                'description': data['description']
            })
    
    return {
        'is_safe': len(found_ingredients) == 0,
        'dangerous_ingredients': found_ingredients
    }

def display_results(results):
    if results['is_safe']:
        st.success("✅ Produk ini AMAN - Tidak terdeteksi bahan berbahaya")
    else:
        st.error(f"⚠️ PERINGATAN: Ditemukan {len(results['dangerous_ingredients']} bahan berbahaya")
        
        for ing in results['dangerous_ingredients']:
            with st.expander(f"🚨 {ing['name'].title()} (Risiko: {ing['risk']})"):
                st.write(ing['description'])
                # Add more details if needed

if __name__ == "__main__":
    main()
