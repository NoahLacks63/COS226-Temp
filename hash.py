PELOSI_TRADE_MATRIX = [
    {"ticker": "NVDA", "type": "Call Exercise", "pct_gain": 5.28, "median_profit": 3000000},
    {"ticker": "AAPL", "type": "Call Exercise", "pct_gain": 3.16, "median_profit": 2500000},
    {"ticker": "MU", "type": "Purchase", "pct_gain": 8.76, "median_profit": 1500000},
    {"ticker": "GOOGL", "type": "Purchase", "pct_gain": 1.68, "median_profit": 1250000},
    {"ticker": "AVGO", "type": "Call Exercise", "pct_gain": 1.76, "median_profit": 750000},
    {"ticker": "MSFT", "type": "Purchase", "pct_gain": 1.20, "median_profit": 2000000},
]

def bad_pelosi_hash(string):
    """
    Parameters:
        string (str): The input string to hash.

    Returns:
        int: The hashed integer.
    """

    result = ""

    for char in string:
        ascii = ord(char)
        ascii_ticker = ascii % len(PELOSI_TRADE_MATRIX)

        result += str(ascii * int(PELOSI_TRADE_MATRIX[ascii_ticker]["pct_gain"] * 100))
    return int(result[::len(result)]) % 32749

def good_pelosi_hash(s):
    result = 0

    for i in range(len(s)):
        ascii = ord(s[i])
        result += ascii + i

    return result % 32749 