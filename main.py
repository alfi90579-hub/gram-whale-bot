import time
import requests

WATCHLIST_80 = ["GRAM","BTC","ETH","SOL","XRP","DOGE","SHIB","PEPE","BNB","ADA","AVAX","DOT","MATIC","LINK","LTC","TRX","ETC","BCH","XLM","ATOM","NEAR","APT","ARB","OP","SUI","SEI","TIA","WIF","BONK","FLOKI","TON","NOT","USDT","USDC","DAI","UNI","AAVE","MKR","LDO","RNDR","FET","TAO","INJ","STX","IMX","GALA","SAND","MANA","AXS","FLOW","EGLD","HBAR","VET","ALGO","QNT","FIL","THETA","XMR","KAS","RUNE","STG","BLUR","STRK","JUP","PYTH","JTO","W","ENA","ETHFI","BOME","MEME","ZK","ZRO","IO","BEAM","GRT","CHZ"]

print("BOT START: SCAN 80 COIN, CUMA OPEN GRAM")

while True:
    for coin in WATCHLIST_80:
        if coin == "GRAM":
            print(f"WHALE SCAN -> {coin}: CEK VOLUME")
        else:
            print(f"SKIP -> {coin}")
    time.sleep(5)
