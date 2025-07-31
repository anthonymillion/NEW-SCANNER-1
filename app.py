import streamlit as st
from modules.economic_calendar import get_economic_events
from modules.geopolitical_risk import get_geopolitical_sentiment
from modules.cot_data import get_cot_sentiment
from modules.options_flow import get_options_sentiment
from modules.utils import generate_sentiment_score

st.set_page_config(layout="wide")
st.title("🌍 AI Sentiment Scanner")

symbols = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "NZD",
           "GOLD", "SILVER", "OIL", "SP500", "NASDAQ", "DOW", "DAX", "NIKKEI", 
           "BTCUSD", "ETHUSD", "NVDA", "TSLA", "AAPL", "AMZN", "GOOGL", "META"]

# Fetch data
calendar_data = get_economic_events()
geopolitical_sentiment = get_geopolitical_sentiment()
cot_sentiment = get_cot_sentiment()
options_sentiment = get_options_sentiment()

# Display table
st.markdown("### 🌐 Sentiment Dashboard")
rows = []
for symbol in symbols:
    score, driver = generate_sentiment_score(
        symbol, calendar_data, geopolitical_sentiment, cot_sentiment, options_sentiment
    )
    rows.append((symbol, driver, score))

st.dataframe(
    rows,
    column_config={"Symbol": "Symbol", "Driver": "Driver", "Sentiment": "Sentiment"},
    use_container_width=True
)