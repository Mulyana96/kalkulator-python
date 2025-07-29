import streamlit as st

# Header dengan styling lebih ringkas
st.markdown(
    """
    <div style='background-color: #4CAF50; padding: 7px; border-radius: 8px;'>
        <h2 style='color: white; text-align: center; font-family: monospace, sans-serif; margin-bottom: 5px;'>
            Kalkulator
        </h2>
        <p style='color: white; text-align: center; font-size: 14px; margin: 0;'>
            Pilih operasi matematika, masukkan angka, dan lihat hasilnya!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")

# Kalimat menarik setelah header, rata tengah
st.markdown(
    """
    <div style="text-align: center; font-size: 18px; color: #333; font-family: Times New Roman;">
        💡 <strong>Tips:</strong> Gunakan kalkulator ini untuk mempermudah perhitungan sehari-hari. Mulai dari menghitung belanjaan, tugas sekolah, hingga analisis data sederhana!
    </div>
    """,
    unsafe_allow_html=True,
)

# Garis pembatas
st.markdown(
    """
    <hr style="border: 1px solid #4CAF50; margin: 20px 0; width: 100%;"/>
    """,
    unsafe_allow_html=True,
)

# Menambahkan font Times New Roman di sidebar
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            font-family: 'Monospace', Times, serif;
            font-size: 16px;
        }
        .sidebar h1, .sidebar h2, .sidebar h3 {
            font-family: 'Monospace', Times, serif;
            color: #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar untuk memilih operasi
st.sidebar.header("Aplikasi")
operation = st.sidebar.selectbox(
    "Pilih Menu : ",
    ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"]
)

# Input angka menggunakan slider
num1 = st.slider("Pilih angka pertama:", min_value=0, max_value=100, value=0, step=1)
num2 = st.slider("Pilih angka kedua:", min_value=0, max_value=100, value=0, step=1)

# Tombol untuk melakukan perhitungan


if st.button("Hitung"):
     result = None
if operation == "Penjumlahan":
        result = num1 + num2
        st.success(f"Hasil Penjumlahan: {result}")
elif operation == "Pengurangan":
        result = num1 - num2
        st.success(f"Hasil Pengurangan: {result}")
elif operation == "Perkalian":
        result = num1 * num2
        st.success(f"Hasil Perkalian: {result}")
elif operation == "Pembagian":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Hasil Pembagian: {result}")
        else:
            st.error("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
else:
      st.info("Masukkan angka dan klik tombol 'Hitung' untuk melihat hasil.")

st.sidebar.markdown(
    """
    <hr style="border: 1px solid #4CAF50; margin: 10px 0;"/>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
     <div style='text-align: center; font-size: 14px; padding-top: 10px; color: white; background-color: #4CAF50; padding: 10px; border-radius: 5px;'>
        Dibuat dengan ❤️ oleh <b style="color: yellow;">Mulyana</b> |
        <a href="https://github.com/Mulyana96" target="_blank" style="color: white; text-decoration: none;">GitHub</a> |
        <a href="https://linkedin.com/in/Mulyana" target="_blank" style="color: white; text-decoration: none;">LinkedIn</a>
    </div>
    """,

 unsafe_allow_html=True,)

# Jika Menu yang Dipilih adalah "Sejarah"
st.sidebar.markdown('<h2 class="center-text">News</h2>', unsafe_allow_html=True)
st.sidebar.markdown(
        """
        <div style="border-top: 2px solid #4CAF50; padding-top: 10px; padding-bottom: 10px;">
            <h4 style="color: #4CAF50;">Chapter 1</h4>
            <p style="color: #333; font-size: 14px; text-align: justify;">
                Aplikasi Kalkulator ini telah mengalami banyak perkembangan sejak pertama kali dibuat. Saat ini,
                aplikasi kalkulator dapat digunakan untuk melakukan berbagai operasi matematika, baik penjumlahan,
                pengurangan, perkalian, maupun pembagian dengan tampilan yang sederhana dan mudah dioperasikan.
            </p>
        </div>

        <div style="border-top: 2px solid #4CAF50; padding-top: 10px; padding-bottom: 10px;">
            <h4 style="color: #4CAF50;">Chapter 2</h4>
            <p style="color: #333; font-size: 14px; text-align: justify;">
                Kalkulator adalah alat yang digunakan untuk melakukan operasi matematika seperti penjumlahan,
                pengurangan, perkalian, dan pembagian. Seiring berjalannya waktu, kalkulator telah berkembang
                dari alat mekanik sederhana menjadi aplikasi perangkat lunak yang sangat canggih.
            </p>
        </div>

        <div style="border-top: 2px solid #4CAF50; padding-top: 10px; padding-bottom: 10px;">
            <h4 style="color: #4CAF50;">Chapter 3</h4>
            <p style="color: #333; font-size: 14px; text-align: justify;">
                Kalkulator pertama kali ditemukan oleh Blaise Pascal pada tahun 1642 dengan nama Pascaline. Pascaline
                adalah kalkulator mekanik yang dirancang untuk melakukan penjumlahan dan pengurangan. Pada abad ke-20,
                teknologi elektronik memperkenalkan kalkulator modern yang lebih efisien dan cepat.
        </div>
        """,
        unsafe_allow_html=True
    )
