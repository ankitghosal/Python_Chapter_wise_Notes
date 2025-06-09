# wat will be the length of the following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s)) # python set checks values only not data type. if values are same it won't consider both
