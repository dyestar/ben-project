import sys
f=open(sys.argv[1],chr(114),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
c=f.read()
f.close()
d=chr(34)
s=chr(39)
eq=chr(61)+d
c=c.replace(eq,chr(61)+s)
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(c)
f.close()
print(chr(70)+chr(105)+chr(120)+chr(101)+chr(100))
