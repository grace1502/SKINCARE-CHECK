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

# Custom CSS dengan desain aesthetic
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
        color: #c2185b !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        font-size: 3rem !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Subjudul */
    h2 {
        color: #c2185b !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 500 !important;
        border-bottom: 2px solid var(--primary-light);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem !important;
    }
    
    h3 {
        font-family: 'Playfair Display', serif !important;
        color: #2c2c2c !important;
        font-weight: 500 !important;
    }
    
    h4 {
        color: #2c2c2c !important;
        font-weight: 600 !important;
    }
    
    /* Text color improvements */
    p, div, span {
        color: #2c2c2c !important;
    }
    
    .stMarkdown p {
        color: #2c2c2c !important;
    }
    
    /* Tombol */
    .stButton button {
        background-color: #e91e63 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton button:hover {
        background-color: #c2185b !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
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
        background-color: #f5f5f5 !important;
        color: #2c2c2c !important;
        border-radius: 8px !important;
        margin-right: 0 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease;
        border: 1px solid #e0e0e0 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #e91e63 !important;
        font-weight: 600 !important;
        color: white !important;
        border: 1px solid #e91e63 !important;
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

# Database bahan yang dikenal (aman)
KNOWN_SAFE_INGREDIENTS = {
    'aqua', 'water', 'glycerin', 'glycerine', 'hyaluronic acid', 'niacinamide', 
    'ceramide', 'panthenol', 'tocopherol', 'vitamin e', 'aloe vera', 'retinol',
    'salicylic acid', 'lactic acid', 'glycolic acid', 'mandelic acid', 'azelaic acid',
    'zinc oxide', 'titanium dioxide', 'dimethicone', 'cyclomethicone', 'squalane',
    'jojoba oil', 'argan oil', 'rosehip oil', 'shea butter', 'cocoa butter',
    'petrolatum', 'mineral oil', 'lanolin', 'beeswax', 'carnauba wax',
    'stearic acid', 'palmitic acid', 'oleic acid', 'linoleic acid', 'cetyl alcohol',
    'stearyl alcohol', 'cetearyl alcohol', 'sodium chloride', 'potassium sorbate',
    'phenoxyethanol', 'ethylhexylglycerin', 'caprylyl glycol', 'pentylene glycol',
    'propylene glycol', 'butylene glycol', 'hexylene glycol', 'dipropylene glycol',
    'peg', 'ppg', 'carbomer', 'acrylates', 'xanthan gum', 'sodium hydroxide',
    'citric acid', 'sodium citrate', 'disodium edta', 'tetrasodium edta',
    'allantoin', 'bisabolol', 'chamomile', 'green tea', 'vitamin c', 'ascorbic acid',
    'magnesium ascorbyl phosphate', 'sodium ascorbyl phosphate', 'kojic acid',
    'arbutin', 'licorice extract', 'centella asiatica', 'calendula', 'cucumber',
    'almond oil', 'coconut oil', 'olive oil', 'sunflower oil', 'grapeseed oil'
}

def parse_ingredients(ingredients_text):
    """Fungsi untuk memparse dan membersihkan daftar bahan"""
    # Bersihkan teks dan split berdasarkan koma
    ingredients_text = ingredients_text.replace('\n', ' ').replace('\r', ' ')
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
        ingredient_lower = ingredient.lower()
        
        # Cek apakah bahan berbahaya
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
            # Cek apakah bahan aman yang dikenal
            is_known_safe = False
            for safe_ingredient in KNOWN_SAFE_INGREDIENTS:
                if safe_ingredient in ingredient_lower or ingredient_lower in safe_ingredient:
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
    dangerous, safe, unknown = categorize_ingredients(ingredients_list)
    
    return {
        'is_safe': len(dangerous) == 0,
        'dangerous_ingredients': dangerous,
        'safe_ingredients': safe,
        'unknown_ingredients': unknown,
        'total_ingredients': len(ingredients_list)
    }

def display_results(results):
    """Fungsi untuk menampilkan hasil analisis"""
    # Summary statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Bahan", results['total_ingredients'])
    with col2:
        st.metric("Bahan Berbahaya", len(results['dangerous_ingredients']))
    with col3:
        st.metric("Bahan Aman", len(results['safe_ingredients']))
    with col4:
        st.metric("Tidak Dikenali", len(results['unknown_ingredients']))
    
    st.markdown("---")
    
    # Main safety assessment
    if len(results['dangerous_ingredients']) > 0:
        # Ada bahan berbahaya
        st.error(f"⚠️ **Ditemukan {len(results['dangerous_ingredients'])} Bahan Potensial Berbahaya**")
        
        st.warning("""
        **🚨 Peringatan Penting:**
        
        Produk ini mengandung bahan-bahan yang berpotensi menimbulkan efek samping atau reaksi negatif pada kulit. 
        Kami menyarankan untuk mempertimbangkan kembali penggunaan produk ini, terutama jika Anda memiliki kulit sensitif.
        """)
        
        for ing in results['dangerous_ingredients']:
            with st.expander(f"🚨 {ing['name'].title()} (Ditemukan sebagai: {ing['original_name']}) - Risiko: {ing['risk']}"):
                st.write(f"**Kategori:** {ing['category']}")
                st.write(f"**Deskripsi:** {ing['description']}")
                st.write(f"**Detail:** {ing['details']}")
        
        st.info("""
        **💡 Rekomendasi Alternatif:**
        
        Pertimbangkan untuk mencari produk dengan label:
        - **Paraben-free** - Bebas paraben
        - **Sulfate-free** - Bebas sulfate  
        - **Fragrance-free** - Bebas wewangian sintetis
        - **Hypoallergenic** - Formulasi untuk kulit sensitif
        - **Non-comedogenic** - Tidak menyumbat pori
        - **Dermatologist-tested** - Telah diuji dermatolog
        
        **Langkah Selanjutnya:**
        - Konsultasikan dengan dermatolog sebelum menggunakan produk
        - Cari merek yang transparan tentang formulasi mereka
        - Baca review dari pengguna dengan tipe kulit serupa
        - Pertimbangkan produk dengan sertifikasi organik atau natural
        """)
    
    elif len(results['safe_ingredients']) > 0 and len(results['unknown_ingredients']) == 0:
        # Hanya ada bahan aman, tidak ada yang tidak dikenali
        st.success("""
        ✅ **Produk Ini Aman!**
        
        Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan. Produk ini tampaknya menggunakan formulasi yang lebih aman untuk kulit. 
        
        **Namun tetap perhatikan:**
        - Reaksi kulit Anda terhadap produk baru
        - Selalu lakukan patch test sebelum penggunaan penuh
        - Hentikan penggunaan jika terjadi iritasi atau reaksi alergi
        - Konsultasikan dengan dermatolog jika memiliki kulit sensitif atau kondisi kulit tertentu
        """)
        
        st.info("""
        **🌟 Tips Penggunaan Produk Aman:**
        
        - **Patch Test:** Oleskan sedikit produk di belakang telinga atau pergelangan tangan, tunggu 24-48 jam
        - **Gradual Introduction:** Mulai gunakan produk secara bertahap, 2-3 kali seminggu
        - **Monitor Reaksi:** Perhatikan tanda-tanda kemerahan, gatal, atau iritasi
        - **Storage:** Simpan produk di tempat sejuk dan kering untuk menjaga kualitas
        """)
    
    elif len(results['safe_ingredients']) > 0 and len(results['unknown_ingredients']) > 0:
        # Ada bahan aman dan bahan tidak dikenali
        st.success("""
        ✅ **Produk Ini Aman!**
        
        Tidak terdeteksi bahan berbahaya dalam daftar yang diberikan. Produk ini tampaknya menggunakan formulasi yang lebih aman untuk kulit. 
        
        **Namun tetap perhatikan:**
        - Reaksi kulit Anda terhadap produk baru
        - Selalu lakukan patch test sebelum penggunaan penuh
        - Hentikan penggunaan jika terjadi iritasi atau reaksi alergi
        - Konsultasikan dengan dermatolog jika memiliki kulit sensitif atau kondisi kulit tertentu
        """)
        
        st.info("""
        **🌟 Tips Penggunaan Produk Aman:**
        
        - **Patch Test:** Oleskan sedikit produk di belakang telinga atau pergelangan tangan, tunggu 24-48 jam
        - **Gradual Introduction:** Mulai gunakan produk secara bertahap, 2-3 kali seminggu
        - **Monitor Reaksi:** Perhatikan tanda-tanda kemerahan, gatal, atau iritasi
        - **Storage:** Simpan produk di tempat sejuk dan kering untuk menjaga kualitas
        """)
    
    # Display unknown ingredients if any
    if results['unknown_ingredients']:
        st.markdown("---")
        st.warning(f"🔍 **Ditemukan {len(results['unknown_ingredients'])} Bahan Tidak Dikenali**")
        
        with st.expander("Lihat Bahan yang Tidak Dikenali"):
            st.write("**Bahan-bahan berikut tidak terdeteksi pada sistem:**")
            
            # Group ingredients for better display
            unknown_list = results['unknown_ingredients']
            for i in range(0, len(unknown_list), 3):
                cols = st.columns(3)
                for j, col in enumerate(cols):
                    if i + j < len(unknown_list):
                        col.write(f"• {unknown_list[i + j].title()}")
    
    # Display safe ingredients summary
    if results['safe_ingredients']:
        st.markdown("---")
        st.success(f"✅ **Ditemukan {len(results['safe_ingredients'])} Bahan Aman**")
        
        with st.expander("Lihat Bahan yang Aman"):
            safe_list = results['safe_ingredients']
            for i in range(0, len(safe_list), 4):
                cols = st.columns(4)
                for j, col in enumerate(cols):
                    if i + j < len(safe_list):
                        col.write(f"• {safe_list[i + j].title()}")

# Main App
def main():
    # Header dengan styling modern dan gambar
    st.markdown("""
    <div style="position: relative; padding: 2rem 0; margin-bottom: 2rem;">
        <div style="position: absolute; top: 0; right: 0; width: 200px; height: 150px; background: url('https://images.unsplash.com/photo-1570194065650-d99fb4bedf0d?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80') no-repeat center center; background-size: cover; border-radius: 15px; opacity: 0.3; z-index: 0;"></div>
        <div style="position: relative; z-index: 1;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="width: 60px; height: 60px; background: url('https://images.unsplash.com/photo-1596755389378-c31d21fd1273?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80') no-repeat center center; background-size: cover; border-radius: 50%; border: 3px solid #e91e63;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.title("Pemeriksa Keamanan Skincare")
    st.markdown("### Temukan Analisis Mendalam Mengenai Produk Perawatan Kulit Anda")
    
    # Navigation
    tab1, tab2, tab3 = st.tabs(["🏠 Beranda", "🔍 Analisis Bahan", "ℹ️ Tentang Website"])
    
    with tab1:
        st.markdown("---")
        
        # Hero Section
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(255,182,193,0.2) 0%, rgba(255,255,255,0.8) 100%); border-radius: 15px; margin-bottom: 2rem;">
            <h2>Analisis Instan Berdasarkan Penelitian Ilmiah</h2>
            <p style="font-size: 1.1rem;">Platform terpercaya untuk membantu Anda membuat keputusan yang lebih baik tentang produk perawatan kulit</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #e91e63;">🔬</div>
                <h4 style="color: #2c2c2c; margin: 0.5rem 0;">Analisis Mendalam</h4>
                <p style="color: #555555;">Sistem memeriksa berbagai jenis bahan berbahaya berdasarkan sumber terpercaya</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #e91e63;">⚡</div>
                <h4 style="color: #2c2c2c; margin: 0.5rem 0;">Hasil Instan</h4>
                <p style="color: #555555;">Dapatkan hasil analisis komprehensif dalam hitungan detik</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #e91e63;">📚</div>
                <h4 style="color: #2c2c2c; margin: 0.5rem 0;">Edukasi Komprehensif</h4>
                <p style="color: #555555;">Pelajari tentang bahan berbahaya dan alternatif yang lebih aman</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="font-size: 2.5rem; color: #e91e63;">🛡️</div>
                <h4 style="color: #2c2c2c; margin: 0.5rem 0;">Keamanan Terjamin</h4>
                <p style="color: #555555;">Berdasarkan regulasi dan penelitian ilmiah terbaru</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # How it works
        st.subheader("Bagaimana Cara Kerjanya?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **1️⃣ Masukkan Daftar Bahan**
            
            <span style="color: #555555;">Salin dan tempel daftar bahan (INGREDIENTS) dari produk skincare Anda</span>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            **2️⃣ Proses Analisis**
            
            <span style="color: #555555;">Sistem akan memindai bahan-bahan yang terindikasi berbahaya </span>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            **3️⃣ Dapatkan Hasil**
            
            <span style="color: #555555;">Lihat laporan lengkap tentang keamanan produk dan rekomendasi alternatif</span>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("---")
        st.subheader("Analisis Bahan Skincare")
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
     
        
        # Hero section untuk About
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(255,182,193,0.2) 0%, rgba(255,255,255,0.8) 100%); border-radius: 15px; margin-bottom: 2rem;">
            <h3>Transparansi Untuk Kesehatan Kulit Anda</h3>
            <p style="font-size: 1.1rem;">Memberdayakan konsumen dengan informasi berbasis sains tentang keamanan produk skincare</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Main content dalam 2 kolom yang seimbang
        col1, col2 = st.columns(2)
        
        with col1:
            # Mission section dengan styling
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 1.5rem;">
                <h4 style="color: #e91e63; margin-top: 0;">🎯 Misi </h4>
                <p style="line-height: 1.6;">Berkomitmen untuk meningkatkan transparansi dalam industri kecantikan dengan memberikan informasi yang jelas dan dapat diakses tentang bahan-bahan dalam produk perawatan kulit. Tujuan dibuatnya sistem ini adalah memberdayakan konsumen untuk membuat pilihan yang tepat berdasarkan data dan penelitian ilmiah.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Methodology section
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <h4 style="color: #e91e63; margin-top: 0;">🔬 Metodologi</h4>
                <p style="margin-bottom: 1rem; line-height: 1.6;">Website ini dikembangkan berdasarkan:</p>
                <ul style="line-height: 1.6;">
                    <li>Regulasi Uni Eropa (EU Regulation No. 1223/2009)</li>
                     <li>Lembaga pengawas BPOM</li>
                    <li>Pedoman FDA tentang kosmetik</li>
                    <li>Penelitian ilmiah peer-reviewed</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Data sources section
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 1.5rem;">
                <h4 style="color: #e91e63; margin-top: 0;">📚 Sumber Data</h4>
                <p style="margin-bottom: 1rem; line-height: 1.6;">Informasi dalam website ini bersumber dari:</p>
                <ul style="line-height: 1.6;">
                    <li>Environmental Working Group's Skin Deep Database</li>
                    <li>Cosmetic Ingredient Review (CIR)</li>
                    <li>Journal of the American Academy of Dermatology</li>
                    <li>BPOM RI</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Tips section
            st.markdown("""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <h4 style="color: #e91e63; margin-top: 0;">💡 Tips Memilih Skincare Aman</h4>
                <ul style="line-height: 1.6;">
                    <li><strong>Baca Label:</strong> Selalu periksa daftar bahan sebelum membeli</li>
                    <li><strong>Mulai Sederhana:</strong> Produk dengan daftar bahan pendek cenderung lebih aman</li>
                    <li><strong>Uji Sensitivitas:</strong> Selalu lakukan patch test sebelum penggunaan penuh</li>
                    <li><strong>Konsultasi Ahli:</strong> Tanyakan pada dermatolog untuk kulit sensitif</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Disclaimer dengan styling yang lebih menarik
        st.markdown("---")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffecb3 100%); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #ff9800; margin-top: 2rem;">
            <h4 style="color: #ef6c00; margin-top: 0;">⚠️ Disclaimer</h4>
            <p style="margin-bottom: 0; line-height: 1.6; color: #bf360c;">Website ini hanya untuk tujuan informasi dan tidak menggantikan nasihat profesional dari dermatolog atau ahli kesehatan kulit. Selalu konsultasikan dengan profesional kesehatan untuk masalah kulit yang serius.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #888888; font-size: 0.9rem; padding: 1rem 0;">
        <p>© 2025 Pemeriksa Keamanan Skincare | Dibuat dengan ❤️ untuk kulit wajah yang lebih sehat</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
