import sys
sys.stdout.reconfigure(encoding='utf-8')

f=open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html","r",encoding="utf-8")
lines=f.read().split(chr(10))
f.close()

# Fix by content pattern matching
changes=0
for i in range(len(lines)):
    line=lines[i]
    new_line=line
    
    # Fix lines that have JS double-quoted strings with HTML double-quoted attributes
    # Strategy: for any line starting a JS string with " that contains <div, <span, </div>, etc.
    # change the JS delimiter to '
    
    # Pattern 1: = "<div... or += "<div...
    # These should use ' for JS string delimiter
    if '= "<div' in new_line or '+= "<div' in new_line:
        # Change the opening delimiter from " to '
        new_line=new_line.replace('= "<div', "= '<div")
        new_line=new_line.replace('+= "<div', "+= '<div")
    
    # Pattern 2: </div>" or </span>" - closing HTML tags at end of JS strings
    # These should use ' for JS string delimiter
    if '</div>"' in new_line:
        new_line=new_line.replace('</div>"', "</div>'")
    if '</span>"' in new_line:
        new_line=new_line.replace('</span>"', "</span>'")
    if '</div>"' in new_line:
        new_line=new_line.replace('</div>"', "</div>'")
    
    # Pattern 3: " + variable + " - concatenation inside JS strings
    # When the string started with ', these need to be ' + variable + '
    if new_line != line and '" + ' in new_line:
        # But we need to be careful not to replace JS-level string delimiters
        # Only replace if we already changed the outer delimiters
        parts=new_line.split("' + ")
        if len(parts)>1:
            # The line uses single quotes for JS strings now
            # Check for remaining " patterns
            pass
    
    if new_line != line:
        changes+=1
        lines[i]=new_line

# Actually, the above approach is not precise enough. Let me just manually fix specific patterns.

# Read fresh
f=open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html","r",encoding="utf-8")
c=f.read()
f.close()

dqt=chr(34)  # double quote "
sqt=chr(39)  # single quote '

# Fix 1: btn.innerHTML (line ~162)
c=c.replace(
    'btn.innerHTML = ch.name + '+dqt+'<div class='+dqt+'count'+dqt+'>单选 '+dqt+' + ch.single + '+dqt+' · 多选 '+dqt+' + ch.multiple + '+dqt+' · 判断 '+dqt+' + ch.judge + '+dqt+' · 共 '+dqt+' + total + '+dqt+' 题</div>'+dqt+';',
    "btn.innerHTML = ch.name + '<div class=\\\\\"count\\\\\">单选 ' + ch.single + ' · 多选 ' + ch.multiple + ' · 判断 ' + ch.judge + ' · 共 ' + total + ' 题</div>';"
)

print("Fix 1 applied" if "Fix 1" not in c else "Fix 1 NOT applied")
print(f"Changes: {changes}")