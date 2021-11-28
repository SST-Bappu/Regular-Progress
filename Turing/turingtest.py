t= '%(a)s %(b)s %(c)s'
print(t%dict(a='Welcome',b='to',c='here'))
print(2**(3**2),(2**3)**2, (2**3)**3)

z= set('abc')
z.add('san')
z.update(set(['p','q']))

a='abc'
a[0].upper()
print(a)

print(z)
print([i.lower() for i in 'ABC'])
abc = [1,2,3,4]
bb = [sum(a[0:x+1]) for x in range(0,len(a))]
print(bb)