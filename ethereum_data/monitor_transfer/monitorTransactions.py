from web3 import Web3
import time 

infura_url = 'https://mainnet.infura.io/v3/865751797f4045019b7203001b8c7c91'
account = '0xE592427A0AEce92De3Edee1F18E0157C05861564'
web3 = Web3(Web3.HTTPProvider(infura_url))

def confirmations(tx_hash):
    tx = web3.eth.get_transaction(tx_hash)
    return web3.eth.block_number - tx.blockNumber

def watch():
    while True:
        block = web3.eth.get_block('latest')
        print("Searching in block " + str(block.number))

        if block and block.transactions: 
            for transaction in block.transactions: 
                tx_hash = transaction.hex() # the hashes are stored in a hexBytes format
                tx = web3.eth.get_transaction(tx_hash)
                if tx.to != None:
                    if tx.to == account:
                        print("Transaction found in block {} :".format(block.number))
                        print({
                            "hash": tx_hash,
                            "from": tx["from"],
                            "value": web3.fromWei(tx["value"], 'ether')
                            })
        time.sleep(5)

watch()
# print(confirmations("0x0d40d60e118e9e1f61c2baa2252cc5f8b8ed491c885ec35db6fd6cfc8589c1a7"))