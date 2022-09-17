from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account
from openlp.utils import defaults


class OpenLP:
    """
    Instantiate a Open Loyality Point Client object.
    OpenLP object can help interact easily with the OpenLP smart contract.

    :param network_address: Network address of blockchain.
    :type network_address: string
    :example http://localhost:port/

    :param contract_address: OpenLP smart contract Address.
    :type contract_address: string

    :param owner_private_key: The multiplier.
    :type owner_private_key: string

    :param abi: The abi for the deployed OpenLP smart contract.
    :type abi: string

    :param transaction: dict.
    :type transaction: string
    example {
            'gas': 1
        }
    """

    def __init__(self, network_address, contract_address,
                 owner_private_key, abi=None, transaction=None):
        self.owner = Account.from_key(owner_private_key)
        self.w3 = Web3(Web3.HTTPProvider(network_address))
        self.w3.eth.default_account = self.owner.address
        self.w3.middleware_onion.add(
            construct_sign_and_send_raw_middleware(
                self.owner))
        abi = abi if abi else defaults.abi
        self.contract = self.w3.eth.contract(contract_address, abi=abi)
        self.functions = self.contract.functions
        self.caller = self.contract.caller()
        self.transaction_obj = transaction if transaction else defaults.transaction

    def contract_info(self):
        """
        :return: OpenLP Smart contract details
        :rtype: string
        """
        return self.caller.getInfo()

    @staticmethod
    def version():
        """
        :return: OpenLP Python SDK version
        :rtype: string
        """
        return "OpenLP Version Python SDK 0.1.0"

    def user_points(self, user_address):
        """
        Point issue activity interface.

        :param user_address: User wallet address to get point balance.
        :type user_address: string

        :return: Activity response
        :rtype: int
        """
        return self.caller.userPoints(user_address)

    def issue_points(self, user_address, points):
        """
        Point issue activity interface.

        :param user_address: User wallet address to issue points.
        :type user_address: string

        :param points: Points to be issued.
        :type points: int

        :return: Activity response
        :rtype: string
        """
        return self.functions.issuePoint(
            user_address, points).transact(
            self.transaction_obj)

    def burn_points(self, user_address, points):
        """
        Point issue activity interface.

        :param user_address: User wallet address to burn points.
        :type user_address: string

        :param points: Points to be issued.
        :type points: int

        :return: Activity response
        :rtype: string
        """
        return self.functions.burnPoint(
            user_address, points).transact(
            self.transaction_obj)
