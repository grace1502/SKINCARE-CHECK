# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import pandas as pd
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS yang lebih sederhana dan efektif
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-title {
        color: #d35d6e;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .feature-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        height: 100%;
    }
    
    .feature-icon {
        font-size: 2rem;
        color: #d35d6e;
        margin-bottom: 1rem;
    }
    
    .stButton>button {
        background-color: #d35d6e;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
    }
    
    .ingredient-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #d35d6e;
    }
    
    .risk-high {
        color: #c62828;
        font-weight: bold;
    }
    
    .risk-medium {
        color: #ff8f00;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Database bahan berbahaya yang lebih lengkap
DANGEROUS_INGREDIENTS = {
    'paraben': {
        'description': 'Dapat mengganggu sistem hormon (Regulasi EU No. 1223/2009)',
        'category': 'Pengganggu Endokrin',
        'risk_level': 'Tinggi',
        'common_names': ['methylparaben', 'propylparaben', 'butylparaben', 'ethylparaben'],
        'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik. Studi menunjukkan paraben dapat meniru estrogen dan berpotensi mengganggu sistem hormon tubuh.'
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
        'category': 'Iritan',
        'risk_level': 'Sedang',
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate', 'ammonium lauryl sulfate'],
        'details': 'Sulfate adalah surfaktan yang digunakan untuk membuat busa. Bahan ini dapat menghilangkan minyak alami kulit, menyebabkan kekeringan dan iritasi.'
    },
    'phthalate': {
        'description': 'Dikaitkan dengan gangguan hormon dan reproduksi',
        'category': 'Pengganggu Endokrin',
        'risk_level': 'Tinggi',
        'common_names': ['dibutyl phthalate', 'dbp', 'diethyl phthalate', 'dehp'],
        'details': 'Phthalates sering digunakan sebagai pelarut dan pengikat wewangian. Telah dikaitkan dengan masalah reproduksi dan perkembangan.'
    },
    'formaldehyde': {
        'description': 'Karsinogen yang diketahui dan iritan kuat',
        'category': 'Karsinogen',
        'risk_level': 'Tinggi',
        'common_names': ['formalin', 'methanal', 'methyl aldehyde', 'dmdm hydantoin'],
        'details': 'Formaldehyde dan pelepas formaldehyde digunakan sebagai pengawet. Zat ini diklasifikasikan sebagai karsinogen manusia.'
    },
    'fragrance': {
        'description': 'Dapat menyebabkan iritasi dan reaksi alergi',
        'category': 'Alergen',
        'risk_level': 'Sedang',
        'common_names': ['parfum', 'aroma', 'perfume', 'fragrance mix'],
        'details': 'Istilah "fragrance" dapat mencakup ratusan bahan kimia yang tidak diungkapkan, banyak di antaranya dapat menyebabkan iritasi kulit atau alergi.'
    },
    'alcohol': {
        'description': 'Dapat menyebabkan kekeringan dan iritasi',
        'category': 'Iritan',
        'risk_level': 'Sedang',
        'common_names': ['alcohol denat', 'ethanol', 'isopropyl alcohol', 'sd alcohol'],
        'details': 'Alkohol tertentu dalam konsentrasi tinggi dapat mengeringkan kulit dan merusak skin barrier.'
    }
}

def main():
    """Fungsi utama untuk tampilan Streamlit"""
    st.sidebar.title("Navigasi")
    page = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Analisis Bahan", "Tentang Kami"])
    
    if page == "Beranda":
        show_home()
    elif page == "Analisis Bahan":
        show_analyzer()
    elif page == "Tentang Kami":
        show_about()

def show_home():
    """Tampilan halaman beranda"""
    st.markdown('<h1 class="main-title">🧪 Pemeriksa Keamanan Skincare</h1>', unsafe_allow_html=True)
    st.markdown("**Temukan kebenaran di balik bahan-bahan produk perawatan kulit Anda**")
    st.markdown("Analisis instan berdasarkan penelitian ilmiah dan regulasi internasional")
    
    if st.button("Mulai Analisis Sekarang", type="primary"):
        st.session_state.current_page = "Analisis Bahan"
        st.experimental_rerun()
    
    st.markdown("---")
    st.subheader("Kenapa Memilih Pemeriksa Kami?")
    
    cols = st.columns(4)
    features = [
        ("🔬", "Analisis Mendalam", "Memeriksa berbagai jenis bahan berbahaya"),
        ("⚡", "Hasil Instan", "Analisis cepat dalam hitungan detik"),
        ("📚", "Edukasi", "Penjelasan lengkap tentang bahan"),
        ("🛡️", "Terpercaya", "Berdasarkan regulasi dan penelitian")
    ]
    
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Bagaimana Cara Kerjanya?")
    
    steps = [
        ("1", "Masukkan Daftar Bahan", "Salin dan tempel daftar bahan dari produk Anda"),
        ("2", "Proses Analisis", "Sistem kami akan memindai bahan berbahaya"),
        ("3", "Dapatkan Hasil", "Lihat laporan lengkap tentang keamanan produk")
    ]
    
    for step in steps:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <h4>{step[0]}. {step[1]}</h4>
            <p>{step[2]}</p>
        </div>
        """, unsafe_allow_html=True)

def show_analyzer():
    """Tampilan halaman analisis"""
    st.markdown('<h1 class="main-title">🔍 Analisis Bahan Skincare</h1>', unsafe_allow_html=True)
    
    ingredients = st.text_area(
        "Masukkan daftar bahan produk skincare Anda:",
        placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate, Methylparaben",
        height=150
    )
    
    if st.button("Analisis Bahan", type="primary"):
        if not ingredients.strip():
            st.warning("Silakan masukkan daftar bahan terlebih dahulu")
        else:
            with st.spinner("Sedang menganalisis bahan..."):
                time.sleep(1.5)
                results = analyze_ingredients(ingredients)
                display_results(results)

def show_about():
    """Tampilan halaman tentang kami"""
    st.markdown('<h1 class="main-title">ℹ️ Tentang Kami</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h3>Misi Kami</h3>
        <p>Kami berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas tentang bahan-bahan dalam produk perawatan kulit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h3>Sumber Data</h3>
        <p>Database kami dikembangkan berdasarkan:</p>
        <ul>
            <li>Regulasi Uni Eropa (EU Regulation No. 1223/2009)</li>
            <li>Pedoman FDA tentang kosmetik</li>
            <li>Penelitian ilmiah terbaru</li>
            <li>Rekomendasi dermatolog</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div>
        <h3>Tim Kami</h3>
        <p>Konten kami ditinjau oleh:</p>
        <ul>
            <li>Dermatolog bersertifikat</li>
            <li>Ahli toksikologi kosmetik</li>
            <li>Peneliti bahan kosmetik</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def analyze_ingredients(ingredients_text):
    """Fungsi untuk menganalisis bahan-bahan skincare"""
    found_ingredients = []
    text_lower = ingredients_text.lower()
    
    for ing, data in DANGEROUS_INGREDIENTS.items():
        all_names = [ing] + data['common_names']
        if any(name in text_lower for name in all_names):
            found_ingredients.append({
                'name': ing.capitalize(),
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
        ## ✅ Produk ini AMAN!
        Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan.
        """)
    else:
        st.error(f"""
        ## ⚠️ Ditemukan {len(results['dangerous_ingredients'])} bahan yang perlu diperhatikan
        """)
        
        for ing in results['dangerous_ingredients']:
            risk_class = "risk-high" if ing['risk'] == "Tinggi" else "risk-medium"
            
            st.markdown(f"""
            <div class="ingredient-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3>{ing['name']}</h3>
                    <span class="{risk_class}">Risiko: {ing['risk']}</span>
                </div>
                <p><strong>Kategori:</strong> {ing['category']}</p>
                <p><strong>Deskripsi:</strong> {ing['description']}</p>
                <p><strong>Detail:</strong> {ing['details']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="margin-top: 2rem; padding: 1rem; background-color: #fff9fa; border-radius: 10px;">
            <h4>💡 Tips Memilih Produk yang Lebih Aman:</h4>
            <ul>
                <li>Cari produk dengan label "hypoallergenic" untuk kulit sensitif</li>
                <li>Pilih produk "fragrance-free" untuk menghindari iritasi</li>
                <li>Produk dengan daftar bahan lebih pendek cenderung lebih aman</li>
                <li>Selalu lakukan patch test sebelum penggunaan pertama</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
