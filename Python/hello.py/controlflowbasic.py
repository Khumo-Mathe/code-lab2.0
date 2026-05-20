from datetime import datetime
import statistics


class StockPriceAnalyzer:
    """
    Analyze stock price movements
    and generate trading signals.
    """

    def __init__(self):
        self.price_history = []

    def add_price(
        self,
        symbol,
        price
    ):
        """
        Store stock price data.
        """

        self.price_history.append({
            "symbol": symbol,
            "price": price,
            "timestamp": datetime.now()
        })

    def moving_average(
        self,
        period
    ):
        """
        Calculate moving average.
        """

        if len(self.price_history) < period:
            return None

        recent_prices = [
            entry["price"]
            for entry in self.price_history[-period:]
        ]

        return round(
            statistics.mean(recent_prices),
            2
        )

    def generate_signal(self):
        """
        Generate simple trading signal.

        Buy:
            Short-term MA > Long-term MA

        Sell:
            Short-term MA < Long-term MA
        """

        short_ma = self.moving_average(3)
        long_ma = self.moving_average(5)

        if short_ma is None or long_ma is None:
            return {
                "signal": "INSUFFICIENT_DATA"
            }

        if short_ma > long_ma:
            signal = "BUY"

        elif short_ma < long_ma:
            signal = "SELL"

        else:
            signal = "HOLD"

        return {
            "signal": signal,
            "short_ma": short_ma,
            "long_ma": long_ma
        }

    def volatility(self):
        """
        Calculate price volatility
        using standard deviation.
        """

        if len(self.price_history) < 2:
            return None

        prices = [
            entry["price"]
            for entry in self.price_history
        ]

        return round(
            statistics.stdev(prices),
            2
        )


# Example usage
analyzer = StockPriceAnalyzer()

prices = [100, 102, 105, 103, 108, 110]

for price in prices:
    analyzer.add_price(
        symbol="AAPL",
        price=price
    )

signal = analyzer.generate_signal()

volatility = analyzer.volatility()