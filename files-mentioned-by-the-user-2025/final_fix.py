import sys
f=open(sys.argv[1],chr(114),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
lines=f.read().split(chr(10))
f.close()
for i in range(len(lines)):
    l=lines[i]
    if chr(34) in l and (chr(46)+chr(105)+chr(110)+chr(110)+chr(101)+chr(114)+chr(72)+chr(84)+chr(77)+chr(76) in l or chr(111)+chr(112)+chr(116)+chr(105)+chr(111)+chr(110)+chr(115)+chr(72)+chr(84)+chr(77)+chr(76) in l):
        l=l.replace(chr(32)+chr(61)+chr(32)+chr(34)+chr(60),chr(32)+chr(61)+chr(32)+chr(39)+chr(60))
        l=l.replace(chr(32)+chr(43)+chr(61)+chr(32)+chr(34)+chr(60),chr(32)+chr(43)+chr(61)+chr(32)+chr(39)+chr(60))
        l=l.replace(chr(62)+chr(34)+chr(32)+chr(43),chr(62)+chr(39)+chr(32)+chr(43))
        l=l.replace(chr(62)+chr(34)+chr(59),chr(62)+chr(39)+chr(59))
        lines[i]=l
f=open(sys.argv[1],chr(119),encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56))
f.write(chr(10).join(lines))
f.close()
print(chr(70)+chr(105)+chr(120)+chr(101)+chr(100))