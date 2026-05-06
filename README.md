# Bitcoin Testnet Generator

This repository provides a simple backend for creating Bitcoin Testnet wallets, sending transactions, and checking wallet balances. It is designed for Testnet4 and includes features such as transaction limits and seamless API integration.

## Features
- Generate Bitcoin Testnet wallets.
- Send BTC to other Testnet wallets.
- Receive BTC in generated wallets.
- Check wallet balances in Testnet.

## Requirements
- Python 3.9+
- Flask
- bitcoinlib

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/coviafinance35-droid/Bitcoin-Testnet-Generator-.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Bitcoin-Testnet-Generator-
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints
### 1. Generate Wallet
**Endpoint:** `/generate_wallet`
- Method: `POST`
- Response:
  ```json
  {
    "message": "Wallet successfully created!",
    "address": "mz8J28ZX...",
    "private_key": "L1aW4aubDFB7yfras2S ..."
  }
  ```

### 2. Send BTC
**Endpoint:** `/send_transaction`
- Method: `POST`
- Body:
  ```json
  {
    "private_key": "...",
    "recipient_address": "...",
    "amount_satoshis": 100000000
  }
  ```

### 3. Check Balance
**Endpoint:** `/check_balance`
- Method: `GET`
- Params: `wallet_name`
- Response:
  ```json
  {
    "message": "Wallet balance fetched successfully!",
    "wallet_name": "test_wallet",
    "balance": "1.234 BTC"
  }
  ```