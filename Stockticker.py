import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class StockPriceWidget(QWidget):
    def __init__(self, stock_prices):
        super().__init__()
        self.stock_prices = stock_prices
        self.current_index = 0

        self.label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stock_price)
        self.timer.start(1000)  # Update every second

    def update_stock_price(self):
        self.label.setText(self.stock_prices[self.current_index])
        self.current_index = (self.current_index + 1) % len(self.stock_prices)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    stock_prices = [
        'AAPL: $142.23',
        'GOOGL: $2700.15',
        'MSFT: $256.78',
        'AMZN: $3515.00',
    ]

    widget = StockPriceWidget(stock_prices)
    widget.show()

    sys.exit(app.exec_())
