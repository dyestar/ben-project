import sys, json
sys.stdout.reconfigure(encoding='utf-8')
fp = r'C:\Users\Ben\Documents\Codex\2026-05-27\new-chat\maogai_quiz.html'
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()

# ----- Add CSS for confirm button and auto-advance hint -----
css_add = (
    ".confirm-btn{display:block;width:100%;padding:12px;margin-top:14px;"
    "background:#1a73e8;color:white;border:none;border-radius:10px;"
    "font-size:15px;font-weight:600;cursor:pointer;transition:all 0.2s}"
    ".confirm-btn:hover{background:#1557b0;transform:translateY(-1px)}"
    ".confirm-btn:disabled{opacity:0.4;cursor:not-allowed;transform:none}"
    ".auto-advance-hint{font-size:12px;color:#43a047;text-align:center;margin-top:8px;display:none}"
)
style_end = c.find('</style>')
c = c[:style_end] + css_add + c[style_end:]

# ----- Add confirm button HTML inside quizView -----
old_quiz = '<div class="quiz-card" id="quizCard"></div>\n<div class="nav-btns">'
new_quiz = (
    '<div class="quiz-card" id="quizCard"></div>\n'
    '<div class="auto-advance-hint" id="autoAdvanceHint"></div>\n'
    '<button class="confirm-btn" id="confirmBtn" style="display:none;">\u2705 \u786e\u8ba4\u7b54\u6848</button>\n'
    '<div class="nav-btns">'
)
c = c.replace(old_quiz, new_quiz)

# ----- Modify renderQuestion: handle confirm button visibility -----
old_rq_part = (
    'document.querySelector("#progressText span").textContent = currentIndex + 1;\n'
    '    document.getElementById("prevBtn").disabled = (currentIndex === 0);\n'
    '    document.getElementById("nextBtn").textContent = (currentIndex === currentQuestions.length - 1) ? "\U0001f4ca \u67e5\u770b\u7ed3\u679c" : "\u4e0b\u4e00\u9898 \u2192";\n'
    '    updateWrongCount();'
)
new_rq_part = (
    'document.querySelector("#progressText span").textContent = currentIndex + 1;\n'
    '    document.getElementById("prevBtn").disabled = (currentIndex === 0);\n'
    '    document.getElementById("nextBtn").textContent = (currentIndex === currentQuestions.length - 1) ? "\U0001f4ca \u67e5\u770b\u7ed3\u679c" : "\u4e0b\u4e00\u9898 \u2192";\n'
    '    updateWrongCount();\n'
    '    var confirmBtn = document.getElementById("confirmBtn");\n'
    '    var autoHint = document.getElementById("autoAdvanceHint");\n'
    '    if (confirmBtn) {\n'
    '        if (q.type === "multiple") {\n'
    '            confirmBtn.style.display = "block";\n'
    '            confirmBtn.disabled = true;\n'
    '            if (autoHint) autoHint.style.display = "none";\n'
    '        } else {\n'
    '            confirmBtn.style.display = "none";\n'
    '            if (autoHint) autoHint.style.display = "none";\n'
    '        }\n'
    '    }'
)
c = c.replace(old_rq_part, new_rq_part)

# ----- Modify selectOption: enable confirm button when options selected -----
old_so_part = (
    'if (q.type === "multiple") {\n'
    '        el.classList.toggle("selected");\n'
    '        var sel = document.querySelectorAll(".option.selected");\n'
    '        var ans = [];\n'
    '        for (var i = 0; i < sel.length; i++) {\n'
    '            ans.push(sel[i].getAttribute("data-value"));\n'
    '        }\n'
    '        ans.sort();\n'
    '        userAnswers[currentIndex] = ans.join("");\n'
    '    } else {'
)
new_so_part = (
    'if (q.type === "multiple") {\n'
    '        el.classList.toggle("selected");\n'
    '        var sel = document.querySelectorAll(".option.selected");\n'
    '        var ans = [];\n'
    '        for (var i = 0; i < sel.length; i++) {\n'
    '            ans.push(sel[i].getAttribute("data-value"));\n'
    '        }\n'
    '        ans.sort();\n'
    '        userAnswers[currentIndex] = ans.join("");\n'
    '        var confirmBtn = document.getElementById("confirmBtn");\n'
    '        if (confirmBtn) confirmBtn.disabled = (sel.length === 0);\n'
    '    } else {'
)
c = c.replace(old_so_part, new_so_part)

# ----- Add confirmMultipleChoice function -----
old_aq = 'function addWrongQuestion(q) {'
new_aq_func = (
    'function confirmMultipleChoice() {\n'
    '    var confirmBtn = document.getElementById("confirmBtn");\n'
    '    confirmBtn.disabled = true;\n'
    '    confirmBtn.textContent = "\u63d0\u4ea4\u4e2d...";\n'
    '    checkAnswer();\n'
    '}\n\n'
    'function addWrongQuestion(q) {'
)
c = c.replace(old_aq, new_aq_func)

# ----- Modify checkAnswer: auto-advance on correct, disable confirm after check -----
old_ca_correct = (
    'if (isCorrect) {\n'
    '        feedback.className = "feedback correct";\n'
    '        feedback.innerHTML = "\u2705 \u56de\u7b54\u6b63\u786e\uff01";\n'
    '        var selOpts = document.querySelectorAll(".option.selected");\n'
    '        for (var i = 0; i < selOpts.length; i++) {\n'
    '            selOpts[i].classList.add("correct");\n'
    '        }\n'
    '    } else {'
)
new_ca_correct = (
    'if (isCorrect) {\n'
    '        feedback.className = "feedback correct";\n'
    '        feedback.innerHTML = "\u2705 \u56de\u7b54\u6b63\u786e\uff01";\n'
    '        var selOpts = document.querySelectorAll(".option.selected");\n'
    '        for (var i = 0; i < selOpts.length; i++) {\n'
    '            selOpts[i].classList.add("correct");\n'
    '        }\n'
    '        var autoHint = document.getElementById("autoAdvanceHint");\n'
    '        if (autoHint) {\n'
    '            autoHint.style.display = "block";\n'
    '            if (currentIndex < currentQuestions.length - 1) {\n'
    '                autoHint.textContent = "\u2705 \u56de\u7b54\u6b63\u786e\uff01\u5373\u5c06\u8fdb\u5165\u4e0b\u4e00\u9898...";\n'
    '                setTimeout(function() {\n'
    '                    currentIndex++;\n'
    '                    renderQuestion();\n'
    '                }, 1200);\n'
    '            } else {\n'
    '                autoHint.textContent = "\u2705 \u56de\u7b54\u6b63\u786e\uff01\u5373\u5c06\u67e5\u770b\u7ed3\u679c...";\n'
    '                setTimeout(function() {\n'
    '                    finishQuiz();\n'
    '                }, 1200);\n'
    '            }\n'
    '        }\n'
    '    } else {'
)
c = c.replace(old_ca_correct, new_ca_correct)

# ----- Disable confirm button after checkAnswer disables options -----
old_disable_opts = (
    'var opts = document.querySelectorAll(".option");\n'
    '    for (var i = 0; i < opts.length; i++) {\n'
    '        opts[i].classList.add("disabled");\n'
    '    }'
)
new_disable_opts = (
    'var opts = document.querySelectorAll(".option");\n'
    '    for (var i = 0; i < opts.length; i++) {\n'
    '        opts[i].classList.add("disabled");\n'
    '    }\n'
    '    var confirmBtn = document.getElementById("confirmBtn");\n'
    '    if (confirmBtn) confirmBtn.disabled = true;'
)
c = c.replace(old_disable_opts, new_disable_opts)

# ----- Wire up confirm button onclick -----
old_onclick_wire = 'document.getElementById("wrongReviewBtn").onclick = showWrongReview;'
new_onclick_wire = (
    'document.getElementById("wrongReviewBtn").onclick = showWrongReview;\n'
    'document.getElementById("confirmBtn").onclick = confirmMultipleChoice;'
)
c = c.replace(old_onclick_wire, new_onclick_wire)

with open(fp, 'w', encoding='utf-8') as f:
    f.write(c)
print('All modifications applied successfully!')
