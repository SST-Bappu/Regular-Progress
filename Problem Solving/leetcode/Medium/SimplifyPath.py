def SimplifyPath(path):
    path = path.strip().split('/')
    stack = []
    for i in path:
        if i == '..':
            if stack:
                stack.pop()
            continue
        if i=='.' or i=="" or i==" ":
            continue
        stack.append(i)
    result = ""
    if not stack:
        return "/"
    for p in stack:
        result += '/'+p
    return result
if __name__=="__main__":
    path = "/home/"
    result = SimplifyPath(path)
    print(result)