def IntegerToRoman(num):
    unit = [1,5,10,50,100,500,1000]
    hash ={
        1:'I',
        5:'V',
        10:'X',
        50:'L',
        100:'C',
        500:'D',
        1000:'M'
    }
    result = ""
    n = len(unit)-1
    while num:
        if num + 1 == 5:
            result+=hash[1]+hash[5]
            num -= 4
        elif num+1 == 10:
            result+=hash[1]+hash[10]
            num-=9
        elif (num+10>=50 and num+10<60) or (num+10>=100 and num+10<110):
            if num>50:
                result+=hash[10]+hash[100]
                num-=90
            else:
                result+=hash[10]+hash[50]
                num-=40
        elif (num+100>=500 and num+100<600) or (num+100>=1000 and num+100<1100):
            if num>500:
                result+=hash[100]+hash[1000]
                num-=900
            else:
                result+=hash[100]+hash[500]
                num-=400
        elif num>=unit[n]:
            x = num//unit[n]
            result+= hash[unit[n]]*x
            num = num%unit[n]
        n-=1
    return result
def IntToRoman(num):
    dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
           4: 'IV', 1: 'I'}
    out = ''
    for i in dic:
        out += (num // i) * dic[i]
        num = num % i
    return (out)
if __name__=="__main__":
    print(IntegerToRoman(85))
    print(IntToRoman(85))
