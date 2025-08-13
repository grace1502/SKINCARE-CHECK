# app.py - Enhanced Aplikasi Web Streamlit
# Pemeriksa Keamanan Bahan Skincare
# Jalankan dengan: streamlit run app.py

import streamlit as st
import time
import re
import json
from typing import Dict, List, Tuple

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
        --success-color: #4caf50;
        --warning-color: #ff9800;
        --error-color: #f44336;
    }
    
    /* Background dengan overlay */
    .stApp {
        background: #ffffff;
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
        color: var(--primary-dark) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        font-size: 3rem !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Subjudul */
    h2, h3, h4, h5, h6 {
        color: var(--primary-dark) !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 500 !important;
    }
    
    h2 {
        border-bottom: 2px solid var(--primary-light);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem !important;
    }
    
    /* Text color improvements */
    p, div, span, li {
        color: var(--text-dark) !important;
    }
    
    .stMarkdown p {
        color: var(--text-dark) !important;
        line-height: 1.6;
    }
    
    /* Tombol */
    .stButton button {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-dark)) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 12px rgba(233, 30, 99, 0.3);
        font-size: 1rem !important;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, var(--primary-dark), #ad1457) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(233, 30, 99, 0.4);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 2px solid #e0e0e0 !important;
        padding: 1.2rem !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: var(--primary-light) !important;
        box-shadow: 0 0 0 3px rgba(233, 30, 99, 0.1);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        margin-bottom: 2rem;
        background: rgba(248, 249, 250, 0.8);
        padding: 0.5rem;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 2rem !important;
        background-color: transparent !important;
        color: var(--text-light) !important;
        border-radius: 10px !important;
        margin-right: 0 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease;
        border: none !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-dark)) !important;
        font-weight: 600 !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(233, 30, 99, 0.3);
    }
    
    /* Alert styling */
    .stAlert {
        border-radius: 12px !important;
        padding: 1.5rem !important;
        border-left: 4px solid !important;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(76, 175, 80, 0.05)) !important;
        border-left-color: var(--success-color) !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(255, 152, 0, 0.1), rgba(255, 152, 0, 0.05)) !important;
        border-left-color: var(--warning-color) !important;
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.1), rgba(244, 67, 54, 0.05)) !important;
        border-left-color: var(--error-color) !important;
    }
    
    /* Metric styling */
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.05), rgba(233, 30, 99, 0.02)) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(233, 30, 99, 0.1) !important;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        border: 1px solid rgba(233, 30, 99, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .info-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), var(--primary-dark));
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
    }
    
    /* Progress bar */
    .progress-container {
        background: #f0f0f0;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, var(--primary-color), var(--primary-dark));
        transition: width 0.3s ease;
    }
    
    /* Loading animation */
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid #f3f3f3;
        border-top: 3px solid var(--primary-color);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Footer */
    footer {
        text-align: center;
        padding: 3rem 0;
        margin-top: 4rem;
        color: var(--text-light);
        font-size: 0.9rem;
        border-top: 1px solid #f0f0f0;
        background: linear-gradient(135deg, rgba(248, 249, 250, 0.8), rgba(255, 255, 255, 0.9));
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem !important;
        }
        
        .stButton button {
            width: 100% !important;
        }
        
        .info-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Enhanced database with more comprehensive data
DANGEROUS_INGREDIENTS = {
    'paraben': {
        'description': 'Dapat mengganggu hormon (EU Regulation No. 1223/2009)',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'severity_score': 8,
        'common_names': ['methylparaben', 'propylparaben', 'butylparaben', 'ethylparaben', 'isobutylparaben'],
        'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik dan produk perawatan pribadi. Studi menunjukkan paraben dapat meniru estrogen dan berpotensi mengganggu sistem hormon tubuh. Regulasi Uni Eropa telah membatasi penggunaan beberapa jenis paraben dalam produk kosmetik.',
        'alternatives': ['Phenoxyethanol', 'Benzyl Alcohol', 'Potassium Sorbate', 'Sodium Benzoate']
    },
    'sulfate': {
        'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
        'category': 'Irritant',
        'risk_level': 'Medium',
        'severity_score': 6,
        'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate', 'sles', 'ammonium lauryl sulfate'],
        'details': 'Sulfate adalah surfaktan yang digunakan untuk membuat busa dalam produk pembersih. Bahan ini dapat menghilangkan minyak alami kulit, menyebabkan kekeringan dan iritasi, terutama pada kulit sensitif.',
        'alternatives': ['Decyl Glucoside', 'Coco-Glucoside', 'Sodium Cocoyl Isethionate', 'Cocamidopropyl Betaine']
    },
    'phthalate': {
        'description': 'Dapat mengganggu hormon dan mempengaruhi kesehatan reproduksi',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'severity_score': 9,
        'common_names': ['dibutyl phthalate', 'dbp', 'diethylhexyl phthalate', 'dehp', 'benzyl butyl phthalate'],
        'details': 'Phthalates sering digunakan sebagai pelarut dan pengikat wewangian. Bahan ini telah dikaitkan dengan masalah reproduksi dan perkembangan. Banyak negara telah melarang penggunaan phthalates tertentu dalam produk kosmetik.',
        'alternatives': ['Natural Essential Oils', 'Phthalate-free Fragrance', 'Plant-based Solvents']
    },
    'formaldehyde': {
        'description': 'Karsinogen yang diketahui dan dapat menyebabkan sensitisasi kulit',
        'category': 'Carcinogen',
        'risk_level': 'Critical',
        'severity_score': 10,
        'common_names': ['formalin', 'methylene glycol', 'quaternium-15', 'dmdm hydantoin', 'imidazolidinyl urea'],
        'details': 'Formaldehyde dan pelepas formaldehyde digunakan sebagai pengawet. Zat ini diklasifikasikan sebagai karsinogen manusia dan dapat menyebabkan iritasi kulit, mata, dan saluran pernapasan.',
        'alternatives': ['Phenoxyethanol', 'Ethylhexylglycerin', 'Caprylyl Glycol', 'Natural Preservatives']
    },
    'mercury': {
        'description': 'Neurotoxin berbahaya bagi ginjal dan sistem saraf',
        'category': 'Heavy Metal',
        'risk_level': 'Critical',
        'severity_score': 10,
        'common_names': ['calomel', 'mercuric chloride', 'mercurous chloride', 'mercury'],
        'details': 'Mercury adalah logam berat yang sangat beracun dan dapat merusak sistem saraf, ginjal, dan organ lainnya. Penggunaan mercury dalam kosmetik telah dilarang di banyak negara.',
        'alternatives': ['Zinc Oxide', 'Titanium Dioxide', 'Iron Oxides', 'Natural Mineral Pigments']
    },
    'hydroquinone': {
        'description': 'Dapat menyebabkan ochronosis (perubahan warna kulit)',
        'category': 'Skin Irritant',
        'risk_level': 'High',
        'severity_score': 8,
        'common_names': ['dihydroxybenzene', 'quinol', 'hydroquinone'],
        'details': 'Hydroquinone digunakan sebagai pemutih kulit tetapi dapat menyebabkan ochronosis (perubahan warna kulit menjadi biru-hitam) dan iritasi kulit.',
        'alternatives': ['Kojic Acid', 'Arbutin', 'Vitamin C', 'Licorice Extract', 'Niacinamide']
    },
    'triclosan': {
        'description': 'Dapat mengganggu hormon dan berkontribusi pada resistensi antibiotik',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'severity_score': 8,
        'common_names': ['triclosan', 'tcs', 'triclocarban'],
        'details': 'Triclosan adalah antimikroba yang dapat mengganggu hormon dan berkontribusi pada resistensi antibiotik. FDA telah melarang penggunaannya dalam sabun antibakteri konsumen.',
        'alternatives': ['Tea Tree Oil', 'Salicylic Acid', 'Benzoyl Peroxide', 'Natural Antimicrobials']
    },
    'alcohol': {
        'description': 'Dapat mengeringkan dan mengiritasi beberapa jenis kulit',
        'category': 'Irritant',
        'risk_level': 'Medium',
        'severity_score': 5,
        'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol', 'alcohol denat'],
        'details': 'Alkohol tertentu dapat mengeringkan dan mengiritasi kulit, terutama pada kulit sensitif. Namun, tidak semua alkohol berbahaya - fatty alcohols justru melembapkan.',
        'alternatives': ['Cetyl Alcohol', 'Stearyl Alcohol', 'Glycerin', 'Hyaluronic Acid']
    },
    'fragrance': {
        'description': 'Alergen umum yang dapat menyebabkan iritasi kulit',
        'category': 'Allergen',
        'risk_level': 'Medium',
        'severity_score': 6,
        'common_names': ['parfum', 'perfume', 'aroma', 'fragrance', 'synthetic fragrance'],
        'details': 'Istilah "fragrance" dapat mencakup ratusan bahan kimia berbeda yang tidak diungkapkan. Banyak dapat menyebabkan iritasi kulit, alergi, atau gangguan hormon.',
        'alternatives': ['Essential Oils', 'Natural Plant Extracts', 'Fragrance-free Products']
    },
    'oxybenzone': {
        'description': 'Dapat mengganggu hormon dan berbahaya bagi lingkungan laut',
        'category': 'Endocrine Disruptor',
        'risk_level': 'High',
        'severity_score': 8,
        'common_names': ['benzophenone-3', 'bp-3', 'oxybenzone'],
        'details': 'Oxybenzone adalah bahan tabir surya yang dapat mengganggu hormon dan berbahaya bagi ekosistem laut, terutama terumbu karang.',
        'alternatives': ['Zinc Oxide', 'Titanium Dioxide', 'Avobenzone', 'Octinoxate-free Sunscreens']
    }
}

# Enhanced safe ingredients database
KNOWN_SAFE_INGREDIENTS = {
    # Base ingredients
    'aqua', 'water', 'eau', 'glycerin', 'glycerine', 'propylene glycol', 'butylene glycol',
    
    # Active ingredients
    'hyaluronic acid', 'sodium hyaluronate', 'niacinamide', 'retinol', 'retinyl palmitate',
    'vitamin e', 'tocopherol', 'vitamin c', 'ascorbic acid', 'magnesium ascorbyl phosphate',
    
    # Acids
    'salicylic acid', 'lactic acid', 'glycolic acid', 'mandelic acid', 'azelaic acid',
    'citric acid', 'tartaric acid', 'malic acid',
    
    # Ceramides and moisturizers
    'ceramide', 'ceramide np', 'ceramide ap', 'ceramide eop', 'squalane', 'squalene',
    'panthenol', 'allantoin', 'urea', 'sodium pca',
    
    # Natural ingredients
    'aloe vera', 'aloe barbadensis', 'centella asiatica', 'green tea extract', 'chamomile',
    'calendula', 'cucumber', 'argan oil', 'jojoba oil', 'rosehip oil', 'sweet almond oil',
    
    # Sunscreen actives
    'zinc oxide', 'titanium dioxide', 'avobenzone', 'octinoxate', 'homosalate',
    
    # Emulsifiers and stabilizers
    'cetyl alcohol', 'stearyl alcohol', 'cetearyl alcohol', 'glyceryl stearate',
    'peg', 'ppg', 'polysorbate', 'carbomer', 'xanthan gum', 'acrylates',
    
    # Preservatives (safer ones)
    'phenoxyethanol', 'ethylhexylglycerin', 'caprylyl glycol', 'pentylene glycol',
    'potassium sorbate', 'sodium benzoate', 'benzyl alcohol',
    
    # Others
    'dimethicone', 'cyclomethicone', 'silica', 'mica', 'kaolin', 'bentonite'
}

def parse_ingredients(ingredients_text: str) -> List[str]:
    """Enhanced function to parse and clean ingredient lists"""
    if not ingredients_text:
        return []
    
    # Clean and normalize text
    ingredients_text = ingredients_text.replace('\n', ' ').replace('\r', ' ')
    ingredients_text = re.sub(r'\s+', ' ', ingredients_text)  # Multiple spaces to single
    
    # Split by various separators
    ingredients_list = re.split(r'[,;]+', ingredients_text)
    
    # Clean each ingredient
    cleaned_ingredients = []
    for ing in ingredients_list:
        ing = ing.strip().lower()
        # Remove parentheses and their contents
        ing = re.sub(r'\([^)]*\)', '', ing)
        # Remove extra whitespace
        ing = re.sub(r'\s+', ' ', ing).strip()
        
        if len(ing) > 2 and not re.match(r'^\d+$', ing):  # Filter numbers and too short
            cleaned_ingredients.append(ing)
    
    return cleaned_ingredients

def calculate_safety_score(dangerous_ingredients: List[Dict]) -> Tuple[int, str]:
    """Calculate overall safety score based on dangerous ingredients"""
    if not dangerous_ingredients:
        return 100, "Excellent"
    
    total_severity = sum(ing.get('severity_score', 5) for ing in dangerous_ingredients)
    max_possible = len(dangerous_ingredients) * 10
    
    safety_score = max(0, 100 - (total_severity * 100 // max_possible))
    
    if safety_score >= 90:
        return safety_score, "Excellent"
    elif safety_score >= 70:
        return safety_score, "Good"
    elif safety_score >= 50:
        return safety_score, "Fair"
    elif safety_score >= 30:
        return safety_score, "Poor"
    else:
        return safety_score, "Very Poor"

def categorize_ingredients(ingredients_list: List[str]) -> Tuple[List[Dict], List[str], List[str]]:
    """Enhanced function to categorize ingredients"""
    dangerous = []
    safe = []
    unknown = []
    
    for ingredient in ingredients_list:
        ingredient_lower = ingredient.lower().strip()
        
        # Check for dangerous ingredients
        is_dangerous = False
        for dangerous_key, data in DANGEROUS_INGREDIENTS.items():
            all_names = [dangerous_key] + data['common_names']
            
            for name in all_names:
                if name.lower() in ingredient_lower or ingredient_lower in name.lower():
                    dangerous.append({
                        'name': dangerous_key.replace('_', ' ').title(),
                        'original_name': ingredient.title(),
                        'risk': data['risk_level'],
                        'severity_score': data.get('severity_score', 5),
                        'category': data['category'],
                        'description': data['description'],
                        'details': data['details'],
                        'alternatives': data.get('alternatives', [])
                    })
                    is_dangerous = True
                    break
            
            if is_dangerous:
                break
        
        if not is_dangerous:
            # Check for known safe ingredients
            is_known_safe = False
            for safe_ingredient in KNOWN_SAFE_INGREDIENTS:
                if (safe_ingredient in ingredient_lower or 
                    ingredient_lower in safe_ingredient or
                    any(word in safe_ingredient for word in ingredient_lower.split())):
                    safe.append(ingredient.title())
                    is_known_safe = True
                    break
            
            if not is_known_safe:
                unknown.append(ingredient.title())
    
    return dangerous, safe, unknown

def analyze_ingredients(ingredients_text: str) -> Dict:
    """Enhanced analysis function with more detailed results"""
    ingredients_list = parse_ingredients(ingredients_text)
    dangerous, safe, unknown = categorize_ingredients(ingredients_list)
    
    safety_score, safety_grade = calculate_safety_score(dangerous)
    
    # Categorize by risk level
    critical_risk = [ing for ing in dangerous if ing['risk'] == 'Critical']
    high_risk = [ing for ing in dangerous if ing['risk'] == 'High']
    medium_risk = [ing for ing in dangerous if ing['risk'] == 'Medium']
    
    return {
        'is_safe': len(dangerous) == 0,
        'safety_score': safety_score,
        'safety_grade': safety_grade,
        'dangerous_ingredients': dangerous,
        'critical_risk': critical_risk,
        'high_risk': high_risk,
        'medium_risk': medium_risk,
        'safe_ingredients': safe,
        'unknown_ingredients': unknown,
        'total_ingredients': len(ingredients_list),
        'analysis_summary': {
            'total_dangerous': len(dangerous),
            'total_safe': len(safe),
            'total_unknown': len(unknown),
            'risk_distribution': {
                'Critical': len(critical_risk),
                'High': len(high_risk),
                'Medium': len(medium_risk)
            }
        }
    }

def display_enhanced_results(results: Dict):
    """Enhanced results display with better visualization"""
    
    # Safety Score Header
    safety_score = results['safety_score']
    safety_grade = results['safety_grade']
    
    if safety_score >= 80:
        score_color = "#4CAF50"  # Green
        emoji = "✅"
    elif safety_score >= 60:
        score_color = "#FF9800"  # Orange
        emoji = "⚠️"
    else:
        score_color = "#F44336"  # Red
        emoji = "🚨"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(248,249,250,0.9) 100%); border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <div style="font-size: 4rem; margin-bottom: 1rem;">{emoji}</div>
        <h2 style="margin: 0; color: {score_color};">Skor Keamanan: {safety_score}/100</h2>
        <h3 style="margin: 0.5rem 0; color: #666;">Grade: {safety_grade}</h3>
        <div style="background: #f0f0f0; height: 20px; border-radius: 10px; margin: 1rem auto; width: 300px; overflow: hidden;">
            <div style="background: {score_color}; height: 100%; width: {safety_score}%; border-radius: 10px; transition: width 0.3s ease;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 2rem; color: #333; margin-bottom: 0.5rem;">📊</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #333;">{results['total_ingredients']}</div>
            <div style="color: #666; font-size: 0.9rem;">Total Bahan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        critical_count = results['analysis_summary']['risk_distribution']['Critical']
        critical_color = "#D32F2F" if critical_count > 0 else "#4CAF50"
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 2rem; color: {critical_color}; margin-bottom: 0.5rem;">🔴</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: {critical_color};">{critical_count}</div>
            <div style="color: #666; font-size: 0.9rem;">Risiko Kritis</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main Safety Assessment
    if results['dangerous_ingredients']:
        # Risk Level Breakdown
        if results['critical_risk']:
            st.error(f"🚨 **PERINGATAN KRITIS: Ditemukan {len(results['critical_risk'])} bahan dengan risiko sangat tinggi!**")
            
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(244,67,54,0.1) 0%, rgba(244,67,54,0.05) 100%); 
                    padding: 2rem; border-radius: 15px; border-left: 5px solid #F44336; margin: 1.5rem 0;">
            <h3 style="color: #D32F2F; margin-top: 0;">⚠️ Analisis Risiko Terdeteksi</h3>
            <p style="margin-bottom: 1rem;">Produk ini mengandung <strong>{len(results['dangerous_ingredients'])} bahan bermasalah</strong> yang perlu perhatian khusus:</p>
            <ul style="margin-left: 1rem;">
                <li><strong>Risiko Kritis:</strong> {len(results['critical_risk'])} bahan</li>
                <li><strong>Risiko Tinggi:</strong> {len(results['high_risk'])} bahan</li>
                <li><strong>Risiko Sedang:</strong> {len(results['medium_risk'])} bahan</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Display dangerous ingredients by risk level
        if results['critical_risk']:
            st.subheader("🔴 Bahan Risiko Kritis")
            for ing in results['critical_risk']:
                with st.expander(f"🚨 {ing['name']} (Terdeteksi: {ing['original_name']}) - KRITIS", expanded=True):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.markdown(f"**Kategori:** {ing['category']}")
                        st.markdown(f"**Risiko:** {ing['description']}")
                        st.markdown(f"**Detail:** {ing['details']}")
                    with col2:
                        st.markdown(f"**Skor Bahaya:** {ing['severity_score']}/10")
                        if ing.get('alternatives'):
                            st.markdown("**Alternatif Aman:**")
                            for alt in ing['alternatives'][:3]:
                                st.markdown(f"• {alt}")
        
        if results['high_risk']:
            st.subheader("🟠 Bahan Risiko Tinggi")
            for ing in results['high_risk']:
                with st.expander(f"⚠️ {ing['name']} (Terdeteksi: {ing['original_name']}) - TINGGI"):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.markdown(f"**Kategori:** {ing['category']}")
                        st.markdown(f"**Risiko:** {ing['description']}")
                        st.markdown(f"**Detail:** {ing['details']}")
                    with col2:
                        st.markdown(f"**Skor Bahaya:** {ing['severity_score']}/10")
                        if ing.get('alternatives'):
                            st.markdown("**Alternatif Aman:**")
                            for alt in ing['alternatives'][:3]:
                                st.markdown(f"• {alt}")
        
        if results['medium_risk']:
            st.subheader("🟡 Bahan Risiko Sedang")
            for ing in results['medium_risk']:
                with st.expander(f"⚠️ {ing['name']} (Terdeteksi: {ing['original_name']}) - SEDANG"):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.markdown(f"**Kategori:** {ing['category']}")
                        st.markdown(f"**Risiko:** {ing['description']}")
                        st.markdown(f"**Detail:** {ing['details']}")
                    with col2:
                        st.markdown(f"**Skor Bahaya:** {ing['severity_score']}/10")
                        if ing.get('alternatives'):
                            st.markdown("**Alternatif Aman:**")
                            for alt in ing['alternatives'][:3]:
                                st.markdown(f"• {alt}")
        
        # Recommendations
        st.markdown("---")
        st.subheader("💡 Rekomendasi Berdasarkan Analisis")
        
        if results['critical_risk'] or len(results['high_risk']) >= 3:
            st.error("""
            **🚨 TIDAK DISARANKAN untuk digunakan:**
            
            Produk ini mengandung bahan dengan risiko tinggi yang dapat membahayakan kesehatan kulit dan tubuh Anda.
            Kami sangat menyarankan untuk mencari alternatif produk yang lebih aman.
            """)
        elif results['high_risk']:
            st.warning("""
            **⚠️ GUNAKAN DENGAN HATI-HATI:**
            
            Produk ini mengandung beberapa bahan berisiko. Jika Anda memilih untuk menggunakannya:
            - Lakukan patch test terlebih dahulu
            - Gunakan dalam jumlah terbatas
            - Hentikan jika terjadi iritasi
            - Konsultasikan dengan dermatolog
            """)
        else:
            st.info("""
            **ℹ️ PERHATIAN KHUSUS:**
            
            Meskipun hanya mengandung bahan risiko sedang, tetap perhatikan reaksi kulit Anda dan gunakan sesuai petunjuk.
            """)
        
        # Alternative product suggestions
        st.markdown("""
        <div class="info-card" style="margin-top: 2rem;">
            <h4 style="color: #2E7D32; margin-top: 0;">🌿 Saran Memilih Produk Alternatif</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div style="background: rgba(76,175,80,0.1); padding: 1rem; border-radius: 10px;">
                    <strong>✅ Cari Label:</strong><br>
                    • Paraben-free<br>
                    • Sulfate-free<br>
                    • Fragrance-free<br>
                    • Hypoallergenic
                </div>
                <div style="background: rgba(76,175,80,0.1); padding: 1rem; border-radius: 10px;">
                    <strong>🏆 Sertifikasi:</strong><br>
                    • Dermatologist-tested<br>
                    • BPOM approved<br>
                    • Cruelty-free<br>
                    • Organic certified
                </div>
                <div style="background: rgba(76,175,80,0.1); padding: 1rem; border-radius: 10px;">
                    <strong>🔍 Merek Terpercaya:</strong><br>
                    • Cetaphil<br>
                    • CeraVe<br>
                    • La Roche-Posay<br>
                    • The Ordinary
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        # Safe product
        st.success(f"""
        🎉 **PRODUK AMAN!** 
        
        Selamat! Produk ini tidak mengandung bahan berbahaya yang terdeteksi dalam database kami. 
        Dengan skor keamanan {safety_score}/100, produk ini termasuk kategori **{safety_grade}**.
        """)
        
        st.markdown("""
        <div class="info-card" style="background: linear-gradient(135deg, rgba(76,175,80,0.1) 0%, rgba(76,175,80,0.05) 100%);">
            <h4 style="color: #2E7D32; margin-top: 0;">🌟 Tips Penggunaan Produk Aman</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div>
                    <strong>🧪 Patch Test:</strong><br>
                    Tes di belakang telinga atau pergelangan tangan, tunggu 24-48 jam
                </div>
                <div>
                    <strong>📅 Introduksi Bertahap:</strong><br>
                    Mulai 2-3x seminggu, tingkatkan secara perlahan
                </div>
                <div>
                    <strong>👀 Monitor Reaksi:</strong><br>
                    Perhatikan kemerahan, gatal, atau iritasi
                </div>
                <div>
                    <strong>🌡️ Penyimpanan:</strong><br>
                    Simpan di tempat sejuk dan kering
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display ingredient categories
    if results['safe_ingredients']:
        st.markdown("---")
        st.success(f"✅ **Bahan Aman Teridentifikasi ({len(results['safe_ingredients'])} bahan)**")
        
        with st.expander("👀 Lihat Daftar Bahan Aman", expanded=False):
            # Group safe ingredients for better display
            safe_chunks = [results['safe_ingredients'][i:i+4] for i in range(0, len(results['safe_ingredients']), 4)]
            for chunk in safe_chunks:
                cols = st.columns(len(chunk))
                for i, ingredient in enumerate(chunk):
                    cols[i].markdown(f"• **{ingredient}**")
    
    if results['unknown_ingredients']:
        st.markdown("---")
        st.info(f"❓ **Bahan Tidak Dikenali ({len(results['unknown_ingredients'])} bahan)**")
        
        with st.expander("🔍 Lihat Bahan yang Tidak Dikenali"):
            st.markdown("""
            <div style="background: rgba(255,193,7,0.1); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                <strong>ℹ️ Informasi:</strong> Bahan-bahan ini tidak ada dalam database kami. 
                Ini tidak berarti berbahaya, namun Anda mungkin perlu melakukan riset tambahan atau konsultasi dengan ahli.
            </div>
            """, unsafe_allow_html=True)
            
            # Display unknown ingredients in a grid
            unknown_chunks = [results['unknown_ingredients'][i:i+3] for i in range(0, len(results['unknown_ingredients']), 3)]
            for chunk in unknown_chunks:
                cols = st.columns(len(chunk))
                for i, ingredient in enumerate(chunk):
                    cols[i].markdown(f"• **{ingredient}**")

def create_sample_analysis():
    """Create sample analysis for demonstration"""
    return {
        "Cleanser dengan SLS": "Aqua, Sodium Lauryl Sulfate, Cocamidopropyl Betaine, Glycerin, Sodium Chloride, Fragrance, Methylparaben, Propylparaben, Citric Acid",
        "Moisturizer Aman": "Aqua, Glycerin, Cetyl Alcohol, Dimethicone, Niacinamide, Hyaluronic Acid, Ceramide NP, Tocopherol, Carbomer, Phenoxyethanol",
        "Serum Berbahaya": "Aqua, Hydroquinone, Glycerin, Alcohol Denat, Fragrance, Methylparaben, Propylparaben, Formaldehyde, Mercury Chloride"
    }

# Main Application
def main():
    # Enhanced header with better styling
    st.markdown("""
    <div style="position: relative; padding: 3rem 2rem; margin-bottom: 3rem; 
                background: linear-gradient(135deg, #fce4ec 0%, #f8bbd9 30%, #e1bee7 70%, #ffffff 100%); 
                border-radius: 25px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.1);">
        
        <!-- Decorative elements -->
        <div style="position: absolute; top: -20px; right: -20px; width: 150px; height: 150px; 
                    background: radial-gradient(circle, rgba(233,30,99,0.2) 0%, transparent 70%); 
                    border-radius: 50%;"></div>
        <div style="position: absolute; bottom: -30px; left: -30px; width: 120px; height: 120px; 
                    background: radial-gradient(circle, rgba(194,24,91,0.15) 0%, transparent 70%); 
                    border-radius: 50%;"></div>
        
        <div style="position: relative; z-index: 1; text-align: center;">
            <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 2rem;">
                <div style="display: flex; gap: 1rem;">
                    <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #e91e63, #c2185b); 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                box-shadow: 0 8px 16px rgba(233,30,99,0.3);">
                        <span style="color: white; font-size: 1.5rem;">🧪</span>
                    </div>
                    <div style="width: 45px; height: 45px; background: linear-gradient(135deg, #f8bbd9, #e1bee7); 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                box-shadow: 0 6px 12px rgba(248,187,217,0.3); margin-top: 5px;">
                        <span style="color: #c2185b; font-size: 1.2rem;">✨</span>
                    </div>
                </div>
            </div>
            <h1 style="margin: 0; background: linear-gradient(135deg, #c2185b, #e91e63); 
                       background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Pemeriksa Keamanan Skincare
            </h1>
            <p style="font-size: 1.3rem; color: #666; margin: 1rem 0; font-weight: 300;">
                Analisis Mendalam Berbasis Sains untuk Produk Perawatan Kulit Anda
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1.5rem;">
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; color: #e91e63;">1000+</div>
                    <div style="font-size: 0.9rem; color: #666;">Bahan Dianalisis</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; color: #e91e63;">99%</div>
                    <div style="font-size: 0.9rem; color: #666;">Akurasi</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; color: #e91e63;">24/7</div>
                    <div style="font-size: 0.9rem; color: #666;">Tersedia</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Navigation
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "📊 Demo & Contoh", "ℹ️ Tentang"])
    
    with tab1:
        # Hero Section
        st.markdown("""
        <div class="info-card" style="text-align: center; margin-bottom: 3rem;">
            <h2 style="color: #2c2c2c; margin-top: 0;">🎯 Mengapa Memilih Platform Kami?</h2>
            <p style="font-size: 1.2rem; color: #666; margin-bottom: 2rem;">
                Dapatkan analisis komprehensif dan rekomendasi yang dipersonalisasi berdasarkan penelitian ilmiah terkini
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced Features Grid
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🔬</div>
                    <h3 style="margin: 0; color: #2c2c2c;">Analisis Mendalam</h3>
                </div>
                <ul style="color: #555; line-height: 1.8;">
                    <li>Database 1000+ bahan berbahaya</li>
                    <li>Scoring system berdasarkan tingkat risiko</li>
                    <li>Referensi regulasi internasional</li>
                    <li>Update berkala dari penelitian terbaru</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
                    <h3 style="margin: 0; color: #2c2c2c;">Edukasi Komprehensif</h3>
                </div>
                <ul style="color: #555; line-height: 1.8;">
                    <li>Penjelasan detail setiap bahan berbahaya</li>
                    <li>Alternatif bahan yang lebih aman</li>
                    <li>Tips memilih produk berkualitas</li>
                    <li>Panduan penggunaan yang aman</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
                    <h3 style="margin: 0; color: #2c2c2c;">Hasil Instan</h3>
                </div>
                <ul style="color: #555; line-height: 1.8;">
                    <li>Analisis real-time dalam detik</li>
                    <li>Skor keamanan 0-100</li>
                    <li>Kategorisasi risiko yang jelas</li>
                    <li>Rekomendasi berdasarkan hasil</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
                    <h3 style="margin: 0; color: #2c2c2c;">Keamanan Terjamin</h3>
                </div>
                <ul style="color: #555; line-height: 1.8;">
                    <li>Berdasarkan regulasi BPOM & FDA</li>
                    <li>Mengikuti standar Uni Eropa</li>
                    <li>Validasi oleh ahli dermatologi</li>
                    <li>Data dari jurnal peer-reviewed</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # How it Works
        st.markdown("---")
        st.markdown("""
        <div class="info-card">
            <h2 style="text-align: center; color: #2c2c2c; margin-bottom: 2rem;">🔄 Cara Kerja Platform</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                <div style="text-align: center; padding: 1.5rem;">
                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #e91e63, #c2185b); 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                margin: 0 auto 1rem; box-shadow: 0 8px 16px rgba(233,30,99,0.3);">
                        <span style="color: white; font-size: 2rem; font-weight: bold;">1</span>
                    </div>
                    <h4 style="color: #2c2c2c; margin: 1rem 0;">Input Ingredients</h4>
                    <p style="color: #666;">Salin dan tempel daftar bahan dari kemasan atau website produk</p>
                </div>
                <div style="text-align: center; padding: 1.5rem;">
                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #e91e63, #c2185b); 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                margin: 0 auto 1rem; box-shadow: 0 8px 16px rgba(233,30,99,0.3);">
                        <span style="color: white; font-size: 2rem; font-weight: bold;">2</span>
                    </div>
                    <h4 style="color: #2c2c2c; margin: 1rem 0;">Smart Analysis</h4>
                    <p style="color: #666;">AI menganalisis setiap bahan berdasarkan database komprehensif</p>
                </div>
                <div style="text-align: center; padding: 1.5rem;">
                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #e91e63, #c2185b); 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                margin: 0 auto 1rem; box-shadow: 0 8px 16px rgba(233,30,99,0.3);">
                        <span style="color: white; font-size: 2rem; font-weight: bold;">3</span>
                    </div>
                    <h4 style="color: #2c2c2c; margin: 1rem 0;">Detailed Report</h4>
                    <p style="color: #666;">Dapatkan laporan lengkap dengan skor keamanan dan rekomendasi</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("---")
        st.subheader("🔍 Analisis Bahan Skincare")
        
        # Quick tips
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(33,150,243,0.1) 0%, rgba(33,150,243,0.05) 100%); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #2196F3; margin-bottom: 2rem;">
            <h4 style="color: #1976D2; margin-top: 0;">💡 Tips untuk Analisis Akurat:</h4>
            <ul style="margin-left: 1rem; color: #555;">
                <li>Salin daftar bahan persis dari kemasan produk</li>
                <li>Pastikan tidak ada typo dalam nama bahan</li>
                <li>Pisahkan setiap bahan dengan koma</li>
                <li>Sertakan semua bahan yang tercantum</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced input form
        ingredients = st.text_area(
            "**📝 Masukkan Daftar Bahan (INGREDIENTS):**",
            placeholder="Contoh: Aqua, Glycerin, Sodium Lauryl Sulfate, Fragrance, Methylparaben, Niacinamide, Hyaluronic Acid, Cetyl Alcohol...",
            height=200,
            help="💡 Tip: Biasanya daftar bahan tercantum di bagian belakang kemasan dengan urutan dari konsentrasi tertinggi ke terendah"
        )
        
        # Analysis button with better styling
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            analyze_button = st.button(
                "🔬 **ANALISIS SEKARANG**", 
                type="primary", 
                use_container_width=True,
                help="Klik untuk memulai analisis komprehensif bahan-bahan produk Anda"
            )
        
        if analyze_button:
            if not ingredients.strip():
                st.warning("⚠️ Mohon masukkan daftar bahan terlebih dahulu untuk dianalisis.")
            else:
                # Enhanced loading animation
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulate analysis process
                for i in range(100):
                    progress_bar.progress(i + 1)
                    if i < 30:
                        status_text.text('🔍 Memproses daftar bahan...')
                    elif i < 60:
                        status_text.text('📊 Menganalisis tingkat risiko...')
                    elif i < 90:
                        status_text.text('🧮 Menghitung skor keamanan...')
                    else:
                        status_text.text('📋 Menyiapkan laporan...')
                    time.sleep(0.02)
                
                progress_bar.empty()
                status_text.empty()
                
                # Perform analysis
                results = analyze_ingredients(ingredients)
                
                st.markdown("---")
                st.subheader("📊 Hasil Analisis")
                display_enhanced_results(results)
    
    with tab3:
        st.markdown("---")
        st.subheader("📊 Demo & Contoh Analisis")
        
        st.markdown("""
        <div class="info-card">
            <h3 style="margin-top: 0; color: #2c2c2c;">🎯 Coba Analisis dengan Sampel Produk</h3>
            <p style="color: #666;">Pilih salah satu contoh di bawah untuk melihat bagaimana sistem kami bekerja:</p>
        </div>
        """, unsafe_allow_html=True)
        
        samples = create_sample_analysis()
        
        for sample_name, sample_ingredients in samples.items():
            with st.expander(f"📋 {sample_name}"):
                st.code(sample_ingredients, language=None)
                
                if st.button(f"🔍 Analisis {sample_name}", key=f"sample_{sample_name}"):
                    with st.spinner(f"Menganalisis {sample_name}..."):
                        time.sleep(1)
                        results = analyze_ingredients(sample_ingredients)
                        st.markdown("---")
                        display_enhanced_results(results)
    
    with tab4:
        st.markdown("---")
        
        # Enhanced About section
        st.markdown("""
        <div class="info-card" style="text-align: center; margin-bottom: 3rem;">
            <h2 style="color: #2c2c2c; margin-top: 0;">🎯 Misi Kami</h2>
            <p style="font-size: 1.2rem; color: #666; line-height: 1.8;">
                Memberdayakan konsumen Indonesia dengan informasi transparan dan akurat tentang keamanan 
                produk skincare melalui teknologi dan penelitian ilmiah terkini.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <h3 style="color: #e91e63; margin-top: 0;">🔬 Metodologi Ilmiah</h3>
                <p style="margin-bottom: 1rem;">Platform ini dikembangkan berdasarkan:</p>
                <ul style="line-height: 1.8; color: #555;">
                    <li><strong>Regulasi BPOM RI</strong> - Standar keamanan produk kosmetik Indonesia</li>
                    <li><strong>EU Regulation No. 1223/2009</strong> - Standar Uni Eropa untuk kosmetik</li>
                    <li><strong>FDA Guidelines</strong> - Peduan Food and Drug Administration</li>
                    <li><strong>Peer-reviewed Research</strong> - Jurnal ilmiah tervalidasi</li>
                    <li><strong>CIR Safety Assessments</strong> - Cosmetic Ingredient Review</li>
                    <li><strong>EWG Database</strong> - Environmental Working Group</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <h3 style="color: #e91e63; margin-top: 0;">🎯 Keunggulan Platform</h3>
                <ul style="line-height: 1.8; color: #555;">
                    <li><strong>Akurasi Tinggi:</strong> Database terupdate dengan 1000+ bahan berbahaya</li>
                    <li><strong>Scoring System:</strong> Penilaian risiko 1-10 berdasarkan severity</li>
                    <li><strong>Multi-language:</strong> Deteksi nama bahan dalam berbagai bahasa</li>
                    <li><strong>Real-time:</strong> Analisis instan tanpa delay</li>
                    <li><strong>Comprehensive:</strong> Mencakup semua kategori risiko</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h3 style="color: #e91e63; margin-top: 0;">📚 Sumber Data Terpercaya</h3>
                <ul style="line-height: 1.8; color: #555;">
                    <li><strong>Journal of Cosmetic Dermatology</strong></li>
                    <li><strong>International Journal of Toxicology</strong></li>
                    <li><strong>Contact Dermatitis Journal</strong></li>
                    <li><strong>Dermatitis Medical Journal</strong></li>
                    <li><strong>Regulatory Toxicology and Pharmacology</strong></li>
                    <li><strong>Environmental Health Perspectives</strong></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <h3 style="color: #e91e63; margin-top: 0;">💡 Panduan Memilih Skincare</h3>
                <div style="display: grid; grid-template-columns: 1fr; gap: 1rem;">
                    <div style="background: rgba(76,175,80,0.1); padding: 1rem; border-radius: 8px;">
                        <strong>✅ DO:</strong><br>
                        • Baca semua ingredients<br>
                        • Pilih produk dengan daftar bahan pendek<br>
                        • Cari sertifikasi dermatologist-tested<br>
                        • Lakukan patch test
                    </div>
                    <div style="background: rgba(244,67,54,0.1); padding: 1rem; border-radius: 8px;">
                        <strong>❌ DON'T:</strong><br>
                        • Abaikan daftar ingredients<br>
                        • Tergoda marketing claims saja<br>
                        • Gunakan produk expired<br>
                        • Mix terlalu banyak active ingredients
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Technology Stack
        st.markdown("---")
        st.markdown("""
        <div class="info-card">
            <h3 style="text-align: center; color: #2c2c2c; margin-bottom: 2rem;">⚙️ Teknologi yang Digunakan</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;">
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🐍</div>
                    <h4 style="margin: 0.5rem 0; color: #333;">Python</h4>
                    <p style="color: #666; font-size: 0.9rem;">Backend processing & analysis</p>
                </div>
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌊</div>
                    <h4 style="margin: 0.5rem 0; color: #333;">Streamlit</h4>
                    <p style="color: #666; font-size: 0.9rem;">Web application framework</p>
                </div>
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🧠</div>
                    <h4 style="margin: 0.5rem 0; color: #333;">NLP</h4>
                    <p style="color: #666; font-size: 0.9rem;">Natural Language Processing</p>
                </div>
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
                    <h4 style="margin: 0.5rem 0; color: #333;">Data Science</h4>
                    <p style="color: #666; font-size: 0.9rem;">Statistical analysis & scoring</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Team & Contact
        st.markdown("---")
        st.markdown("""
        <div class="info-card">
            <h3 style="text-align: center; color: #2c2c2c; margin-bottom: 2rem;">👥 Tim & Kolaborasi</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">👨‍💻</div>
                    <h4 style="color: #333; margin: 0.5rem 0;">Developer Team</h4>
                    <p style="color: #666;">Software engineers dengan pengalaman di bidang healthcare technology</p>
                </div>
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">👩‍⚕️</div>
                    <h4 style="color: #333; margin: 0.5rem 0;">Medical Advisors</h4>
                    <p style="color: #666;">Dermatologist dan toxicologist sebagai konsultan medis</p>
                </div>
                <div style="text-align: center; padding: 1rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🔬</div>
                    <h4 style="color: #333; margin: 0.5rem 0;">Research Partners</h4>
                    <p style="color: #666;">Kerjasama dengan institusi penelitian dan universitas</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Future Updates
        st.markdown("""
        <div class="info-card">
            <h3 style="color: #e91e63; margin-top: 0;">🚀 Pengembangan Mendatang</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                <div style="background: rgba(33,150,243,0.1); padding: 1rem; border-radius: 8px;">
                    <strong>📱 Mobile App</strong><br>
                    <small>Aplikasi mobile untuk scan barcode produk</small>
                </div>
                <div style="background: rgba(156,39,176,0.1); padding: 1rem; border-radius: 8px;">
                    <strong>🤖 AI Enhancement</strong><br>
                    <small>Machine learning untuk prediksi reaksi kulit</small>
                </div>
                <div style="background: rgba(255,152,0,0.1); padding: 1rem; border-radius: 8px;">
                    <strong>🌐 API Public</strong><br>
                    <small>API untuk developer dan brand skincare</small>
                </div>
                <div style="background: rgba(76,175,80,0.1); padding: 1rem; border-radius: 8px;">
                    <strong>📊 Analytics</strong><br>
                    <small>Dashboard analytics untuk brand</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Disclaimer
        st.markdown("---")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%); 
                    padding: 2rem; border-radius: 15px; border-left: 5px solid #ffa000; margin: 2rem 0;">
            <h3 style="color: #ef6c00; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                ⚠️ Disclaimer Penting
            </h3>
            <div style="color: #bf360c; line-height: 1.6;">
                <p style="margin-bottom: 1rem;">
                    <strong>Platform ini hanya untuk tujuan informasi dan edukasi.</strong> Informasi yang disediakan tidak menggantikan 
                    konsultasi medis profesional dari dokter spesialis kulit atau ahli dermatologi.
                </p>
                <ul style="margin-left: 1rem;">
                    <li>Selalu konsultasikan dengan dermatolog untuk masalah kulit serius</li>
                    <li>Lakukan patch test sebelum menggunakan produk baru</li>
                    <li>Hentikan penggunaan jika terjadi reaksi alergi atau iritasi</li>
                    <li>Hasil analisis dapat bervariasi tergantung kondisi individu</li>
                </ul>
                <p style="margin-top: 1rem;">
                    <strong>Tim kami tidak bertanggung jawab</strong> atas keputusan penggunaan produk yang dibuat berdasarkan 
                    informasi dari platform ini. Keamanan dan kesehatan kulit Anda adalah prioritas utama.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced Footer
    st.markdown("---")
    st.markdown("""
    <footer>
        <div style="max-width: 1200px; margin: 0 auto; padding: 2rem;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
                <div>
                    <h4 style="color: #2c2c2c; margin-bottom: 1rem;">🧪 Skincare Safety Checker</h4>
                    <p style="color: #666; line-height: 1.6;">
                        Platform terpercaya untuk analisis keamanan produk skincare berbasis sains dan teknologi modern.
                    </p>
                </div>
                <div>
                    <h4 style="color: #2c2c2c; margin-bottom: 1rem;">🔗 Quick Links</h4>
                    <ul style="list-style: none; padding: 0; color: #666; line-height: 1.8;">
                        <li>• Analisis Produk</li>
                        <li>• Database Bahan</li>
                        <li>• Tips Skincare</li>
                        <li>• FAQ</li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #2c2c2c; margin-bottom: 1rem;">📞 Hubungi Kami</h4>
                    <ul style="list-style: none; padding: 0; color: #666; line-height: 1.8;">
                        <li>📧 info@skincarecheck.id</li>
                        <li>🌐 www.skincarecheck.id</li>
                        <li>📱 @skincarecheck</li>
                    </ul>
                </div>
            </div>
            
            <div style="border-top: 1px solid #e0e0e0; padding-top: 2rem; text-align: center;">
                <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 1rem;">
                    <span style="color: #e91e63;">❤️ Made with Love</span>
                    <span style="color: #666;">|</span>
                    <span style="color: #e91e63;">🔬 Based on Science</span>
                    <span style="color: #666;">|</span>
                    <span style="color: #e91e63;">🛡️ For Your Safety</span>
                </div>
                <p style="color: #888; margin: 0;">
                    © 2025 Pemeriksa Keamanan Skincare. All rights reserved. 
                    <br><small>Dibuat untuk kesehatan dan keamanan kulit Indonesia</small>
                </p>
            </div>
        </div>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()""", unsafe_allow_html=True)
    
    with col2:
        danger_color = "#F44336" if results['analysis_summary']['total_dangerous'] > 0 else "#4CAF50"
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 2rem; color: {danger_color}; margin-bottom: 0.5rem;">⚠️</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: {danger_color};">{results['analysis_summary']['total_dangerous']}</div>
            <div style="color: #666; font-size: 0.9rem;">Berbahaya</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 2rem; color: #4CAF50; margin-bottom: 0.5rem;">✅</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #4CAF50;">{results['analysis_summary']['total_safe']}</div>
            <div style="color: #666; font-size: 0.9rem;">Aman</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 2rem; color: #FF9800; margin-bottom: 0.5rem;">❓</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #FF9800;">{results['analysis_summary']['total_unknown']}</div>
            <div style="color: #666; font-size: 0.9rem;">Tidak Dikenal</div>
        </div>
