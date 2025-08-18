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

# Custom CSS dengan desain aesthetic yang diperbaiki
st.markdown("""
<style>
    /* Font dan warna dasar */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #333333;
    }
    
    /* Warna tema soft pink */
    :root {
        --primary-color: #e91e63;
        --primary-dark: #c2185b;
        --primary-light: #f8bbd9;
        --secondary-color: #f8f9fa;
        --text-dark: #2c2c2c;
        --text-light: #555555;
    }
    
    /* Background dengan overlay dan gambar aesthetic */
    .stApp {
        background: 
            linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.85)),
            linear-gradient(45deg, rgba(233, 30, 99, 0.03) 0%, rgba(255, 182, 193, 0.05) 50%, rgba(255, 255, 255, 0.02) 100%),
            url('https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'),
            url('https://images.unsplash.com/photo-1570194065650-d99fb4bedf0d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover, cover, cover, cover;
        background-position: center, center, center top, center bottom;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
        position: relative;
    }
    
    /* Alternative background untuk mobile */
    @media (max-width: 768px) {
        .stApp {
            background-attachment: scroll;
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.94), rgba(255, 255, 255, 0.88)),
                linear-gradient(45deg, rgba(233, 30, 99, 0.02) 0%, rgba(255, 182, 193, 0.03) 100%),
                url('https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=70');
        }
    }
    
    /* Decorative elements */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(233, 30, 99, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(194, 24, 91, 0.02) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(248, 187, 217, 0.04) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    
    /* Main container dengan glassmorphism effect */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 
            0 15px 35px rgba(0, 0, 0, 0.1),
            0 5px 15px rgba(0, 0, 0, 0.07),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        padding: 2rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    /* Decorative overlay untuk container */
    .main-container::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 200px;
        height: 200px;
        background: 
            url('https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80'),
            linear-gradient(135deg, rgba(233, 30, 99, 0.05), rgba(194, 24, 91, 0.03));
        background-size: cover;
        background-position: center;
        border-radius: 0 20px 0 100px;
        opacity: 0.1;
        z-index: 0;
        pointer-events: none;
    }
    
    /* Content positioning */
    .main-container > * {
        position: relative;
        z-index: 1;
    }
    
    /* Judul utama */
    h1 {
        color: #c2185b !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        font-size: 2.5rem !important;
        letter-spacing: -0.02em !important;
        text-align: center !important;
    }
    
    /* Subjudul */
    h2 {
        color: #c2185b !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-bottom: 2px solid var(--primary-light);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem !important;
    }
    
    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #2c2c2c !important;
        font-weight: 600 !important;
        text-align: center !important;
    }
    
    h4 {
        color: #2c2c2c !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Text color improvements */
    p, div, span, .stMarkdown {
        color: #2c2c2c !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stMarkdown p {
        color: #2c2c2c !important;
        line-height: 1.6 !important;
    }
    
    /* Tombol */
    .stButton button {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.3) !important;
        text-transform: none !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #c2185b 0%, #ad1457 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.4) !important;
    }
    
    .stButton button:active {
        transform: translateY(0px) !important;
    }
    
    /* Text area */
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 2px solid #f0f0f0 !important;
        padding: 1rem !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        transition: border-color 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: var(--primary-light) !important;
        box-shadow: 0 0 0 3px rgba(233, 30, 99, 0.1) !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        margin-bottom: 2rem;
        justify-content: center;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 1.5rem !important;
        background-color: #f8f9fa !important;
        color: #2c2c2c !important;
        border-radius: 12px !important;
        margin-right: 0 !important;
        font-weight: 500 !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
        border: 2px solid transparent !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e3f2fd !important;
        transform: translateY(-1px) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #e91e63 0%, #c2185b 100%) !important;
        font-weight: 600 !important;
        color: white !important;
        border: 2px solid #e91e63 !important;
        box-shadow: 0 4px 12px rgba(233, 30, 99, 0.3) !important;
    }
    
    /* Alert styling dengan glassmorphism */
    .stAlert {
        border-radius: 16px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        border: none !important;
        font-family: 'Inter', sans-serif !important;
        backdrop-filter: blur(10px) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stAlert::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=30');
        background-size: cover;
        background-position: center;
        opacity: 0.02;
        pointer-events: none;
        z-index: 0;
    }
    
    .stAlert > div {
        font-weight: 500 !important;
        position: relative !important;
        z-index: 1 !important;
    }
    
    /* Success alert */
    [data-testid="stAlert"] div:first-child {
        background: rgba(232, 245, 232, 0.95) !important;
        border-left: 4px solid #4caf50 !important;
        box-shadow: 0 4px 20px rgba(76, 175, 80, 0.1) !important;
    }
    
    /* Warning alert */
    .stWarning {
        background: rgba(255, 243, 224, 0.95) !important;
        border-left: 4px solid #ff9800 !important;
        box-shadow: 0 4px 20px rgba(255, 152, 0, 0.1) !important;
    }
    
    /* Error alert */
    .stError {
        background: rgba(255, 235, 238, 0.95) !important;
        border-left: 4px solid #f44336 !important;
        box-shadow: 0 4px 20px rgba(244, 67, 54, 0.1) !important;
    }
    
    /* Info alert */
    .stInfo {
        background: rgba(227, 242, 253, 0.95) !important;
        border-left: 4px solid #2196f3 !important;
        box-shadow: 0 4px 20px rgba(33, 150, 243, 0.1) !important;
    }
    
    /* Metrics dengan glassmorphism */
    .stMetric {
        background: rgba(255, 255, 255, 0.9) !important;
        padding: 1.2rem !important;
        border-radius: 16px !important;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.08),
            0 2px 8px rgba(0, 0, 0, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        text-align: center !important;
        backdrop-filter: blur(15px) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stMetric::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.02) 0%, rgba(255, 255, 255, 0.03) 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
        z-index: 0;
    }
    
    .stMetric:hover {
        transform: translateY(-2px) !important;
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.12),
            0 4px 12px rgba(233, 30, 99, 0.05) !important;
        border-color: rgba(233, 30, 99, 0.15) !important;
    }
    
    .stMetric:hover::before {
        opacity: 1;
    }
    
    .stMetric > div {
        position: relative !important;
        z-index: 1 !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #f8f9fa !important;
        border-radius: 8px !important;
        padding: 0.8rem !important;
        margin: 0.5rem 0 !important;
        font-weight: 500 !important;
        color: #2c2c2c !important;
    }
    
    .streamlit-expanderContent {
        border: 1px solid #f0f0f0 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin-top: 0.5rem !important;
    }
    
    /* Column spacing */
    .stColumn {
        padding: 0 0.5rem !important;
    }
    
    /* Feature cards dengan glassmorphism */
    .feature-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            0 2px 8px rgba(0, 0, 0, 0.05);
        text-align: center;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.02) 0%, rgba(255, 255, 255, 0.05) 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
    }
    
    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.15),
            0 5px 15px rgba(233, 30, 99, 0.1);
        border-color: rgba(233, 30, 99, 0.2);
    }
    
    .feature-card:hover::before {
        opacity: 1;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #e91e63;
    }
    
    .feature-title {
        color: #2c2c2c;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.8rem;
    }
    
    .feature-description {
        color: #555555;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    /* Hero section dengan background image overlay */
    .hero-section {
        background: 
            linear-gradient(135deg, rgba(233, 30, 99, 0.08) 0%, rgba(255, 255, 255, 0.95) 50%, rgba(248, 187, 217, 0.05) 100%),
            url('https://images.unsplash.com/photo-1596755389378-c31d21fd1273?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80');
        background-size: cover, cover;
        background-position: center, center;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 
            0 15px 35px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 30% 70%, rgba(233, 30, 99, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 70% 30%, rgba(248, 187, 217, 0.04) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    .hero-section > * {
        position: relative;
        z-index: 1;
    }
    
    /* Footer dengan background subtle */
    .footer {
        text-align: center;
        padding: 2.5rem 0;
        margin-top: 3rem;
        color: #666666;
        font-size: 0.9rem;
        border-top: 1px solid rgba(233, 30, 99, 0.1);
        background: 
            linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(248, 187, 217, 0.05) 100%),
            url('https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=20');
        background-size: cover, cover;
        background-position: center, center;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 50% 50%, rgba(233, 30, 99, 0.02) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }
    
    .footer > * {
        position: relative;
        z-index: 1;
    }
</style>
""", unsafe_allow_html=True)

# CSS PERBAIKAN MOBILE RESPONSIF
st.markdown("""
<style>
    /* MOBILE RESPONSIVE IMPROVEMENTS */
    @media (max-width: 768px) {
        /* Container adjustments */
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
        
        /* Header adjustments */
        h1 {
            font-size: 2rem !important;
            line-height: 1.2 !important;
        }
        
        h3 {
            font-size: 1.3rem !important;
            line-height: 1.3 !important;
        }
        
        /* Tab improvements */
        .stTabs [data-baseweb="tab"] {
            padding: 0.8rem 1rem !important;
            font-size: 0.9rem !important;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            flex-wrap: wrap !important;
            gap: 0.3rem !important;
        }
        
        /* Button improvements */
        .stButton button {
            width: 100% !important;
            padding: 1rem !important;
            font-size: 1rem !important;
        }
        
        /* Feature cards stack */
        .feature-card {
            margin-bottom: 1rem;
            height: auto;
            min-height: 180px;
        }
        
        /* Hero section */
        .hero-section {
            padding: 1.5rem;
        }
        
        /* Metrics stack */
        .stMetric {
            margin-bottom: 1rem !important;
        }
    }
    
    @media (max-width: 480px) {
        h1 {
            font-size: 1.8rem !important;
        }
        
        .main .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.6rem 0.8rem !important;
            font-size: 0.85rem !important;
        }
        
        .feature-card {
            min-height: 160px;
        }
        
        .hero-section {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Database bahan berbahaya (diperbaiki dan diperluas)
DANGEROUS_INGREDIENTS = {
   'paraben': {
        'description': 'Dapat mengganggu hormon (EU Regulation No. 1223/2009)',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'common_names': ['methylparaben', 'propylparaben', 'butylparaben'],
        'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik dan produk perawatan pribadi. Studi menunjukkan paraben dapat meniru estrogen dan berpotensi mengganggu sistem hormon tubuh. Regulasi Uni Eropa telah membatasi penggunaan beberapa jenis paraben dalam produk kosmetik.'
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit',
        'category': 'Irritant',
        'risk_level': 'Medium',
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate'],
        'details': 'Sulfate adalah surfaktan yang digunakan untuk membuat busa dalam produk pembersih. Bahan ini dapat menghilangkan minyak alami kulit, menyebabkan kekeringan dan iritasi, terutama pada kulit sensitif. Alternatif yang lebih lembut termasuk decyl glucoside atau coco-glucoside.'
    },
    'phthalate': {
        'description': 'May disrupt hormones and affect reproductive health (EU Regulation No. 1223/2009)',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'common_names': ['dibutyl phthalate (dbp)', 'diethylhexyl phthalate (dehp)'],
        'details': 'Phthalates sering digunakan sebagai pelarut dan pengikat wewangian. Bahan ini telah dikaitkan dengan masalah reproduksi dan perkembangan. Banyak negara telah melarang penggunaan phthalates tertentu dalam produk kosmetik dan mainan anak-anak.'
    },
    'formaldehyde': {
        'description': 'Known carcinogen and skin sensitizer',
        'category': 'Carcinogen, Allergen',
        'risk_level': 'High',
        'common_names': ['formalin', 'methylene glycol', 'quaternium-15'],
        'details': 'Formaldehyde dan pelepas formaldehyde digunakan sebagai pengawet. Zat ini diklasifikasikan sebagai karsinogen manusia dan dapat menyebabkan iritasi kulit, mata, dan saluran pernapasan. Hindari produk yang mengandung DMDM hydantoin, imidazolidinyl urea, atau quaternium-15.'
    },
    'mercury': {
        'description': 'Neurotoxin, harmful to kidney and nervous system',
        'category': 'Heavy Metal, Neurotoxin',
        'risk_level': 'Critical',
        'common_names': ['calomel', 'mercuric chloride'],
        'details': 'Mercury adalah logam berat yang sangat beracun dan dapat merusak sistem saraf, ginjal, dan organ lainnya. Penggunaan mercury dalam kosmetik telah dilarang di banyak negara karena risiko kesehatan yang serius.'
    },
    'hydroquinone': {
        'description': 'Skin lightener, can cause ochronosis (skin discoloration)',
        'category': 'Skin Irritant, Pigmentation Disrupter',
        'risk_level': 'High',
        'common_names': ['dihydroxybenzene', 'quinol'],
        'details': 'Hydroquinone digunakan sebagai pemutih kulit tetapi dapat menyebabkan ochronosis (perubahan warna kulit menjadi biru-hitam) dan iritasi kulit. Penggunaannya dibatasi atau dilarang di beberapa negara.'
    },
    'triclosan': {
        'description': 'May disrupt hormones and contribute to antibiotic resistance',
        'category': 'Endocrine Disruptor, Antibiotic Resistance',
        'risk_level': 'High',
        'common_names': ['triclosan', 'tcs'],
        'details': 'Triclosan adalah antimikroba yang dapat mengganggu hormon dan berkontribusi pada resistensi antibiotik. FDA telah melarang penggunaannya dalam sabun antibakteri konsumen.'
    },
    'alcohol': {
        'description': 'Can be drying and irritating for some skin types (depending on type and concentration)',
        'category': 'Irritant, Drying Agent',
        'risk_level': 'Medium',
        'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol'],
        'details': 'Alkohol tertentu dapat mengeringkan dan mengiritasi kulit, terutama pada kulit sensitif. Namun, tidak semua alkohol berbahaya - fatty alcohols seperti cetyl alcohol justru melembapkan.'
    },
    'fragrance': {
        'description': 'Common allergen and can cause skin irritation (often a mix of undisclosed chemicals)',
        'category': 'Allergen, Irritant',
        'risk_level': 'Medium',
        'common_names': ['parfum', 'perfume', 'aroma'],
        'details': 'Istilah "fragrance" atau "parfum" dapat mencakup ratusan bahan kimia berbeda yang tidak diungkapkan. Banyak di antaranya dapat menyebabkan iritasi kulit, alergi, atau gangguan hormon. Pilih produk yang bebas wewangian atau menggunakan minyak esensial alami sebagai alternatif.'
    },
    'lead': {
        'description': 'Neurotoxin, harmful to nervous system (especially in children)',
        'category': 'Heavy Metal, Neurotoxin',
        'risk_level': 'Critical',
        'common_names': ['lead acetate'],
        'details': 'Lead adalah logam berat yang sangat beracun, terutama berbahaya bagi anak-anak. Dapat merusak sistem saraf dan menyebabkan masalah perkembangan. Penggunaannya dalam kosmetik dilarang di banyak negara.'
    },
    'toluene': {
        'description': 'Can affect respiratory system and nervous system',
        'category': 'Toxin',
        'risk_level': 'High',
        'common_names': ['methylbenzene', 'toluol'],
        'details': 'Toluene adalah pelarut yang dapat mempengaruhi sistem pernapasan dan saraf. Sering ditemukan dalam cat kuku dan produk kosmetik lainnya. Paparan jangka panjang dapat menyebabkan masalah kesehatan serius.'
    },
    'bha': {
        'description': 'Possible endocrine disruptor and carcinogen',
        'category': 'Endocrine Disruptor, Possible Carcinogen',
        'risk_level': 'High',
        'common_names': ['butylated hydroxyanisole'],
        'details': 'BHA (Butylated Hydroxyanisole) adalah antioksidan sintetis yang diduga dapat mengganggu hormon dan berpotensi karsinogenik. Penggunaannya dibatasi di beberapa negara.'
    },
    'bht': {
        'description': 'Possible endocrine disruptor and skin allergen',
        'category': 'Endocrine Disruptor, Allergen',
        'risk_level': 'Medium',
        'common_names': ['butylated hydroxytoluene'],
        'details': 'BHT (Butylated Hydroxytoluene) adalah antioksidan sintetis yang dapat menyebabkan alergi kulit dan diduga mengganggu sistem hormon. Sering digunakan sebagai pengawet dalam kosmetik.'
    },
    'petrolatum': {
        'description': 'Can be contaminated with PAHs (polycyclic aromatic hydrocarbons) if not refined properly',
        'category': 'Contaminant Risk',
        'risk_level': 'Medium',
        'common_names': ['petroleum jelly', 'mineral oil jelly'],
        'details': 'Petrolatum yang tidak dimurnikan dengan baik dapat terkontaminasi dengan PAHs (polycyclic aromatic hydrocarbons) yang berpotensi karsinogenik. Pastikan menggunakan produk dengan petrolatum berkualitas farmasi.'
    },
    'phenoxyethanol': {
        'description': 'Preservative, can be an allergen and skin irritant (restricted in some countries)',
        'category': 'Preservative, Allergen, Irritant',
        'risk_level': 'Medium',
        'common_names': ['ethylene glycol phenyl ether'],
        'details': 'Phenoxyethanol adalah pengawet yang dapat menyebabkan alergi dan iritasi kulit. Penggunaannya dibatasi dalam produk bayi dan anak-anak di beberapa negara.'
    },
    'propylene glycol': {
        'description': 'Can be a skin irritant and allergen',
        'category': 'Irritant, Allergen',
        'risk_level': 'Medium',
        'common_names': ['1,2-propanediol'],
        'details': 'Propylene glycol dapat menyebabkan iritasi dan alergi kulit pada beberapa orang, terutama mereka dengan kulit sensitif. Namun, umumnya dianggap aman dalam konsentrasi rendah.'
    },
    'siloxane': {
        'description': 'Possible endocrine disruptors (especially cyclosiloxanes like cyclopentasiloxane and cyclohexasiloxane)',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'common_names': ['cyclopentasiloxane', 'cyclohexasiloxane', 'dimethicone', 'cyclomethicone'],
        'details': 'Beberapa siloxane, terutama cyclosiloxanes, diduga dapat mengganggu sistem hormon dan berbahaya bagi lingkungan. EU telah membatasi penggunaan beberapa jenis siloxane dalam kosmetik.'
    },
    'oxybenzone': {
        'description': 'Sunscreen ingredient, can be a hormone disruptor and marine pollutant',
        'category': 'Endocrine Disruptor, Environmental Hazard',
        'risk_level': 'High',
        'common_names': ['benzophenone-3'],
        'details': 'Oxybenzone adalah bahan tabir surya yang dapat mengganggu hormon dan berbahaya bagi ekosistem laut, terutama terumbu karang. Sudah dilarang di beberapa daerah wisata bahari.'
    },
    'benzoyl peroxide': {
        'description': 'Can be a skin irritant and sensitizer',
        'category': 'Irritant, Sensitizer',
        'risk_level': 'Medium',
        'common_names': ['benzyl peroxide'],
        'details': 'Benzoyl peroxide efektif untuk mengobati jerawat tetapi dapat menyebabkan iritasi, kekeringan, dan sensitivitas kulit. Penggunaan harus dimulai dengan konsentrasi rendah.'
    },
    'resorcinol': {
        'description': 'Possible endocrine disruptor and allergen',
        'category': 'Endocrine Disruptor, Allergen',
        'risk_level': 'High',
        'common_names': ['1,3-benzenediol'],
        'details': 'Resorcinol dapat mengganggu fungsi tiroid dan menyebabkan alergi kulit. Penggunaannya dalam kosmetik dibatasi di beberapa negara karena potensi risiko kesehatan.'
    },
    'synthetic dyes': {
        'description': 'Some synthetic dyes (e.g., coal tar dyes) can be carcinogens or allergens',
        'category': 'Possible Carcinogen, Allergen',
        'risk_level': 'High',
        'common_names': ['ci 19140', 'yellow 5', 'red 40'],
        'details': 'Beberapa pewarna sintetis, terutama yang berasal dari coal tar, dapat bersifat karsinogenik atau menyebabkan alergi. Pewarna tertentu telah dilarang dalam kosmetik di berbagai negara.'
    }
}

# Database bahan yang dikenal aman (diperluas)
KNOWN_SAFE_INGREDIENTS = {
    'aqua', 'water', 'glycerin', 'glycerine', 'hyaluronic acid', 'niacinamide', 
    'ceramide', 'panthenol', 'tocopherol', 'vitamin e', 'aloe vera', 'retinol',
    'salicylic acid', 'lactic acid', 'glycolic acid', 'mandelic acid', 'azelaic acid',
    'zinc oxide', 'titanium dioxide', 'dimethicone', 'squalane', 'peptides',
    'jojoba oil', 'argan oil', 'rosehip oil', 'shea butter', 'cocoa butter',
    'petrolatum', 'mineral oil', 'lanolin', 'beeswax', 'carnauba wax',
    'stearic acid', 'palmitic acid', 'oleic acid', 'linoleic acid', 'cetyl alcohol',
    'stearyl alcohol', 'cetearyl alcohol', 'sodium chloride', 'potassium sorbate',
    'phenoxyethanol', 'ethylhexylglycerin', 'caprylyl glycol', 'pentylene glycol',
    'propylene glycol', 'butylene glycol', 'hexylene glycol', 'carbomer',
    'xanthan gum', 'sodium hydroxide', 'citric acid', 'sodium citrate',
    'disodium edta', 'tetrasodium edta', 'allantoin', 'bisabolol',
    'chamomile', 'green tea', 'vitamin c', 'ascorbic acid', 'kojic acid',
    'arbutin', 'licorice extract', 'centella asiatica', 'calendula', 'cucumber'
}

def parse_ingredients(ingredients_text):
    """Fungsi untuk memparse dan membersihkan daftar bahan"""
    if not ingredients_text or not ingredients_text.strip():
        return []
    
    # Bersihkan teks dan split berdasarkan koma
    ingredients_text = ingredients_text.replace('\n', ' ').replace('\r', ' ')
    ingredients_text = re.sub(r'\s+', ' ', ingredients_text)  # Normalize whitespace
    
    # Split berdasarkan koma atau titik koma
    ingredients_list = [ing.strip().lower() for ing in re.split(r'[,;]+', ingredients_text) if ing.strip()]
    
    # Filter bahan yang terlalu pendek atau kosong
    ingredients_list = [ing for ing in ingredients_list if len(ing) > 2]
    
    return ingredients_list

def categorize_ingredients(ingredients_list):
    """Fungsi untuk mengkategorikan bahan menjadi berbahaya, aman, dan tidak dikenal"""
    dangerous = []
    safe = []
    unknown = []
    
    for ingredient in ingredients_list:
        ingredient_lower = ingredient.lower().strip()
        
        # Cek apakah bahan berbahaya
        is_dangerous = False
        for dangerous_key, data in DANGEROUS_INGREDIENTS.items():
            all_names = [dangerous_key] + data['common_names']
            if any(name.lower() in ingredient_lower or ingredient_lower in name.lower() for name in all_names):
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
            # Cek apakah bahan aman yang dikenal
            is_known_safe = False
            for safe_ingredient in KNOWN_SAFE_INGREDIENTS:
                if (safe_ingredient.lower() in ingredient_lower or 
                    ingredient_lower in safe_ingredient.lower() or
                    safe_ingredient.lower().replace(' ', '') in ingredient_lower.replace(' ', '')):
                    safe.append(ingredient)
                    is_known_safe = True
                    break
            
            # Jika tidak termasuk berbahaya atau aman yang dikenal, masukkan ke unknown
            if not is_known_safe:
                unknown.append(ingredient)
    
    return dangerous, safe, unknown

def analyze_ingredients(ingredients_text):
    """Fungsi untuk menganalisis bahan-bahan skincare"""
    ingredients_list = parse_ingredients(ingredients_text)
    
    if not ingredients_list:
        return {
            'is_safe': None,
            'dangerous_ingredients': [],
            'safe_ingredients': [],
            'unknown_ingredients': [],
            'total_ingredients': 0
        }
    
    dangerous, safe, unknown = categorize_ingredients(ingredients_list)
    
    return {
        'is_safe': len(dangerous) == 0,
        'dangerous_ingredients': dangerous,
        'safe_ingredients': safe,
        'unknown_ingredients': unknown,
        'total_ingredients': len(ingredients_list)
    }

def get_risk_color(risk_level):
    """Mendapatkan warna berdasarkan tingkat risiko"""
    colors = {
        'Critical': '#d32f2f',
        'High': '#f57c00',
        'Medium': '#fbc02d',
        'Low': '#388e3c'
    }
    return colors.get(risk_level, '#666666')

def display_results(results):
    """Fungsi untuk menampilkan hasil analisis dengan design yang diperbaiki"""
    if results['total_ingredients'] == 0:
        st.warning("⚠️ Tidak ada bahan yang terdeteksi. Pastikan Anda memasukkan daftar bahan dengan benar.")
        return
    
    # Summary statistics dengan design yang lebih baik
    st.markdown("### 📊 Ringkasan Analisis")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Bahan", 
            value=results['total_ingredients'],
            help="Total jumlah bahan yang dianalisis"
        )
    
    with col2:
        dangerous_count = len(results['dangerous_ingredients'])
        st.metric(
            label="Bahan Berbahaya", 
            value=dangerous_count,
            delta=f"-{dangerous_count}" if dangerous_count > 0 else "✓",
            delta_color="inverse" if dangerous_count > 0 else "normal",
            help="Jumlah bahan yang berpotensi berbahaya"
        )
    
    with col3:
        st.metric(
            label="Bahan Aman", 
            value=len(results['safe_ingredients']),
            delta=f"+{len(results['safe_ingredients'])}",
            delta_color="normal",
            help="Jumlah bahan yang dikenal aman"
        )
    
    with col4:
        st.metric(
            label="Tidak Dikenali", 
            value=len(results['unknown_ingredients']),
            help="Jumlah bahan yang tidak ada dalam database"
        )
    
    st.markdown("---")
    
    # Main safety assessment dengan design yang diperbaiki
    if len(results['dangerous_ingredients']) > 0:
        # Ada bahan berbahaya
        st.markdown(f"### ⚠️ Ditemukan {len(results['dangerous_ingredients'])} Bahan Berpotensi Berbahaya")
        
        # Peringatan utama
        st.error("""
        🚨 **PERINGATAN PENTING**
        
        Produk ini mengandung bahan-bahan yang berpotensi menimbulkan efek samping atau reaksi negatif pada kulit. 
        Kami menyarankan untuk mempertimbangkan kembali penggunaan produk ini, terutama jika Anda memiliki kulit sensitif.
        """)
        
        # Detail bahan berbahaya
        st.markdown("#### 🔍 Detail Bahan Berbahaya:")
        
        for i, ing in enumerate(results['dangerous_ingredients'], 1):
            risk_color = get_risk_color(ing['risk'])
            
            with st.expander(
                f"🚨 {ing['name'].title()} (Ditemukan sebagai: {ing['original_name']}) - "
                f"Risiko: {ing['risk']}", 
                expanded=i <= 2  # Expand first 2 items by default
            ):
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.markdown(f"**Kategori:** {ing['category']}")
                    st.markdown(f"**Tingkat Risiko:** <span style='color: {risk_color}; font-weight: bold;'>{ing['risk']}</span>", unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"**Deskripsi:** {ing['description']}")
                
                st.markdown("---")
                st.markdown(f"**Detail Lengkap:** {ing['details']}")
        
        # Rekomendasi alternatif
        st.markdown("#### 💡 Rekomendasi & Langkah Selanjutnya")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            **🔍 Cari Produk dengan Label:**
            - ✅ Paraben-free
            - ✅ Sulfate-free  
            - ✅ Fragrance-free
            - ✅ Hypoallergenic
            - ✅ Non-comedogenic
            - ✅ Dermatologist-tested
            """)
        
        with col2:
            st.info("""
            **🩺 Langkah yang Disarankan:**
            - 👨‍⚕️ Konsultasi dengan dermatolog
            - 🔍 Cari merek yang transparan
            - 📖 Baca review pengguna
            - 🌿 Pertimbangkan produk organik
            - 🧪 Lakukan patch test
            """)
    
    elif results['total_ingredients'] > 0:
        # Produk aman
        st.markdown("### ✅ Produk Ini Terindikasi Aman!")
        
        st.success("""
        🎉 **Selamat!** Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan. 
        
        Produk ini tampaknya menggunakan formulasi yang lebih aman untuk kulit. Namun, tetap perhatikan reaksi kulit Anda karena setiap orang memiliki sensitivitas yang berbeda.
        """)
        
        # Tips penggunaan produk aman
        st.markdown("#### 🌟 Tips Penggunaan Produk Aman")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            **🧪 Sebelum Penggunaan:**
            - Lakukan patch test 24-48 jam
            - Mulai dengan frekuensi rendah
            - Perhatikan reaksi kulit
            - Simpan di tempat sejuk & kering
            """)
        
        with col2:
            st.info("""
            **⚠️ Tetap Waspada:**
            - Hentikan jika ada iritasi
            - Konsultasi untuk kulit sensitif
            - Monitor perubahan kulit
            - Gunakan sunscreen jika ada AHA/BHA
            """)
    
    # Display bahan yang tidak dikenali
    if results['unknown_ingredients']:
        st.markdown("---")
        st.markdown("### 🔍 Bahan yang Tidak Dikenali")
        
        st.warning(f"Ditemukan {len(results['unknown_ingredients'])} bahan yang tidak ada dalam database kami.")
        
        with st.expander("📋 Lihat Daftar Bahan yang Tidak Dikenali", expanded=False):
            st.markdown("""
            **Catatan:** Bahan-bahan ini tidak otomatis berbahaya, namun tidak ada dalam database kami. 
            Disarankan untuk melakukan riset tambahan atau konsultasi dengan ahli.
            """)
            
            # Tampilkan dalam format yang lebih rapi
            unknown_list = results['unknown_ingredients']
            cols = st.columns(3)
            
            for i, ingredient in enumerate(unknown_list):
                col_idx = i % 3
                with cols[col_idx]:
                    st.write(f"• {ingredient.title()}")
    
    # Display bahan aman
    if results['safe_ingredients']:
        st.markdown("---")
        st.markdown("### ✅ Bahan yang Dikenal Aman")
        
        st.success(f"Ditemukan {len(results['safe_ingredients'])} bahan yang dikenal aman dan umum digunakan dalam produk skincare.")
        
        with st.expander("📋 Lihat Daftar Bahan Aman", expanded=False):
            safe_list = results['safe_ingredients']
            cols = st.columns(4)
            
            for i, ingredient in enumerate(safe_list):
                col_idx = i % 4
                with cols[col_idx]:
                    st.write(f"✅ {ingredient.title()}")

# Fungsi untuk halaman beranda
def show_home_page():
    """Menampilkan halaman beranda"""
    # Hero Section dengan design yang lebih menarik
    st.markdown("""
    <div class="hero-section">
        <h2 style="margin-bottom: 1rem; color: #2c2c2c;">Analisis Instan Berdasarkan Penelitian Ilmiah</h2>
        <p style="font-size: 1.2rem; color: #555555; margin-bottom: 0;">Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features dengan card design yang lebih baik
    st.markdown("#### Mengapa memilih platform ini?")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <div class="feature-title">Analisis Mendalam</div>
            <div class="feature-description">Sistem memeriksa berbagai jenis bahan berbahaya berdasarkan sumber terpercaya</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Hasil Instan</div>
            <div class="feature-description">Dapatkan hasil analisis komprehensif dalam hitungan detik</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Edukasi Komprehensif</div>
            <div class="feature-description">Pelajari tentang bahan berbahaya dan alternatif yang lebih aman</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <div class="feature-title">Keamanan Terjamin</div>
            <div class="feature-description">Berdasarkan regulasi dan penelitian ilmiah terbaru</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # How it works section
    st.markdown("####  Cara Menggunakan Platform")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: #f8f9fa; border-radius: 12px; height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">1️⃣</div>
            <h4 style="color: #2c2c2c; margin-bottom: 0.8rem;">Masukkan Daftar Bahan</h4>
            <p style="color: #555555; font-size: 0.9rem; margin: 0;">Salin dan tempel daftar bahan (INGREDIENTS) dari produk skincare Anda</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: #f8f9fa; border-radius: 12px; height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">2️⃣</div>
            <h4 style="color: #2c2c2c; margin-bottom: 0.8rem;">Proses Analisis</h4>
            <p style="color: #555555; font-size: 0.9rem; margin: 0;">Sistem akan memindai bahan-bahan yang terindikasi berbahaya</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: #f8f9fa; border-radius: 12px; height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">3️⃣</div>
            <h4 style="color: #2c2c2c; margin-bottom: 0.8rem;">Dapatkan Hasil</h4>
            <p style="color: #555555; font-size: 0.9rem; margin: 0;">Lihat laporan lengkap tentang keamanan produk dan rekomendasi</p>
        </div>
        """, unsafe_allow_html=True)
    

# Fungsi untuk halaman analisis
def show_analysis_page():
    """Menampilkan halaman analisis bahan"""
    st.markdown("Masukkan daftar bahan produk skincare Anda di bawah ini untuk memeriksa potensi bahan berbahaya")
    
    # Input form dengan design yang diperbaiki
    st.markdown("#### Input Bahan")
    
    ingredients = st.text_area(
        "**Daftar Bahan (INGREDIENTS):**",
        placeholder="Contoh: Aqua, Glycerin, Niacinamide, Sodium Hyaluronate, Panthenol, Tocopherol, Phenoxyethanol, Ethylhexylglycerin",
        height=120,
        help="💡 Tips: Salin dan tempel daftar bahan dari kemasan produk atau website resmi. Pisahkan dengan koma."
    )
    
    # Tombol analisis
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button(
            "🔬 **Analisis Bahan Sekarang**", 
            type="primary", 
            use_container_width=True,
            help="Klik untuk memulai analisis keamanan bahan"
        )
    
    if analyze_button:
        if not ingredients or not ingredients.strip():
            st.error("⚠️ **Silakan masukkan daftar bahan terlebih dahulu**")
            st.info("💡 **Tip:** Salin daftar bahan dari kemasan produk atau website resmi, lalu tempel di area teks di atas.")
        else:
            with st.spinner("🔬 Menganalisis bahan-bahan... Mohon tunggu sebentar."):
                # Progress bar untuk UX yang lebih baik
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                results = analyze_ingredients(ingredients)
                st.markdown("---")
                display_results(results)

# Fungsi untuk halaman tentang
def show_about_page():
    """Menampilkan halaman tentang website"""
    # Hero section untuk About
    st.markdown("""
    <div class="hero-section">
        <h3 style="margin-bottom: 1rem; color: #2c2c2c;">Transparansi Untuk Kesehatan Kulit Anda</h3>
        <p style="font-size: 1.2rem; color: #555555; margin-bottom: 0;">Memberdayakan konsumen dengan informasi berbasis sains tentang keamanan produk skincare</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content dalam 2 kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card" style="height: 280px;">
            <h4 style="color: #e91e63; margin-top: 0;">🎯 Tujuan </h4>
            <p style="line-height: 1.6; flex-grow: 1; text-align: justify;">
            Bertujuan untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit. Tujuan dibuatnya platform ini adalah memberdayakan konsumen untuk membuat pilihan yang tepat berdasarkan data dan penelitian ilmiah terkini.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card" style="height: 280px; margin-top: 1rem;">
            <h4 style="color: #e91e63; margin-top: 0;">🔬 Metodologi</h4>
            <div style="flex-grow: 1;">
                <p style="margin-bottom: 1rem; line-height: 1.6; text-align: justify;">Platform ini dikembangkan berdasarkan:</p>
                <div style="line-height: 1.8;">
                    <div>• Regulasi Uni Eropa (EU Regulation No. 1223/2009)</div>
                    <div>• Pedoman BPOM Indonesia</div>
                    <div>• Standar FDA tentang kosmetik</div>
                    <div>• Penelitian ilmiah peer-reviewed</div>
                    <div>• Database keamanan internasional</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card" style="height: 280px;">
            <h4 style="color: #e91e63; margin-top: 0;">📚 Sumber Data</h4>
            <div style="flex-grow: 1;">
                <p style="margin-bottom: 1rem; line-height: 1.6; text-align: justify;">Informasi dalam platform ini bersumber dari:</p>
                <div style="line-height: 1.8;">
                    <div>• Environmental Working Group (EWG)</div>
                    <div>• Cosmetic Ingredient Review (CIR)</div>
                    <div>• Journal of the American Academy of Dermatology</div>
                    <div>• BPOM RI</div>
                    <div>• European Medicines Agency</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card" style="height: 280px; margin-top: 1rem;">
            <h4 style="color: #e91e63; margin-top: 0;">💡 Tips Memilih Skincare Aman</h4>
            <div style="flex-grow: 1;">
                <div style="line-height: 1.8;">
                    <div><strong>📖 Baca Label:</strong> Selalu periksa daftar bahan sebelum membeli</div>
                    <div><strong>🎯 Mulai Sederhana:</strong> Produk dengan daftar bahan pendek cenderung lebih aman</div>
                    <div><strong>🧪 Uji Sensitivitas:</strong> Selalu lakukan patch test sebelum penggunaan penuh</div>
                    <div><strong>👨‍⚕️ Konsultasi Ahli:</strong> Tanyakan pada dermatolog untuk kulit sensitif</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics section
    st.markdown("---")
    st.markdown("#### 📊 Statistik Platform")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Bahan Berbahaya",
            value=len(DANGEROUS_INGREDIENTS),
            help="Jumlah bahan berbahaya dalam database"
        )
    
    with col2:
        st.metric(
            label="Bahan Aman",
            value=len(KNOWN_SAFE_INGREDIENTS),
            help="Jumlah bahan aman dalam database"
        )
    
    with col3:
        st.metric(
            label="Kategori Risiko",
            value="4",
            help="Critical, High, Medium, Low"
        )
    
    with col4:
        st.metric(
            label="Sumber Referensi",
            value="10+",
            help="Jurnal dan regulasi internasional"
        )
    
    # Disclaimer dengan styling yang lebih menarik
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffecb3 100%); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #ff9800; margin-top: 2rem;">
        <h4 style="color: #ef6c00; margin-top: 0;">⚠️ Disclaimer Penting</h4>
        <p style="margin-bottom: 0; line-height: 1.6; color: #bf360c; text-align: justify;">
        Platform ini hanya untuk tujuan informasi dan edukasi. Tidak menggantikan nasihat profesional dari dermatolog atau ahli kesehatan kulit. Selalu konsultasikan dengan profesional kesehatan untuk masalah kulit yang serius atau jika Anda memiliki kondisi kulit tertentu. Hasil analisis berdasarkan database yang terus diperbarui sesuai penelitian terbaru.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main App Function
def main():
    """Fungsi utama aplikasi"""
    # Header dengan styling modern
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0 2rem 0;">
        <div style="display: inline-flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
            <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #e91e63, #c2185b); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: bold;">🧪</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.title("Pemeriksa Keamanan Skincare")
    st.markdown("### Temukan Analisis Mendalam Mengenai Produk Perawatan Kulit Anda")
    
    # Initialize session state for tab management
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "Beranda"
    
    # Navigation tabs
    tabs = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "ℹ️ Tentang Platform"])
    
    with tabs[0]:
        show_home_page()
    
    with tabs[1]:
        show_analysis_page()
    
    with tabs[2]:
        show_about_page()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p><strong>© 2025 Pemeriksa Keamanan Skincare</strong></p>
        <p style="margin-top: 0.5rem;">Dibuat dengan ❤️ untuk kulit yang lebih sehat dan terawat</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #888;">
            Platform ini dikembangkan untuk edukasi dan informasi. Selalu konsultasikan dengan ahli untuk keputusan kesehatan kulit Anda.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
