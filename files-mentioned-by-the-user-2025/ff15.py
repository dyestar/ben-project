import sys
f=open(sys.argv[1],chr(114),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
c=f.read()
f.close()
d=chr(34)
s=chr(39)
pairs = [
  (chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(61)+d, chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(61)+s),
  (chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)+chr(61)+d, chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)+chr(61)+s),
  (chr(105)+chr(100)+chr(61)+d, chr(105)+chr(100)+chr(61)+s),
  (chr(115)+chr(116)+chr(121)+chr(108)+chr(101)+chr(61)+d, chr(115)+chr(116)+chr(121)+chr(108)+chr(101)+chr(61)+s),
]
for old,new in pairs:
    c=c.replace(old,new)
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(c)
f.close()
print(chr(70)+chr(105)+chr(120)+chr(101)+chr(100))
