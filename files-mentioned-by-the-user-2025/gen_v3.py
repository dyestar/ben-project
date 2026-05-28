import json, os

with open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\questions.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

# Chapters data
chapters = []
seen = set()
for q in qs:
    if q["chapter"] not in seen:
        seen.add(q["chapter"])
        chapters.append(q["chapter"])

stats = {}
for q in qs:
    ch = q["chapter"]
    stats.setdefault(ch, {"single":0, "multiple":0, "judge":0})
    stats[ch][q["type"]] += 1

chapter_items = []
for ch in chapters:
    s = stats[ch]
    import json as j2
    chapter_items.append(j2.dumps({"name": ch, "single": s["single"], "multiple": s["multiple"], "judge": s["judge"]}, ensure_ascii=False))

chapters_js = "[" + ",".join(chapter_items) + "]"
questions_js = json.dumps(qs, ensure_ascii=False)

total = len(qs)
single_c = len([q for q in qs if q["type"]=="single"])
multi_c = len([q for q in qs if q["type"]=="multiple"])
judge_c = len([q for q in qs if q["type"]=="judge"])

# Build HTML
html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>毛概期末练习题库 - 刷题系统</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,"Microsoft YaHei",sans-serif;background:#f0f2f5;color:#333}
.container{max-width:900px;margin:0 auto;padding:20px}
.header{background:linear-gradient(135deg,#1a73e8,#0d47a1);color:white;padding:20px 30px;border-radius:16px;margin-bottom:24px}
.header h1{font-size:22px;font-weight:600}
.header .stats{font-size:13px;opacity:0.9;margin-top:4px}
.menu{background:white;border-radius:16px;padding:20px;margin-bottom:20px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.menu-title{font-size:15px;font-weight:600;margin-bottom:14px;color:#555}
.chapter-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin-bottom:16px}
.chapter-btn{padding:12px 16px;border:2px solid #e0e0e0;border-radius:10px;background:white;cursor:pointer;font-size:14px;text-align:left;transition:all 0.2s}
.chapter-btn:hover{border-color:#1a73e8;background:#f5f8ff}
.chapter-btn.active{border-color:#1a73e8;background:#e8f0fe;color:#1a73e8;font-weight:600}
.chapter-btn .count{font-size:11px;color:#999;margin-top:4px}
.type-filter{display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap}
.type-btn{padding:8px 20px;border:2px solid #e0e0e0;border-radius:20px;background:white;cursor:pointer;font-size:13px;transition:all 0.2s}
.type-btn:hover{border-color:#1a73e8}
.type-btn.active{background:#1a73e8;color:white;border-color:#1a73e8}
.start-btn{display:block;width:100%;padding:14px;background:linear-gradient(135deg,#1a73e8,#0d47a1);color:white;border:none;border-radius:12px;font-size:17px;font-weight:600;cursor:pointer;transition:all 0.2s}
.start-btn:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(26,115,232,0.35)}
.start-btn:disabled{opacity:0.4;cursor:not-allowed;transform:none}
.quiz-area{display:none}
.quiz-header{background:white;border-radius:16px;padding:16px 20px;margin-bottom:16px;box-shadow:0 2px 8px rgba(0,0,0,0.06);display:flex;justify-content:space-between;align-items:center}
.quiz-header .progress{font-size:14px;color:#666}
.quiz-header .progress span{color:#1a73e8;font-weight:600}
.quiz-header .wrong-count{font-size:13px;color:#e53935}
.quiz-card{background:white;border-radius:16px;padding:28px;box-shadow:0 2px 8px rgba(0,0,0,0.06);margin-bottom:16px}
.quiz-card .q-meta{font-size:12px;color:#999;margin-bottom:8px}
.quiz-card .q-tag{display:inline-block;padding:2px 10px;border-radius:10px;font-size:11px;font-weight:600;margin-right:6px}
.tag-single{background:#e3f2fd;color:#1565c0}
.tag-multiple{background:#fff3e0;color:#e65100}
.tag-judge{background:#e8f5e9;color:#2e7d32}
.quiz-card .q-text{font-size:16px;line-height:1.7;margin-bottom:20px}
.options{display:flex;flex-direction:column;gap:10px}
.option{padding:14px 18px;border:2px solid #e8e8e8;border-radius:12px;cursor:pointer;font-size:15px;line-height:1.5;transition:all 0.2s}
.option:hover{border-color:#90caf9;background:#f5f8ff}
.option.selected{border-color:#1a73e8;background:#e8f0fe}
.option.correct{border-color:#43a047;background:#e8f5e9;color:#2e7d32}
.option.wrong{border-color:#e53935;background:#ffebee;color:#c62828}
.option.show-correct{border-color:#43a047;background:#e8f5e9}
.option.disabled{pointer-events:none;opacity:0.7}
.feedback{margin-top:16px;padding:14px 18px;border-radius:12px;font-size:14px;display:none}
.feedback.correct{display:block;background:#e8f5e9;color:#2e7d32;border:1px solid #c8e6c9}
.feedback.wrong{display:block;background:#ffebee;color:#c62828;border:1px solid #ffcdd2}
.feedback .answer-text{margin-top:6px;font-weight:500}
.nav-btns{display:flex;gap:12px;margin-top:16px}
.nav-btn{flex:1;padding:12px;border:2px solid #e0e0e0;border-radius:12px;background:white;cursor:pointer;font-size:15px;font-weight:500;transition:all 0.2s}
.nav-btn:hover{border-color:#1a73e8}
.nav-btn.primary{background:#1a73e8;color:white;border-color:#1a73e8}
.nav-btn:disabled{opacity:0.4;cursor:not-allowed}
.wrong-panel{display:none;background:white;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.wrong-panel h3{font-size:18px;margin-bottom:16px}
.wrong-item{padding:16px;border:1px solid #ffcdd2;border-radius:12px;margin-bottom:12px;background:#fff5f5}
.wrong-item .wi-q{font-size:15px;margin-bottom:8px}
.wrong-item .wi-answer{font-size:13px}
.wrong-item .wi-answer .wrong-a{color:#e53935}
.wrong-item .wi-answer .correct-a{color:#43a047}
.btn-back{padding:10px 24px;border:2px solid #e0e0e0;border-radius:10px;background:white;cursor:pointer;font-size:14px;margin-top:12px}
.btn-back:hover{border-color:#1a73e8}
.empty-state{text-align:center;padding:60px 20px;color:#999}
.summary{display:none;background:white;border-radius:16px;padding:28px;box-shadow:0 2px 8px rgba(0,0,0,0.06);text-align:center}
.summary h2{font-size:22px;margin-bottom:12px}
.summary .score{font-size:48px;font-weight:700;color:#1a73e8;margin:16px 0}
.summary .detail{font-size:15px;color:#666;margin-bottom:20px}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>\U0001f4d6 毛概期末练习题库</h1>
<div class="stats">共 """ + str(total) + """ 道题 · 单选 """ + str(single_c) + """ · 多选 """ + str(multi_c) + """ · 判断 """ + str(judge_c) + """</div>
</div>

<div id="menuView">
<div class="menu">
<div class="menu-title">\U0001f4c2 选择章节</div>
<div class="chapter-list" id="chapterList"></div>
<div class="menu-title" style="margin-top:16px;">\U0001f4cb 题目类型</div>
<div class="type-filter" id="typeFilter">
<button class="type-btn active" data-type="all">全部</button>
<button class="type-btn" data-type="single">单选题</button>
<button class="type-btn" data-type="multiple">多选题</button>
<button class="type-btn" data-type="judge">判断题</button>
</div>
<div style="margin-top:6px;margin-bottom:16px;font-size:13px;color:#999;" id="selectedInfo">已选：""" + str(total) + """ 道题</div>
<button class="start-btn" id="startBtn">\U0001f680 开始答题</button>
</div>
<div class="menu" style="margin-top:16px;">
<div class="menu-title">\U0001f4d6 其他功能</div>
<button class="start-btn" id="wrongReviewBtn" style="background:linear-gradient(135deg,#e53935,#b71c1c);margin-top:0;">\U0001f4dd 查看错题本</button>
</div>
</div>

<div class="quiz-area" id="quizView">
<div class="quiz-header">
<div class="progress" id="progressText">第 <span>1</span> / <span id="totalQ">?</span> 题</div>
<div class="wrong-count" id="wrongCount">\u274c 错题：0</div>
</div>
<div class="quiz-card" id="quizCard"></div>
<div class="nav-btns">
<button class="nav-btn" id="prevBtn" disabled>\u2190 上一题</button>
<button class="nav-btn primary" id="nextBtn">下一题 \u2192</button>
</div>
</div>

<div class="summary" id="summaryView">
<h2>\U0001f389 答题完成！</h2>
<div class="score" id="finalScore">0%</div>
<div class="detail" id="finalDetail">正确 <span id="correctCount">0</span> 题 · 错误 <span id="incorrectCount">0</span> 题 · 共 <span id="totalCount">0</span> 题</div>
<button class="start-btn" onclick="location.reload()" style="margin-top:20px;display:inline-block;width:auto;padding:12px 40px;">返回主菜单</button>
<button class="start-btn" id="reviewWrongBtn" style="margin-top:12px;display:inline-block;width:auto;padding:12px 40px;background:linear-gradient(135deg,#e53935,#b71c1c);">\U0001f4dd 复习错题</button>
</div>

<div class="wrong-panel" id="wrongView">
<h3>\U0001f4dd 错题本 <span class="count" id="wrongTotalCount"></span></h3>
<div id="wrongList"></div>
<button class="btn-back" onclick="showMenu()">\u2190 返回主菜单</button>
</div>
</div>

<script>
var ALL_QUESTIONS = """ + questions_js + """;
var CHAPTERS = """ + chapters_js + """;
var selectedChapters = [];
var selectedTypes = ["all"];
var currentQuestions = [];
var currentIndex = 0;
var userAnswers = {};
var wrongQuestions = [];

function initWrongQuestions() {
    var stored = localStorage.getItem("maogai_wrong");
    if (stored) {
        try { wrongQuestions = JSON.parse(stored); } catch(e) { wrongQuestions = []; }
    }
}

function init() {
    initWrongQuestions();
    for (var i = 0; i < CHAPTERS.length; i++) {
        selectedChapters.push(CHAPTERS[i].name);
    }
    renderChapters();
    renderTypeFilter();
    document.getElementById("startBtn").disabled = false;
}

function renderChapters() {
    var list = document.getElementById("chapterList");
    list.innerHTML = "";
    for (var i = 0; i < CHAPTERS.length; i++) {
        var ch = CHAPTERS[i];
        var btn = document.createElement("button");
        btn.className = "chapter-btn active";
        var total = ch.single + ch.multiple + ch.judge;
        btn.innerHTML = ch.name + "<div class=\"count\">单选 " + ch.single + " \u00b7 多选 " + ch.multiple + " \u00b7 判断 " + ch.judge + " \u00b7 共 " + total + " 题</div>";
        btn.onclick = (function(idx) {
            return function() { toggleChapter(idx); };
        })(i);
        list.appendChild(btn);
    }
}

function toggleChapter(index) {
    var chName = CHAPTERS[index].name;
    var pos = selectedChapters.indexOf(chName);
    var btns = document.querySelectorAll(".chapter-btn");
    if (pos >= 0) {
        selectedChapters.splice(pos, 1);
        btns[index].classList.remove("active");
    } else {
        selectedChapters.push(chName);
        btns[index].classList.add("active");
    }
    if (selectedChapters.length === 0) {
        for (var i = 0; i < CHAPTERS.length; i++) {
            selectedChapters.push(CHAPTERS[i].name);
            btns[i].classList.add("active");
        }
    }
    updateSelectedInfo();
}

function renderTypeFilter() {
    var btns = document.querySelectorAll(".type-btn");
    for (var i = 0; i < btns.length; i++) {
        btns[i].onclick = (function(btn) {
            return function() {
                var type = btn.getAttribute("data-type");
                if (type === "all") {
                    selectedTypes = ["all"];
                    var allBtns = document.querySelectorAll(".type-btn");
                    for (var j = 0; j < allBtns.length; j++) {
                        allBtns[j].className = "type-btn" + (allBtns[j].getAttribute("data-type") === "all" ? " active" : "");
                    }
                } else {
                    var idx = selectedTypes.indexOf(type);
                    if (idx >= 0) { selectedTypes.splice(idx, 1); }
                    else {
                        var allIdx = selectedTypes.indexOf("all");
                        if (allIdx >= 0) selectedTypes.splice(allIdx, 1);
                        selectedTypes.push(type);
                    }
                    btn.classList.toggle("active");
                    if (selectedTypes.length === 0) {
                        selectedTypes = ["all"];
                        var allBtns2 = document.querySelectorAll(".type-btn");
                        for (var k = 0; k < allBtns2.length; k++) {
                            allBtns2[k].className = "type-btn" + (allBtns2[k].getAttribute("data-type") === "all" ? " active" : "");
                        }
                    } else {
                        document.querySelector(".type-btn[data-type=all]").classList.remove("active");
                    }
                }
                updateSelectedInfo();
            };
        })(btns[i]);
    }
}

function updateSelectedInfo() {
    var types = (selectedTypes.indexOf("all") >= 0) ? ["single", "multiple", "judge"] : selectedTypes;
    var filtered = ALL_QUESTIONS.filter(function(q) {
        return selectedChapters.indexOf(q.chapter) >= 0 && types.indexOf(q.type) >= 0;
    });
    document.getElementById("selectedInfo").textContent = "\u5df2\u9009\uff1a" + filtered.length + " \u9053\u9898";
}

function startQuiz() {
    var types = (selectedTypes.indexOf("all") >= 0) ? ["single", "multiple", "judge"] : selectedTypes;
    currentQuestions = ALL_QUESTIONS.filter(function(q) {
        return selectedChapters.indexOf(q.chapter) >= 0 && types.indexOf(q.type) >= 0;
    });
    currentIndex = 0;
    userAnswers = {};
    document.getElementById("menuView").style.display = "none";
    document.getElementById("quizView").style.display = "block";
    document.getElementById("summaryView").style.display = "none";
    document.getElementById("wrongView").style.display = "none";
    document.getElementById("totalQ").textContent = currentQuestions.length;
    renderQuestion();
}

function renderQuestion() {
    if (currentIndex >= currentQuestions.length) { finishQuiz(); return; }
    var q = currentQuestions[currentIndex];
    var card = document.getElementById("quizCard");
    var typeMap = {single:"单选题", multiple:"多选题", judge:"判断题"};
    var tagClass = {single:"tag-single", multiple:"tag-multiple", judge:"tag-judge"};
    var optionsHTML = "";
    if (q.type === "judge") {
        optionsHTML = "<div class=\"options\"><div class=\"option\" data-value=\"\u6b63\u786e\">\u2705 \u6b63\u786e</div><div class=\"option\" data-value=\"\u9519\u8bef\">\u274c \u9519\u8bef</div></div>";
    } else {
        optionsHTML = "<div class=\"options\">";
        for (var i = 0; i < q.options.length; i++) {
            var o = q.options[i];
            optionsHTML += "<div class=\"option\" data-value=\"" + o.letter + "\">" + o.letter + ". " + o.text + "</div>";
        }
        optionsHTML += "</div>";
    }
    card.innerHTML = "<div class=\"q-meta\"><span class=\"q-tag " + tagClass[q.type] + "\">" + typeMap[q.type] + "</span><span>" + q.chapter + "</span></div><div class=\"q-text\">" + q.num + ". " + q.question + "</div>" + optionsHTML + "<div class=\"feedback\" id=\"feedback\"></div>";
    var prevAns = userAnswers[currentIndex];
    if (prevAns) {
        var opts = card.querySelectorAll(".option");
        if (q.type === "single" || q.type === "judge") {
            for (var i = 0; i < opts.length; i++) {
                if (opts[i].getAttribute("data-value") === prevAns) opts[i].classList.add("selected");
            }
        } else {
            for (var i = 0; i < prevAns.length; i++) {
                for (var j = 0; j < opts.length; j++) {
                    if (opts[j].getAttribute("data-value") === prevAns[i]) opts[j].classList.add("selected");
                }
            }
        }
    }
    var opts2 = card.querySelectorAll(".option");
    for (var i = 0; i < opts2.length; i++) {
        opts2[i].onclick = (function(el) {
            return function() { selectOption(el); };
        })(opts2[i]);
    }
    document.querySelector("#progressText span").textContent = currentIndex + 1;
    document.getElementById("prevBtn").disabled = (currentIndex === 0);
    document.getElementById("nextBtn").textContent = (currentIndex === currentQuestions.length - 1) ? "\U0001f4ca 查看结果" : "下一题 \u2192";
    updateWrongCount();
}

function selectOption(el) {
    var q = currentQuestions[currentIndex];
    if (q.type === "multiple") {
        el.classList.toggle("selected");
        var sel = document.querySelectorAll(".option.selected");
        var ans = [];
        for (var i = 0; i < sel.length; i++) {
            ans.push(sel[i].getAttribute("data-value"));
        }
        ans.sort();
        userAnswers[currentIndex] = ans.join("");
    } else {
        var opts = document.querySelectorAll(".option");
        for (var i = 0; i < opts.length; i++) {
            opts[i].classList.remove("selected");
        }
        el.classList.add("selected");
        userAnswers[currentIndex] = el.getAttribute("data-value");
        checkAnswer();
    }
}

function checkAnswer() {
    var q = currentQuestions[currentIndex];
    var feedback = document.getElementById("feedback");
    var userAns = userAnswers[currentIndex];
    if (!userAns) return false;
    var isCorrect = false;
    if (q.type === "multiple") {
        isCorrect = (userAns.split("").sort().join("") === q.answer.split("").sort().join(""));
    } else {
        isCorrect = (userAns === q.answer);
    }
    var opts = document.querySelectorAll(".option");
    for (var i = 0; i < opts.length; i++) {
        opts[i].classList.add("disabled");
    }
    if (isCorrect) {
        feedback.className = "feedback correct";
        feedback.innerHTML = "\u2705 回答正确！";
        var selOpts = document.querySelectorAll(".option.selected");
        for (var i = 0; i < selOpts.length; i++) {
            selOpts[i].classList.add("correct");
        }
    } else {
        feedback.className = "feedback wrong";
        feedback.innerHTML = "\u274c 回答错误<div class=\"answer-text\">正确答案：" + q.answer + "</div>";
        var selOpts2 = document.querySelectorAll(".option.selected");
        for (var i = 0; i < selOpts2.length; i++) {
            selOpts2[i].classList.add("wrong");
        }
        if (q.type === "judge") {
            for (var i = 0; i < opts.length; i++) {
                if (opts[i].getAttribute("data-value") === q.answer) opts[i].classList.add("show-correct");
            }
        } else {
            for (var i = 0; i < q.answer.length; i++) {
                for (var j = 0; j < opts.length; j++) {
                    if (opts[j].getAttribute("data-value") === q.answer[i]) opts[j].classList.add("show-correct");
                }
            }
        }
        addWrongQuestion(q);
    }
    updateWrongCount();
}

function addWrongQuestion(q) {
    var exists = false;
    for (var i = 0; i < wrongQuestions.length; i++) {
        var w = wrongQuestions[i];
        if (w.chapter === q.chapter && w.num === q.num && w.type === q.type) { exists = true; break; }
    }
    if (!exists) {
        var copy = JSON.parse(JSON.stringify(q));
        copy.wrongAnswer = userAnswers[currentIndex];
        wrongQuestions.push(copy);
        localStorage.setItem("maogai_wrong", JSON.stringify(wrongQuestions));
    }
}

function updateWrongCount() {
    document.getElementById("wrongCount").textContent = "\u274c 错题：" + wrongQuestions.length;
}

document.getElementById("startBtn").onclick = startQuiz;
document.getElementById("wrongReviewBtn").onclick = showWrongReview;
document.getElementById("reviewWrongBtn").onclick = reviewWrong;
document.getElementById("prevBtn").onclick = function() { if (currentIndex > 0) { currentIndex--; renderQuestion(); } };
document.getElementById("nextBtn").onclick = function() {
    if (currentIndex < currentQuestions.length - 1) {
        currentIndex++;
        renderQuestion();
    } else {
        for (var i = 0; i < currentQuestions.length; i++) {
            if (!userAnswers[i]) { currentIndex = i; renderQuestion(); return; }
        }
        finishQuiz();
    }
};

function finishQuiz() {
    var correct = 0, incorrect = 0;
    for (var i = 0; i < currentQuestions.length; i++) {
        var q = currentQuestions[i];
        var ans = userAnswers[i];
        if (!ans) continue;
        var isC = (q.type === "multiple")
            ? (ans.split("").sort().join("") === q.answer.split("").sort().join(""))
            : (ans === q.answer);
        if (isC) correct++; else incorrect++;
    }
    document.getElementById("quizView").style.display = "none";
    document.getElementById("summaryView").style.display = "block";
    var total = correct + incorrect;
    var score = total > 0 ? Math.round(correct / total * 100) : 0;
    document.getElementById("finalScore").textContent = score + "%";
    document.getElementById("correctCount").textContent = correct;
    document.getElementById("incorrectCount").textContent = incorrect;
    document.getElementById("totalCount").textContent = total;
}

function showWrongReview() {
    document.getElementById("menuView").style.display = "none";
    document.getElementById("quizView").style.display = "none";
    document.getElementById("summaryView").style.display = "none";
    document.getElementById("wrongView").style.display = "block";
    var list = document.getElementById("wrongList");
    var typeMap = {single:"单选题", multiple:"多选题", judge:"判断题"};
    if (wrongQuestions.length === 0) {
        list.innerHTML = "<div class=\"empty-state\" style=\"padding:60px 20px;text-align:center;color:#999;\"><div style=\"font-size:48px;margin-bottom:16px;\">\U0001f389</div><div>还没有错题，继续保持！</div></div>";
        document.getElementById("wrongTotalCount").textContent = "(0)";
        return;
    }
    document.getElementById("wrongTotalCount").textContent = "(共 " + wrongQuestions.length + " 题)";
    list.innerHTML = "";
    for (var i = 0; i < wrongQuestions.length; i++) {
        var q = wrongQuestions[i];
        var div = document.createElement("div");
        div.className = "wrong-item";
        var displayAns = q.wrongAnswer || "未提交";
        div.innerHTML = "<div class=\"wi-q\"><strong>" + (i+1) + ".</strong> [" + typeMap[q.type] + "] " + q.question + "</div><div class=\"wi-answer\"><span class=\"wrong-a\">你的答案：" + displayAns + "</span> \u00b7 <span class=\"correct-a\">正确答案：" + q.answer + "</span></div>";
        list.appendChild(div);
    }
}

function reviewWrong() {
    if (wrongQuestions.length === 0) return;
    currentQuestions = [];
    for (var i = 0; i < wrongQuestions.length; i++) {
        var copy = JSON.parse(JSON.stringify(wrongQuestions[i]));
        if (!copy.options) copy.options = [];
        currentQuestions.push(copy);
    }
    currentIndex = 0;
    userAnswers = {};
    document.getElementById("summaryView").style.display = "none";
    document.getElementById("totalQ").textContent = currentQuestions.length;
    document.getElementById("quizView").style.display = "block";
    renderQuestion();
}

function showMenu() {
    document.getElementById("menuView").style.display = "block";
    document.getElementById("quizView").style.display = "none";
    document.getElementById("summaryView").style.display = "none";
    document.getElementById("wrongView").style.display = "none";
}

init();
</script>
</body>
</html>""")

with open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html", "w", encoding="utf-8") as f:
    f.write(html_parts[0])

print("OK")
print("Size: " + str(os.path.getsize("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html")))
