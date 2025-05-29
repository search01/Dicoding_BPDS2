# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Hal ini berdampak pada performa bisnis, retensi pelanggan, dan persepsi publik terhadap layanan mereka. Oleh karena itu, perlu dilakukan analisis data untuk mengidentifikasi penyebab utama dropout dan membantu manajemen mengambil keputusan berbasis data.

## Permasalahan Bisnis
* Tingginya angka dropout siswa dari sistem pembelajaran.
* Kurangnya sistem monitoring yang mampu mendeteksi potensi dropout lebih awal.
* Minimnya dashboard yang dapat memberikan insight komprehensif terhadap faktor-faktor penyebab dropout.

## Cakupan Proyek
* Membangun model prediksi dropout mahasiswa menggunakan algoritma Machine Learning.
* Membuat dashboard interaktif untuk monitoring dan analisis dropout berbasis Metabase.
* Memberikan rekomendasi kebijakan berbasis data.

## Persiapan
### Sumber Data
Dataset yang digunakan dalam proyek ini disediakan oleh Jaya Jaya Institut, yang mencakup informasi tentang:
- Status siswa (Dropout, Enrolled, Graduate)
- Nilai akademik (semester 1 dan 2)
- Biaya pendidikan
- Penerimaan beasiswa
- Nilai ujian masuk siswa
  
### Setup Environment
Langkah-langkah persiapan environment adalah sebagai berikut:

#### 1. Buat Environment Python
```bash
conda create --name bpds_sub2 python=3.9.15 -y
conda activate bpds_sub2
```

#### 2. Install Library yang Dibutuhkan
```bash
pip install -r requirements.txt
```

#### 3. Setup Metabase
Menggunakan Metabase untuk pembuatan dashboard:
```bash
docker pull metabase/metabase:v0.46.4
docker run -p 3000:3000 --name metabase metabase/metabase
```
Akses Metabase melalui [http://localhost:3000/setup](http://localhost:3000/setup).

#### 4. Setup Database Supabase
- Buat akun di [Supabase](https://supabase.com/dashboard/sign-in).
- Buat project baru dan salin URI database.
- Kirim dataset ke database menggunakan SQLAlchemy:

```python
from sqlalchemy import create_engine
URL = "DATABASE_URL"  # Ganti dengan URL database Supabase Anda
engine = create_engine(URL)
df.to_sql('dataset', engine)
```
## Modeling
Model yang digunakan untuk memprediksi adalah Random Forest Classifier, karena kemampuannya menangani fitur kategorikal dan numerik secara bersamaan serta memberikan interpretasi lewat feature importance.  
### Evaluasi Model
* Akurasi: 0.87
* Precision dan Recall seimbang
* Confusion matrix menunjukkan model mampu mendeteksi karyawan yang berisiko keluar dengan cukup baik.   
    ![Image](https://github.com/user-attachments/assets/fdd6f36a-e48d-485b-bec3-ef3d94c80fc8)
  
Berdasarkan hasil feature importance, atribut-atribut yang paling berkontribusi terhadap prediksi dropout antara lain:
* Curricular_units_2nd_sem_approved
* Admission_grade
* Curricular_units_1st_sem_approved  
![Image](https://github.com/user-attachments/assets/5852b6a9-3896-46cf-8306-4b7a419e5782)

## Business Dashboard
Dashboard visual dibuat menggunakan Metabase untuk memberikan gambaran menyeluruh tentang distribusi dan faktor-faktor dropout mahasiswa. Dashboard ini menampilkan:
* Jumlah total mahasiswa dan yang dropout
* Distribusi dropout berdasarkan:
  * Nilai akademik (Semester 1 & 2)
  * Status pembayaran
  * Penerima beasiswa
  * Status pernikahan
  * Program studi
  * Kelompok usia  
![Image](https://github.com/user-attachments/assets/5bc8b781-312f-4f72-92c1-b758cbe2c22b)

**Akses Dashboard melalui akun metabase:**  
Username : rosalia03rrrbkl@gmail.com  
Password : metabaserosa01 

## Menjalankan Sistem Machine Learning
### Menjalankan Sistem Machine Learning Secara Lokal
1. Pastikan Anda sudah memiliki file berikut di direktori kerja:
   - `app.py` (kode aplikasi Streamlit)
   - `model.joblib` (model machine learning yang sudah dilatih)
   - `scaler.pkl` (scaler yang digunakan untuk preprocessing fitur)
2. Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```
### Menjalankan Prototype Machine Learning yang sudah dideploy
Jika prototype sudah di-deploy di Streamlit Community, dapat mengaksesnya melalui link berikut:
- [Link Prototype Streamlit](https://dicodingbpds2-cqyxhltmrsw6tv759dwg8s.streamlit.app/)

## Conclusion
Model prediksi dropout mampu mengidentifikasi mahasiswa dengan risiko tinggi secara cukup akurat, memungkinkan intervensi dini oleh pihak kampus. Dashboard interaktif Metabase memberikan insight yang komprehensif terhadap penyebab dropout, memudahkan pengambilan keputusan berbasis data.

### Rekomendasi Action Items
1. Berikan perhatian lebih kepada mahasiswa dengan nilai rendah di semester pertama dan kedua.
2. Lakukan pengecekan terhadap mahasiswa yang tidak melunasi biaya kuliah.
3. Tindak lanjuti secara khusus mahasiswa di kelompok usia 18–22 yang berisiko lebih tinggi untuk dropout.
4. Lakukan kampanye kesadaran dan dukungan akademik untuk mahasiswa di program studi dengan dropout tertinggi.
