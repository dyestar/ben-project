import sys
f=open(sys.argv[1],chr(114),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
c=f.read()
f.close()
d=chr(34)
s=chr(39)
attrs=[chr(99)+chr(108)+chr(97)+chr(115)+chr(115),chr(105)+chr(100),chr(115)+chr(116)+chr(121)+chr(108)+chr(101),chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)]
for attr in attrs:
    old_open=attr+chr(61)+d
    new_open=attr+chr(61)+s
    c=c.replace(old_open,new_open)
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(c)
f.close()
print(chr(70)+chr(105)+chr(120)+chr(101)+chr(100))
