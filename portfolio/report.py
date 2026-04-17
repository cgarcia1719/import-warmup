from portfolio import metrics

def print_report(portfolio: list[dict]) -> None:
    total = metrics.calculate_portfolio_value(portfolio)
    print(f"PORTFOLIO SUMMARY\nPortfolio Name: {portfolio["name"]}")
    print("--------------------")
    print(f"Number of assets: {len(portfolio["assets"])}")
    print(f"Total value: ${total:,.2f}")
