class Solution:
    def build_str(self,x):
        y1 = []
        j = -1
        i = 0
        a = len(x)
        while i < a:
            if (x[i]=='#'):
                if y1:
                    y1.pop()
            else:
                y1.extend(x[i])
            i+=1
        return y1
    def cmp_str(self,x,x1):
        x = self.build_str(x)
        x1 = self.build_str(x1)
        if len(x) != len(x1):
            return False
        for i in range(len(x)):
            if x[i]!=x1[i]:
                return False

        return True

if __name__=="__main__":
    str="ab###d"
    str2="abg###d"
    x = list(str)
    x1 = list(str2)
    y1 = Solution()
    print(y1.cmp_str(x,x1))