import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Daftar lengkap bahan berbahaya dalam skincare
bahan_berbahaya = {
    'paraben': 'Dapat mengganggu hormon (EU Regulation No. 1223/2009)',
    'sulfate': 'Bersifat keras dan dapat mengiritasi kulit',
    'phthalate': 'Dikaitkan dengan gangguan endokrin (FDA)',
    'formaldehyde': 'Karsinogenik (dilarang BPOM)',
    'mercury': 'Beracun bagi sistem saraf (dilarang FDA)',
    'hydroquinone': 'Dilarang BPOM (Keputusan HK.00.05.42.1018)',
    'triclosan': 'Dapat menyebabkan resistensi antibiotik',
    'alcohol': 'Dapat menyebabkan kekeringan dan iritasi ekstrim',
    'fragrance': 'Dapat menyebabkan alergi dan iritasi',
    'lead': 'Logam berat beracun',
    'toluene': 'Berbahaya untuk sistem saraf',
    'formaldehida': 'Karsinogenik (varian formaldehyde)',
    'petrolatum': 'Dapat terkontaminasi PAH (karsinogenik)',
    'phenoxyethanol': 'Dapat menyebabkan iritasi kulit',
    'propylene glycol': 'Dapat menyebabkan iritasi pada kulit sensitif',
    'siloxane': 'Dapat mengganggu hormon',
    'oxybenzone': 'Dikaitkan dengan gangguan hormon',
    'benzoyl peroxide': 'Dapat menyebabkan iritasi parah',
    'resorsinol': 'Berpotensi mengganggu fungsi tiroid',
    'pewarna sintetis': 'Dapat menyebabkan iritasi dan alergi'
}

# Model sederhana
model = Pipeline([
    ('tfidf', TfidfVectorizer(token_pattern=r'\b\w+\b')),
    ('clf', MultinomialNB())
])

# Data latih dummy
data = {
    'ingredients': [
        'aqua glycerin niacinamide',
        'hydroquinone mercury parabens',
        'aloe vera ceramide',
        'fragrance alcohol phenoxyethanol'
    ],
    'label': ['aman', 'berbahaya', 'aman', 'berbahaya']
}
df = pd.DataFrame(data)
model.fit(df['ingredients'], df['label'])

# Tampilan Streamlit
st.set_page_config(page_title="Skincare Safety Checker", layout="wide")

st.title("🔍 Skincare Ingredient Safety Checker")
st.markdown("""
**Deteksi bahan berbahaya dalam produk skincare Anda!**  
Masukkan daftar bahan dibawah ini:
""")

# Input pengguna
col1, col2 = st.columns(2)
with col1:
    user_input = st.text_area(
        "Contoh: aqua, glycerin, hydroquinone, fragrance",
        height=200,
        key="ingredient_input"
    )

# Tombol analisis
if st.button("🚀 Analisis Sekarang", type="primary"):
    if not user_input.strip():
        st.error("Masukkan bahan skincare terlebih dahulu!")
    else:
        with st.spinner("Menganalisis bahan..."):
            # Prediksi
            prediction = model.predict([user_input])[0]
            proba = model.predict_proba([user_input])[0].max() * 100
            
            # Deteksi bahan berbahaya
            detected = []
            for bahan, desc in bahan_berbahaya.items():
                if bahan in user_input.lower():
                    detected.append((bahan, desc))

            # Tampilkan hasil
            st.subheader("📋 Hasil Analisis")
            
            if detected:
                # Tampilan untuk produk berbahaya
                st.error(f"**Status:** {prediction.upper()} (Akurasi: {proba:.0f}%)")
                
                st.warning("**⛔ BAHAN BERBAHAYA TERDETEKSI:**")
                for bahan, desc in detected:
                    st.markdown(f"""
                    - **{bahan.capitalize()}**:  
                      {desc}
                    """)
                
                st.markdown("""
                **💡 Rekomendasi:**  
                Hindari produk ini dan konsultasikan dengan dermatologis
                """)
            else:
                # Tampilan untuk produk aman
                st.success(f"**Status:** {prediction.upper()} (Akurasi: {proba:.0f}%)")
                st.balloons()
                st.markdown("""
                **✅ AMAN: Tidak terdeteksi bahan berbahaya**  
                **💡 Tips:**  
                Tetap periksa reaksi kulit Anda terhadap produk baru
                """)

# Footer
st.markdown("---")
st.caption("""
**Referensi:** BPOM, FDA, EWG, EU Cosmetic Regulation  
Aplikasi ini menggunakan model machine learning untuk analisis prediktif
""")
