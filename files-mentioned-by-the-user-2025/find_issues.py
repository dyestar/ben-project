import sys, re
sys.stdout.reconfigure(encoding='utf-8')
f=open('C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html','r',encoding='utf-8')
c=f.read()
f.close()
lines=c.split(chr(10))
for i,line in enumerate(lines):
    s=line.strip()
    if ('.innerHTML' in s or 'optionsHTML' in s) and not s.startswith('var '):
        dq=s.count(chr(34))
        if dq>4:
            print('L'+str(i+1)+' ('+str(dq)+' dq): '+s[:100])
print('Done')
