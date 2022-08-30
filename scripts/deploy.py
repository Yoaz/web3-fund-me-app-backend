from brownie import accounts, network, config, FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mock, LOCAL_BLOCKCHAIN_ENVIORNMENTS


def deploy_fund_me():
    account = get_account();
    # Pass the priceFeed address based on the current active network
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed_address"]
    else:
       deploy_mock()
       price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(fund_me)
    return fund_me

def main():
    deploy_fund_me()
