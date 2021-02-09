from web3 import Web3
import sys
import json
import binascii, os
import random
import time

# account info
WEB3_PROVIDER_ADDRESS = "https://ropsten.infura.io/v3/YOUR_ENDPOINT"
MY_ADDRESS = Web3.toChecksumAddress("YOUR_ACCOUNT_ADDRESS")
MY_PRIVATE_KEY = "YOUR_PRIVATE_KEY"

# betting params
INITIAL_BET_AMOUNT = 4 # min value: 2
ONE_SHOT_BET_AMOUNT = 2002
BET_PROBABILITY = 40 # percent
GAS_AMOUNT = 500000
TARGET_AMOUNT = 200000
TX_WAIT_TIMEOUT = 300 # seconds

# Ropsten test net addresses
BET_CONTRACT_ADDRESS = Web3.toChecksumAddress("0x85F90E26704053464C6A07a79c9792c292e420Ce")
LPT_TOKEN_CONTRACT_ADDRESS = Web3.toChecksumAddress("0x7FDC8ebAa8a239D1a2b197aB27A9784a35a7D087")

# get contract
def getContract(address, abiString):
    address = Web3.toChecksumAddress(address)
    contractABI = json.loads(abiString)
    contract = fullnode.eth.contract(address=address, abi=contractABI)
    return contract

# connect to infura test net
fullnode = Web3(Web3.HTTPProvider(WEB3_PROVIDER_ADDRESS))
print("is full node connected:", fullnode.isConnected())
print("current block number:", fullnode.eth.blockNumber)

# get contract
betContractABIStr = '[ { "inputs": [ { "internalType": "address", "name": "initialLPTAddress", "type": "address" }, { "internalType": "address", "name": "initialRandomAddress", "type": "address" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "who", "type": "address" }, { "indexed": false, "internalType": "uint24", "name": "amount", "type": "uint24" }, { "indexed": false, "internalType": "uint8", "name": "percentage", "type": "uint8" } ], "name": "Bet", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "previousOwner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "newOwner", "type": "address" }, { "indexed": false, "internalType": "uint8", "name": "level", "type": "uint8" } ], "name": "OwnershipTransferred", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "who", "type": "address" }, { "indexed": false, "internalType": "bool", "name": "success", "type": "bool" }, { "indexed": false, "internalType": "uint256", "name": "reward", "type": "uint256" } ], "name": "Result", "type": "event" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint8", "name": "level", "type": "uint8" } ], "name": "addOwnership", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "uint24", "name": "amount", "type": "uint24" }, { "internalType": "uint8", "name": "percentage", "type": "uint8" } ], "name": "bet", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint8", "name": "level", "type": "uint8" } ], "name": "changeOwnershipLevel", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "claimWinner", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "deleteOwnership", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getEndState", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getFeeConst", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getLPTAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getRandomAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getTargetPrice", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getWinner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "uint8", "name": "level", "type": "uint8" } ], "name": "isValid", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "levelOf", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "bool", "name": "newENDSTATE", "type": "bool" } ], "name": "setEndState", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "uint8", "name": "newFeeConst", "type": "uint8" } ], "name": "setFeeConst", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "newLPTAddress", "type": "address" } ], "name": "setLPTAddress", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "newRandomAddress", "type": "address" } ], "name": "setRandomAddress", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "uint256", "name": "newTargetPrice", "type": "uint256" } ], "name": "setTargetPrice", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "oldOwner", "type": "address" }, { "internalType": "address", "name": "newOwner", "type": "address" } ], "name": "transferOwnership", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" } ]'
betContract = getContract(BET_CONTRACT_ADDRESS, betContractABIStr)
ERC20ContractABIStr = '[ { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "balance", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" }, { "name": "_spender", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "payable": true, "stateMutability": "payable", "type": "fallback" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "owner", "type": "address" }, { "indexed": true, "name": "spender", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" } ]'
LPTContract = getContract(LPT_TOKEN_CONTRACT_ADDRESS, ERC20ContractABIStr)

# start betting!
intro = """
_______                                __ 
/       \                              /  |
$$$$$$$  | ______   _______   ________ $$/ 
$$ |__$$ |/      \ /       \ /        |/  |
$$    $$//$$$$$$  |$$$$$$$  |$$$$$$$$/ $$ |
$$$$$$$/ $$ |  $$ |$$ |  $$ |  /  $$/  $$ |
$$ |     $$ \__$$ |$$ |  $$ | /$$$$/__ $$ |
$$ |     $$    $$/ $$ |  $$ |/$$      |$$ |
$$/       $$$$$$/  $$/   $$/ $$$$$$$$/ $$/
"""
print(intro)

# print("wait for the bet game start time...")
# while int(time.time()) < 1612710020:
#     time.sleep(1)
print("it's time to bet!")

winCount = 0
loseCount = 0
oneshotCount = 0
lastOneshotTryTime = int(time.time())
oneshotTimeEpochs = []
didWin = True
initialBalance = LPTContract.functions.balanceOf(MY_ADDRESS).call()
initialStartTime = int(time.time())
blockNumber = fullnode.eth.blockNumber
while(True):
    try:
        # wait for new block
        while blockNumber == fullnode.eth.blockNumber:
            pass
        blockNumber = fullnode.eth.blockNumber
        print("\n\n\nblock", blockNumber, "mined!")

        # get my LPT balance
        balanceBefore = LPTContract.functions.balanceOf(MY_ADDRESS).call()
        print("my LPT balance (before):", balanceBefore, "(net income:", balanceBefore-initialBalance, "for", int(time.time())-initialStartTime, "seconds)")
        if balanceBefore == 0:
            print("you lose... no token left")
            sys.exit()

        # make claim get winner transaction
        if balanceBefore >= TARGET_AMOUNT:
            # send transaction
            while betContract.functions.getWinner().call() != MY_ADDRESS:
                transaction = betContract.functions.claimWinner().buildTransaction({'from':MY_ADDRESS})
                transaction.update({ 'gas' : GAS_AMOUNT })
                transaction.update({ 'nonce' : fullnode.eth.getTransactionCount(MY_ADDRESS) })
                signed_tx = fullnode.eth.account.signTransaction(transaction, MY_PRIVATE_KEY)
                txn_hash = fullnode.eth.sendRawTransaction(signed_tx.rawTransaction)
                txn_receipt = fullnode.eth.waitForTransactionReceipt(txn_hash, TX_WAIT_TIMEOUT)

            print("congratulations, you are the winner!")
            sys.exit()

        # make bet transaction (Martingale strategy)
        if balanceBefore > 3030:
            # try oneshot to make target amount at once
            BET_PROBABILITY = 1
            betAmount = ONE_SHOT_BET_AMOUNT
        else:
            # not enough balance for oneshot
            BET_PROBABILITY = 40
            # did win || tried oneshot
            if didWin or betAmount == ONE_SHOT_BET_AMOUNT:
                betAmount = INITIAL_BET_AMOUNT
            # did lose
            else:
                # Martingale betting: betAmount x 2
                betAmount *= 2
                # not enough balance... just all in (considering bet fee)
                if betAmount >= balanceBefore:
                    betAmount = int(balanceBefore * 0.98)
        print("go bet -> bet amount:", betAmount, "/ bet prob:", BET_PROBABILITY)
        transaction = betContract.functions.bet(betAmount, BET_PROBABILITY).buildTransaction({'from':MY_ADDRESS})
        transaction.update({ 'gas' : GAS_AMOUNT })
        transaction.update({ 'nonce' : fullnode.eth.getTransactionCount(MY_ADDRESS) })
        signed_tx = fullnode.eth.account.signTransaction(transaction, MY_PRIVATE_KEY)
        txn_hash = fullnode.eth.sendRawTransaction(signed_tx.rawTransaction)
        txn_receipt = fullnode.eth.waitForTransactionReceipt(txn_hash, TX_WAIT_TIMEOUT)

        # check result
        balanceAfter = LPTContract.functions.balanceOf(MY_ADDRESS).call()
        if balanceBefore < balanceAfter:
            winCount = winCount + 1
            didWin = True
        else:
            loseCount = loseCount + 1
            didWin = False
        print("my LPT balance (after):", balanceAfter, "(result: get", balanceAfter-balanceBefore, "tokens) / (win:", winCount, "/ lose:", loseCount, "/ win rate:", int(winCount/(winCount+loseCount)*100) ,"%)")
        if betAmount == ONE_SHOT_BET_AMOUNT:
            oneshotCount = oneshotCount + 1
            oneshotTimeEpochs.append(int(time.time()) - lastOneshotTryTime)
            lastOneshotTryTime = int(time.time())
        if oneshotCount != 0:
            print("oneshot try count:", oneshotCount, "(it takes", lastOneshotTryTime, "seconds / avg:", int(sum(oneshotTimeEpochs) / len(oneshotTimeEpochs)), "sec)")
        print("\n")
    except Exception as e:
        print(e)
        print("\nERROR occured, wait for a while...\n")
        # wait for enough time
        time.sleep(60)
        pass
