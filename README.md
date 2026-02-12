# 🪙 Real-Time Crypto Market Tracker

A sophisticated Python application that monitors the top cryptocurrency assets by market capitalization. This tool provides a live, auto-refreshing terminal dashboard powered by the CoinGecko REST API.

## 🛠 Key Technical Features
* **REST API Integration:** Performs high-speed data fetching using the `Requests` library to communicate with professional financial APIs.
* **Dynamic Terminal UI:** Features an automated screen-clearing logic and a formatted table structure for a clean, real-time monitoring experience.
* **Intelligent Data Formatting:** Automatically converts large financial numbers into readable formats (K, M, B) and implements color-coded logic for 24h price fluctuations.
* **Error Resilience:** Includes robust exception handling for network interruptions and API request failures to ensure continuous operation.

## 📦 Tech Stack
* **Python:** Core Logic & Formatting.
* **Requests:** REST API communication.
* **Colorama:** Enhanced UI feedback with color-coded market trends.
* **CoinGecko API:** Professional-grade market data source.

## 🚀 How to Run
1. Install dependencies: `pip install requests colorama`.
2. Run the tracker: `python crypto_tracker.py`.
3. View live updates for Bitcoin, Ethereum, and more every 10 seconds.