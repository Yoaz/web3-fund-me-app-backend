from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIORNMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, FundMe, exceptions
import pytest 


def test_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fees = fund_me.getEntranceFees()
    tx = fund_me.fund({"from": account, "value": entrance_fees})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account) == entrance_fees
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account) == 0

def test_only_owner_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        pytest.skip()
    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})


       

