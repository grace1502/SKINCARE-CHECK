import streamlit as st
import pickle

# Load model dan vectorizer
with open('model_naive_bayes.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Judul aplikasi
st.title("Klasifikasi Kandungan Skincare Aman vs Berbahaya")
st.markdown("Masukkan daftar kandungan produk skincare (ingredients), pisahkan dengan koma.")

# Input user
user_input = st.text_area("Contoh: aqua, glycerin, paraben, alcohol")

if st.button("Klasifikasi"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan kandungan skincare terlebih dahulu.")
    else:
        # Preprocessing input
        input_clean = [user_input.lower()]
        input_vectorized = vectorizer.transform(input_clean)

        # Prediksi
        prediction = model.predict(input_vectorized)[0]

        if prediction == 0:
            st.success("✅ Kandungan skincare tersebut tergolong **AMAN**.")
        else:
            st.error("⚠️ Kandungan skincare tersebut tergolong **BERBAHAYA**.")
