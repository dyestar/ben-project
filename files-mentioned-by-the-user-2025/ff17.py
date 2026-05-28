import sys
f=open(sys.argv[1],chr(114),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
lines=f.read().split(chr(10))
f.close()
d=chr(34)
s=chr(39)
for i in range(len(lines)):
    l=lines[i]
    if (chr(46)+chr(105)+chr(110)+chr(110)+chr(101)+chr(114)+chr(72)+chr(84)+chr(77)+chr(76) in l or chr(111)+chr(112)+chr(116)+chr(105)+chr(111)+chr(110)+chr(115)+chr(72)+chr(84)+chr(77)+chr(76) in l):
        if not l.strip().startswith(chr(118)+chr(97)+chr(114)):
            l=l.replace(chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(61)+d,chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(61)+s)
            l=l.replace(d+chr(62),s+chr(62))
            l=l.replace(chr(105)+chr(100)+chr(61)+d,chr(105)+chr(100)+chr(61)+s)
            l=l.replace(chr(115)+chr(116)+chr(121)+chr(108)+chr(101)+chr(61)+d,chr(115)+chr(116)+chr(121)+chr(108)+chr(101)+chr(61)+s)
            l=l.replace(chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)+chr(61)+d,chr(100)+chr(97)+chr(116)+chr(97)+chr(45)+chr(118)+chr(97)+chr(108)+chr(117)+chr(101)+chr(61)+s)
            l=l.replace(d+chr(32)+chr(47)+chr(62),s+chr(32)+chr(47)+chr(62))
        lines[i]=l
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(chr(10).join(lines))
f.close()
print(chr(70)+chr(105)+chr(120)+chr(101)+chr(100))
