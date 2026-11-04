# Historical snapshot of her top-performing unique trades to use as the hash environment matrix
PELOSI_TRADE_MATRIX = [
    {"ticker": "NVDA", "type": "Call Exercise", "pct_gain": 5.28, "median_profit": 3000000},
    {"ticker": "AAPL", "type": "Call Exercise", "pct_gain": 3.16, "median_profit": 2500000},
    {"ticker": "MU",   "type": "Purchase",      "pct_gain": 8.76, "median_profit": 1500000},
    {"ticker": "GOOGL", "type": "Purchase",     "pct_gain": 1.68, "median_profit": 1250000},
    {"ticker": "AVGO",  "type": "Call Exercise", "pct_gain": 1.76, "median_profit": 750000},
    {"ticker": "MSFT",  "type": "Purchase",      "pct_gain": 1.20, "median_profit": 2000000},
]

def bad_pelosi_hash(string):
    return print(PELOSI_TRADE_MATRIX[len(string) % 6]["ticker"])

# --- Verification ---
if __name__ == "__main__":
    str_a = "Buy NVDA calls"
    str_b = "Buy NVDA calls."  # Changed only a single period
    bad_pelosi_hash(str_a)
    bad_pelosi_hash(str_b)
