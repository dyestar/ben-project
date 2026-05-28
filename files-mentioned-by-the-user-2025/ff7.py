import sys
f=open(sys.argv[1],chr(114),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
c=f.read()
f.close()
d=chr(34)
s=chr(39)
for pat in [chr(61)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116),chr(61)+chr(113)+chr(45)+chr(109)+chr(101)+chr(116)+chr(97),chr(61)+chr(113)+chr(45)+chr(116)+chr(97)+chr(103),chr(61)+chr(113)+chr(45)+chr(116)+chr(101)+chr(120)+chr(116),chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)+chr(61),chr(61)+chr(97)+chr(110)+chr(115)+chr(119)+chr(101)+chr(114)+chr(45)+chr(116)+chr(101)+chr(120)+chr(116),chr(61)+chr(119)+chr(105)+chr(45)+chr(113),chr(61)+chr(119)+chr(105)+chr(45)+chr(97)+chr(110)+chr(115)+chr(119)+chr(101)+chr(114)]:
    c=c.replace(pat+d,pat+s)
    c=c.replace(d+chr(62)+chr(32)+chr(43),s+chr(62)+chr(32)+chr(43))
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(c)
f.close()
print(chr(70)+chr(105)+chr(120)+chr(101)+chr(100))
