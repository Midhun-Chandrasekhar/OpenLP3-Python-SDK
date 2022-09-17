# OpenLP Python SDK
Open Loyality Points (OpenLP) is an opensource Loyality Point platform build top on public blockchain.

##Installation
pip install openlp

##Usage
###Import
from openlp import OpenLP

###Initializing
olp = OpenLP("network_address", "contract_address", "contract_owner_private_key", "contract_abi")

###Contract Information
olp.contract_info()

###Issue loyality point to wallet
olp.issue_points("wallet_address", 1000)

###Burn loyality point to wallet
olp.burn_points("wallet_address", 100)

###Get Loyality balance
olp.user_points("wallet_address")