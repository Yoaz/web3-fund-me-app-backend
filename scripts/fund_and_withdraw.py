from brownie import FundMe
from scripts.helpful_scripts import get_account

fund_me = FundMe[-1]
account = get_account()
entrance_fee = fund_me.getEntranceFees()

def fund(): 
    print(f"The current entrance fees are: {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    print("Withdrawing")
    fund_me.withdraw({"from": account})
    

def main():
    fund() 
    withdraw()