# 🌤️ Weather ETL Dashboard

A modern and interactive **Weather Dashboard** built with **Python**, **Streamlit**, and **Plotly**, powered by the **OpenWeather API**.  
This project includes a custom **ETL pipeline**, unit conversion system, and real-time weather visualization.

---

## ✨ Features

- 🔍 **Search weather by city**
- 🔄 **Custom ETL pipeline** (Extract → Transform → Load)
- 🌡️ Convert temperature between **Celsius / Fahrenheit**
- 🍃 Convert wind speed between **km/h / m/s**
- 🔵 Convert pressure between **hPa / atm**
- 📊 Beautiful interactive charts using **Plotly**
- ⚡ Fast performance with local caching
- 🎨 Clean and responsive Streamlit UI

---

## 📁 Project Structure

```
project/
│── app/
│   └── main.py
│
│── etl/
│   └── weather_etl.py
│
│── cache/
│── README.md
```

---

## 🚀 How to Run

1. Install packages:
   ```bash
   pip install streamlit plotly requests
   ```

2. Run the app:
   ```bash
   streamlit run main.py
   ```

---

## 🔑 API Key Setup

Replace your API key in the script:

```python
API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

---

---

## 👨‍💻 Author
Aman Siddiqui
