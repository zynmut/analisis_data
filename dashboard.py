import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')



day_df = pd.read_csv("day (1).csv")
hour_df = pd.read_csv("hour (1).csv")

datetime_columns = ['Date Time']
day_df.sort_values(by='Date Time', inplace=True)
day_df.reset_index(inplace = True)

for column in datetime_columns :
    day_df['Date Time'] = pd.to_datetime(day_df['Date Time'])

min_date = day_df['Date Time'].min()
max_date = day_df['Date Time'].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label = 'Rentang Waktu', min_value = min_date,
        max_value = max_date,
        value=[min_date,max_date]
    )


st.header('Bike Rent Trend Dashboard')

col1 = st.columns(1)[0]

with col1:
    total_rentals_by_year = day_df.groupby('Year')['cnt'].sum()
    for year, total_rentals in total_rentals_by_year.items():
        st.metric(f"Total Rentals in {'year'}", value=total_rentals, delta=None)


fig, ax = plt.subplots()
bars = ax.bar(total_rentals_by_year.index.astype(str), total_rentals_by_year.values, color=["#4CB9E7"])


ax.set_ylabel('Total Rental')
ax.set_title('Perbandingan Jumlah Rental 2011 dan 2012')

for bar in bars:
    yposs = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yposs, round(yposs, 2), ha='center', va='bottom')

st.pyplot(fig)

# Menghitung Total Rental Berdasarkan Musim

sum_of_total_rentals = day_df.groupby('weathersit')['cnt'].sum()

fig, ax = plt.subplots()
bars = ax.bar(sum_of_total_rentals.index, sum_of_total_rentals.values, color=['#4CB9E7'])

ax.set_xlabel('Musim (Weather Situation)')
ax.set_ylabel('Total Rental')
ax.set_title('Perbandingan Jumlah Rental Sepeda Pada Tiap Jenis Cuaca')

for bar in bars:
    yposs = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yposs, round(yposs, 2),ha='center', va='bottom')

st.pyplot(fig)

# Menghitung total rental untuk working day dan holiday
Rental_by_day = day_df.groupby('workingday')['cnt'].sum()

fig, ax = plt.subplots()
bars = ax.bar(Rental_by_day.index, Rental_by_day.values, color=['#4CB9E7'])

ax.set_xlabel('Hari')
ax.set_ylabel('Total Rental')
ax.set_title('Perbandingan Jumlah Rental Sepeda pada Working Day dan Hari Lainnya')

for bar in bars:
    yposs = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yposs, round(yposs, 2),ha='center', va='bottom')

st.pyplot(fig)

# Menghitung total rental untuk setiap musim
Rental_by_season = day_df.groupby('season')['cnt'].sum()

fig, ax = plt.subplots()
bars = ax.bar(Rental_by_season .index, Rental_by_season.values, color=['#4CB9E7'])

ax.set_xlabel('Musim')
ax.set_ylabel('Total Rental')
ax.set_title('Perbandingan Jumlah Rental Sepeda Pada Tiap Musim')

for bar in bars:
    yposs= bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yposs, round(yposs, 2),ha='center', va='bottom')

st.pyplot(fig)





