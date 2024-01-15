price=int(input())
coins=[25,10,5,1]
num_coins=0
for coin in coins:
    num_coins+=price//coin
    price%=coin
print(num_coins)