# Uniswap Memecoin Swapper on Base Network

This script allows you to swap memecoins on Uniswap V3 using the Base network. It interacts with Uniswap's smart contracts via Web3.py and executes token swaps.

## Features
- Uses **Uniswap V3 Router** to swap WETH for a memecoin.
- Supports the **Base network** (Layer 2 solution).
- Uses **Web3.py** to connect to Ethereum and sign transactions.
- Customizable **slippage settings** and **gas limits**.

---

## Requirements
### **Install Dependencies**
Ensure you have Python installed, then install the required packages:
```sh
pip install web3 eth-account
```

### **Set Up Environment Variables**
Before running the script, set up your wallet details:
```sh
export PRIVATE_KEY="your_private_key"
export INFURA_URL="https://base-mainnet.infura.io/v3/your_project_id"
export WALLET_ADDRESS="your_wallet_address"
```

### **Base Network Uniswap V3 Router**
- **Router Address**: `0xE592427A0AEce92De3Edee1F18E0157C05861564`
- **WETH Contract**: `0x4200000000000000000000000000000000000006`
- **Memecoin Address**: Replace with your desired token contract

---

## Usage
### **Run the Swap Script**
```sh
python swap_memecoin.py
```
This will swap **0.01 WETH** for your selected memecoin.

---

## Code Explanation
- **Connects to Base Network** via Infura/Alchemy.
- **Builds a Uniswap transaction** using `exactInputSingle`.
- **Signs and broadcasts** the transaction to the network.
- **Prints the transaction hash** for tracking.

---

## Notes
- Make sure you have **enough ETH for gas fees**.
- Adjust **`fee` parameter** (3000 for 0.3%, 500 for 0.05% pools).
- Consider **implementing slippage protection** (`amountOutMinimum > 0`).
- Use [Basescan](https://basescan.org) to track transactions.

---

## License
This project is open-source and free to use under the **MIT License**.

