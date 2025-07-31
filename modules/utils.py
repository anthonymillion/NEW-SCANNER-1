def generate_sentiment_score(symbol, calendar, geopolitics, cot, options):
    driver = ""
    sentiment = "Neutral"

    # Geopolitical bias
    if symbol in ["GOLD", "OIL", "SP500", "DAX", "BTCUSD", "ETHUSD"]:
        if len(geopolitics) > 10:
            driver += "Heavy Geopolitical Risk | "
            if symbol in ["GOLD", "BTCUSD"]:
                sentiment = "Bullish"
            elif symbol in ["SP500", "DAX"]:
                sentiment = "Bearish"

    # Economic events
    for event in calendar:
        if symbol in event.get("Country", ""):
            if "Actual" in event and "Forecast" in event:
                if event["Actual"] > event["Forecast"]:
                    driver += f"{event['Event']} beat | "
                    sentiment = "Bullish"
                else:
                    driver += f"{event['Event']} miss | "
                    sentiment = "Bearish"

    # COT
    cot_sent = cot.get(symbol)
    if cot_sent:
        driver += f"COT {cot_sent} | "
        sentiment = cot_sent

    # Options Flow
    option_sent = options.get(symbol)
    if option_sent:
        driver += f"Options Flow {option_sent} | "
        sentiment = option_sent

    return sentiment, driver.strip(" | ")