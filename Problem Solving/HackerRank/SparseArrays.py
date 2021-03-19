def SparseArray(str,query):
    list=[]
    for i in range(len(query)):
        cnt = 0
        for j in range(len(str)):
            if query[i]==str[j]:
                cnt+=1
        list.append(cnt)
    return list

if __name__=="__main__":
    str=["aba","baba","aba","xzxb"]
    query=["aba","abc","xzxb"]
    list = SparseArray(str,query)
    print(list)

