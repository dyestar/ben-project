import sys
sys.stdout.reconfigure(encoding='utf-8')
fp = r'C:\Users\Ben\Documents\Codex\2026-05-27\new-chat\maogai_quiz.html'
data = open(fp, 'rb').read()
for b, n in [(b'option" data-value=', 'option" data-value'), (b'feedback" id=', 'feedback" id='), (b'empty-state" style=', 'empty-state" style=')]:
    c = data.count(b)
    print(f'{n}: {c} - {"OK" if c==0 else "BROKEN"}')

# Also check confirm wire
c_str = open(fp, 'r', encoding='utf-8').read()
if 'confirmBtn.onclick = confirmMultipleChoice' in c_str:
    print('confirmBtn.onclick: WIRED')
else:
    # Find the actual text
    idx = c_str.find('confirmBtn')
    if idx >= 0:
        ctx = c_str[max(0,idx-5):idx+55]
        print(f'confirmBtn context: ...{ctx}...')
