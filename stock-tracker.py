import csv

def stock_portfolio_tracker():
    # 1. Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 140.0,
        "MSFT": 400.0,
        "AMZN": 175.0
    }

    portfolio = {}

    print("==========================================")
    print("      STOCK PORTFOLIO TRACKER             ")
    print("==========================================")
    print("Available Stocks and Prices:")
    for stock, price in stock_prices.items():
        print(f"  • {stock}: ${price:.2f}")
    print("==========================================\n")

    # 2. User Input Loop
    while True:
        symbol = input("Enter stock symbol to add (or type 'DONE' to calculate): ").strip().upper()

        if symbol == 'DONE':
            break

        if symbol not in stock_prices:
            print(f"❌ '{symbol}' is not in the price list. Please choose from: {', '.join(stock_prices.keys())}\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.\n")
                continue
            
            # Add or update quantity in user's portfolio
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
            print(f"✅ Added {quantity} shares of {symbol}.\n")

        except ValueError:
            print("❌ Invalid input! Quantity must be a whole number.\n")

    # If portfolio is empty, exit
    if not portfolio:
        print("\nNo stocks added. Portfolio is empty.")
        return

    # 3. Calculate Total Investment Value
    print("\n==========================================")
    print("         YOUR PORTFOLIO SUMMARY           ")
    print("==========================================")
    print(f"{'Stock':<10} {'Qty':<10} {'Price ($)':<12} {'Total Value ($)':<15}")
    print("-" * 48)

    grand_total = 0.0
    summary_data = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        total_value = qty * price
        grand_total += total_value
        
        summary_data.append([stock, qty, f"${price:.2f}", f"${total_value:.2f}"])
        print(f"{stock:<10} {qty:<10} ${price:<11.2f} ${total_value:<14.2f}")

    print("-" * 48)
    print(f"TOTAL INVESTMENT VALUE: ${grand_total:,.2f}")
    print("==========================================\n")

    # 4. File Handling (Save to .txt or .csv)
    save_file = input("Would you like to save this summary to a file? (txt/csv/no): ").strip().lower()

    if save_file == 'txt':
        with open("portfolio_summary.txt", "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 35 + "\n")
            for stock, qty, price, total in summary_data:
                file.write(f"{stock}: {qty} shares @ {price} = {total}\n")
            file.write("=" * 35 + "\n")
            file.write(f"Total Investment Value: ${grand_total:,.2f}\n")
        print("💾 Portfolio saved successfully as 'portfolio_summary.txt'!")

    elif save_file == 'csv':
        with open("portfolio_summary.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock Symbol", "Quantity", "Unit Price", "Total Value"])
            for row in summary_data:
                writer.writerow(row)
            writer.writerow([])
            writer.writerow(["TOTAL INVESTMENT", "", "", f"${grand_total:,.2f}"])
        print("💾 Portfolio saved successfully as 'portfolio_summary.csv'!")

    else:
        print("Summary not saved to file.")

# Run the program
if __name__ == "__main__":
    stock_portfolio_tracker()