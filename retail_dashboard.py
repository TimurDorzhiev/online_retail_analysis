import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# Заголовок
st.title("Анализ продаж онлайн-магазина")


# Загрузка данных
st.cache_data


def load_data():
    df = pd.read_csv('data/O_Retail.csv')
    df = df.dropna(subset=['CustomerID'])
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df


df = load_data()


# Фильтр по стране
country = st.selectbox("Выберите страну:", df['Country'].unique())
filtered_df = df[df['Country'] == country]


# Метрики
st.metric("Общая выручка", f"{filtered_df['TotalPrice'].sum():,.2f} ")
st.metric("Количество заказов", filtered_df['InvoiceNo'].nunique())
st.metric("Средний чек", f"{filtered_df['TotalPrice'].mean():.2f} ")


# График по дням
df_daily = filtered_df.resample('D', on='InvoiceDate')['TotalPrice'].sum()
st.line_chart(df_daily)


# Топ товаров
top_items = filtered_df.groupby('Description')[
    'TotalPrice'].sum().sort_values(ascending=False).head(10)
st.subheader("Топ-10 товаров по выручке")
st.bar_chart(top_items)
