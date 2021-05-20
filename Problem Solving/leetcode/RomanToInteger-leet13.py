def RomanToInt(Roman):
    dic = {'M':1000, 'CM':900 , 'D':500, 'CD':400, 'C':100, 'XC':90 , 'L':50, 'XL':40 , 'X':10, 'IX':9, 'V':5,
           'IV':4, 'I':1}
    n = len(Roman)
    numb = 0
    i=0
    while i<n:
        if i+1<n and dic.get(Roman[i]+Roman[i+1]):
            numb += dic[Roman[i]+Roman[i+1]]
            i+=2
        else:
            numb+=dic[Roman[i]]
            i+=1
    return numb
if __name__=="__main__":
    s="MCMXCIV"
    print(RomanToInt(s))