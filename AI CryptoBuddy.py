# CryptoBuddy - Your First AI-Powered Financial Sidekick!..
# A beginner-friendly crypto advisor chatbot with basic AI logic in Python.

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

def get_most_sustainable():
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    score = crypto_db[recommend]["sustainability_score"]
    return f"{recommend} is the most sustainable coin with a sustainability score of {score*10:.0f}/10! 🌱"

def get_trending_cryptos():
    trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
    if trending:
        return f"The trending cryptocurrencies are: {', '.join(trending)}! 🚀"
    else:
        return "No cryptocurrencies are currently trending up."

def get_best_for_growth():
    # Prioritize coins with price_trend "rising" and market_cap "high"
    candidates = [coin for coin, data in crypto_db.items() if 
                  data["price_trend"] == "rising" and data["market_cap"] == "high"]
    if candidates:
        return f"For long-term growth, consider {candidates[0]}! It's trending up with a high market cap. 🚀"
    else:
        # fallback to any rising and medium cap coin
        candidates = [coin for coin, data in crypto_db.items() if 
                      data["price_trend"] == "rising" and data["market_cap"] == "medium"]
        if candidates:
            return f"{candidates[0]} is trending up and has medium market cap. It might be worth considering."
        else:
            return "No strong growth recommendations at the moment."

def get_best_for_sustainability():
    # Prioritize coins with energy_use "low" and sustainability_score > 7/10
    candidates = [coin for coin, data in crypto_db.items() if 
                  data["energy_use"] == "low" and data["sustainability_score"] > 0.7]
    if candidates:
        return f"For eco-friendly investment, {candidates[0]} stands out with low energy use and high sustainability."
    else:
        return "No eco-friendly options meet the criteria right now."

def print_welcome():
    print("CryptoBuddy: Hey there! Let’s find you a green and growing crypto! 🌱")
    print("Ask me things like:")
    print("- Which crypto is trending up?")
    print("- What’s the most sustainable coin?")
    print("- Which crypto should I buy for long-term growth?")
    print("- Recommend me an eco-friendly coin")
    print("Type 'exit' or 'quit' to leave.\n")

def main():
    print_welcome()
    while True:
        user_query = input("You: ").strip().lower()
        if user_query in ("exit", "quit"):
            print("CryptoBuddy: Goodbye! Happy investing! 💰")
            break
        response = "Sorry, I didn't quite catch that. Please ask about trending, sustainability, or growth."
        if "sustainable" in user_query or "eco" in user_query or "green" in user_query:
            response = get_most_sustainable()
        elif "trending" in user_query or ("price" in user_query and "trend" in user_query):
            response = get_trending_cryptos()
        elif "growth" in user_query or "long-term" in user_query or "buy" in user_query:
            response = get_best_for_growth()
        elif "eco-friendly" in user_query or "energy" in user_query:
            response = get_best_for_sustainability()

        print(f"CryptoBuddy: {response}")
        print("CryptoBuddy: Remember, crypto is risky—always do your own research! ⚠️\n")

if __name__ == "__main__":
    main()

