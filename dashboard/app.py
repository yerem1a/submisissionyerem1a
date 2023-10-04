import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menghitung korelasi
def calculate_correlation():
    # Menghitung korelasi antara temperatur dan peminjaman sepeda (hari)
    correlation_temp_day = df_combined['temp_day'].corr(df_combined['cnt_day'])

    # Menghitung korelasi antara kelembaban dan peminjaman sepeda (hari)
    correlation_humidity_day = df_combined['hum_day'].corr(df_combined['cnt_day'])

    return correlation_temp_day, correlation_humidity_day

# Fungsi untuk menampilkan visualisasi
def plot_correlation():
    # Visualisasi korelasi antara temperatur dan peminjaman sepeda (hari)
    plt.figure(figsize=(10, 5))
    plt.scatter(df_combined['temp_day'], df_combined['cnt_day'], color='blue', alpha=0.5)
    plt.xlabel('Temperatur (°C)')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.title(f'Korelasi antara Temperatur dan Peminjaman Sepeda (Corr: {correlation_temp_day:.2f})')
    plt.grid(True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # Visualisasi korelasi antara kelembaban dan peminjaman sepeda (hari)
    plt.figure(figsize=(10, 5))
    plt.scatter(df_combined['hum_day'], df_combined['cnt_day'], color='green', alpha=0.5)
    plt.xlabel('Kelembaban (%)')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.title(f'Korelasi antara Kelembaban dan Peminjaman Sepeda (Corr: {correlation_humidity_day:.2f})')
    plt.grid(True)
    st.pyplot()

# Fungsi untuk analisis
def performa_peminjaman(df_combined):
    # Analisis peminjaman berdasarkan hari dalam seminggu pada DataFrame 'df_combined'
    peminjaman_per_hari = df_combined.groupby('weekday_day')['cnt_day'].mean()

    # Analisis peminjaman berdasarkan jam dalam sehari pada DataFrame 'df_combined'
    peminjaman_per_jam = df_combined.groupby('hr')['cnt_hour'].mean()

    return peminjaman_per_hari, peminjaman_per_jam

# Fungsi untuk visualisasi
def visualisasi_peminjaman(peminjaman_per_hari, peminjaman_per_jam):
    # Visualisasi performa penggunaan sepeda berdasarkan hari dalam seminggu
    plt.figure(figsize=(10, 5))
    plt.bar(peminjaman_per_hari.index, peminjaman_per_hari.values, color='skyblue')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Peminjaman Rata-rata')
    plt.title('Performa Penggunaan Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xticks(range(7), ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot()

    # Visualisasi performa penggunaan sepeda berdasarkan jam dalam sehari
    plt.figure(figsize=(10, 5))
    plt.plot(peminjaman_per_jam.index, peminjaman_per_jam.values, marker='o', color='green')
    plt.xlabel('Jam dalam Sehari')
    plt.ylabel('Jumlah Peminjaman Rata-rata')
    plt.title('Performa Penggunaan Sepeda Berdasarkan Jam dalam Sehari')
    plt.xticks(range(24))
    plt.grid(True)
    st.pyplot()


# Memuat dataset
df_combined = pd.read_csv('dashboard/main_data.csv')  # Gantilah dengan nama sebenarnya

# Judul aplikasi
st.title("Analisis Data Bike Sharing")

# Pertanyaan
st.subheader("Pertanyaan:")
st.write("1. Apa hubungan antara temperatur dan jumlah peminjaman sepeda?")
st.write("2. Apa hubungan antara kelembaban dan jumlah peminjaman sepeda?")

# Menghitung korelasi
correlation_temp_day, correlation_humidity_day = calculate_correlation()

# Menampilkan visualisasi
st.subheader("Visualisasi Korelasi:")
plot_correlation()

# Analisis
st.header("Analisis Peminjaman Sepeda")
peminjaman_per_hari, peminjaman_per_jam = performa_peminjaman(df_combined)

# Visualisasi
st.header("Visualisasi Performa Peminjaman Sepeda")
visualisasi_peminjaman(peminjaman_per_hari, peminjaman_per_jam)

# Kesimpulan
st.subheader("Kesimpulan:")
st.write(f"Korelasi antara temperatur dan peminjaman sepeda (hari): {correlation_temp_day:.2f}")
st.write(f"Korelasi antara kelembaban dan peminjaman sepeda (hari): {correlation_humidity_day:.2f}")
st.write(f"Berdasarkan analisis, peminjaman sepeda cenderung lebih tinggi pada hari Kamis hingga Sabtu, terutama pada jam 7-9 pagi dan 16-18 sore, sementara pada hari Minggu dan pada malam hari terjadi penurunan peminjaman.")
