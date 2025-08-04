# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time
from PIL import Image # Ini mungkin tidak digunakan jika tidak ada elemen gambar

# --- Fungsi untuk memuat CSS eksternal ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- Konfigurasi halaman ---
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Panggil fungsi untuk memuat CSS ---
# Pastikan 'style.css' berada di direktori yang sama dengan script Streamlit Anda
load_css("style.css")

# --- Database bahan berbahaya ---
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
        # Menggunakan kelas CSS untuk styling
        st.success("""
        <div class="safe-product-message">
            <h2 class="safe-product-title">✅ Produk Ini Aman!</h2>
            <p class="safe-product-text">Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan</p>
            <p class="safe-product-note">Tetap perhatikan reaksi kulit Anda terhadap produk baru dan selalu lakukan patch test sebelum penggunaan penuh.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Menggunakan kelas CSS untuk styling
        st.error(f"""
        <div class="dangerous-product-message">
            <h2 class="dangerous-product-title">⚠️ Ditemukan {len(results['dangerous_ingredients'])} Bahan Potensial Berbahaya</h2>
            <p class="dangerous-product-text">Berikut bahan-bahan yang perlu diperhatikan:</p>
        </div>
        """, unsafe_allow_html=True)
        
        for ing in results['dangerous_ingredients']:
            risk_class = "risk-high" if ing['risk'] == "Tinggi" else "risk-medium"
            st.markdown(f"""
            <div class="ingredient-card detailed-card">
                <div class="ingredient-header">
                    <h3>{ing['name'].title()}</h3>
                    <span class="{risk_class}">Risiko: {ing['risk']}</span>
                </div>
                <p><strong>Kategori:</strong> {ing['category']}</p>
                <p><strong>Deskripsi:</strong> {ing['description']}</p>
                <p><strong>Detail:</strong> {ing['details']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="recommendation-section">
            <h3 class="recommendation-title">💡 Rekomendasi</h3>
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
    <section class="hero-section">
        <h1 class="hero-title">🧪 Pemeriksa Keamanan Skincare</h1>
        <p class="hero-subtitle">
            Temukan kebenaran di balik bahan-bahan produk perawatan kulit Anda. Analisis instan berdasarkan penelitian ilmiah dan regulasi internasional.
        </p>
    </section>
    """, unsafe_allow_html=True)
    
    if st.button("Mulai Analisis Sekarang", type="primary"):
        st.session_state.current_tab = "🔍 Analisis Bahan"
    
    # Features Section
    st.markdown("""
    <section class="main-content-section">
        <h2 class="section-heading-centered">Kenapa Memilih Pemeriksa Kami?</h2>
        
        <div class="features-grid">
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
    </section>
    """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("""
    <section class="main-content-section">
        <h2 class="section-heading-centered">Bagaimana Cara Kerjanya?</h2>
        
        <div class="steps-grid">
            <div class="step-item">
                <div class="step-number">1</div>
                <div>
                    <h3>Masukkan Daftar Bahan</h3>
                    <p>Salin dan tempel daftar bahan (INGREDIENTS) dari produk skincare Anda</p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">2</div>
                <div>
                    <h3>Proses Analisis</h3>
                    <p>Sistem kami akan memindai bahan-bahan berbahaya dalam database kami</p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">3</div>
                <div>
                    <h3>Dapatkan Hasil</h3>
                    <p>Lihat laporan lengkap tentang keamanan produk dan rekomendasi alternatif</p>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

def show_analyzer():
    """Tampilan halaman analisis"""
    st.markdown("""
    <section class="analysis-section">
        <h1 class="page-title-centered">🔍 Analisis Bahan Skincare</h1>
        <p class="page-subtitle-centered">
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
    
    st.markdown("</section>", unsafe_allow_html=True) # Tutup section analysis-section

def show_about():
    """Tampilan halaman tentang kami"""
    st.markdown("""
    <section class="about-section">
        <h1 class="page-title-centered">ℹ️ Tentang Pemeriksa Keamanan Skincare</h1>
        <p class="page-subtitle-centered">
            Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit
        </p>
        
        <div class="grid-container about-grid">
            <div>
                <h2 class="section-title">🎯 Misi Kami</h2>
                <p>Kami berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit. Tujuan kami adalah memberdayakan konsumen untuk membuat pilihan yang tepat berdasarkan data dan penelitian ilmiah.</p>
                
                <h2 class="section-title methodology-title">🔬 Metodologi</h2>
                <p>Database kami dikembangkan berdasarkan:</p>
                <ul>
                    <li>Regulasi Uni Eropa (EU Regulation No. 1223/2009)</li>
                    <li>Pedoman FDA tentang kosmetik</li>
                    <li>Penelitian ilmiah peer-reviewed</li>
                    <li>Rekomendasi dari dermatolog terkemuka</li>
                </ul>
            </div>
            <div>
                <h2 class="section-title">📚 Sumber Data</h2>
                <p>Informasi dalam aplikasi ini bersumber dari:</p>
                <ul>
                    <li>Environmental Working Group's Skin Deep Database</li>
                    <li>Cosmetic Ingredient Review (CIR)</li>
                    <li>Journal of the American Academy of Dermatology</li>
                    <li>International Journal of Toxicology</li>
                </ul>
            </div>
        </div>
        
        <div class="tips-section">
            <h2 class="tips-title">💡 Tips Memilih Skincare Aman</h2>
            <div class="tips-grid">
                <div class="tip-card">
                    <h3 class="tip-card-title">Baca Label</h3>
                    <p>Selalu periksa daftar bahan sebelum membeli produk skincare</p>
                </div>
                <div class="tip-card">
                    <h3 class="tip-card-title">Mulai dari Sederhana</h3>
                    <p>Produk dengan daftar bahan yang lebih pendek cenderung lebih aman</p>
                </div>
                <div class="tip-card">
                    <h3 class="tip-card-title">Uji Sensitivitas</h3>
                    <p>Selalu lakukan patch test sebelum menggunakan produk baru</p>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

def main():
    """Fungsi utama untuk tampilan Streamlit"""
    # Initialize session state for tab control
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "🏠 Beranda"
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "ℹ️ Tentang Kami"])
    
    # Display the appropriate tab content without re-rendering all tabs
    if st.session_state.current_tab == "🏠 Beranda":
        with tab1:
            show_home()
    elif st.session_state.current_tab == "🔍 Analisis Bahan":
        with tab2:
            show_analyzer()
    elif st.session_state.current_tab == "ℹ️ Tentang Kami":
        with tab3:
            show_about()

    # Footer
    st.markdown("""
    <footer>
        <p>© 2023 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit yang lebih sehat</p>
        <p class="disclaimer">Disclaimer: Aplikasi ini hanya untuk tujuan informasi dan tidak menggantikan nasihat profesional.</p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
