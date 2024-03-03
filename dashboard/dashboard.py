import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df_day = pd.read_csv("dashboard/all_data.csv")  

# Tittle Dashboard
st.title("Bike Sharing Rentals Dashboard :man-biking:")

# Add sidebar
st.sidebar.header("Galih Rakasiwi")
selected_columns = st.sidebar.multiselect("Select Columns", df_day.columns)
if selected_columns:
    st.write("Selected Columns:")
    st.write(df_day[selected_columns])
else:
    st.write("")

image_path = "bangkit1.jpg" 
st.sidebar.image(image_path, caption="BANGKIT 2024", use_column_width=True)

# Visualization of seasonal distribution
st.subheader("Distribution of Bikes for Rent by Season")
fig_season, ax_season = plt.subplots()
sns.barplot(x='season', y='cnt', data=df_day, ax=ax_season)
st.pyplot(fig_season)

# Correlation between temperature and number of bikes rented
st.subheader("Correlation between Temperature and Number of Bikes Rented")
fig_corr, ax_corr = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=df_day, ax=ax_corr)
st.pyplot(fig_corr)

# Visualization of Number of Rentals per Day
st.subheader("Number of Rentals per Day")
fig_daily_rentals, ax_daily_rentals = plt.subplots(figsize=(10, 5))
ax_daily_rentals.plot(df_day['dteday'], df_day['cnt'], color='blue', marker='o', label='Daily Rentals')
ax_daily_rentals.set_title("Bike Rental Trends")
ax_daily_rentals.set_xlabel("Date")
ax_daily_rentals.set_ylabel("Total Rentals")
ax_daily_rentals.legend()
st.pyplot(fig_daily_rentals)
