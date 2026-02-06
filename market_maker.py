import ccxt
import time

class SimpleMarketMaker:
    def __init__(self, symbol='BTC/USDT'):
        self.exchange = ccxt.binance()
        self.symbol = symbol
        self.spread = 0.001

    def get_market_price(self):
        ticker = self.exchange.fetch_ticker(self.symbol)
        return ticker['last']

    def run(self):
        print(f"--- Starting Market Maker on {self.symbol} ---")
        while True:
            try:
                mid_price = self.get_market_price()
                
                bid_price = mid_price * (1 - self.spread)
                ask_price = mid_price * (1 + self.spread)
                
                print(f"Market: ${mid_price:,.2f}")
                print(f"  🔹 PLACING BID: ${bid_price:,.2f} (Buy)")
                print(f"  🔸 PLACING ASK: ${ask_price:,.2f} (Sell)")
                print(f"  💰 Target Spread: ${ask_price - bid_price:.2f}")
                
                time.sleep(5)
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    mm = SimpleMarketMaker()
    mm.run()