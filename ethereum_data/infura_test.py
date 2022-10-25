#pip install web3
#python3 -m pip install web3
#pip install etherscan
# python3 -m pip install etherscan

import Web3, HTTPProvider
connection = Web3(HTTPProvider('https://mainnet.infura.io/v3/865751797f4045019b7203001b8c7c91'))
print ("Latest Ethereum block number", connection.eth.blockNumber)

# import pandas as pd
# import web3
# import etherscan
# import warnings

# warnings.filterwarnings('ignore')

# # APIs 
# eth = etherscan("QS7M5JJPJFDNKQA1THE6PYAZSCNRC287DY")
# projectID= '865751797f4045019b7203001b8c7c91'
# w3 = web3(web3.HTTPProvider(projectID))

# target_address='0xa57Bd00134B2850B2a1c55860c9e9ea100fDd6CF'
# start_block=14640000
# end_block=14650000

# transactions=eth.get_normal_txs_by_address(address=target_address, startblock= start_block, endblock= end_block, sort="asc")
# tx_df=pd.DataFrame(transactions)