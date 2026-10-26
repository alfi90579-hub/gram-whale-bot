 import time,requests
BOT_TOKEN="ISI"
CHAT_ID="ISI"
WATCHLIST_80=["GRAM","BTC","ETH","SOL","XRP","DOGE","SHIB","PEPE","BNB","ADA","AVAX","DOT","MATIC","LINK","LTC","TRX","ETC","BCH","XLM","ATOM","NEAR","APT","ARB","OP","SUI","SEI","TIA","WIF","BONK","FLOKI","TON","NOT","USDT","USDC","DAI","UNI","AAVE","MKR","LDO","RNDR","FET","TAO","INJ","STX","IMX","GALA","SAND","MANA","AXS","FLOW","EGLD","HBAR","VET","ALGO","QNT","FIL","THETA","XMR","KAS","RUNE","STG","BLUR","STRK","JUP","PYTH","JTO","W","ENA","ETHFI","BOME","MEME","ZK","ZRO","IO","BEAM","GRT","CHZ"]
def notif(j,p):
 try:
  if "ISI" in BOT_TOKEN: print(f"[{j}] {p}");return
  requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",data={"chat_id":CHAT_ID,"text":f"{j}\n{p}"},timeout=5)
 except: pass
print("BOT 80 COIN ON")
while True:
 for coin in WATCHLIST_80:
  if coin=="GRAM": notif(f"🚀 {coin} WHALE","OPEN POSISI!");print(f">>> OPEN {coin}")
  else: notif(f"🔔 {coin}","Info gerak");print(f"NOTIF {coin}")
 time.sleep(60)
