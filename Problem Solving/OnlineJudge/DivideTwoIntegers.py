def divide(dividend: int, divisor: int) -> int:
    d = abs(divisor)
    de = abs(dividend)
    if d > de:
        return 0
    if d == de:
        return 1 if divisor > 0 else (-1)
    result = helper(de,d,0)
    return result if divisor>0 else (-result)
def helper(dividend, divisor, count):
    if divisor >= dividend:
        return count
    return helper(dividend-divisor,divisor,count+1)


if __name__=="__main__":
    print(divide(-1,1))