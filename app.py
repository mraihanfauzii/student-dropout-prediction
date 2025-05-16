import streamlit as st
import pandas as pd
import joblib

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Drop-out Predictor",
    page_icon="🎓",
    layout="centered"
)

@st.cache_resource
def load_model():
    """Memuat pipeline Random-Forest 15-fitur."""
    return joblib.load("model.pkl")

model = load_model()

st.title("🎓 Prediksi Risiko *Drop-out* Mahasiswa")
st.markdown("Isi formulir, lalu klik **Predict** untuk melihat hasil.")

# ---------- mapping label → angka ----------
bin_map    = {"Ya": 1, "Tidak": 0}
gender_map = {"Pria": 1, "Wanita": 0}

# ---------- daftar Application-mode ----------
app_mode_dict = {
    1 : "1st phase – general",
    2 : "Ord. 612/93",
    5 : "1st phase – Azores",
    7 : "Other higher course",
    10: "Ord. 854-B/99",
    15: "International student",
    16: "1st phase – Madeira",
    17: "2nd phase – general",
    18: "3rd phase – general",
    26: "533-A/99 b2 (Diff Plan)",
    27: "533-A/99 b3 (Other Inst)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change course",
    44: "Tech-spec diploma",
    51: "Change inst/course",
    53: "Short-cycle diploma",
    57: "Change inst/course (Int.)"
}

# 👉 balik jadi “teks ➜ kode”
app_mode_map = {v: k for k, v in app_mode_dict.items()}

# Urutkan opsi alfabetis agar mudah dipilih
app_mode_options = sorted(app_mode_map.keys())

# -------------- FORM INPUT --------------
with st.form("input_form"):
    c1, c2 = st.columns(2)

    # ▸ kolom kiri
    with c1:
        cu2_app   = st.number_input("CU 2nd Sem Approved", 0, 60, 10)
        cu2_grade = st.slider("CU 2nd Sem Grade", 0.0, 20.0, 10.0)
        cu1_app   = st.number_input("CU 1st Sem Approved", 0, 60, 10)
        cu1_grade = st.slider("CU 1st Sem Grade", 0.0, 20.0, 10.0)
        tuition   = st.radio("Uang Kuliah Lunas?", list(bin_map))
        scholar   = st.radio("Penerima Beasiswa?", list(bin_map))
        debtor    = st.radio("Memiliki Tunggakan?", list(bin_map))
        displaced = st.radio("Mahasiswa Rantau?", list(bin_map))

    # ▸ kolom kanan
    with c2:
        age       = st.slider("Usia Saat Daftar", 16, 60, 20)
        admit_gr  = st.slider("Admission Grade", 0, 200, 120)
        prev_gr   = st.slider("Nilai Kualifikasi Sebelumnya", 0, 200, 130)
        cu2_enr   = st.number_input("CU 2nd Sem Enrolled", 0, 60, 12)
        cu1_enr   = st.number_input("CU 1st Sem Enrolled", 0, 60, 12)
        gender    = st.radio("Jenis Kelamin", list(gender_map))
        app_mode  = st.selectbox("Application Mode", app_mode_options)

    submitted = st.form_submit_button("Predict")

# -------------- PREDICTION --------------
if submitted:
    row = pd.DataFrame([{
        "Curricular_units_2nd_sem_approved" : cu2_app,
        "Curricular_units_2nd_sem_grade"    : cu2_grade,
        "Curricular_units_1st_sem_approved" : cu1_app,
        "Curricular_units_1st_sem_grade"    : cu1_grade,
        "Tuition_fees_up_to_date"           : bin_map[tuition],
        "Scholarship_holder"                : bin_map[scholar],
        "Age_at_enrollment"                 : age,
        "Debtor"                            : bin_map[debtor],
        "Gender"                            : gender_map[gender],
        "Application_mode"                  : app_mode_map[app_mode],
        "Curricular_units_2nd_sem_enrolled" : cu2_enr,
        "Curricular_units_1st_sem_enrolled" : cu1_enr,
        "Admission_grade"                   : admit_gr,
        "Displaced"                         : bin_map[displaced],
        "Previous_qualification_grade"      : prev_gr
    }])

    pred_label = model.predict(row)[0]
    class_idx  = list(model.classes_).index(pred_label)
    proba      = model.predict_proba(row)[0, class_idx]

    # tentukan warna kotak
    if pred_label == "Graduate":
        box = st.success
    elif pred_label == "Dropout":
        box = st.error
    else:                       # Enrolled
        box = st.info

    box(
        f"### Hasil Prediksi\n"
        f"Status paling mungkin: **{pred_label}**  \n"
        f"Probabilitas: **{proba:.2%}**"
    )
