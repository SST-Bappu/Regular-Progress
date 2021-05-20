def minSwaps(binString):
    zeros=ones=0
    for i in binString:
        if i=='0':
            zeros+=1
        else:
            ones+=1
    dif = abs(zeros-ones)
    if dif > 1:
        return -1
    if zeros==ones:
        firstChar='1'
        secondChar = '0'
        result = ""
        first = zeros
        second = ones
        while first and second:
            result += firstChar
            result += secondChar
            first -= 1
            second -= 1
        changes1 = 0
        for i in range(len(binString)):
            if binString[i] != result[i]:
                changes1 += 1

        firstChar = '0'
        secondChar = '1'
        result = ""
        while zeros and ones:
            result += firstChar
            result += secondChar
            zeros -= 1
            ones -= 1
        changes2 = 0
        for i in range(len(binString)):
            if binString[i] != result[i]:
                changes2 += 1
        changes = min(changes1,changes2)

    else:
        if zeros>ones:
            first = zeros
            firstChar = '0'
            second = ones
            secondChar = '1'
        else:
            first = ones
            firstChar = '1'
            second = zeros
            secondChar = '0'
        result = ""
        while first and second:
            result+=firstChar
            result+=secondChar
            first-=1
            second-=1
        if first:
            result += firstChar
        changes = 0
        for i in range(len(binString)):
            if binString[i]!=result[i]:
                changes+=1
    return changes//2
if __name__=="__main__":
    #str = "1110000000100001010100101010000101010101001000001110101000010111101100000111110001000111010111101100001100001001100101011110100011111100000000100011111011110111111011110111010100111101011111111101101100101010110000011110110100101111000100000001100000"
    str ="00111"
    print(minSwaps(str))