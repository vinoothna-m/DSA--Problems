def max_profit(price):
    res=0
    for i in range(1,len(price)):
        if price[i]>price[i-1]:
            res+=price[i]-price[i-1]
    return res
print(max_profit([100,180,260,310,40,535,695]))


"""Time complexity=O(n)
Space complexity=O(1)"""
