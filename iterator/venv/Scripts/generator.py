def remote_control():
    yield "CCN"
    yield "ESPN"
    yield "Star Sports"

itr = remote_control()
print(next(itr))

for i in remote_control():
     print(i)