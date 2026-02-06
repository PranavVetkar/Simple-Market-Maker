# 🏦 Simple Market Maker (Crypto)

A Python-based **market making simulator** that demonstrates how liquidity providers place buy and sell orders around the current market price to capture the bid–ask spread.

This project models the core mechanics of market making without executing real trades.

---

## 🚀 What This Project Does

- Connects to Binance via **CCXT**
- Fetches the live market price
- Calculates bid & ask quotes around mid-price
- Simulates spread capture opportunities
- Continuously updates quotes in real time

---

## 🧠 Market Making Concept

Market makers provide liquidity by placing:

- **Bid Orders** → Buy below market price  
- **Ask Orders** → Sell above market price  

Profit comes from the **spread**:
- Spread Profit = Ask Price − Bid Price
- This project simulates that quoting behavior.

---

## ⚙️ Strategy Logic

1. Fetch current market price (mid-price)
2. Apply target spread percentage
3. Calculate quotes:

- Bid = Mid × (1 − Spread)
- Ask = Mid × (1 + Spread)


4. Display simulated order placements

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **CCXT**
- **Binance API**
- **Time-based polling**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Simple-Market-Maker.git
cd Simple-Market-Maker
