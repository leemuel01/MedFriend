import math
from statistics import mean

num1 = [8349200,
        8366600,
        8374100,
        8362500,
        8366700,
        8399700,
        8399800,
        8404900,
        8460700]

num2 = [33800,
        33200,
        32700,
        32200,
        31600,
        30900,
        30300,
        29400,
        25000]
pre = [1.40995, 1.40601, 1.39917]
data = [12140000, 12140000, 12140000, 12860000, 12860000, 12860000, 13300000, 13300000, 13300000]
for i in range(len(num1)):
        sum = num1[i]-num2[i]
        aaaa= data[i]/sum
        # print(num1[i]-num2[i])
        pre.append(aaaa)
        # print("%.5f" % aaaa)


print(mean(pre))

