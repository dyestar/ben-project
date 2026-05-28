# fix scriptimport sys
f=open(sys.argv[1],"r",encoding="utf-8")
c=f.read()
f.close()
d=chr(34)
s=chr(39)
for pat in [chr(61)+chr(99)+chr(111)+chr(117)+chr(110)+chr(116),chr(61)+chr(111)+chr(112)+chr(116)+chr(105)+chr(111)+chr(110)+chr(115),chr(61)+chr(111)+chr(112)+chr(116)+chr(105)+chr(111)+chr(110),chr(61)+chr(113)+chr(45)+chr(109)+chr(101)+chr(116)+chr(97),chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)+chr(61)]:
    c=c.replace(pat+d,pat+s)
    c=c.replace(chr(47)+chr(62)+d,chr(47)+chr(62)+s)
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(c)
f.close()
print("Fixed!")
