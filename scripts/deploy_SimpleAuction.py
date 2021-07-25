#!/usr/bin/python3
from brownie import SimpleAuction, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    get_contract,
)


def deploy_SimpleAuction():
    account = get_account()
    print(f"On network {network.show_active()}")
    keyhash = config["networks"][network.show_active()]["keyhash"]
    fee = config["networks"][network.show_active()]["fee"]
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")

    return SimpleAuction.deploy(
        keyhash,
        vrf_coordinator,
        link_token,
        fee,
        {"from": account},
        publish_source=get_verify_status(),
    )


def main():
    deploy_SimpleAuction()