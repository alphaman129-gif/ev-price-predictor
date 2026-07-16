import streamlit as st
import pickle
import numpy as np

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="EV Price Predictor",
    page_icon="⚡",
    layout="centered"
)

# ── CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #050b18;
    color: #e2e8f0;
}
.main { background-color: #050b18; }

.hero {
    background: linear-gradient(135deg, #0a1628 0%, #0d2347 60%, #0f2d5e 100%);
    border: 1px solid #1e40af44;
    border-radius: 20px;
    padding: 38px 30px 32px;
    text-align: center;
    margin-bottom: 28px;
    box-shadow: 0 0 80px #3b82f622;
}
.hero-icon { font-size: 3.2rem; display: block; margin-bottom: 10px; }
.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 8px;
    letter-spacing: 2px;
}
.hero p { font-size: 0.95rem; color: #93c5fd; margin: 0; font-weight: 300; }

.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 2.5px;
    color: #60a5fa;
    text-transform: uppercase;
    margin: 24px 0 12px;
}

.card {
    background: #0d1526;
    border: 1px solid #1e3a5f;
    border-radius: 14px;
    padding: 22px 22px 6px;
    margin-bottom: 16px;
}

div.stButton > button {
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    color: #ffffff;
    font-family: 'Orbitron', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 1px;
    border: none;
    border-radius: 12px;
    padding: 16px 0;
    width: 100%;
    cursor: pointer;
    box-shadow: 0 4px 20px #2563eb55;
    margin-top: 8px;
    transition: all 0.2s ease;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    box-shadow: 0 6px 28px #3b82f677;
    transform: translateY(-1px);
}

.result-box {
    border-radius: 18px;
    padding: 36px 20px;
    text-align: center;
    margin-top: 24px;
    animation: fadeIn 0.5s ease;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-label {
    font-size: 0.78rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 10px;
}
.result-value {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1;
}
.result-verdict { font-size: 1rem; margin-top: 12px; font-weight: 400; }

.footer {
    text-align: center;
    color: #1e3a5f;
    font-size: 0.75rem;
    margin-top: 40px;
    padding-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ── Load Model ────────────────────────────────────────────────
@st.cache_resource
def load_model():
    with open('EV_PricePridictor.pickle', 'rb') as f:
        return pickle.load(f)

model = load_model()

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="hero-icon">⚡</span>
    <h1>EV Price Predictor</h1>
    <p>Enter electric vehicle specifications to get an instant AI-powered price prediction</p>
</div>
""", unsafe_allow_html=True)

# ── Battery & Range ───────────────────────────────────────────
st.markdown('<div class="section-label">🔋 Battery & Range</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    battery_capacity_kwh = st.slider("Battery Capacity (kWh)", 20, 200, 75)
with col2:
    range_miles = st.slider("Range (Miles)", 50, 600, 300)
st.markdown('</div>', unsafe_allow_html=True)

# ── Performance ───────────────────────────────────────────────
st.markdown('<div class="section-label">⚡ Performance</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
col3, col4, col5 = st.columns(3)
with col3:
    horsepower = st.slider("Horsepower (HP)", 100, 1200, 400)
with col4:
    charging_speed_kw = st.slider("Charging Speed (kW)", 10, 350, 150)
with col5:
    acceleration_0_60_mph = st.slider("0-60 mph (sec)", 1.0, 15.0, 4.5, step=0.1)
st.markdown('</div>', unsafe_allow_html=True)

# ── Ratings ───────────────────────────────────────────────────
st.markdown('<div class="section-label">⭐ Ratings & Warranty</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
col6, col7, col8 = st.columns(3)
with col6:
    safety_rating = st.slider("Safety Rating (1-5)", 1.0, 5.0, 4.5, step=0.1)
with col7:
    customer_rating = st.slider("Customer Rating (1-5)", 1.0, 5.0, 4.2, step=0.1)
with col8:
    warranty_years = st.slider("Warranty (Years)", 1, 15, 8)
st.markdown('</div>', unsafe_allow_html=True)

# ── Predict ───────────────────────────────────────────────────
if st.button("⚡ Predict EV Price"):
    features = np.array([[battery_capacity_kwh, range_miles, horsepower,
                          charging_speed_kw, acceleration_0_60_mph,
                          safety_rating, customer_rating, warranty_years]])
    predicted = model.predict(features)[0]

    if predicted >= 80000:
        verdict = "🔥 Luxury / Premium EV"
        color   = "linear-gradient(135deg, #7c2d12, #b45309)"
        border  = "#f59e0b"
        tc      = "#fef3c7"
    elif predicted >= 50000:
        verdict = "✅ High-End EV"
        color   = "linear-gradient(135deg, #0f2d5e, #1d4ed8)"
        border  = "#60a5fa"
        tc      = "#dbeafe"
    elif predicted >= 30000:
        verdict = "👍 Mid-Range EV"
        color   = "linear-gradient(135deg, #14532d, #166534)"
        border  = "#4ade80"
        tc      = "#dcfce7"
    else:
        verdict = "💡 Budget EV"
        color   = "linear-gradient(135deg, #3b0764, #6b21a8)"
        border  = "#c084fc"
        tc      = "#f3e8ff"

    st.markdown(f"""
    <div class="result-box" style="background:{color}; border:1px solid {border}; box-shadow: 0 0 40px {border}44;">
        <div class="result-label" style="color:{tc};">Predicted Market Price</div>
        <div class="result-value" style="color:#ffffff;">${predicted:,.0f}</div>
        <div class="result-verdict" style="color:{tc};">{verdict}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown('<div class="footer">Built with Streamlit & Scikit-learn · EV Price Predictor v1.0</div>',
            unsafe_allow_html=True)
