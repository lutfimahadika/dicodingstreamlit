import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
# Load the dataset
day_df = pd.read_csv("E:/Belajar/all_data.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday']) 
day_df['month'] = day_df['dteday'].dt.month

# Menghitung jumlah total pengguna sepeda per bulan
monthly_counts = day_df.groupby('month')['cnt'].sum().reset_index()

# Membuat plot tren penggunaan sepeda per bulan
st.title('Tren Penggunaan Sepeda per Bulan')
fig, ax = plt.subplots(figsize=(10, 6))
sn.lineplot(x='month', y='cnt', data=monthly_counts, marker='o', ax=ax)
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)


total_per_musim = day_df.groupby('season')['cnt'].sum().reset_index()

# Membuat bar chart
st.title('Jumlah Penggunaan Sepeda per Musim')
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(total_per_musim['season'], total_per_musim['cnt'], color=['springgreen', 'gold', 'tomato', 'cornflowerblue'])
ax.set_xlabel('Musim')
ax.set_ylabel('Total Penggunaan Sepeda')
ax.set_xticks(total_per_musim['season'])
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
ax.ticklabel_format(style='plain', axis='y')  # Mengatur format sumbu y menjadi format angka biasa
st.pyplot(fig)