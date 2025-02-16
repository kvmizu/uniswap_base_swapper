from web3 import Web3
import json
import os

# Load environment variables (Set these before running the script)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet private key
INFURA_URL = os.getenv("INFURA_URL")  # Your Base network RPC (Infura/Alchemy)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Your wallet address

# Uniswap V3 router on Base
UNISWAP_V3_ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"

# Token Addresses (Example: WETH & Memecoin)
WETH = "0x4200000000000000000000000000000000000006"  # Wrapped ETH on Base
MEMECOIN = "0xYourMemecoinContractAddressHere"  # Replace with your meme coin contract

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
assert web3.is_connected(), "Failed to connect to Base Network"

# Load Uniswap Router ABI (Minimal ABI for `exactInputSingle`)
UNISWAP_ROUTER_ABI = json.loads('[{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactInputSingleParams","name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"}]')

# Initialize Uniswap contract
uniswap_router = web3.eth.contract(address=UNISWAP_V3_ROUTER, abi=UNISWAP_ROUTER_ABI)

def swap_tokens(amount_in_wei):
    """Swap WETH for Memecoin on Uniswap V3 (Base Network)"""
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    
    # Define transaction parameters
    swap_params = (
        WETH,          # tokenIn (WETH)
        MEMECOIN,      # tokenOut (Memecoin)
        3000,          # fee (0.3% fee tier, adjust as needed)
        WALLET_ADDRESS, # recipient
        web3.eth.get_block('latest')['timestamp'] + 600,  # deadline (10 minutes)
        amount_in_wei,  # amountIn
        0,              # amountOutMinimum (Set to 0 for no slippage protection)
        0               # sqrtPriceLimitX96 (0 means no limit)
    )
    
    # Encode function call
    txn = uniswap_router.functions.exactInputSingle(swap_params).build_transaction({
        'from': WALLET_ADDRESS,
        'value': 0,  # Uniswap V3 uses ERC-20 swaps, so value is 0
        'gas': 250000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce
    })
    
    # Sign and send transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    print(f"Transaction sent! Hash: {tx_hash.hex()}")

# Example: Swap 0.01 WETH for Memecoins
swap_tokens(web3.to_wei(0.01, 'ether'))
