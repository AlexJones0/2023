A=0;m=eval('{},'*256)
h=lambda s,v:h(s[1:],(v+ord(s[0]))*17%256)if s else v
for s in input().split(","):
 A+=h(s,0);l,f=s.replace("-","=").split("=")
 "="in s and(not m[h(l,0)].update({l:int(f)}))or m[h(l,0)].pop(l,0)
print(A,sum(b*s*f for b,y in enumerate(m,1) for s,f in enumerate(y.values(),1)))