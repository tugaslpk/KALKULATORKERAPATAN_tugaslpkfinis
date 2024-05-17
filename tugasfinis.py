import streamlit as st
import pandas as pd

def home():
    st.markdown("<h1 style='color: blue;'>Berikut adalah daftar nama yang terlibat</h1>", unsafe_allow_html=True)
    st.write("1. Deva Nova Moza Auriel (2360101)")
    st.write("2. Bella Naomi Ginting (2360088)")
    st.write("3. Fadilah Aulia (2360120)")
    st.write("4. Hanisa Aulia Rachmawati (2360137)")
    st.write("5. Barra Yudhistira (2360086)")
    # Tambahkan konten lainnya untuk halaman utama

def density_info():
    st.markdown("<h1 style='color: blue;'>Informasi Kerapatan</h1>", unsafe_allow_html=True)
    st.write("Kerapatan dapat didefinisikan sebagai bobot per volume. Untuk benda yang berbentuk butiran (yang bisa dicurahkan), dapat dibedakan antara kerapatan curah dan kerapatan absolut. Dari kedua kerapatan ini dapat diturunkan menjadi nilai kerapatan relatif. Nilai kerapatan dapat digunakan dalam perhitungan nilai koreksi. Kerapatan juga dapat menentukan kepekatan larutan atau kekompakan bentuk padat. Kerapatan juga memiliki berbagai jenis seperti:")
    st.title("Kerapatan Curah")
    st.write("Kerapatan curah adalah bobot bahan padat berbentuk butiran dibagi volume curah yaitu volume bahan dalam bentuk tercurah (seperti beras pada takaran).")
    st.title("Kerapatan Absolut")
    st.write("Kerapatan absolut adalah bobot bahan dibagi volume nyata bahan. Untuk benda yang bersifat curah, volume nyata adalah volume curah dikurangi volume udara di antara butiran-butiran bahan. Volume celah-celah butiran ini bisa diketahui dengan cara menambahkan cairan (yang akan mengisi celah-celah butiran) yang tidak bereaksi (diserap, diresap, atau membentuk ikatan) dengan bahan.")
    st.title("Kerapatan Relatif")
    st.write("Kerapatan Relatif adalah perbandingan kerapatan bahan dengan kerapatan air pada temperatur dan tekanan yang sama.")

def Densitas():
    st.markdown("<h1 style='color: blue;'>DENSITAS AIR</h1>", unsafe_allow_html=True)
    st.write("Densitas air adalah ukuran berapa banyak massa yang dimiliki oleh air dalam suatu volume tertentu. Ini dapat dipengaruhi oleh suhu air, karena suhu memengaruhi jarak antara molekul air. Pada suhu ruang sekitar 20 derajat Celsius (°C), densitas air biasanya sekitar 1 gram per sentimeter kubik (g/cm³). Namun, pada suhu yang lebih rendah daripada suhu ruang, densitas air meningkat karena molekul air mendekat satu sama lain. Sebaliknya, pada suhu yang lebih tinggi daripada suhu ruang, densitas air cenderung menurun karena molekul air bergerak lebih cepat dan jarak antara mereka menjadi lebih besar. Berikut adalah tabel data densitas air dari suhu 1°C hingga 30°C:")

    # Membuat dataframe untuk tabel densitas air
    data = {
        "Temperatur (°C)": list(range(1, 31)),
        "Densitas (mPa.s)": [
            0.9999, 0.9999, 0.9999, 1.0000, 0.9999, 0.9999, 0.9999, 0.9999,
            0.9998, 0.9997, 0.9996, 0.9995, 0.9994, 0.9993, 0.9991, 0.9990,
            0.9988, 0.9986, 0.9984, 0.9982, 0.9980, 0.9978, 0.9976, 0.9973, 0.9971, 0.9968, 0.9965, 0.9962, 0.9959, 0.9956 
        ]
    }
    df = pd.DataFrame(data)
    st.write(df)


def calculate_absolute_density():
    st.markdown("<h1 style='color: blue;'>Kalkulator Kerapatan Absolut</h1>", unsafe_allow_html=True)
    st.title('Bagaimana cara mendapatkan data untuk perhitungan kerapatan Absolut? Simak caranya berikut ini:')
    st.write('1. Gelas ukur di isi dengan aquadest sebanyak 25,00 mL lalu seka bagian dalam tabung, dicatat sebagai volume awal, setelah itu ditimbang dan catat hasil nilai yang didapat sebagai Wa')
    st.write('2. Gelas ukur ditambahkan sampel (kacang hijau) sebanyak 15,00 mL, sehingga menghasilkan volume akhir sebesar 40,00 mL dicatat sebagai volume akhir, ditimbang kembali gelas ukur berisi air dan sampel dan catat hasil nilai yang didapat sehagai Wb')
    st.write('3. Masukan data yang telah dihasilkan dalam perhitungan kelakulator')
    st.markdown("<h1 style='color: green;'>Masukkan Data Untuk Menghitung Kerapatan Absolut:</h1>", unsafe_allow_html=True)
    sample_weight_abs = st.number_input('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, step=0.1, format="%.4f")
    water_weight_abs = st.number_input('Bobot Gelas Ukur Isi Air (mg):', min_value=0.0, step=0.1, format="%.4f")
    sample_volume_abs = st.number_input('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, step=0.1, format="%.4f")
    water_volume_abs = st.number_input('Volume Gelas Ukur Isi Air (mL):', min_value=0.0, step=0.1, format="%.4f")

    if st.button('Hitung Kerapatan Absolut'):
        try:
            absolute_density = (sample_weight_abs - water_weight_abs) / (sample_volume_abs - water_volume_abs)
            st.subheader('Hasil Perhitungan Kerapatan Absolut:')
            st.write('Kerapatan Absolut:', absolute_density, 'mg/mL')
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

def calculate_bulk_density():
    st.markdown("<h1 style='color: blue;'>Kalkulator Kerapatan Curah</h1>", unsafe_allow_html=True)
    st.title('Bagaimana cara mendapatkan data untuk perhitungan kerapatan curah? Simak caranya berikut ini:')
    st.write('1. Gelas ukur kosong ditimbang, catat sebagai Wgu')
    st.write('2. Sampel (sampel dalam bentuk padatan berupa butiran) dimasukkan ke dalam gelas ukur sambil diketuk-ketuk sampai tanda tera 25,0 mL. Catat sebagai Vc. (Volume 25 mL tidak standar, bisa diubah ke volume berapa saja).')
    st.write('3. Gelas ukur berisi sampel ditimbang, catat sebagai Wgb. Hitung bobot sampel (Wgb-Wgu) dan catat sebagai W.')
    st.write('4. Masukan data yang telah dihasilkan dalam perhitungan kelakulator')
    st.markdown("<h1 style='color: green;'>Masukkan Data Untuk Menghitung Kerapatan Curah:</h1>", unsafe_allow_html=True)
    sample_weight_bulk = st.number_input('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, format="%.4f", key='bulk_sample_weight')
    berat_wadah_bulk = st.number_input('Bobot Gelas Ukur (mg):', min_value=0.0, format="%.4f", key='bulk_berat_wadah')
    sample_volume_bulk = st.number_input('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, format="%.4f", key='bulk_sample_volume')

    if st.button('Hitung Kerapatan Curah'):
        try:
            bulk_density = (sample_weight_bulk - berat_wadah_bulk) / sample_volume_bulk
            st.subheader('Hasil Perhitungan Kerapatan Curah:')
            st.write('Kerapatan Curah:', bulk_density, 'mg/mL')
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

def calculate_relative_density():
    st.markdown("<h1 style='color: blue;'>Kalkulator Kerapatan Relatif</h1>", unsafe_allow_html=True)
    st.title('Bagaimana cara mendapatkan data untuk perhitungan kerapatan Absolut? Simak caranya berikut ini:')
    st.write('1. Gelas ukur di isi dengan aquadest sebanyak 25,00 mL lalu seka bagian dalam tabung, dicatat sebagai volume awal, setelah itu ditimbang dan catat hasil nilai yang didapat sebagai Wa')
    st.write('2. Gelas ukur ditambahkan sampel (kacang hijau) sebanyak 15,00 mL, sehingga menghasilkan volume akhir sebesar 40,00 mL dicatat sebagai volume akhir, ditimbang kembali gelas ukur berisi air dan sampel dan catat hasil nilai yang didapat sehagai Wb')
    st.write('3. Masukan data dalam perhitungan kalkulator dan tambahkan nilai densitas air berdasarkan suhu ruang')
    st.markdown("<h1 style='color: green;'>Masukkan Data Untuk Menghitung Kerapatan Relatif</h1>", unsafe_allow_html=True)
    sample_weight_abs = st.number_input('Bobot Gelas Ukur Isi Sampel (mg):', min_value=0.0, step=0.1, format="%.4f", key='rel_sample_weight')
    water_weight_abs = st.number_input('Bobot Gelas Ukur Isi Air (mg):', min_value=0.0, step=0.1, format="%.4f", key='rel_water_weight')
    sample_volume_abs = st.number_input('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, step=0.1, format="%.4f", key='rel_sample_volume')
    water_volume_abs = st.number_input('Volume Gelas Ukur Isi Air (mL):', min_value=0.0, step=0.1, format="%.4f", key='rel_water_volume')
    temperature = st.number_input('Suhu Air (°C):', min_value=1, max_value=30, step=1, format="%d", key='rel_temperature')

    # Data densitas air berdasarkan suhu
    densitas_data = {
        1: 0.9999, 2: 0.9999, 3: 0.9999, 4: 1.0000, 5: 0.9999, 6: 0.9999, 7: 0.9999, 8: 0.9999,
        9: 0.9998, 10: 0.9997, 11: 0.9996, 12: 0.9995, 13: 0.9994, 14: 0.9993, 15: 0.9991, 16: 0.9990,
        17: 0.9988, 18: 0.9986, 19: 0.9984, 20: 0.9982, 21: 0.9980, 22: 0.9978, 23: 0.9976, 24: 0.9973, 25: 0.9971, 26: 0.9968, 27: 0.9965, 28: 0.9962, 29: 0.9959, 30: 0.9956 
    }
    nilai_densitas_air = densitas_data.get(temperature, 1.0)

    if st.button('Hitung Kerapatan Relatif'):
        try:
            absolute_density = (sample_weight_abs - water_weight_abs) / (sample_volume_abs - water_volume_abs)
            relative_density = absolute_density / nilai_densitas_air
            st.subheader('Hasil Perhitungan Kerapatan Relatif:')
            st.write('Kerapatan Relatif:', relative_density)
        except ZeroDivisionError:
            st.error("Error: Pembagian dengan nol tidak diizinkan.")

def main():
    st.markdown("<h1 style='color: red;'>SELAMAT DATANG DI APLIKASI KALKULATOR KERAPATAN</h1>", unsafe_allow_html=True)
    st.markdown("---")  # Menambahkan garis horizontal
    st.title("Aplikasi Yang Dapat Membantu Anda Dalam Menghitung Kerapatan Absolut, Kerapatan Curah, Dan Kerapatan Relatif")
    menu = ["HOME", "INFORMASI KERAPATAN", "DENSITAS AIR", "KALKULATOR KERAPATAN ABSOLUT", "KALKULATOR KERAPATAN CURAH", "KALKULATOR KERAPATAN RELATIF"]
    choice = st.radio("PILIH HALAMAN:", menu)

    if choice == "HOME":
        home()
    elif choice == "INFORMASI KERAPATAN":
        density_info()
    elif choice == "DENSITAS AIR":
        Densitas()
    elif choice == "KALKULATOR KERAPATAN ABSOLUT":
        calculate_absolute_density()
    elif choice == "KALKULATOR KERAPATAN CURAH":
        calculate_bulk_density()
    elif choice == "KALKULATOR KERAPATAN RELATIF":
        calculate_relative_density()

if __name__ == "__main__":
    main()
