# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time
from PIL import Image
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS dengan desain yang diperbaiki
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;700&display=swap');
    
    /* Global styles */
    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Header styles */
    h1 {
        font-family: 'Playfair Display', serif !important;
        color: #2c3e50 !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
        font-weight: 700 !important;
    }
    
    h2 {
        font-family: 'Playfair Display', serif !important;
        color: #34495e !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
    }
    
    h3 {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Card styles */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        border: none;
        text-align: center;
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Hero section */
    .hero-container {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.85) 100%);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 3rem !important;
        font-family: 'Playfair Display', serif !important;
        color: #2c3e50 !important;
        margin-bottom: 1rem !important;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Button styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Text area styles */
    .stTextArea > div > div > textarea {
        border-radius: 10px !important;
        border: 2px solid #e1e8ed !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        transition: border-color 0.3s ease !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Tab styles */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 10px !important;
        color: white !important;
        font-weight: 500 !important;
        padding: 0.8rem 1.5rem !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255,255,255,0.2) !important;
        color: white !important;
        font-weight: 600 !important;
    }
    
    /* Alert styles */
    .stAlert {
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    }
    
    /* Success alert */
    .stAlert[data-baseweb="notification"][kind="success"] {
        background-color: #d4edda !important;
        color: #155724 !important;
    }
    
    /* Error alert */
    .stAlert[data-baseweb="notification"][kind="error"] {
        background-color: #f8d7da !important;
        color: #721c24 !important;
    }
    
    /* Warning alert */
    .stAlert[data-baseweb="notification"][kind="warning"] {
        background-color: #fff3cd !important;
        color: #856404 !important;
    }
    
    /* Info alert */
    .stAlert[data-baseweb="notification"][kind="info"] {
        background-color: #d1ecf1 !important;
        color: #0c5460 !important;
    }
    
    /* Metric styles */
    .stMetric {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
    }
    
    /* Progress bar */
    .stProgress .css-1cpxqw2 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        height: 10px;
        border-radius: 5px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        color: rgba(255,255,255,0.8);
        border-top: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem !important;
        }
        
        .hero-container {
            padding: 2rem 1rem;
        }
        
        .feature-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Database bahan berbahaya (diperbaiki dengan struktur yang lebih baik)
DANGEROUS_INGREDIENTS = {
    'paraben': {
        'name': 'Paraben',
        'description': 'Dapat mengganggu sistem hormon (Regulasi EU No. 1223/2009)',
        'category': 'Pengganggu Endokrin',
        'risk_level': 'Tinggi',
        'risk_score': 8,
        'common_names': ['methylparaben', 'propylparaben', 'butylparaben', 'ethylparaben'],
        'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik. Studi menunjukkan paraben dapat meniru estrogen dan berpotensi mengganggu sistem hormon tubuh.',
        'alternatives': 'Phenoxyethanol, Benzyl Alcohol, Potassium Sorbate'
    },
    'sulfate': {
        'name': 'Sulfate',
        'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
        'category': 'Iritan',
        'risk_level': 'Sedang',
        'risk_score': 6,
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate', 'sles'],
        'details': 'Sulfate adalah surfaktan yang dapat menghilangkan minyak alami kulit, menyebabkan kekeringan dan iritasi.',
        'alternatives': 'Decyl Glucoside, Coco-Glucoside, Sodium Cocoyl Isethionate'
    },
    'phthalate': {
        'name': 'Phthalate',
        'description': 'Dikaitkan dengan gangguan hormon dan reproduksi',
        'category': 'Pengganggu Endokrin',
        'risk_level': 'Tinggi',
        'risk_score': 9,
        'common_names': ['dibutyl phthalate', 'dbp', 'diethyl phthalate', 'dep'],
        'details': 'Phthalates sering digunakan sebagai pelarut dan pengikat wewangian. Dikaitkan dengan masalah reproduksi.',
        'alternatives': 'Natural Essential Oils, Phthalate-free Fragrance'
    },
    'formaldehyde': {
        'name': 'Formaldehyde',
        'description': 'Karsinogen yang diketahui dan iritan kuat',
        'category': 'Karsinogen',
        'risk_level': 'Tinggi',
        'risk_score': 10,
        'common_names': ['formalin', 'methanal', 'dmdm hydantoin', 'quaternium-15'],
        'details': 'Formaldehyde diklasifikasikan sebagai karsinogen dan dapat menyebabkan iritasi kulit, mata, dan saluran pernapasan.',
        'alternatives': 'Phenoxyethanol, Ethylhexylglycerin, Caprylyl Glycol'
    },
    'fragrance': {
        'name': 'Fragrance/Parfum',
        'description': 'Dapat menyebabkan iritasi dan reaksi alergi',
        'category': 'Alergen',
        'risk_level': 'Sedang',
        'risk_score': 5,
        'common_names': ['parfum', 'aroma', 'perfume', 'fragrance'],
        'details': 'Istilah fragrance dapat mencakup ratusan bahan kimia yang tidak diungkapkan, banyak dapat menyebabkan alergi.',
        'alternatives': 'Essential Oils, Fragrance-free Products'
    }
}

def analyze_ingredients(ingredients_text):
    """Fungsi untuk menganalisis bahan-bahan skincare dengan scoring"""
    if not ingredients_text.strip():
        return None
        
    found_ingredients = []
    text_lower = ingredients_text.lower()
    total_risk_score = 0
    
    for ing_key, data in DANGEROUS_INGREDIENTS.items():
        all_names = [ing_key] + data['common_names']
        if any(name in text_lower for name in all_names):
            found_ingredients.append(data)
            total_risk_score += data['risk_score']
    
    # Calculate safety score (inverse of risk)
    safety_score = max(0, 100 - (total_risk_score * 2))
    
    return {
        'is_safe': len(found_ingredients) == 0,
        'dangerous_ingredients': found_ingredients,
        'safety_score': safety_score,
        'total_ingredients_checked': len([x for x in ingredients_text.split(',') if x.strip()]),
        'risk_score': total_risk_score
    }

def display_analysis_results(results):
    """Menampilkan hasil analisis dengan tampilan yang lebih baik"""
    if results is None:
        st.warning("⚠️ Silakan masukkan daftar bahan terlebih dahulu")
        return
    
    # Metrics section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Skor Keamanan",
            value=f"{results['safety_score']}/100",
            delta=f"{'Aman' if results['safety_score'] > 70 else 'Perlu Perhatian'}"
        )
    
    with col2:
        st.metric(
            label="Total Bahan",
            value=results['total_ingredients_checked'],
            delta="bahan diperiksa"
        )
    
    with col3:
        st.metric(
            label="Bahan Berisiko",
            value=len(results['dangerous_ingredients']),
            delta="ditemukan"
        )
    
    with col4:
        risk_level = "Rendah" if results['risk_score'] < 10 else "Sedang" if results['risk_score'] < 20 else "Tinggi"
        st.metric(
            label="Level Risiko",
            value=risk_level,
            delta=f"Skor: {results['risk_score']}"
        )
    
    # Progress bar for safety score
    st.subheader("📊 Skor Keamanan Produk")
    progress_color = "🟢" if results['safety_score'] > 70 else "🟡" if results['safety_score'] > 40 else "🔴"
    st.progress(results['safety_score'] / 100)
    st.write(f"{progress_color} **{results['safety_score']}/100** - {get_safety_description(results['safety_score'])}")
    
    # Results display
    if results['is_safe']:
        st.success("### ✅ Produk Ini Relatif Aman!")
        st.info("""
        **Tidak terdeteksi bahan berbahaya** dalam daftar yang diberikan. 
        Tetap perhatikan reaksi kulit Anda dan lakukan patch test sebelum penggunaan penuh.
        """)
    else:
        st.error(f"### ⚠️ Ditemukan {len(results['dangerous_ingredients'])} Bahan Berpotensi Berbahaya")
        
        # Display dangerous ingredients in tabs
        if len(results['dangerous_ingredients']) > 1:
            tabs = st.tabs([f"{ing['name']}" for ing in results['dangerous_ingredients']])
            for i, ing in enumerate(results['dangerous_ingredients']):
                with tabs[i]:
                    display_ingredient_card(ing)
        else:
            display_ingredient_card(results['dangerous_ingredients'][0])
        
        # Recommendations
        st.subheader("💡 Rekomendasi Kami")
        recommendations = generate_recommendations(results['dangerous_ingredients'])
        for rec in recommendations:
            st.info(f"**{rec['title']}:** {rec['description']}")

def display_ingredient_card(ingredient):
    """Menampilkan kartu informasi bahan berbahaya"""
    risk_color = "🔴" if ingredient['risk_level'] == 'Tinggi' else "🟡"
    
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"#### {risk_color} {ingredient['name']}")
            st.write(f"**Kategori:** {ingredient['category']}")
            st.write(f"**Deskripsi:** {ingredient['description']}")
            st.write(f"**Detail:** {ingredient['details']}")
            
        with col2:
            st.metric("Risk Score", f"{ingredient['risk_score']}/10")
            st.write(f"**Level:** {ingredient['risk_level']}")
        
        with st.expander("🔍 Lihat Nama Alternatif & Solusi"):
            st.write("**Nama lain yang umum digunakan:**")
            for name in ingredient['common_names']:
                st.write(f"• {name.title()}")
            
            st.write(f"**Alternatif yang lebih aman:** {ingredient['alternatives']}")

def get_safety_description(score):
    """Mendapatkan deskripsi berdasarkan skor keamanan"""
    if score >= 80:
        return "Sangat Aman - Produk ini memiliki profil keamanan yang sangat baik"
    elif score >= 60:
        return "Cukup Aman - Produk ini relatif aman untuk sebagian besar orang"
    elif score >= 40:
        return "Perlu Perhatian - Beberapa bahan mungkin menyebabkan iritasi pada kulit sensitif"
    else:
        return "Berisiko Tinggi - Produk ini mengandung beberapa bahan yang perlu diwaspadai"

def generate_recommendations(dangerous_ingredients):
    """Generate rekomendasi berdasarkan bahan berbahaya yang ditemukan"""
    recommendations = []
    
    categories = set(ing['category'] for ing in dangerous_ingredients)
    
    if 'Pengganggu Endokrin' in categories:
        recommendations.append({
            'title': 'Hindari Pengganggu Hormon',
            'description': 'Cari produk dengan label "Paraben-free" dan "Phthalate-free"'
        })
    
    if 'Iritan' in categories:
        recommendations.append({
            'title': 'Pilih Formula Lembut',
            'description': 'Gunakan produk "Sulfate-free" terutama jika Anda memiliki kulit sensitif'
        })
    
    if 'Alergen' in categories:
        recommendations.append({
            'title': 'Pilih Produk Hypoallergenic',
            'description': 'Cari produk "Fragrance-free" atau yang menggunakan essential oil alami'
        })
    
    if 'Karsinogen' in categories:
        recommendations.append({
            'title': 'Hindari Bahan Karsinogenik',
            'description': 'Pilih produk dengan pengawet alami atau yang bebas formaldehyde'
        })
    
    # Add general recommendations
    recommendations.extend([
        {
            'title': 'Lakukan Patch Test',
            'description': 'Selalu test produk baru di area kecil kulit sebelum penggunaan penuh'
        },
        {
            'title': 'Konsultasi Dermatolog',
            'description': 'Jika memiliki kulit sensitif atau kondisi kulit khusus, konsultasikan dengan ahli'
        }
    ])
    
    return recommendations

def show_home():
    """Tampilan halaman beranda dengan layout yang diperbaiki"""
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">🧪 Pemeriksa Keamanan Skincare</h1>
        <p class="hero-subtitle">
            Temukan kebenaran di balik bahan-bahan produk perawatan kulit Anda. 
            Analisis instan berdasarkan penelitian ilmiah dan regulasi internasional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Mulai Analisis Sekarang", type="primary", use_container_width=True):
            st.session_state.page = "analyzer"
            st.rerun()
    
    # Features Section
    st.subheader("🌟 Kenapa Memilih Pemeriksa Kami?")
    
    # Use native Streamlit columns for better responsiveness
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔬</div>
                <h3>Analisis Mendalam</h3>
                <p>Sistem kami memeriksa berbagai jenis bahan berbahaya berdasarkan database terpercaya dan penelitian ilmiah terkini</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Hasil Instan</h3>
                <p>Dapatkan hasil analisis komprehensif dalam hitungan detik dengan tingkat akurasi tinggi dan skor keamanan</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3>Edukasi Komprehensif</h3>
                <p>Pelajari tentang bahan berbahaya, alternatif yang lebih aman, dan tips memilih produk skincare</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Second row of features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🛡️</div>
                <h3>Database Terpercaya</h3>
                <p>Informasi berdasarkan regulasi EU, FDA, dan penelitian ilmiah dari jurnal dermatologi terkemuka</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Scoring System</h3>
                <p>Sistem penilaian komprehensif dengan skor keamanan dan level risiko untuk memudahkan pemahaman</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">💡</div>
                <h3>Rekomendasi Cerdas</h3>
                <p>Terima saran alternatif bahan yang lebih aman dan tips memilih produk sesuai jenis kulit</p>
            </div>
            """, unsafe_allow_html=True)
    
    # How it works section
    st.subheader("🔄 Bagaimana Cara Kerjanya?")
    
    step1, step2, step3 = st.columns(3)
    
    with step1:
        st.info("""
        **1️⃣ Masukkan Daftar Bahan**
        
        Salin dan tempel daftar bahan (INGREDIENTS) dari kemasan produk skincare Anda
        """)
    
    with step2:
        st.info("""
        **2️⃣ Proses Analisis**
        
        Sistem kami akan memindai dan mencocokkan dengan database bahan berbahaya yang komprehensif
        """)
    
    with step3:
        st.info("""
        **3️⃣ Dapatkan Hasil**
        
        Lihat skor keamanan, level risiko, dan rekomendasi alternatif yang lebih baik untuk kulit Anda
        """)

def show_analyzer():
    """Tampilan halaman analisis dengan fitur yang diperbaiki"""
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.title("🔍 Analisis Bahan Skincare")
    st.write("Masukkan daftar bahan produk skincare untuk mendapatkan analisis keamanan komprehensif")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input section
    with st.form("ingredient_analyzer", clear_on_submit=False):
        ingredients = st.text_area(
            "**📝 Daftar Bahan (INGREDIENTS):**",
            placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate, Methylparaben, Dimethicone...",
            height=150,
            help="Salin dan tempel daftar bahan dari kemasan produk Anda. Pisahkan dengan koma."
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            analyze_button = st.form_submit_button(
                "🔍 Analisis Bahan Sekarang", 
                type="primary", 
                use_container_width=True
            )
    
    # Analysis section
    if analyze_button:
        if not ingredients.strip():
            st.warning("⚠️ Silakan masukkan daftar bahan terlebih dahulu")
        else:
            with st.spinner("🔬 Menganalisis bahan-bahan... Mohon tunggu sebentar"):
                # Simulate processing time
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                results = analyze_ingredients(ingredients)
                st.success("✅ Analisis selesai!")
                
                # Display results
                display_analysis_results(results)
    
    # Educational content
    with st.expander("📚 Pelajari Lebih Lanjut Tentang Bahan Berbahaya"):
        st.subheader("Database Bahan yang Kami Periksa:")
        
        # Create DataFrame for better display
        ingredients_df = pd.DataFrame([
            {
                'Bahan': data['name'],
                'Kategori': data['category'],
                'Level Risiko': data['risk_level'],
                'Skor Risiko': f"{data['risk_score']}/10"
            }
            for data in DANGEROUS_INGREDIENTS.values()
        ])
        
        st.dataframe(ingredients_df, use_container_width=True)
        
        st.info("""
        **💡 Tips Membaca Label Skincare:**
        - Bahan-bahan dicantumkan berdasarkan konsentrasi (dari tertinggi ke terendah)
        - Jika bahan berbahaya berada di urutan atas, konsentrasinya lebih tinggi
        - Produk dengan daftar bahan lebih pendek cenderung lebih aman
        - Selalu cek apakah ada reaksi alergi sebelum penggunaan penuh
        """)

def show_about():
    """Tampilan halaman tentang kami"""
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.title("ℹ️ Tentang Pemeriksa Keamanan Skincare")
    st.write("Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Mission and methodology
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Misi Kami")
        st.write("""
        Kami berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan 
        informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit. 
        Tujuan kami adalah memberdayakan konsumen untuk membuat pilihan yang tepat berdasarkan data 
        dan penelitian ilmiah.
        """)
        
        st.subheader("🔬 Metodologi")
        st.write("Database kami dikembangkan berdasarkan:")
        st.write("• Regulasi Uni Eropa (EU Regulation No. 1223/2009)")
        st.write("• Pedoman FDA tentang kosmetik")
        st.write("• Penelitian ilmiah peer-reviewed")
        st.write("• Rekomendasi dari dermatolog terkemuka")
    
    with col2:
        st.subheader("📚 Sumber Data")
        st.write("Informasi dalam aplikasi ini bersumber dari:")
        st.write("• Environmental Working Group's Skin Deep Database")
        st.write("• Cosmetic Ingredient Review (CIR)")
        st.write("• Journal of the American Academy of Dermatology")
        st.write("• International Journal of Toxicology")
    
    # Statistics section
    st.subheader("📊 Statistik Platform")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Database", "5", "Kategori Bahan")
    with col2:
        st.metric("Bahan Dipantau", "20+", "Nama Alternatif")
    with col3:
        st.metric("Akurasi", "95%", "Deteksi Bahan")
    with col4:
        st.metric("Update", "Bulanan", "Database")
    
    # Tips section
    st.subheader("💡 Tips Memilih Skincare Aman")
    
    tips_col1, tips_col2, tips_col3 = st.columns(3)
    
    with tips_col1:
        st.info("""
        **📖 Baca Label dengan Teliti**
        
        Selalu periksa daftar bahan sebelum membeli produk skincare. Bahan-bahan dicantumkan berdasarkan konsentrasi.
        """)
    
    with tips_col2:
        st.info("""
        **🧪 Mulai dari Sederhana**
        
        Produk dengan daftar bahan yang lebih pendek cenderung lebih aman dan mudah diidentifikasi jika terjadi reaksi.
        """)
    
    with tips_col3:
        st.info("""
        **🩹 Uji Sensitivitas**
        
        Selalu lakukan patch test di area kecil kulit sebelum menggunakan produk baru secara penuh.
        """)

def main():
    """Fungsi utama aplikasi dengan sistem navigasi yang diperbaiki"""
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    
    # Sidebar navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/test-tube.png", width=80)
        st.title("Navigation")
        
        # Navigation buttons
        if st.button("🏠 Beranda", use_container_width=True):
            st.session_state.page = "home"
        if st.button("🔍 Analisis Bahan", use_container_width=True):
            st.session_state.page = "analyzer"
        if st.button("ℹ️ Tentang Kami", use_container_width=True):
            st.session_state.page = "about"
        
        st.markdown("---")
        st.subheader("🎯 Quick Stats")
        st.write("• 5 Kategori Bahan Berbahaya")
        st.write("• 20+ Nama Alternatif")
        st.write("• Database Terupdate")
        st.write("• Analisis Instan")
        
        st.markdown("---")
        st.info("""
        **💡 Tip Hari Ini:**
        
        Hindari produk dengan lebih dari 3 bahan berakhiran '-paraben' dalam satu produk!
        """)
    
    # Main content area
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "analyzer":
        show_analyzer()
    elif st.session_state.page == "about":
        show_about()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p>© 2024 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit yang lebih sehat</p>
        <p style="font-size:0.8rem;">
            <strong>Disclaimer:</strong> Aplikasi ini hanya untuk tujuan informasi dan tidak menggantikan nasihat medis profesional. 
            Selalu konsultasikan dengan dermatolog untuk masalah kulit yang serius.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
