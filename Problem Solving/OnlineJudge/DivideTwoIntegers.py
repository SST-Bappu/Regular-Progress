import timeit
def divide(dividend: int, divisor: int) -> int:
   positive = (dividend<0) is (divisor<0)
   dividend = abs(dividend)
   divisor = abs(divisor)
   q = 0
   while divisor <= dividend:
       temp = divisor
       cnt = 1
       while temp <= dividend:
           dividend-=temp
           q+=cnt
           temp <<=1
           cnt <<=1

   result = q if positive else -q
   return min(2**31-1,max(-2**31,result))

def divide_E(dividend: int, divisor: int) -> int: #a bit optimized compared to previous one
   positive = (dividend<0) is (divisor<0)
   dividend = abs(dividend)
   divisor = abs(divisor)
   q = 0
   while divisor <= dividend:
       temp = divisor
       cnt = 1
       while (temp<<1) <= dividend:
           temp <<=1
           cnt <<=1
       dividend-=temp
       q+=cnt
   result = q if positive else -q
   return min(2**31-1,max(-2**31,result))

if __name__=="__main__":
    start = timeit.default_timer()
    print(divide(-158,3))
    print(timeit.default_timer()-start)
    start = timeit.default_timer()
    print(divide_E(-158, 3))
    print(timeit.default_timer() - start)