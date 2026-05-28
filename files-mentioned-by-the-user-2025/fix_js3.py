import json, re

f = open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html", "r", encoding="utf-8")
c = f.read()
f.close()

lines = c.split(chr(10))

for i in range(len(lines)):
    line = lines[i]
    
    # Fix lines with innerHTML/optionsHTML assignments
    if "card.innerHTML" in line or "optionsHTML" in line or "btn.innerHTML" in line:
        # Replace all double quotes in HTML attributes with single quotes
        # Pattern: ="attribute" -> ='attribute'
        # This regex finds ="... " inside JS strings
        
        # Fix common patterns
        import re as regex
        
        # Replace all ="" (attribute assignment with double quotes) with =''
        line = regex.sub(r'="([^"]*)"', "='\\1'", line)
        
        # But we need to be careful not to replace JS string delimiters
        # The issue is that some ="" patterns might be JS assignments not HTML
        
        lines[i] = line

c = chr(10).join(lines)

f = open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html", "w", encoding="utf-8")
f.write(c)
f.close()
print("Fix applied")