import subprocess
import sys
# PyQt5 looks better than Tkinter
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Packages to install
required_packages = ['requests', 'pyqt5']

# Check if a package is already installed
def is_package_installed(package):
    return package in sys.modules

# Install required packages
def install_packages(packages):
    for package in packages:
        if not is_package_installed(package):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Install required packages automatically
install_packages(required_packages)

import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def get_price(symbol):
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {
        'symbol': symbol
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['price']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Prices")
        self.label = QLabel(self)
        font = self.label.font()
        font.setPointSize(font.pointSize() + 4)  # Set the font size
        self.label.setFont(font)
        self.setCentralWidget(self.label)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.fetch_and_display_prices)
        self.timer.start(1000)  # Update every second (1000 milliseconds)

    def fetch_and_display_prices(self):
        btc_price = get_price('BTCUSDT')
        eth_price = get_price('ETHUSDT')
        self.label.setText(f'BTC: {btc_price}\nETH: {eth_price}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 250, 150)
    window.show()
    sys.exit(app.exec_())
