import streamlit as st
import pandas as pd
import joblib

# Load model dan scaler
model = joblib.load("rdf_model.joblib")
scaler = joblib.load("scaler.pkl")

# Judul aplikasi
st.title("Prediksi Status Mahasiswa")
st.write("Masukkan data berikut untuk memprediksi status mahasiswa:")

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

# Ambil input
input_df = user_input()

# Tombol prediksi
if st.button("Prediksi Status Mahasiswa"):
    # Preprocessing
    input_scaled = scaler.transform(input_df)

    # Prediksi
    pred_class = model.predict(input_scaled)[0]

    # Mapping hasil prediksi
    label_dict = {
        0: "Mahasiswa berpotensi dropout",
        1: "Mahasiswa masih terdaftar dan belum lulus",
        2: "Mahasiswa diprediksi lulus"
    }

    # Tampilkan hasil
    st.subheader("Hasil Prediksi")
    st.success(label_dict.get(int(pred_class), "Status tidak diketahui"))
