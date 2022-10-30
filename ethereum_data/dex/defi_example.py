import pandas as pd
from web3 import Web3
from etherscan import Etherscan
import warnings
warnings.filterwarnings('ignore')

eth = Etherscan("QS7M5JJPJFDNKQA1THE6PYAZSCNRC287DY")
projectID= '865751797f4045019b7203001b8c7c91'
w3 = Web3(Web3.HTTPProvider(projectID))

target_address='0xa57Bd00134B2850B2a1c55860c9e9ea100fDd6CF'
start_block=14640000
end_block=14650000

transactions=eth.get_normal_txs_by_address(address=target_address, startblock= start_block, endblock= end_block, sort="asc")
tx_df=pd.DataFrame(transactions)