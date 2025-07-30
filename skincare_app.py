# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import pandas as pd# app.py - Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="🧪 Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS dengan warna pink soft dan lilac
st.markdown("""
<style>
/* Background utama aplikasi dengan gradasi lilac */
.stApp {
    background: linear-gradient(135deg, #E8D5F2 0%, #D8BFD8 50%, #DDA0DD 100%);
}

/* Background untuk main content area */
.main .block-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    margin-top: 1rem;
}

/* Header utama */
.main-header {
    background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0 8px 32px rgba(255, 105, 180, 0.3);
    margin-bottom: 2rem;
}

/* Card untuk hasil aman - pink soft */
.safe-card {
    background: linear-gradient(135deg, #FFB6C1 0%, #FFC0CB 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #28a745;
    color: #2d5016;
    box-shadow: 0 4px 15px rgba(255, 182, 193, 0.4);
    margin: 1rem 0;
}

/* Card untuk hasil bahaya - pink lebih gelap */
.danger-card {
    background: linear-gradient(135deg, #FFB6C1 0%, #FF91A4 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #dc3545;
    color: #721c24;
    box-shadow: 0 4px 15px rgba(255, 145, 164, 0.4);
    margin: 1rem 0;
}

/* Item bahan berbahaya - pink soft dengan border */
.ingredient-item {
    background: linear-gradient(135deg, #FFC0CB 0%, #FFE4E1 100%);
    padding: 1.2rem;
    border-radius: 12px;
    border-left: 4px solid #dc3545;
    margin: 0.8rem 0;
    color: #8b1538;
    box-shadow: 0 2px 10px rgba(255, 192, 203, 0.3);
}

/* Sidebar styling */
.css-1d391kg {
    background: linear-gradient(180deg, #E8D5F2 0%, #DDA0DD 100%);
}

/* Text area styling */
.stTextArea > div > div > textarea {
    font-size: 16px;
    background: rgba(139, 21, 56, 0.8) !important;
    color: white !important;
    border-radius: 10px;
    border: 2px solid #DDA0DD;
}

.stTextArea > div > div > textarea::placeholder {
    color: rgba(255, 255, 255, 0.7) !important;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 2rem;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 105, 180, 0.4);
}

/* Header styling */
h1, h2, h3 {
    color: #8b1538;
}

/* Sidebar header */
.css-1lcbmhc {
    color: #8b1538;
    font-weight: bold;
}

/* Info box styling */
.stAlert {
    background: rgba(255, 192, 203, 0.3);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

class SkincareAnalyzer:
    def __init__(self):
        self.dangerous_ingredients = {
            'paraben': {
                'description': 'Dapat mengganggu sistem hormon (Regulasi EU No. 1223/2009)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['methylparaben', 'propylparaben', 'butylparaben']
            },
            'sulfate': {
                'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
                'category': 'Iritan',
                'risk_level': 'Sedang',
                'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate']
            },
            'phthalate': {
                'description': 'Dapat mengganggu hormon dan mempengaruhi kesehatan reproduksi (Regulasi EU No. 1223/2009)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['dibutyl phthalate (dbp)', 'diethylhexyl phthalate (dehp)']
            },
            'formaldehyde': {
                'description': 'Karsinogen yang diketahui dan dapat menyebabkan sensitisasi kulit',
                'category': 'Karsinogen, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['formalin', 'methylene glycol', 'quaternium-15']
            },
            'mercury': {
                'description': 'Neurotoksin, berbahaya bagi ginjal dan sistem saraf',
                'category': 'Logam Berat, Neurotoksin',
                'risk_level': 'Kritis',
                'common_names': ['calomel', 'mercuric chloride']
            },
            'hydroquinone': {
                'description': 'Pemutih kulit, dapat menyebabkan ochronosis (perubahan warna kulit)',
                'category': 'Iritan Kulit, Pengganggu Pigmentasi',
                'risk_level': 'Tinggi',
                'common_names': ['dihydroxybenzene', 'quinol']
            },
            'triclosan': {
                'description': 'Dapat mengganggu hormon dan berkontribusi pada resistensi antibiotik',
                'category': 'Pengganggu Endokrin, Resistensi Antibiotik',
                'risk_level': 'Tinggi',
                'common_names': ['triclosan', 'tcs']
            },
            'alcohol': {
                'description': 'Dapat membuat kulit kering dan iritasi pada beberapa jenis kulit (tergantung jenis dan konsentrasi)',
                'category': 'Iritan, Pengering',
                'risk_level': 'Sedang',
                'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol']
            },
            'fragrance': {
                'description': 'Alergen umum dan dapat menyebabkan iritasi kulit (sering merupakan campuran bahan kimia yang tidak diungkapkan)',
                'category': 'Alergen, Iritan',
                'risk_level': 'Sedang',
                'common_names': ['parfum', 'perfume', 'aroma']
            },
            'lead': {
                'description': 'Neurotoksin, berbahaya bagi sistem saraf (terutama pada anak-anak)',
                'category': 'Logam Berat, Neurotoksin',
                'risk_level': 'Kritis',
                'common_names': ['lead acetate']
            },
             'toluene': {
                'description': 'Dapat mempengaruhi sistem pernapasan dan sistem saraf',
                'category': 'Toksin',
                'risk_level': 'Tinggi',
                'common_names': ['methylbenzene', 'toluol']
            },
            'bha': {
                'description': 'Kemungkinan pengganggu endokrin dan karsinogen',
                'category': 'Pengganggu Endokrin, Kemungkinan Karsinogen',
                'risk_level': 'Tinggi',
                'common_names': ['butylated hydroxyanisole']
            },
            'bht': {
                'description': 'Kemungkinan pengganggu endokrin dan alergen kulit',
                'category': 'Pengganggu Endokrin, Alergen',
                'risk_level': 'Sedang',
                'common_names': ['butylated hydroxytoluene']
            },
            'petrolatum': {
                'description': 'Dapat terkontaminasi dengan PAH (polycyclic aromatic hydrocarbons) jika tidak dimurnikan dengan baik',
                'category': 'Risiko Kontaminan',
                'risk_level': 'Sedang',
                'common_names': ['petroleum jelly', 'mineral oil jelly']
            },
             'phenoxyethanol': {
                'description': 'Pengawet, dapat menjadi alergen dan iritan kulit (dibatasi di beberapa negara)',
                'category': 'Pengawet, Alergen, Iritan',
                'risk_level': 'Sedang',
                'common_names': ['ethylene glycol phenyl ether']
            },
            'propylene glycol': {
                'description': 'Dapat menjadi iritan kulit dan alergen',
                'category': 'Iritan, Alergen',
                'risk_level': 'Sedang',
                'common_names': ['1,2-propanediol']
            },
            'siloxane': {
                'description': 'Kemungkinan pengganggu endokrin (terutama siklosiloksan seperti cyclopentasiloxane dan cyclohexasiloxane)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['cyclopentasiloxane', 'cyclohexasiloxane', 'dimethicone', 'cyclomethicone']
            },
             'oxybenzone': {
                'description': 'Bahan tabir surya, dapat menjadi pengganggu hormon dan polutan laut',
                'category': 'Pengganggu Endokrin, Bahaya Lingkungan',
                'risk_level': 'Tinggi',
                'common_names': ['benzophenone-3']
            },
            'benzoyl peroxide': {
                'description': 'Dapat menjadi iritan kulit dan sensitizer',
                'category': 'Iritan, Sensitizer',
                'risk_level': 'Sedang',
                'common_names': ['benzyl peroxide']
            },
            'resorcinol': {
                'description': 'Kemungkinan pengganggu endokrin dan alergen',
                'category': 'Pengganggu Endokrin, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['1,3-benzenediol']
            },
            'synthetic dyes': {
                'description': 'Beberapa pewarna sintetis (misalnya pewarna tar batubara) dapat menjadi karsinogen atau alergen',
                'category': 'Kemungkinan Karsinogen, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['ci 19140', 'yellow 5', 'red 40']
            }
        }

    def analyze_ingredients(self, ingredients_text):
        ingredients_text_lower = ingredients_text.lower()
        found_dangerous = []
        is_safe = True
        for ingredient, data in self.dangerous_ingredients.items():
            # Periksa nama bahan utama
            if ingredient in ingredients_text_lower:
                found_dangerous.append({'name': ingredient, 'description': data['description'], 'category': data['category'], 'risk_level': data['risk_level']})
                is_safe = False
                continue # Tidak perlu memeriksa nama umum jika nama utama ditemukan

            # Periksa nama umum
            if 'common_names' in data:
                for common_name in data['common_names']:
                    if common_name in ingredients_text_lower:
                        found_dangerous.append({'name': common_name, 'description': data['description'], 'category': data['category'], 'risk_level': data['risk_level']})
                        is_safe = False
                        break # Pindah ke bahan utama berikutnya setelah nama umum ditemukan

        return is_safe, found_dangerous

# Instantiate analyzer
analyzer = SkincareAnalyzer()

# Layout Aplikasi Streamlit
st.markdown('<div class="main-header"><h1>🧪 Pemeriksa Keamanan Bahan Skincare</h1><p>Periksa keamanan produk skincare Anda dengan mudah dan cepat</p></div>', unsafe_allow_html=True)

# Area Input
st.header("📝 Masukkan Daftar Bahan Skincare:")
ingredient_input = st.text_area(
    "Tempel daftar bahan di sini:", 
    height=150, 
    placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate",
    help="Salin dan tempel daftar bahan dari kemasan produk skincare Anda"
)

# Tombol Analisis
if st.button("🔍 Analisis Bahan", help="Klik untuk memeriksa keamanan bahan-bahan"):
    if ingredient_input:
        st.subheader("📊 Hasil Analisis:")
        with st.spinner("Sedang menganalisis..."):
            is_safe, dangerous_ingredients_found = analyzer.analyze_ingredients(ingredient_input)
            time.sleep(1) # Simulasi waktu pemrosesan

        if is_safe:
            st.markdown('''
            <div class="safe-card">
                <h2>✅ Bahan Aman</h2>
                <p>Berdasarkan daftar yang diberikan, tidak ditemukan bahan berbahaya yang umum diketahui. 
                Produk ini kemungkinan aman untuk digunakan.</p>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown('''
            <div class="danger-card">
                <h2>⚠️ Ditemukan Bahan Berpotensi Berbahaya</h2>
                <p>Harap berhati-hati dengan bahan-bahan berikut dalam produk Anda:</p>
            </div>
            ''', unsafe_allow_html=True)
            
            for ingredient_info in dangerous_ingredients_found:
                st.markdown(f"""
                <div class="ingredient-item">
                    <strong>🚨 {ingredient_info['name'].title()}</strong>
                    <p><strong>Tingkat Risiko:</strong> <span style="color: #dc3545;">{ingredient_info['risk_level']}</span></p>
                    <p><strong>Kategori:</strong> {ingredient_info['category']}</p>
                    <p><strong>Penjelasan:</strong> {ingredient_info['description']}</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Silakan masukkan daftar bahan untuk dianalisis.")

# Bagian Informasi di Sidebar
st.sidebar.header("ℹ️ Tentang Aplikasi")
st.sidebar.info(
    "Alat ini memeriksa daftar bahan skincare terhadap daftar zat yang berpotensi berbahaya. "
    "**Catatan Penting:** Ini adalah alat dasar dan bukan pengganti saran profesional. "
    "Keamanan bahan dapat bergantung pada konsentrasi, konteks, dan sensitivitas individu."
)

st.sidebar.header("🔍 Bahan Berbahaya yang Diperiksa")
dangerous_list = [f"- **{k.title()}**: {v['description']}" for k, v in analyzer.dangerous_ingredients.items()]
st.sidebar.markdown("\n".join(dangerous_list))

st.sidebar.header("⚠️ Peringatan")
st.sidebar.warning(
    "Selalu konsultasikan dengan dermatologis untuk masalah kulit serius. "
    "Aplikasi ini hanya untuk referensi dan tidak menggantikan konsultasi medis profesional."
)

st.sidebar.header("📞 Kontak")
st.sidebar.info(
    "Jika Anda memiliki pertanyaan atau saran untuk pengembangan aplikasi ini, "
    "silakan hubungi tim pengembang."
)
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="🧪 Pemeriksa Keamanan Skincare",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS dengan warna pink soft dan lilac
st.markdown("""
<style>
/* Background utama aplikasi dengan gradasi lilac */
.stApp {
    background: linear-gradient(135deg, #E8D5F2 0%, #D8BFD8 50%, #DDA0DD 100%);
}

/* Background untuk main content area */
.main .block-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    margin-top: 1rem;
}

/* Header utama */
.main-header {
    background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0 8px 32px rgba(255, 105, 180, 0.3);
    margin-bottom: 2rem;
}

/* Card untuk hasil aman - pink soft */
.safe-card {
    background: linear-gradient(135deg, #FFB6C1 0%, #FFC0CB 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #28a745;
    color: #2d5016;
    box-shadow: 0 4px 15px rgba(255, 182, 193, 0.4);
    margin: 1rem 0;
}

/* Card untuk hasil bahaya - pink lebih gelap */
.danger-card {
    background: linear-gradient(135deg, #FFB6C1 0%, #FF91A4 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #dc3545;
    color: #721c24;
    box-shadow: 0 4px 15px rgba(255, 145, 164, 0.4);
    margin: 1rem 0;
}

/* Item bahan berbahaya - pink soft dengan border */
.ingredient-item {
    background: linear-gradient(135deg, #FFC0CB 0%, #FFE4E1 100%);
    padding: 1.2rem;
    border-radius: 12px;
    border-left: 4px solid #dc3545;
    margin: 0.8rem 0;
    color: #8b1538;
    box-shadow: 0 2px 10px rgba(255, 192, 203, 0.3);
}

/* Sidebar styling */
.css-1d391kg {
    background: linear-gradient(180deg, #E8D5F2 0%, #DDA0DD 100%);
}

/* Text area styling */
.stTextArea > div > div > textarea {
    font-size: 16px;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    border: 2px solid #DDA0DD;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 2rem;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 105, 180, 0.4);
}

/* Header styling */
h1, h2, h3 {
    color: #8b1538;
}

/* Sidebar header */
.css-1lcbmhc {
    color: #8b1538;
    font-weight: bold;
}

/* Info box styling */
.stAlert {
    background: rgba(255, 192, 203, 0.3);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

class SkincareAnalyzer:
    def __init__(self):
        self.dangerous_ingredients = {
            'paraben': {
                'description': 'Dapat mengganggu sistem hormon (Regulasi EU No. 1223/2009)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['methylparaben', 'propylparaben', 'butylparaben']
            },
            'sulfate': {
                'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
                'category': 'Iritan',
                'risk_level': 'Sedang',
                'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate']
            },
            'phthalate': {
                'description': 'Dapat mengganggu hormon dan mempengaruhi kesehatan reproduksi (Regulasi EU No. 1223/2009)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['dibutyl phthalate (dbp)', 'diethylhexyl phthalate (dehp)']
            },
            'formaldehyde': {
                'description': 'Karsinogen yang diketahui dan dapat menyebabkan sensitisasi kulit',
                'category': 'Karsinogen, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['formalin', 'methylene glycol', 'quaternium-15']
            },
            'mercury': {
                'description': 'Neurotoksin, berbahaya bagi ginjal dan sistem saraf',
                'category': 'Logam Berat, Neurotoksin',
                'risk_level': 'Kritis',
                'common_names': ['calomel', 'mercuric chloride']
            },
            'hydroquinone': {
                'description': 'Pemutih kulit, dapat menyebabkan ochronosis (perubahan warna kulit)',
                'category': 'Iritan Kulit, Pengganggu Pigmentasi',
                'risk_level': 'Tinggi',
                'common_names': ['dihydroxybenzene', 'quinol']
            },
            'triclosan': {
                'description': 'Dapat mengganggu hormon dan berkontribusi pada resistensi antibiotik',
                'category': 'Pengganggu Endokrin, Resistensi Antibiotik',
                'risk_level': 'Tinggi',
                'common_names': ['triclosan', 'tcs']
            },
            'alcohol': {
                'description': 'Dapat membuat kulit kering dan iritasi pada beberapa jenis kulit (tergantung jenis dan konsentrasi)',
                'category': 'Iritan, Pengering',
                'risk_level': 'Sedang',
                'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol']
            },
            'fragrance': {
                'description': 'Alergen umum dan dapat menyebabkan iritasi kulit (sering merupakan campuran bahan kimia yang tidak diungkapkan)',
                'category': 'Alergen, Iritan',
                'risk_level': 'Sedang',
                'common_names': ['parfum', 'perfume', 'aroma']
            },
            'lead': {
                'description': 'Neurotoksin, berbahaya bagi sistem saraf (terutama pada anak-anak)',
                'category': 'Logam Berat, Neurotoksin',
                'risk_level': 'Kritis',
                'common_names': ['lead acetate']
            },
             'toluene': {
                'description': 'Dapat mempengaruhi sistem pernapasan dan sistem saraf',
                'category': 'Toksin',
                'risk_level': 'Tinggi',
                'common_names': ['methylbenzene', 'toluol']
            },
            'bha': {
                'description': 'Kemungkinan pengganggu endokrin dan karsinogen',
                'category': 'Pengganggu Endokrin, Kemungkinan Karsinogen',
                'risk_level': 'Tinggi',
                'common_names': ['butylated hydroxyanisole']
            },
            'bht': {
                'description': 'Kemungkinan pengganggu endokrin dan alergen kulit',
                'category': 'Pengganggu Endokrin, Alergen',
                'risk_level': 'Sedang',
                'common_names': ['butylated hydroxytoluene']
            },
            'petrolatum': {
                'description': 'Dapat terkontaminasi dengan PAH (polycyclic aromatic hydrocarbons) jika tidak dimurnikan dengan baik',
                'category': 'Risiko Kontaminan',
                'risk_level': 'Sedang',
                'common_names': ['petroleum jelly', 'mineral oil jelly']
            },
             'phenoxyethanol': {
                'description': 'Pengawet, dapat menjadi alergen dan iritan kulit (dibatasi di beberapa negara)',
                'category': 'Pengawet, Alergen, Iritan',
                'risk_level': 'Sedang',
                'common_names': ['ethylene glycol phenyl ether']
            },
            'propylene glycol': {
                'description': 'Dapat menjadi iritan kulit dan alergen',
                'category': 'Iritan, Alergen',
                'risk_level': 'Sedang',
                'common_names': ['1,2-propanediol']
            },
            'siloxane': {
                'description': 'Kemungkinan pengganggu endokrin (terutama siklosiloksan seperti cyclopentasiloxane dan cyclohexasiloxane)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['cyclopentasiloxane', 'cyclohexasiloxane', 'dimethicone', 'cyclomethicone']
            },
             'oxybenzone': {
                'description': 'Bahan tabir surya, dapat menjadi pengganggu hormon dan polutan laut',
                'category': 'Pengganggu Endokrin, Bahaya Lingkungan',
                'risk_level': 'Tinggi',
                'common_names': ['benzophenone-3']
            },
            'benzoyl peroxide': {
                'description': 'Dapat menjadi iritan kulit dan sensitizer',
                'category': 'Iritan, Sensitizer',
                'risk_level': 'Sedang',
                'common_names': ['benzyl peroxide']
            },
            'resorcinol': {
                'description': 'Kemungkinan pengganggu endokrin dan alergen',
                'category': 'Pengganggu Endokrin, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['1,3-benzenediol']
            },
            'synthetic dyes': {
                'description': 'Beberapa pewarna sintetis (misalnya pewarna tar batubara) dapat menjadi karsinogen atau alergen',
                'category': 'Kemungkinan Karsinogen, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['ci 19140', 'yellow 5', 'red 40']
            }
        }

    def analyze_ingredients(self, ingredients_text):
        ingredients_text_lower = ingredients_text.lower()
        found_dangerous = []
        is_safe = True
        for ingredient, data in self.dangerous_ingredients.items():
            # Periksa nama bahan utama
            if ingredient in ingredients_text_lower:
                found_dangerous.append({'name': ingredient, 'description': data['description'], 'category': data['category'], 'risk_level': data['risk_level']})
                is_safe = False
                continue # Tidak perlu memeriksa nama umum jika nama utama ditemukan

            # Periksa nama umum
            if 'common_names' in data:
                for common_name in data['common_names']:
                    if common_name in ingredients_text_lower:
                        found_dangerous.append({'name': common_name, 'description': data['description'], 'category': data['category'], 'risk_level': data['risk_level']})
                        is_safe = False
                        break # Pindah ke bahan utama berikutnya setelah nama umum ditemukan

        return is_safe, found_dangerous

# Instantiate analyzer
analyzer = SkincareAnalyzer()

# Layout Aplikasi Streamlit
st.markdown('<div class="main-header"><h1>🧪 Pemeriksa Keamanan Bahan Skincare</h1><p>Periksa keamanan produk skincare Anda dengan mudah dan cepat</p></div>', unsafe_allow_html=True)

# Area Input
st.header("📝 Masukkan Daftar Bahan Skincare:")
ingredient_input = st.text_area(
    "Tempel daftar bahan di sini:", 
    height=150, 
    placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate",
    help="Salin dan tempel daftar bahan dari kemasan produk skincare Anda"
)

# Tombol Analisis
if st.button("🔍 Analisis Bahan", help="Klik untuk memeriksa keamanan bahan-bahan"):
    if ingredient_input:
        st.subheader("📊 Hasil Analisis:")
        with st.spinner("Sedang menganalisis..."):
            is_safe, dangerous_ingredients_found = analyzer.analyze_ingredients(ingredient_input)
            time.sleep(1) # Simulasi waktu pemrosesan

        if is_safe:
            st.markdown('''
            <div class="safe-card">
                <h2>✅ Bahan Aman</h2>
                <p>Berdasarkan daftar yang diberikan, tidak ditemukan bahan berbahaya yang umum diketahui. 
                Produk ini kemungkinan aman untuk digunakan.</p>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown('''
            <div class="danger-card">
                <h2>⚠️ Ditemukan Bahan Berpotensi Berbahaya</h2>
                <p>Harap berhati-hati dengan bahan-bahan berikut dalam produk Anda:</p>
            </div>
            ''', unsafe_allow_html=True)
            
            for ingredient_info in dangerous_ingredients_found:
                st.markdown(f"""
                <div class="ingredient-item">
                    <strong>🚨 {ingredient_info['name'].title()}</strong>
                    <p><strong>Tingkat Risiko:</strong> <span style="color: #dc3545;">{ingredient_info['risk_level']}</span></p>
                    <p><strong>Kategori:</strong> {ingredient_info['category']}</p>
                    <p><strong>Penjelasan:</strong> {ingredient_info['description']}</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Silakan masukkan daftar bahan untuk dianalisis.")

# Bagian Informasi di Sidebar
st.sidebar.header("ℹ️ Tentang Aplikasi")
st.sidebar.info(
    "Alat ini memeriksa daftar bahan skincare terhadap daftar zat yang berpotensi berbahaya. "
    "**Catatan Penting:** Ini adalah alat dasar dan bukan pengganti saran profesional. "
    "Keamanan bahan dapat bergantung pada konsentrasi, konteks, dan sensitivitas individu."
)

st.sidebar.header("🔍 Bahan Berbahaya yang Diperiksa")
dangerous_list = [f"- **{k.title()}**: {v['description']}" for k, v in analyzer.dangerous_ingredients.items()]
st.sidebar.markdown("\n".join(dangerous_list))

st.sidebar.header("⚠️ Peringatan")
st.sidebar.warning(
    "Selalu konsultasikan dengan dermatologis untuk masalah kulit serius. "
    "Aplikasi ini hanya untuk referensi dan tidak menggantikan konsultasi medis profesional."
)

st.sidebar.header("📞 Kontak")
st.sidebar.info(
    "Jika Anda memiliki pertanyaan atau saran untuk pengembangan aplikasi ini, "
    "silakan hubungi tim pengembang."
)
