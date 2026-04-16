# gold_streamlit_app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# page settings
st.set_page_config(page_title="Gold Price Predictor", layout="wide")
st.title("💰 Gold Price Prediction Tool")
st.markdown("Adjust the sliders to predict gold price movement for next month.")

# check and load the model
try:
    model = joblib.load('gold_price_model.pkl')
    scaler = joblib.load('feature_scaler.pkl')
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()


st.sidebar.header("Macroeconomic Factors")

# three silders
col1, col2, col3 = st.sidebar.columns(3)

with col1:
    usd = st.slider(
        "USD Index",
        min_value=80.0,
        max_value=120.0,
        value=100.0,
        step=0.1,
        help="Higher USD makes gold more expensive in other currencies"
    )

with col2:
    treasury = st.slider(
        "Treasury Yield (%)",
        min_value=0.0,
        max_value=8.0,
        value=3.5,
        step=0.1,
        help="Higher yields increase opportunity cost of holding gold"
    )

with col3:
    inflation = st.slider(
        "Inflation Rate (%)",
        min_value=0.0,
        max_value=10.0,
        value=2.5,
        step=0.1,
        help="Higher inflation increases gold's appeal as an inflation hedge"
    )

# precdict button
if st.sidebar.button("Predict", type="primary"):
    # input data
    input_data = pd.DataFrame({
        'usd_index': [usd],
        'treasury_yield': [treasury],
        'inflation_rate': [inflation]
    })
    
    input_scaled = scaler.transform(input_data)
    
    # precdict
    probability = model.predict_proba(input_scaled)[0, 1]
    prediction = model.predict(input_scaled)[0]
    
    # result
    st.subheader("📊 Prediction Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Probability of Increase", f"{probability:.1%}")
    
    with col2:
        st.metric("Predicted Direction", 
                 "📈 Increase" if prediction == 1 else "📉 Decrease")
    
    with col3:
        if probability > 0.7:
            confidence = "High"
        elif probability > 0.6:
            confidence = "Moderate"
        else:
            confidence = "Low"
        st.metric("Confidence Level", confidence)
    
    # trading recommendation
    st.subheader("💡 Trading Recommendation")
    
    if probability > 0.7:
        recommendation = "STRONG BUY"
        color = "green"
        explanation = "High probability of price increase. Favorable conditions for gold."
    elif probability > 0.6:
        recommendation = "BUY"
        color = "lightgreen"
        explanation = "Moderate probability of price increase. Consider accumulating gold."
    elif probability > 0.4:
        recommendation = "HOLD"
        color = "orange"
        explanation = "Unclear direction. Maintain current position."
    elif probability > 0.3:
        recommendation = "SELL"
        color = "pink"
        explanation = "Moderate probability of price decrease. Consider reducing exposure."
    else:
        recommendation = "STRONG SELL"
        color = "red"
        explanation = "High probability of price decrease. Unfavorable conditions."
    
    st.markdown(f"""
    <div style="background-color:{color}20; padding:20px; border-radius:10px; border-left:5px solid {color};">
        <h3 style="color:{color}; text-align:center;">{recommendation}</h3>
        <p style="text-align:center;">{explanation}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # feature impact analysis
    st.subheader("🔍 Feature Impact Analysis")
    
    coefficients = model.coef_[0]
    features = ['USD Index', 'Treasury Yield', 'Inflation Rate']
    
    fig, ax = plt.subplots(figsize=(8, 4))
    colors = ['#FF6B6B' if c < 0 else '#4ECDC4' for c in coefficients]
    bars = ax.barh(features, coefficients, color=colors)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_xlabel('Impact on Price Increase Probability')
    ax.set_title('How Each Factor Affects Gold Price')
    
    for bar, coeff in zip(bars, coefficients):
        width = bar.get_width()
        label_x = width + (0.01 if width >= 0 else -0.01)
        ax.text(label_x, bar.get_y() + bar.get_height()/2, 
                f'{coeff:.3f}', ha='left' if width >= 0 else 'right', 
                va='center')
    
    st.pyplot(fig)
    
    # current input values
    st.subheader("📋 Current Input Values")
    input_df = pd.DataFrame({
        'Factor': ['USD Index', 'Treasury Yield', 'Inflation Rate'],
        'Value': [usd, f"{treasury}%", f"{inflation}%"],
        'Impact': ['Negative' if c < 0 else 'Positive' for c in coefficients]
    })
    st.dataframe(input_df, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.info("""
**About this tool:**
- Uses logistic regression model
- Trained on 2016-2026 monthly data
- For educational purposes only
- Not financial advice
""")

# reset button
if st.sidebar.button("Reset to Defaults"):
    st.rerun()

print("✅ Streamlit app is running...")