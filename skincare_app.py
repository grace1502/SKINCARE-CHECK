# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="🧪 Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS dengan desain modern dan aesthetic
st.markdown("""
<style>
    /* Font dan warna dasar */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;700&display=swap');
    
    :root {
        --primary: #ff6b9d;
        --primary-light: #ffb3d1;
        --primary-dark: #d44d7d;
        --secondary: #9d4edd;
        --light: #f8f9fa;
        --dark: #212529;
        --danger: #dc3545;
        --success: #28a745;
        --warning: #ffc107;
    }
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: var(--dark);
        background-color: #fef6f9;
    }
    
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #fff5f9 0%, #fef0f5 100%);
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(157, 78, 221, 0.2);
    }
    
    /* Card styling */
    .feature-card {
        background: white;
        border-radius: 15px;
        padding: 1.8rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        height: 100%;
        text-align: center;
        border-top: 4px solid var(--primary);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    
    .feature-icon {
        font-size: 2.8rem;
        color: var(--primary);
        margin-bottom: 1.2rem;
    }
    
    /* Result cards */
    .safe-card {
        background: linear-gradient(135deg, #e6f7ee 0%, #c8f0d9 100%);
        border-left: 5px solid var(--success);
        color: #155724;
    }
    
    .danger-card {
        background: linear-gradient(135deg, #ffebee 0%, #ffd6dc 100%);
        border-left: 5px solid var(--danger);
        color: #721c24;
    }
    
    .ingredient-item {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.05);
        border-left: 4px solid var(--primary-dark);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(157, 78, 221, 0.4);
    }
    
    /* Text area styling */
    .stTextArea>div>div>textarea {
        border: 2px solid var(--primary-light);
        border-radius: 12px;
        padding: 1rem;
        font-size: 16px;
    }
    
    /* Tab styling */
    .stTabs [aria-selected="true"] {
        color: var(--primary) !important;
        font-weight: 600;
    }
    
    /* Risk level badges */
    .risk-high {
        background-color: #ffebee;
        color: var(--danger);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    
    .risk-medium {
        background-color: #fff8e1;
        color: #ff8f00;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    
    /* Footer styling */
    footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        color: #6c757d;
        border-top: 1px solid #dee2e6;
    }
    
    /* Section styling */
    .section {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
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
        st.markdown('''
        <div class="section safe-card">
            <h2 style="color: var(--success);">✅ Produk Aman</h2>
            <p>Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan.</p>
            <p><strong>Saran:</strong> Tetap lakukan patch test sebelum penggunaan pertama untuk memastikan tidak ada reaksi alergi.</p>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="section danger-card">
            <h2 style="color: var(--danger);">⚠️ Ditemukan {len(results['dangerous_ingredients'])} Bahan Berpotensi Berbahaya</h2>
            <p>Berikut bahan-bahan yang perlu diperhatikan dalam produk Anda:</p>
        </div>
        ''', unsafe_allow_html=True)
        
        for ing in results['dangerous_ingredients']:
            risk_class = "risk-high" if ing['risk'] == "Tinggi" else "risk-medium"
            st.markdown(f"""
            <div class="ingredient-item">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <h3 style="margin: 0; color: var(--primary-dark);">{ing['name'].title()}</h3>
                    <span class="{risk_class}">Risiko: {ing['risk']}</span>
                </div>
                <p><strong>Kategori:</strong> {ing['category']}</p>
                <p><strong>Penjelasan:</strong> {ing['description']}</p>
                <p><strong>Detail:</strong> {ing['details']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('''
        <div class="section">
            <h3 style="color: var(--primary);">💡 Rekomendasi Produk Aman</h3>
            <p>Pertimbangkan produk dengan kriteria berikut:</p>
            <ul>
                <li><strong>Hypoallergenic</strong> - Formulasi untuk kulit sensitif</li>
                <li><strong>Non-comedogenic</strong> - Tidak menyumbat pori</li>
                <li><strong>Fragrance-free</strong> - Tanpa wewangian sintetis</li>
                <li><strong>Dermatologist-tested</strong> - Diuji oleh ahli kulit</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)

def show_home():
    """Tampilan halaman beranda yang sudah diperbaiki"""
    # Hero Section dengan gradient dan padding yang tepat
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #FF6B9D 0%, #9D4EDD 100%);
        color: white;
        padding: 3rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(157, 78, 221, 0.2);
    ">
        <h1 style="font-size: 2.8rem; margin-bottom: 0.5rem;">🧪 Pemeriksa Keamanan Skincare</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">Analisis instan bahan skincare berdasarkan penelitian ilmiah dan regulasi internasional</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol utama dengan styling yang konsisten
    if st.button("Mulai Analisis Sekarang", type="primary"):
        st.session_state.current_tab = "🔍 Analisis Bahan"
    
    # Features Section dengan grid yang berfungsi
    st.markdown("""
    <div style="
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    ">
        <h2 style="text-align: center; color: #FF6B9D; margin-bottom: 1.5rem;">Kenapa Memilih Pemeriksa Kami?</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
            <div style="
                background: white;
                border-radius: 15px;
                padding: 1.8rem;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease;
                height: 100%;
                text-align: center;
                border-top: 4px solid #FF6B9D;
            ">
                <div style="font-size: 2.8rem; color: #FF6B9D; margin-bottom: 1.2rem;">🔬</div>
                <h3>Analisis Mendalam</h3>
                <p>Memeriksa berbagai jenis bahan berbahaya berdasarkan database terpercaya</p>
            </div>
            
            <div style="
                background: white;
                border-radius: 15px;
                padding: 1.8rem;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease;
                height: 100%;
                text-align: center;
                border-top: 4px solid #FF6B9D;
            ">
                <div style="font-size: 2.8rem; color: #FF6B9D; margin-bottom: 1.2rem;">⚡</div>
                <h3>Hasil Instan</h3>
                <p>Dapatkan hasil analisis komprehensif dalam hitungan detik</p>
            </div>
            
            <div style="
                background: white;
                border-radius: 15px;
                padding: 1.8rem;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease;
                height: 100%;
                text-align: center;
                border-top: 4px solid #FF6B9D;
            ">
                <div style="font-size: 2.8rem; color: #FF6B9D; margin-bottom: 1.2rem;">📚</div>
                <h3>Edukasi Lengkap</h3>
                <p>Pelajari tentang bahan berbahaya dan alternatif yang lebih aman</p>
            </div>
            
            <div style="
                background: white;
                border-radius: 15px;
                padding: 1.8rem;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease;
                height: 100%;
                text-align: center;
                border-top: 4px solid #FF6B9D;
            ">
                <div style="font-size: 2.8rem; color: #FF6B9D; margin-bottom: 1.2rem;">🛡️</div>
                <h3>Keamanan Terjamin</h3>
                <p>Berdasarkan regulasi dan penelitian ilmiah terbaru</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("""
    <div style="
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    ">
        <h2 style="text-align: center; color: #FF6B9D; margin-bottom: 1.5rem;">Bagaimana Cara Kerjanya?</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="
                    background: #FF6B9D;
                    color: white;
                    border-radius: 50%;
                    width: 36px;
                    height: 36px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                    font-weight: bold;
                ">1</div>
                <div>
                    <h3 style="margin-top: 0;">Masukkan Daftar Bahan</h3>
                    <p>Salin dan tempel daftar bahan (INGREDIENTS) dari produk skincare Anda</p>
                </div>
            </div>
            
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="
                    background: #FF6B9D;
                    color: white;
                    border-radius: 50%;
                    width: 36px;
                    height: 36px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                    font-weight: bold;
                ">2</div>
                <div>
                    <h3 style="margin-top: 0;">Proses Analisis</h3>
                    <p>Sistem kami akan memindai bahan-bahan berbahaya dalam database kami</p>
                </div>
            </div>
            
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="
                    background: #FF6B9D;
                    color: white;
                    border-radius: 50%;
                    width: 36px;
                    height: 36px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                    font-weight: bold;
                ">3</div>
                <div>
                    <h3 style="margin-top: 0;">Dapatkan Hasil</h3>
                    <p>Lihat laporan lengkap tentang keamanan produk dan rekomendasi alternatif</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_analyzer():
    """Tampilan halaman analisis"""
    st.markdown("""
    <div class="section">
        <h1 style="text-align: center; color: var(--primary); margin-bottom: 1rem;">🔍 Analisis Bahan Skincare</h1>
        <p style="text-align: center; color: #6c757d; max-width: 700px; margin: 0 auto 2rem;">
            Masukkan daftar bahan produk skincare Anda di bawah ini untuk memeriksa potensi bahan berbahaya
        </p>
    """, unsafe_allow_html=True)
    
    ingredients = st.text_area(
        "**Daftar Bahan:**",
        placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate, Methylparaben",
        height=180,
        key="ingredients_input"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
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
    <div class="section">
        <h1 style="text-align: center; color: var(--primary); margin-bottom: 1rem;">ℹ️ Tentang Pemeriksa Keamanan Skincare</h1>
        <p style="text-align: center; color: #6c757d; max-width: 800px; margin: 0 auto 2rem;">
            Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit
        </p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
            <div>
                <h2 style="color: var(--primary);">🎯 Misi Kami</h2>
                <p>Kami berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit.</p>
                
                <h2 style="color: var(--primary); margin-top: 1.5rem;">🔬 Metodologi</h2>
                <p>Database kami dikembangkan berdasarkan:</p>
                <ul>
                    <li>Regulasi Uni Eropa (EU Regulation No. 1223/2009)</li>
                    <li>Pedoman FDA tentang kosmetik</li>
                    <li>Penelitian ilmiah peer-reviewed</li>
                    <li>Rekomendasi dari dermatolog terkemuka</li>
                </ul>
            </div>
            <div>
                <h2 style="color: var(--primary);">📚 Sumber Data</h2>
                <p>Informasi dalam aplikasi ini bersumber dari:</p>
                <ul>
                    <li>Environmental Working Group's Skin Deep Database</li>
                    <li>Cosmetic Ingredient Review (CIR)</li>
                    <li>Journal of the American Academy of Dermatology</li>
                    <li>International Journal of Toxicology</li>
                </ul>
            </div>
        </div>
        
        <div class="section" style="background-color: #f8f9fa;">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 1.5rem;">💡 Tips Memilih Skincare Aman</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.05);">
                    <h3 style="color: var(--primary); margin-top: 0;">Baca Label</h3>
                    <p>Selalu periksa daftar bahan sebelum membeli produk skincare</p>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.05);">
                    <h3 style="color: var(--primary); margin-top: 0;">Mulai dari Sederhana</h3>
                    <p>Produk dengan daftar bahan yang lebih pendek cenderung lebih aman</p>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.05);">
                    <h3 style="color: var(--primary); margin-top: 0;">Uji Sensitivitas</h3>
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
    
    # Footer
    st.markdown("""
    <footer>
        <p>© 2023 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit yang lebih sehat</p>
        <p style="font-size: 0.9rem;">Disclaimer: Aplikasi ini hanya untuk tujuan informasi dan tidak menggantikan nasihat profesional.</p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
