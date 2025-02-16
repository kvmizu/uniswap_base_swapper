# Uniswap Memecoin Trader on Base Network

This Python script facilitates trading memecoins on Uniswap's Base network using Web3 and the Uniswap v2-style router.

## Features
- Connects to the Base network via Infura.
- Swaps ETH for a specified memecoin.
- Implements transaction signing and submission.
- Customizable slippage and deadline settings.

## Prerequisites
- Python 3.7+
- Infura Project ID
- Web3 Python library
- Private key with funded ETH for gas fees

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/uniswap-base-trader.git
   cd uniswap-base-trader
   ```
2. Install dependencies:
   ```sh
   pip install web3 eth_account
   ```
3. Download the Uniswap router ABI:
   - Save it as `uniswap_router_abi.json` in the project directory.

## Configuration
- Update `INFURA_URL` with your Infura project ID.
- Set `PRIVATE_KEY` to your wallet’s private key.
- Define the `TOKEN_ADDRESS` for the memecoin.

## Usage
Run the script to swap ETH for the specified token:
```sh
python uniswap_base_trader.py
```

## Notes
- Ensure your wallet has enough ETH for gas fees.
- The default slippage is 0.5% and can be adjusted.
- Transactions are sent via the Uniswap router.

## Disclaimer
Use at your own risk. Ensure your private key is kept secure and never exposed in public repositories.

