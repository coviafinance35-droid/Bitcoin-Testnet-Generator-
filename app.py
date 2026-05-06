from flask import Flask, request, jsonify
from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.networks import Network

app = Flask(__name__)

# Define the minimum and maximum transaction amounts (in satoshis)
MIN_BTC = 1 * 10**8  # 1 BTC = 100,000,000 satoshis
MAX_BTC = 10 * 10**8  # 10 BTC = 1,000,000,000 satoshis

# Setting up the Bitcoin Testnet network
Network('bitcoin_testnet')

@app.route('/generate_wallet', methods=['POST'])
def generate_wallet():
    """
    Generate a new wallet with a Bitcoin Testnet Address.
    """
    wallet_name = 'testnet_wallet'
    wallet_delete(wallet_name)  # Clean up old wallet with the same name (for testing)
    wallet = Wallet.create(wallet_name, network='bitcoin_testnet')
    address = wallet.get_key().address
    private_key = wallet.get_key().private_hex

    return jsonify({
        "message": "Wallet successfully created!",
        "address": address,
        "private_key": private_key,
    })


@app.route('/send_transaction', methods=['POST'])
def send_transaction():
    """
    Send BTC to a testnet address.
    """
    data = request.get_json()
    sender_private_key = data.get('private_key')
    recipient_address = data.get('recipient_address')
    amount_satoshis = int(data.get('amount_satoshis'))  # Send amount in satoshis

    if amount_satoshis < MIN_BTC or amount_satoshis > MAX_BTC:
        return jsonify({"error": "Transaction amount must be between 1 BTC and 10 BTC"}), 400

    # Load the sender wallet from the private key (Use existing wallet)
    sender_wallet = Wallet(network='bitcoin_testnet').from_key(sender_private_key)

    # Create and send the transaction
    tx = sender_wallet.send_to(recipient_address, amount_satoshis)

    return jsonify({
        "message": "Transaction successfully sent!",
        "transaction_id": tx.txid,
    })


@app.route('/check_balance', methods=['GET'])
def check_balance():
    """
    Check wallet balance (given a public address).
    """
    wallet_name = request.args.get('wallet_name')

    # Load wallet and check balance
    wallet = Wallet(wallet_name, network='bitcoin_testnet')
    balance = wallet.balance(as_text=True)

    return jsonify({
        "message": "Wallet balance fetched successfully!",
        "wallet_name": wallet_name,
        "balance": balance,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)