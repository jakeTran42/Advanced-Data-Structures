#!python3

import math
import os
import random
import re
import sys


def getWays(total, coin_list):
    
    coin_list_array = [0] * (total+1)
    coin_list_array[0] = 1

    for coin in coin_list:
        for index in range(coin, total+1):
            coin_list_array[index] += coin_list_array[index - coin]
    
    return coin_list_array[total]

print(getWays(10, [1,2,4]))


# if __name__ == '__main__':
#     nm = input().split()

#     n = int(nm[0])

#     m = int(nm[1])

#     c = list(map(int, input().rstrip().split()))

#     # Print the number of ways of making change for 'n' units using coins having the values given       by 'c'

#     # ways = getWays(n, c)
