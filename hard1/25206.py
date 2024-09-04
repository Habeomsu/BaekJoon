import sys
dict={'A+':4.5,
      'A0':4.0,
      'B+':3.5,
      'B0':3.0,
      'C+':2.5,
      'C0':2.0,
      'D+':1.5,
      'D0':1.0,
      'F':0.0}
ctn1=0
ctn2=0
for i in range(20):
      a,b,c = sys.stdin.readline().split()
      if c !='P':
            ctn1 += float(b)
            ctn2 += float(b)*dict[c]
print(ctn2/ctn1)
