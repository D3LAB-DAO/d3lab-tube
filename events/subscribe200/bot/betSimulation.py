from web3 import Web3
import sys
import json
import binascii, os
import random
import time
import math

###### simulation ######

# options
TEST_COUNT = 1000
INITIAL_BALANCE_AMOUNT = 5000
DO_PRINT_SUB_RESULT = False

# my strategy options
INITIAL_BET_AMOUNT = 4
BET_PROBABILITY = 50 # percent
MAX_FAIL_COUNT = 12 # ex. 8 means 8번 초과로 연속 bet 실패하면 망함
TARGET_AMOUNT = 200000

# run simulation
successCount = 0
failCount = 0
maxBalances = []
betCounts = []
for i in range(TEST_COUNT):
    print("\nrun", i+1, "th simulation")

    balance = INITIAL_BALANCE_AMOUNT
    maxBalance = 0
    didWin = True
    winCount = 0
    loseCount = 0
    betCount = 0

    while(True):

        # update max balance
        if balance > maxBalance:
            maxBalance = balance

        # check jackpot or bankrupted
        if balance > TARGET_AMOUNT:
            print("GET AIRPODS!!!")
            successCount += 1
            maxBalances.append(maxBalance)
            betCounts.append(betCount)
            print("simul end -> bet count:", betCount, "/ max balance:", maxBalance)
            break
        elif balance < 2:
            print("you lose...")
            failCount += 1
            maxBalances.append(maxBalance)
            betCounts.append(betCount)
            print("simul end -> bet count:", betCount, "/ max balance:", maxBalance)
            break
        
        # TODO: choose how much amount to bet & probability
        # example aproach: Martinegale strategy
        betProbability = BET_PROBABILITY # fixed prob
        if didWin:
            # check need to increase initial bet amount
            n = int(math.log(balance,2))
            if balance > int(2**n * (1+(betProbability/100)**2*8/100)): # considering bet fee
                INITIAL_BET_AMOUNT = int(2**(n - MAX_FAIL_COUNT))
                if INITIAL_BET_AMOUNT < 2:
                    INITIAL_BET_AMOUNT = 2
            # return to initial bet amount
            betAmount = INITIAL_BET_AMOUNT
        else:
            betAmount *= 2
            if betAmount >= balance:
                # decrease initial bet amount, and reset bet amount... (safe new start)
                n = int(math.log(balance,2))
                if balance > int(2**n * (1+(betProbability/100)**2*8/100)):
                    INITIAL_BET_AMOUNT = int(2**(n - MAX_FAIL_COUNT))
                else:
                    INITIAL_BET_AMOUNT = int(2**(n - MAX_FAIL_COUNT - 1))
                if INITIAL_BET_AMOUNT < 2:
                    INITIAL_BET_AMOUNT = 2
                betAmount = INITIAL_BET_AMOUNT

        # check bet result & update balance
        betCount += 1
        if random.randint(1, 100) <= betProbability:
            didWin = True
            winCount += 1
            newBalance = balance - betAmount + int(betAmount * 100 / betProbability) - int((betAmount * (betProbability/100)**2*8/100))
        else:
            didWin = False
            loseCount += 1
            newBalance = balance - betAmount - int((betAmount * (betProbability/100)**2*8/100))
        if DO_PRINT_SUB_RESULT:
            if didWin:
                print("win")
            else:
                print("lose")
            print("balance:", balance, "/ bet amount:", betAmount, "/ prob:", betProbability, "% / get", newBalance-balance, "tokens / betcount:", betCount, "/ max balance:", maxBalance, "(win:", winCount, "/ lose:", loseCount, "win rate:", int(winCount/(winCount+loseCount)*100), "%)\n")
        balance = newBalance

# print simulation result
print("\n\nsuccess:", successCount, "/ fail:", failCount, "-> airpod prob for this strategy:", float(successCount/(successCount+failCount)*100), "%")
print("avg max balance:", sum(maxBalances)/len(maxBalances), "/ max balance:", max(maxBalances))
print("avg bet count:", sum(betCounts)/len(betCounts), "/ max bet count:", max(betCounts))
