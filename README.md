# ⚡ EV Price Predictor

A Machine Learning web app that predicts the **market price of electric vehicles** based on their technical specifications — built with Python and deployed via Streamlit.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://ev-price-predictor-qkvlpvlhfzcgg4kt5x3pvn.streamlit.app/)

---

## 📌 About the Project

This project uses a **Multiple Linear Regression** model trained on real-world EV market data. Given a set of technical specifications, the model instantly estimates the expected market price and classifies the vehicle into one of four market segments.

| Segment | Price Range |
|---------|------------|
| 💡 Budget EV | Below $30,000 |
| 👍 Mid-Range EV | $30,000 – $50,000 |
| ✅ High-End EV | $50,000 – $80,000 |
| 🔥 Luxury / Premium EV | Above $80,000 |

---

## 🧠 Input Features

| Feature | Description |
|---------|-------------|
| `battery_capacity_kwh` | Battery size in kilowatt-hours |
| `range_miles` | Maximum driving range in miles |
| `horsepower` | Engine power in HP |
| `charging_speed_kw` | Maximum charging speed in kW |
| `acceleration_0_60_mph` | Time to reach 60 mph in seconds |
| `safety_rating` | Safety score out of 5 |
| `customer_rating` | Customer satisfaction score out of 5 |
| `warranty_years` | Warranty duration in years |

---

## 🎯 Target Variable

| Variable | Description |
|----------|-------------|
| `price_usd` | Predicted market price in US Dollars |

---

## 🛠️ Built With

- **Python** — core programming language
- **Scikit-learn** — model training & evaluation
- **Pandas** — data manipulation & cleaning
- **NumPy** — numerical computations
- **Streamlit** — web app deployment
- **Pickle** — model serialization

---

## 📁 Project Structure

```
ev-price-predictor/
│
├── app.py                    # Streamlit web app
├── EV_PricePridictor.pickle  # Trained ML model
├── requirements.txt          # Required libraries
└── README.md                 # Project documentation
```

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ev-price-predictor.git

# 2. Navigate to the project folder
cd ev-price-predictor

# 3. Install required libraries
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Multiple Linear Regression |
| Train/Test Split | 80% / 20% |
| Evaluation Metric | R² Score |

---

## 📸 App Preview

> The app features a dark futuristic UI with interactive sliders for all input features and a color-coded result showing the predicted EV price and market segment.

---

## 👨‍💻 Author

**M Faisal**
- 🌐 GitHub: [@alphaman129-gif](https://alphaman129-gif)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

> Built with ❤️ using Python & Streamlit
