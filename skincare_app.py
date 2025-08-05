# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS dengan desain aesthetic
st.markdown("""
<style>
    /* Font dan warna dasar */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }
    
    /* Warna tema soft pink */
    :root {
        --primary-color: #ffb6c1;
        --primary-dark: #ff8fab;
        --primary-light: #ffdfe5;
        --secondary-color: #f8f9fa;
        --text-dark: #4a4a4a;
        --text-light: #888888;
    }
    
    /* Background dengan overlay */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), 
                    url('https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    /* Main container */
    .main-container {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        padding: 2rem;
        margin-bottom: 2rem;
    }
    
    /* Judul utama */
    h1 {
        color: #d35d6e !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Subjudul */
    h2 {
        color: #d35d6e !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 500 !important;
        border-bottom: 2px solid var(--primary-light);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem !important;
    }
    
    h3 {
        font-family: 'Playfair Display', serif !important;
        color: var(--text-dark) !important;
        font-weight: 500 !important;
    }
    
    /* Tombol */
    .stButton button {
        background-color: var(--primary-color) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.7rem 2rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .stButton button:hover {
        background-color: var(--primary-dark) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    
    /* Text area */
    .stTextArea textarea {
        border-radius: 8px !important;
        border: 1px solid var(--primary-light) !important;
        padding: 1rem !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    
    /* Tab */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.8rem 1.5rem !important;
        background-color: var(--primary-light) !important;
        border-radius: 8px !important;
        margin-right: 0 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color) !important;
        font-weight: 600 !important;
        color: white !important;
    }
    
    /* Hasil analisis */
    .stAlert {
        border-radius: 12px !important;
        padding: 1.5rem !important;
    }
    
    /* Footer */
    footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        color: var(--text-light);
        font-size: 0.9rem;
        border-top: 1px solid #f0f0f0;
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
        'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik dan produk perawatan pribadi. Studi menunjukkan paraben dapat meniru estrogen dan berpotensi mengganggu sistem hormon tubuh. Regulasi Uni Eropa telah membatasi penggunaan beberapa jenis paraben dalam produk kosmetik.'
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
        'category': 'Iritan',
        'risk_level': 'Sedang',
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate'],
        'details': 'Sulfate adalah surfaktan yang digunakan untuk membuat busa dalam produk pembersih. Bahan ini dapat menghilangkan minyak alami kulit, menyebabkan kekeringan dan iritasi, terutama pada kulit sensitif. Alternatif yang lebih lembut termasuk decyl glucoside atau coco-glucoside.'
    },
    'phthalate': {
        'description': 'Dikaitkan dengan gangguan hormon dan reproduksi',
        'category': 'Pengganggu Endokrin',
        'risk_level': 'Tinggi',
        'common_names': ['dibutyl phthalate', 'dbp', 'diethyl phthalate'],
        'details': 'Phthalates sering digunakan sebagai pelarut dan pengikat wewangian. Bahan ini telah dikaitkan dengan masalah reproduksi dan perkembangan. Banyak negara telah melarang penggunaan phthalates tertentu dalam produk kosmetik dan mainan anak-anak.'
    },
    'formaldehyde': {
        'description': 'Karsinogen yang diketahui dan iritan kuat',
        'category': 'Karsinogen',
        'risk_level': 'Tinggi',
        'common_names': ['formalin', 'methanal', 'methyl aldehyde'],
        'details': 'Formaldehyde dan pelepas formaldehyde digunakan sebagai pengawet. Zat ini diklasifikasikan sebagai karsinogen manusia dan dapat menyebabkan iritasi kulit, mata, dan saluran pernapasan. Hindari produk yang mengandung DMDM hydantoin, imidazolidinyl urea, atau quaternium-15.'
    },
    'fragrance': {
        'description': 'Dapat menyebabkan iritasi dan reaksi alergi',
        'category': 'Alergen',
        'risk_level': 'Sedang',
        'common_names': ['parfum', 'aroma', 'perfume'],
        'details': 'Istilah "fragrance" atau "parfum" dapat mencakup ratusan bahan kimia berbeda yang tidak diungkapkan. Banyak di antaranya dapat menyebabkan iritasi kulit, alergi, atau gangguan hormon. Pilih produk yang bebas wewangian atau menggunakan minyak esensial alami sebagai alternatif.'
    }
}

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
        st.success("✅ **Produk Ini Aman!**\n\nTidak terdeteksi bahan berbahaya dalam daftar yang diberikan. Tetap perhatikan reaksi kulit Anda terhadap produk baru dan selalu lakukan patch test sebelum penggunaan penuh.")
    else:
        st.error(f"⚠️ **Ditemukan {len(results['dangerous_ingredients'])} Bahan Potensial Berbahaya**")
        
        for ing in results['dangerous_ingredients']:
            with st.expander(f"🚨 {ing['name'].title()} - Risiko: {ing['risk']}"):
                st.write(f"**Kategori:** {ing['category']}")
                st.write(f"**Deskripsi:** {ing['description']}")
                st.write(f"**Detail:** {ing['details']}")
        
        st.info("""
        **💡 Rekomendasi:**
        
        Pertimbangkan untuk mencari produk dengan label:
        - **Paraben-free** - Bebas paraben
        - **Sulfate-free** - Bebas sulfate  
        - **Fragrance-free** - Bebas wewangian sintetis
        - **Hypoallergenic** - Formulasi untuk kulit sensitif
        - **Non-comedogenic** - Tidak menyumbat pori
        """)

# Main App
def main():
    # Header
    st.title("🧪 Pemeriksa Keamanan Skincare")
    st.markdown("### Temukan kebenaran di balik bahan-bahan produk perawatan kulit Anda")
    
    # Navigation
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "ℹ️ Tentang Kami"])
    
    with tab1:
        st.markdown("---")
        
        # Hero Section
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(255,182,193,0.2) 0%, rgba(255,255,255,0.8) 100%); border-radius: 15px; margin-bottom: 2rem;">
            <h2>🌟 Analisis Instan Berdasarkan Penelitian Ilmiah</h2>
            <p style="font-size: 1.1rem;">Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #d35d6e;">🔬</div>
                <h4>Analisis Mendalam</h4>
                <p>Sistem memeriksa berbagai jenis bahan berbahaya berdasarkan database terpercaya</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #d35d6e;">⚡</div>
                <h4>Hasil Instan</h4>
                <p>Dapatkan hasil analisis komprehensif dalam hitungan detik</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #d35d6e;">📚</div>
                <h4>Edukasi Komprehensif</h4>
                <p>Pelajari tentang bahan berbahaya dan alternatif yang lebih aman</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #d35d6e;">🛡️</div>
                <h4>Keamanan Terjamin</h4>
                <p>Berdasarkan regulasi dan penelitian ilmiah terbaru</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # How it works
        st.subheader("🔄 Bagaimana Cara Kerjanya?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **1️⃣ Masukkan Daftar Bahan**
            
            Salin dan tempel daftar bahan (INGREDIENTS) dari produk skincare Anda
            """)
        
        with col2:
            st.markdown("""
            **2️⃣ Proses Analisis**
            
            Sistem akan memindai bahan-bahan berbahaya dalam database kami
            """)
        
        with col3:
            st.markdown("""
            **3️⃣ Dapatkan Hasil**
            
            Lihat laporan lengkap tentang keamanan produk dan rekomendasi alternatif
            """)
    
    with tab2:
        st.markdown("---")
        st.subheader("🔍 Analisis Bahan Skincare")
        st.write("Masukkan daftar bahan produk skincare Anda di bawah ini untuk memeriksa potensi bahan berbahaya")
        
        # Input form
        ingredients = st.text_area(
            "**Daftar Bahan (INGREDIENTS):**",
            placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate, Methylparaben",
            height=150,
            help="Salin dan tempel daftar bahan dari kemasan produk atau website resmi"
        )
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("🔍 **Analisis Bahan**", type="primary", use_container_width=True):
                if not ingredients.strip():
                    st.warning("⚠️ Silakan masukkan daftar bahan terlebih dahulu")
                else:
                    with st.spinner("🔬 Menganalisis bahan-bahan..."):
                        time.sleep(1.5)  # Simulasi proses analisis
                        results = analyze_ingredients(ingredients)
                        st.markdown("---")
                        display_results(results)
    
    with tab3:
        st.markdown("---")
        st.subheader("ℹ️ Tentang Pemeriksa Keamanan Skincare")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🎯 Misi Kami**
            
            Kami berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit. Tujuan kami adalah memberdayakan konsumen untuk membuat pilihan yang tepat berdasarkan data dan penelitian ilmiah.
            
            **🔬 Metodologi**
            
            Database kami dikembangkan berdasarkan:
            - Regulasi Uni Eropa (EU Regulation No. 1223/2009)
            - Pedoman FDA tentang kosmetik
            - Penelitian ilmiah peer-reviewed
            - Rekomendasi dari dermatolog terkemuka
            """)
        
        with col2:
            st.markdown("""
            **📚 Sumber Data**
            
            Informasi dalam aplikasi ini bersumber dari:
            - Environmental Working Group's Skin Deep Database
            - Cosmetic Ingredient Review (CIR)
            - Journal of the American Academy of Dermatology
            - International Journal of Toxicology
            
            **💡 Tips Memilih Skincare Aman**
            
            - **Baca Label:** Selalu periksa daftar bahan sebelum membeli
            - **Mulai Sederhana:** Produk dengan daftar bahan pendek cenderung lebih aman
            - **Uji Sensitivitas:** Selalu lakukan patch test sebelum penggunaan penuh
            """)
        
        st.info("""
        **⚠️ Disclaimer:** Aplikasi ini hanya untuk tujuan informasi dan tidak menggantikan nasihat profesional dari dermatolog atau ahli kesehatan kulit.
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #888888; font-size: 0.9rem; padding: 1rem 0;">
        <p>© 2023 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit yang lebih sehat</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
