# Анализ продаж интернет-магазина

**Цель:** Выявить ключевые характеристики покупателей, топ-страны и сезонность.

## Используемые инструменты:

- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook

## Что сделано:

- Очистка данных (удаление отменённых заказов и пропусков)
- Построены графики по странам, клиентам, времени
- Сделаны выводы по прибыльности и сезонности

## Файл данных:

`data/O_Retail.csv` (данные из [Kaggle](https://www.kaggle.com/datasets/rahulashok0071/online-retail-dataset))

## 📊 Streamlit Dashboard

В дополнение к EDA-исследованию добавлен интерактивный дашборд.

```bash
conda activate retail-env
streamlit run dashboard/retail_dashboard.py
```
