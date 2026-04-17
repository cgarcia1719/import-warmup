from portfolio import metrics

def make_asset(ticker: str, price: float, quantity: int) -> dict:
    return {
        "ticker": ticker,
        "price": price,
        "quantity": quantity
    }

def get_asset_value(asset: dict) -> float:
    return metrics.calculate_asset_value(asset)