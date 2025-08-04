# -*- coding: utf-8 -*-
# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time
from PIL import Image

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
    
    /* Header */
    .stApp header {
        background-color: white;
        box-shadow: 0 2px 15px rgba(0,0,0,0.08);
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
    
    /* Card fitur */
    .feature-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        border: none;
        height: 100%;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.1);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        color: #d35d6e;
        margin-bottom: 1rem;
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
    
    /* Hero section */
    .hero {
        background: linear-gradient(135deg, rgba(255,182,193,0.2) 0%, rgba(255,255,255,0.8) 100%);
        border-radius: 15px;
        padding: 3rem;
        margin-bottom: 3rem;
        text-align: center;
    }
    
    /* About section */
    .about-section {
        background-color: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    
    /* Analysis section */
    .analysis-section {
        background-color: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    /* Ingredient card */
    .ingredient-card {
        background-color: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        border-left: 4px solid #d35d6e;
    }
    
    .ingredient-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    
    .risk-high {
        background-color: #ffebee;
        color: #c62828;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .risk-medium {
        background-color: #fff8e1;
        color: #ff8f00;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
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
        st.success("""
        <div style="text-align:center; padding:2rem;">
            <h2 style="color:#2e7d32;">✅ Produk Ini Aman!</h2>
            <p style="font-size:1.1rem;">Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan</p>
            <p style="margin-top:1.5rem;">Tetap perhatikan reaksi kulit Anda terhadap produk baru dan selalu lakukan patch test sebelum penggunaan penuh.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"""
        <div style="text-align:center; padding:1rem 0 2rem;">
            <h2 style="color:#c62828;">⚠️ Ditemukan {len(results['dangerous_ingredients'])} Bahan Potensial Berbahaya</h2>
            <p style="font-size:1.1rem;">Berikut bahan-bahan yang perlu diperhatikan:</p>
        </div>
        """, unsafe_allow_html=True)
        
        for ing in results['dangerous_ingredients']:
            risk_class = "risk-high" if ing['risk'] == "Tinggi" else "risk-medium"
            st.markdown(f"""
            <div class="ingredient-card">
                <div class="ingredient-header">
                    <h3 style="margin:0; color:#d35d6e;">{ing['name'].title()}</h3>
                    <span class="{risk_class}">Risiko: {ing['risk']}</span>
                </div>
                <p><strong>Kategori:</strong> {ing['category']}</p>
                <p><strong>Deskripsi:</strong> {ing['description']}</p>
                <p><strong>Detail:</strong> {ing['details']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="margin-top:2rem; background-color:#fff9fa; padding:1.5rem; border-radius:12px;">
            <h3 style="color:#d35d6e; margin-top:0;">💡 Rekomendasi</h3>
            <p>Pertimbangkan untuk mencari produk dengan label:</p>
            <ul>
                <li><strong>Paraben-free</strong> - Bebas paraben</li>
                <li><strong>Sulfate-free</strong> - Bebas sulfate</li>
                <li><strong>Fragrance-free</strong> - Bebas wewangian sintetis</li>
                <li><strong>Hypoallergenic</strong> - Formulasi untuk kulit sensitif</li>
                <li><strong>Non-comedogenic</strong> - Tidak menyumbat pori</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_home():
    """Tampilan halaman beranda"""
    # Hero Section
    st.markdown("""
    <div class="hero">
        <h1 style="font-size:2.8rem;">🧪 Pemeriksa Keamanan Skincare</h1>
        <p style="font-size:1.2rem; color:var(--text-dark); max-width:800px; margin:0 auto 1.5rem;">
            Temukan kebenaran di balik bahan-bahan produk perawatan kulit Anda. Analisis instan berdasarkan penelitian ilmiah dan regulasi internasional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Mulai Analisis Sekarang", type="primary"):
        st.session_state.current_tab = "🔍 Analisis Bahan"
    
    # Features Section
    st.markdown("""
    <div class="main-container">
        <h2 style="text-align:center; margin-bottom:2rem;">Kenapa Memilih Pemeriksa Kami?</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
            <div class="feature-card">
                <div class="feature-icon">🔬</div>
                <h3>Analisis Mendalam</h3>
                <p>Sistem kami memeriksa berbagai jenis bahan berbahaya berdasarkan database terpercaya</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Hasil Instan</h3>
                <p>Dapatkan hasil analisis komprehensif dalam hitungan detik</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Edukasi Komprehensif</h3>
                <p>Pelajari tentang bahan berbahaya dan alternatif yang lebih aman</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🛡️</div>
                <h3>Keamanan Terjamin</h3>
                <p>Berdasarkan regulasi dan penelitian ilmiah terbaru</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("""
    <div class="main-container">
        <h2 style="text-align:center; margin-bottom:2rem;">Bagaimana Cara Kerjanya?</h2>

        st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="background-color: #d35d6e; color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">1</div>
                <div>
                    <h3 style="margin-top:0;">Masukkan Daftar Bahan</h3>
                    <p>Salin dan tempel daftar bahan (INGREDIENTS) dari produk skincare Anda</p>
                </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="background-color: #d35d6e; color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">2</div>
                <div>
                    <h3 style="margin-top:0;">Proses Analisis</h3>
                    <p>Sistem kami akan memindai bahan-bahan berbahaya dalam database kami</p>
                </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="background-color: #d35d6e; color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">3</div>
                <div>
                    <h3 style="margin-top:0;">Dapatkan Hasil</h3>
                    <p>Lihat laporan lengkap tentang keamanan produk dan rekomendasi alternatif</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_analyzer():
    """Tampilan halaman analisis"""
    st.markdown("""
    <div class="analysis-section">
        <h1 style="text-align:center; margin-bottom:1.5rem;">🔍 Analisis Bahan Skincare</h1>
        <p style="text-align:center; color:var(--text-light); max-width:700px; margin:0 auto 2rem;">
            Masukkan daftar bahan produk skincare Anda di bawah ini untuk memeriksa potensi bahan berbahaya
        </p>
    """, unsafe_allow_html=True)
    
    ingredients = st.text_area(
        "**Daftar Bahan:**",
        placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate, Methylparaben",
        height=180,
        key="ingredients_input"
    )
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("**🔍 Analisis Bahan**", type="primary", use_container_width=True):
            if not ingredients.strip():
                st.warning("Silakan masukkan daftar bahan terlebih dahulu")
            else:
                with st.spinner("🔬 Menganalisis bahan-bahan..."):
                    time.sleep(1.5)  # Simulasi proses analisis
                    results = analyze_ingredients(ingredients)
                    display_results(results)
    
    st.markdown("</div>", unsafe_allow_html=True)

def show_about():
    """Tampilan halaman tentang kami"""
    st.markdown("""
    <div class="about-section">
        <h1 style="text-align:center;">ℹ️ Tentang Pemeriksa Keamanan Skincare</h1>
        <p style="text-align:center; color:var(--text-light); max-width:800px; margin:0 auto 2rem;">
            Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit
        </p>

        st.markdown("""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
            <div>
                <h2>🎯 Misi Kami</h2>
                <p>Kami berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit. Tujuan kami adalah memberdayakan konsumen untuk membuat pilihan yang tepat berdasarkan data dan penelitian ilmiah.</p>
                
                <h2 style="margin-top:2rem;">🔬 Metodologi</h2>
                <p>Database kami dikembangkan berdasarkan:</p>
                <ul>
                    <li>Regulasi Uni Eropa (EU Regulation No. 1223/2009)</li>
                    <li>Pedoman FDA tentang kosmetik</li>
                    <li>Penelitian ilmiah peer-reviewed</li>
                    <li>Rekomendasi dari dermatolog terkemuka</li>
                </ul>
            </div>
            <div>
                <h2>📚 Sumber Data</h2>
                <p>Informasi dalam aplikasi ini bersumber dari:</p>
                <ul>
                    <li>Environmental Working Group's Skin Deep Database</li>
                    <li>Cosmetic Ingredient Review (CIR)</li>
                    <li>Journal of the American Academy of Dermatology</li>
                    <li>International Journal of Toxicology</li>
                </ul>
            </div>
        </div>
          """, unsafe_allow_html=True)
          
        <div style="background-color: #fff9fa; border-radius: 12px; padding: 1.5rem; margin-top: 2rem;">
            <h2 style="color:#d35d6e; text-align:center;">💡 Tips Memilih Skincare Aman</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                <div style="background-color: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                    <h3 style="color:#d35d6e; margin-top:0;">Baca Label</h3>
                    <p>Selalu periksa daftar bahan sebelum membeli produk skincare</p>
                </div>
                <div style="background-color: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                    <h3 style="color:#d35d6e; margin-top:0;">Mulai dari Sederhana</h3>
                    <p>Produk dengan daftar bahan yang lebih pendek cenderung lebih aman</p>
                </div>
                <div style="background-color: white; padding: 1rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                    <h3 style="color:#d35d6e; margin-top:0;">Uji Sensitivitas</h3>
                    <p>Selalu lakukan patch test sebelum menggunakan produk baru</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Fungsi utama untuk tampilan Streamlit"""
    # Initialize session state for tab control
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "🏠 Beranda"
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "ℹ️ Tentang Kami"])
    
    # Display the appropriate tab based on session state
    if st.session_state.current_tab == "🏠 Beranda":
        with tab1:
            show_home()
    elif st.session_state.current_tab == "🔍 Analisis Bahan":
        with tab2:
            show_analyzer()
    elif st.session_state.current_tab == "ℹ️ Tentang Kami":
        with tab3:
            show_about()
    else:
        with tab1:
            show_home()
    
    # Always show all tabs content for navigation
    with tab1:
        if st.session_state.current_tab != "🏠 Beranda":
            show_home()
    with tab2:
        if st.session_state.current_tab != "🔍 Analisis Bahan":
            show_analyzer()
    with tab3:
        if st.session_state.current_tab != "ℹ️ Tentang Kami":
            show_about()
    
    # Footer
    st.markdown("""
    <footer>
        <p>© 2023 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit yang lebih sehat</p>
        <p style="font-size:0.8rem;">Disclaimer: Aplikasi ini hanya untuk tujuan informasi dan tidak menggantikan nasihat profesional.</p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
