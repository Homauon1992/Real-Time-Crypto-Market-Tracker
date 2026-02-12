import os
import time
from typing import List, Dict, Any

import requests
from colorama import Fore, Style, init


COIN_IDS = [
    "bitcoin",
    "ethereum",
    "tether",
    "binancecoin",
    "solana",
]

API_URL = "https://api.coingecko.com/api/v3/coins/markets"


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def fetch_market_data(coin_ids: List[str]) -> List[Dict[str, Any]]:
    response = requests.get(
        API_URL,
        params={
            "vs_currency": "usd",
            "ids": ",".join(coin_ids),
            "order": "market_cap_desc",
            "per_page": len(coin_ids),
            "page": 1,
            "sparkline": "false",
            "price_change_percentage": "24h",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def format_currency(value: float) -> str:
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"${value / 1_000:.2f}K"
    return f"${value:,.2f}"


def format_table(rows: List[Dict[str, Any]]) -> str:
    headers = ["Crypto", "Price (USD)", "24h Change", "Market Cap"]
    lines = [headers]

    for coin in rows:
        change = coin.get("price_change_percentage_24h", 0.0)
        change_text = f"{change:+.2f}%"
        color = Fore.GREEN if change >= 0 else Fore.RED
        colored_change = f"{color}{change_text}{Style.RESET_ALL}"

        lines.append(
            [
                coin.get("name", "N/A"),
                f"${coin.get('current_price', 0):,.2f}",
                colored_change,
                format_currency(coin.get("market_cap", 0)),
            ]
        )

    col_widths = [0] * len(headers)
    for row in lines:
        for idx, cell in enumerate(row):
            cell_length = len(str(cell).replace(Fore.GREEN, "").replace(Fore.RED, "").replace(Style.RESET_ALL, ""))
            col_widths[idx] = max(col_widths[idx], cell_length)

    output_lines = []
    for row_index, row in enumerate(lines):
        padded_cells = []
        for idx, cell in enumerate(row):
            cell_str = str(cell)
            plain_len = len(
                cell_str.replace(Fore.GREEN, "").replace(Fore.RED, "").replace(Style.RESET_ALL, "")
            )
            padding = " " * (col_widths[idx] - plain_len)
            padded_cells.append(f"{cell_str}{padding}")
        output_lines.append(" | ".join(padded_cells))
        if row_index == 0:
            separator = "-+-".join("-" * width for width in col_widths)
            output_lines.append(separator)

    return "\n".join(output_lines)


def main() -> None:
    init(autoreset=True)

    while True:
        try:
            data = fetch_market_data(COIN_IDS)
            clear_screen()
            print("Real-Time Crypto Prices (Top 5 by Market Cap)\n")
            print(format_table(data))
        except requests.RequestException as exc:
            clear_screen()
            print("Network error while fetching data.")
            print(f"Details: {exc}")
        except Exception as exc:
            clear_screen()
            print("Unexpected error.")
            print(f"Details: {exc}")

        time.sleep(10)


if __name__ == "__main__":
    main()
