import timeit
STANDARD_COIN_SIZES = [1, 5, 10, 25]
def coins(n):
    coin_sizes = [1, 5, 10, 25]
    ways = [[None for i in range(n + 1)] for j in range(len(coin_sizes))]
    return coin_combinations(n,coin_sizes,ways)
def coin_combinations(amount,coin_sizes,ways):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(coin_sizes) == 0:
        return 0
    m = len(coin_sizes)
    if ways[m-1][amount]!=None:
        print("Here we got one")
        return ways[m-1][amount]
    ways[m-1][amount] = coin_combinations(amount, coin_sizes[: m - 1],ways) + coin_combinations(
        amount - coin_sizes[m - 1], coin_sizes,ways)
    return ways[m-1][amount]

def coin_combinations_iterative(amount, coin_sizes=None):
    table = [0] * (amount + 1)
    # first case 0 value
    table[0] = 1

    if coin_sizes is None:
        coin_sizes = STANDARD_COIN_SIZES
    for i in range(0, len(coin_sizes)):
        for j in range(coin_sizes[i], amount + 1):
            table[j] += table[j - coin_sizes[i]]
    return table[amount]
if __name__=="__main__":
    start = timeit.default_timer()
    print(coins(100))
    print(timeit.default_timer()-start)
    start = timeit.default_timer()
    print(coin_combinations_iterative(100))
    print(timeit.default_timer()-start)