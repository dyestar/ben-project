import sys
f=open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html","r",encoding="utf-8")
c=f.read()
f.close()

# Simple fix: replace all outer double quotes in JS strings with single quotes
d=chr(34)  # double quote "
s=chr(39)  # single quote '

# Here we replace patterns on the HTML output
# Fix 1: ="<div -> ='<div
c=c.replace("="+d+"<div","="+s+"<div")
c=c.replace("+= "+d+"<div","+= "+s+"<div")

# Fix 2: </div>" -> </div>'
c=c.replace("</div>"+d,"</div>"+s)
c=c.replace("</span>"+d,"</span>"+s)

# Fix 3: data-value=" -> data-value='
c=c.replace("data-value="+d,"data-value="+s)

print("Fixed HTML, size: "+str(len(c)))
f=open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html","w",encoding="utf-8")
f.write(c)
f.close()
