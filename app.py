import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("rdf_model.joblib")
scaler = joblib.load("scaler.pkl")

# Judul aplikasi
st.title("Prediksi Status Mahasiswa")
st.write("Aplikasi ini memprediksi apakah mahasiswa akan Dropout, Masih Terdaftar, atau Lulus.")

# Input pengguna
def user_input():
    Curricular_units_2nd_sem_approved = st.number_input("Jumlah MK lulus semester 2", 0, 20, 5)
    Curricular_units_2nd_sem_grade = st.number_input("Rata-rata nilai semester 2", 0.0, 20.0, 12.0)
    Curricular_units_1st_sem_approved = st.number_input("Jumlah MK lulus semester 1", 0, 20, 5)
    Curricular_units_1st_sem_grade = st.number_input("Rata-rata nilai semester 1", 0.0, 20.0, 12.0)
    Tuition_fees_up_to_date = st.selectbox("Pembayaran biaya kuliah lancar?", ["Ya", "Tidak"])
    Scholarship_holder = st.selectbox("Penerima beasiswa?", ["Ya", "Tidak"])
    Curricular_units_2nd_sem_enrolled = st.number_input("Jumlah MK diambil semester 2", 0, 20, 6)
    Curricular_units_1st_sem_enrolled = st.number_input("Jumlah MK diambil semester 1", 0, 20, 6)
    Admission_grade = st.number_input("Nilai masuk", 0.0, 200.0, 120.0)
    Displaced = st.selectbox("Apakah mahasiswa pindahan?", ["Ya", "Tidak"])

    data = {
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Tuition_fees_up_to_date': 1 if Tuition_fees_up_to_date == "Ya" else 0,
        'Scholarship_holder': 1 if Scholarship_holder == "Ya" else 0,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Admission_grade': Admission_grade,
        'Displaced': 1 if Displaced == "Ya" else 0
    }

    return pd.DataFrame([data])

# Ambil data dari input pengguna
input_df = user_input()

# Standarisasi input
input_scaled = scaler.transform(input_df)

# Prediksi
pred_proba = model.predict_proba(input_scaled)
pred_class = model.predict(input_scaled)

# Mapping label integer ke nama kelas
label_dict = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
pred_label = int(pred_class[0])
label_text = label_dict.get(pred_label, "Tidak diketahui")

# Tampilkan hasil
st.subheader("Hasil Prediksi")
st.write(f"**Status Mahasiswa:** {label_text}")

# Opsional: tampilkan probabilitas
st.subheader("Probabilitas Tiap Kelas")
proba_df = pd.DataFrame(pred_proba[0].reshape(-1, 1), index=["Dropout", "Enrolled", "Graduate"], columns=["Probabilitas"])
st.bar_chart(proba_df)
