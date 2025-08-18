# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time
import re

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS yang dioptimasi dan diperbaiki
st.markdown("""
<style>
    /* Font dan warna dasar */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Reset dan base styling */
    * {
        box-sizing: border-box;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        color: #333333 !important;
        overflow-x: hidden;
    }
    
    /* Tema warna */
    :root {
        --primary-color: #e91e63;
        --primary-dark: #c2185b;
        --primary-light: #f8bbd9;
        --secondary-color: #f8f9fa;
        --text-dark: #2c2c2c;
        --text-light: #555555;
        --white: #ffffff;
        --shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    
    /* Main app container */
    .stApp {
        background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
        min-height: 100vh;
    }
    
    /* Container utama */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Typography */
    h1 {
        color: var(--primary-dark) !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        text-align: center;
        font-size: 2.5rem !important;
    }
    
    h2 {
        color: var(--primary-dark) !important;
        font-weight: 600 !important;
        margin: 1.5rem 0 1rem 0 !important;
    }
    
    h3 {
        color: var(--text-dark) !important;
        font-weight: 600 !important;
        margin: 1rem 0 0.5rem 0 !important;
    }
    
    h4 {
        color: var(--text-dark) !important;
        font-weight: 600 !important;
        margin: 0.8rem 0 0.4rem 0 !important;
    }
    
    p, div, span, li {
        color: var(--text-dark) !important;
        line-height: 1.6;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--primary-color) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--shadow);
        width: 100%;
    }
    
    .stButton > button:hover {
        background-color: var(--primary-dark) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.3);
    }
    
    /* Text areas */
    .stTextArea > div > div > textarea {
        border-radius: 8px !important;
        border: 2px solid #e0e0e0 !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        resize: vertical !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 2px rgba(233, 30, 99, 0.2) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        justify-content: center;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 20px !important;
        background-color: white !important;
        color: var(--text-light) !important;
        border-radius: 25px !important;
        border: 2px solid #e0e0e0 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color) !important;
        color: white !important;
        border-color: var(--primary-color) !important;
        box-shadow: var(--shadow);
    }
    
    /* Metrics */
    [data-testid="metric-container"] {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: var(--shadow);
        border: 1px solid #f0f0f0;
    }
    
    /* Alerts */
    .stAlert {
        border-radius: 12px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        border: none !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: white !important;
        border-radius: 8px !important;
        border: 1px solid #e0e0e0 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .streamlit-expanderContent {
        background-color: #fafafa !important;
        border-radius: 0 0 8px 8px !important;
        padding: 1rem !important;
    }
    
    /* Cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: var(--shadow);
        text-align: center;
        height: 100%;
        transition: transform 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Loading spinner custom */
    .stSpinner {
        text-align: center;
    }
    
    /* Mobile responsiveness - Improved */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }
        
        h1 {
            font-size: 2rem !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0px 12px !important;
            font-size: 0.9rem !important;
        }
        
        .feature-card {
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        [data-testid="column"] {
            padding: 0.25rem;
        }
        
        /* Stack cards vertically on mobile */
        .about-card {
            margin-bottom: 1rem !important;
            height: auto !important;
        }
    }
    
    @media (max-width: 480px) {
        h1 {
            font-size: 1.8rem !important;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            flex-direction: column;
            align-items: center;
        }
        
        .stTabs [data-baseweb="tab"] {
            width: 100%;
            max-width: 200px;
            margin-bottom: 0.5rem;
        }
        
        /* Single column on small mobile */
        .about-cards-container {
            flex-direction: column !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Database bahan berbahaya (diperbaiki dan dioptimasi)
DANGEROUS_INGREDIENTS = {
    'paraben': {
        'description': 'Dapat mengganggu hormon',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'common_names': ['methylparaben', 'propylparaben', 'butylparaben', 'ethylparaben'],
        'details': 'Paraben dapat meniru estrogen dan berpotensi mengganggu sistem hormon tubuh.'
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit',
        'category': 'Irritant',
        'risk_level': 'Medium',
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate', 'sles'],
        'details': 'Sulfate dapat menghilangkan minyak alami kulit dan menyebabkan iritasi.'
    },
    'alcohol': {
        'description': 'Dapat mengeringkan kulit',
        'category': 'Drying Agent',
        'risk_level': 'Medium',
        'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol', 'denat alcohol'],
        'details': 'Alkohol tertentu dapat mengeringkan kulit, terutama pada kulit sensitif.'
    },
    'fragrance': {
        'description': 'Dapat menyebabkan alergi',
        'category': 'Allergen',
        'risk_level': 'Medium',
        'common_names': ['parfum', 'perfume', 'aroma', 'fragrance'],
        'details': 'Fragrance sintetis dapat menyebabkan iritasi dan reaksi alergi.'
    },
    'formaldehyde': {
        'description': 'Bahan karsinogenik',
        'category': 'Carcinogen',
        'risk_level': 'High',
        'common_names': ['formalin', 'methylene glycol', 'quaternium-15'],
        'details': 'Formaldehyde diklasifikasikan sebagai karsinogen dan dapat menyebabkan iritasi.'
    }
}

# Database bahan aman (diperbaiki)
KNOWN_SAFE_INGREDIENTS = {
    'aqua', 'water', 'glycerin', 'glycerine', 'hyaluronic acid', 'niacinamide', 
    'ceramide', 'panthenol', 'tocopherol', 'vitamin e', 'aloe vera', 'retinol',
    'salicylic acid', 'lactic acid', 'glycolic acid', 'zinc oxide', 'titanium dioxide',
    'dimethicone', 'squalane', 'jojoba oil', 'shea butter', 'cocoa butter',
    'cetyl alcohol', 'stearyl alcohol', 'sodium chloride', 'citric acid',
    'allantoin', 'chamomile', 'green tea', 'vitamin c', 'ascorbic acid'
}

@st.cache_data
def parse_ingredients(ingredients_text):
    """Parse dan bersihkan daftar bahan"""
    try:
        # Bersihkan teks
        ingredients_text = ingredients_text.replace('\n', ' ').replace('\r', ' ')
        ingredients_list = [ing.strip().lower() for ing in re.split(r'[,;]+', ingredients_text) if ing.strip()]
        
        # Filter bahan yang valid
        ingredients_list = [ing for ing in ingredients_list if len(ing) > 1]
        
        return ingredients_list
    except Exception as e:
        st.error(f"Error parsing ingredients: {str(e)}")
        return []

@st.cache_data
def categorize_ingredients(ingredients_list):
    """Kategorikan bahan menjadi berbahaya, aman, dan tidak dikenal"""
    dangerous = []
    safe = []
    unknown = []
    
    try:
        for ingredient in ingredients_list:
            ingredient_lower = ingredient.lower().strip()
            
            # Cek bahan berbahaya
            is_dangerous = False
            for dangerous_key, data in DANGEROUS_INGREDIENTS.items():
                all_names = [dangerous_key] + data['common_names']
                if any(name in ingredient_lower for name in all_names):
                    dangerous.append({
                        'name': dangerous_key,
                        'original_name': ingredient,
                        'risk': data['risk_level'],
                        'category': data['category'],
                        'description': data['description'],
                        'details': data['details']
                    })
                    is_dangerous = True
                    break
            
            if not is_dangerous:
                # Cek bahan aman
                is_known_safe = any(safe_ingredient in ingredient_lower for safe_ingredient in KNOWN_SAFE_INGREDIENTS)
                
                if is_known_safe:
                    safe.append(ingredient)
                else:
                    unknown.append(ingredient)
        
        return dangerous, safe, unknown
    
    except Exception as e:
        st.error(f"Error categorizing ingredients: {str(e)}")
        return [], [], []

def analyze_ingredients(ingredients_text):
    """Analisis utama bahan-bahan"""
    if not ingredients_text or not ingredients_text.strip():
        return None
    
    try:
        ingredients_list = parse_ingredients(ingredients_text)
        if not ingredients_list:
            return None
            
        dangerous, safe, unknown = categorize_ingredients(ingredients_list)
        
        return {
            'is_safe': len(dangerous) == 0,
            'dangerous_ingredients': dangerous,
            'safe_ingredients': safe,
            'unknown_ingredients': unknown,
            'total_ingredients': len(ingredients_list)
        }
    except Exception as e:
        st.error(f"Error analyzing ingredients: {str(e)}")
        return None

def display_results(results):
    """Tampilkan hasil analisis dengan styling yang diperbaiki"""
    if not results:
        st.error("Tidak dapat menganalisis bahan. Silakan coba lagi.")
        return
    
    # Metrics dalam card
    st.markdown("### 📊 Ringkasan Analisis")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Bahan", results['total_ingredients'])
    with col2:
        st.metric("Bahan Berbahaya", len(results['dangerous_ingredients']), 
                 delta=f"-{len(results['dangerous_ingredients'])}" if len(results['dangerous_ingredients']) > 0 else None)
    with col3:
        st.metric("Bahan Aman", len(results['safe_ingredients']))
    with col4:
        st.metric("Tidak Dikenal", len(results['unknown_ingredients']))
    
    st.markdown("---")
    
    # Assessment utama
    if len(results['dangerous_ingredients']) > 0:
        st.error(f"⚠️ **PERINGATAN: Ditemukan {len(results['dangerous_ingredients'])} Bahan Berpotensi Berbahaya**")
        
        st.markdown("""
        <div style="background: #fff3e0; padding: 1rem; border-radius: 8px; border-left: 4px solid #ff9800; margin: 1rem 0;">
            <strong>🚨 Rekomendasi:</strong><br>
            Pertimbangkan untuk tidak menggunakan produk ini atau konsultasi dengan dermatolog terlebih dahulu.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🔍 Detail Bahan Berbahaya:")
        
        for ing in results['dangerous_ingredients']:
            with st.expander(f"🚨 {ing['name'].title()} - Risiko: {ing['risk']} ({'ditemukan sebagai: ' + ing['original_name']})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Kategori:** {ing['category']}")
                    st.write(f"**Tingkat Risiko:** {ing['risk']}")
                with col2:
                    st.write(f"**Deskripsi:** {ing['description']}")
                st.write(f"**Detail:** {ing['details']}")
        
        # Rekomendasi alternatif
        st.info("""
        **💡 Alternatif yang Disarankan:**
        - Cari produk dengan label "Paraben-Free", "Sulfate-Free", "Fragrance-Free"
        - Pilih produk dengan sertifikasi organik atau natural
        - Konsultasikan dengan dermatolog untuk rekomendasi produk yang sesuai
        """)
    
    else:
        st.success("✅ **AMAN: Tidak Ditemukan Bahan Berbahaya**")
        
        st.markdown("""
        <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50; margin: 1rem 0;">
            <strong>🎉 Bagus!</strong><br>
            Produk ini tampaknya aman untuk digunakan. Namun, tetap lakukan patch test sebelum penggunaan penuh.
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **💡 Tips Penggunaan Aman:**
        - Lakukan patch test di belakang telinga selama 24-48 jam
        - Mulai gunakan secara bertahap
        - Hentikan penggunaan jika terjadi iritasi
        - Simpan di tempat sejuk dan kering
        """)
    
    # Tampilkan bahan yang tidak dikenal jika ada
    if results['unknown_ingredients']:
        st.markdown("---")
        with st.expander(f"🔍 Bahan Tidak Dikenal ({len(results['unknown_ingredients'])} bahan)"):
            st.write("Bahan-bahan berikut tidak terdeteksi dalam database:")
            
            # Tampilkan dalam kolom untuk hemat space
            unknown_chunks = [results['unknown_ingredients'][i:i+3] for i in range(0, len(results['unknown_ingredients']), 3)]
            for chunk in unknown_chunks:
                cols = st.columns(len(chunk))
                for i, ing in enumerate(chunk):
                    cols[i].write(f"• {ing.title()}")

def main():
    """Aplikasi utama"""
    
    # Header
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; margin-bottom: 2rem;">
        <h1>🧪 Pemeriksa Keamanan Skincare</h1>
        <p style="font-size: 1.2rem; color: #666;">Analisis bahan skincare berdasarkan penelitian ilmiah</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "ℹ️ Tentang"])
    
    with tab1:
        st.markdown("---")
        
        # Hero section
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(233,30,99,0.1) 0%, rgba(255,255,255,0.9) 100%); 
                    padding: 2rem; border-radius: 15px; text-align: center; margin-bottom: 2rem;">
            <h2>Keamanan Skincare dalam Genggaman</h2>
            <p style="font-size: 1.1rem;">Platform terpercaya untuk menganalisis keamanan produk perawatan kulit Anda</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features
        col1, col2, col3, col4 = st.columns(4)
        
        features = [
            ("🔬", "Analisis Ilmiah", "Database berdasarkan penelitian terpercaya"),
            ("⚡", "Hasil Instan", "Analisis cepat dalam hitungan detik"),
            ("📚", "Edukasi", "Pelajari tentang bahan berbahaya"),
            ("🛡️", "Keamanan", "Lindungi kulit dari bahan berbahaya")
        ]
        
        for i, (icon, title, desc) in enumerate(features):
            with [col1, col2, col3, col4][i]:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h4>{title}</h4>
                    <p style="font-size: 0.9rem;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # How it works
        st.markdown("### 🚀 Cara Menggunakan")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **1️⃣ Input Bahan**
            
            Salin daftar INGREDIENTS dari kemasan produk atau website resmi
            """)
        
        with col2:
            st.markdown("""
            **2️⃣ Analisis Otomatis**
            
            Sistem memproses dan mengidentifikasi bahan berbahaya
            """)
        
        with col3:
            st.markdown("""
            **3️⃣ Dapatkan Hasil**
            
            Lihat laporan keamanan lengkap dengan rekomendasi
            """)
    
    with tab2:
        st.markdown("---")
        st.markdown("### 🔍 Analisis Bahan Skincare")
        
        # Input form
        st.markdown("**Masukkan Daftar Bahan (INGREDIENTS):**")
        ingredients = st.text_area(
            "",
            placeholder="Contoh: Aqua, Glycerin, Sodium Lauryl Sulfate, Fragrance, Methylparaben, Niacinamide, Hyaluronic Acid",
            height=120,
            help="Salin dan tempel daftar bahan dari kemasan produk"
        )
        
        # Button
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("🔍 Analisis Sekarang", type="primary"):
                if not ingredients.strip():
                    st.warning("⚠️ Silakan masukkan daftar bahan terlebih dahulu")
                else:
                    with st.spinner("🔬 Menganalisis bahan..."):
                        # Simulasi proses
                        progress_bar = st.progress(0)
                        for i in range(100):
                            time.sleep(0.01)
                            progress_bar.progress(i + 1)
                        
                        # Analisis
                        results = analyze_ingredients(ingredients)
                        progress_bar.empty()
                        
                        if results:
                            st.markdown("---")
                            display_results(results)
                        else:
                            st.error("Gagal menganalisis bahan. Silakan periksa format input.")
    
    with tab3:
        st.markdown("---")
        
        # Layout 2x2 yang sejajar dan rapi
        col1, col2 = st.columns(2)
        
        with col1:
            # Misi Kami
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 1.5rem; height: 280px; display: flex; flex-direction: column;">
                <h4 style="color: #e91e63; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <span>🎯</span> Misi Kami
                </h4>
                <p style="line-height: 1.6; flex-grow: 1; color: #555; margin: 0;">
                    Memberikan transparansi dalam industri kecantikan dengan informasi yang jelas dan dapat diakses tentang keamanan bahan skincare.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Metodologi
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); height: 280px; display: flex; flex-direction: column;">
                <h4 style="color: #e91e63; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <span>🔬</span> Metodologi
                </h4>
                <div style="flex-grow: 1;">
                    <p style="margin-bottom: 1rem; color: #555;">Website ini dikembangkan berdasarkan:</p>
                    <ul style="line-height: 1.6; color: #555; margin: 0; padding-left: 1.2rem;">
                        <li>Regulasi EU & FDA</li>
                        <li>Database EWG Skin Deep</li>
                        <li>Penelitian peer-reviewed</li>
                        <li>Pedoman BPOM RI</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Sumber Data
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 1.5rem; height: 280px; display: flex; flex-direction: column;">
                <h4 style="color: #e91e63; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <span>📚</span> Sumber Data
                </h4>
                <div style="flex-grow: 1;">
                    <p style="margin-bottom: 1rem; color: #555;">Informasi dalam website ini bersumber dari:</p>
                    <ul style="line-height: 1.6; color: #555; margin: 0; padding-left: 1.2rem;">
                        <li>Environmental Working Group</li>
                        <li>Cosmetic Ingredient Review</li>
                        <li>Journal of Dermatology</li>
                        <li>BPOM Indonesia</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Tips Keamanan
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); height: 280px; display: flex; flex-direction: column;">
                <h4 style="color: #e91e63; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <span>💡</span> Tips Keamanan
                </h4>
                <div style="flex-grow: 1;">
                    <ul style="line-height: 1.6; color: #555; margin: 0; padding-left: 1.2rem;">
                        <li>Selalu baca label dengan teliti</li>
                        <li>Lakukan patch test</li>
                        <li>Konsultasi dengan dermatolog</li>
                        <li>Pilih produk tersertifikasi</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Disclaimer
        st.markdown("---")
        st.warning("""
        **⚠️ Disclaimer:** Website ini hanya untuk tujuan informasi dan tidak menggantikan 
        nasihat medis profesional. Selalu konsultasikan dengan dermatolog untuk masalah kulit yang serius.
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem; color: #666; font-size: 0.9rem;">
        <p>© 2025 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit yang lebih sehat</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
