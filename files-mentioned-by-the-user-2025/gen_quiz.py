import json, os

with open("C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

chapters = []
seen = set()
for q in questions:
    if q["chapter"] not in seen:
        seen.add(q["chapter"])
        chapters.append(q["chapter"])

stats = {}
for q in questions:
    ch = q["chapter"]
    if ch not in stats:
        stats[ch] = {"single":0, "multiple":0, "judge":0}
    stats[ch][q["type"]] += 1

chapter_items = []
for ch in chapters:
    s = stats[ch]
    chapter_items.append('{"name":' + json.dumps(ch) + ',"single":' + str(s["single"]) + ',"multiple":' + str(s["multiple"]) + ',"judge":' + str(s["judge"]) + '}')

chapters_js = "[" + ",".join(chapter_items) + "]"
questions_js = json.dumps(questions, ensure_ascii=False)

total = len(questions)
single_count = len([q for q in questions if q["type"]=="single"])
multi_count = len([q for q in questions if q["type"]=="multiple"])
judge_count = len([q for q in questions if q["type"]=="judge"])

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>毛概期末练习题库 - 刷题系统</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, 'Microsoft YaHei', sans-serif; background: #f0f2f5; color: #333; }
.container { max-width: 900px; margin: 0 auto; padding: 20px; }
.header { background: linear-gradient(135deg, #1a73e8, #0d47a1); color: white; padding: 20px 30px; border-radius: 16px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; }
.header h1 { font-size: 22px; font-weight: 600; }
.header .stats { font-size: 13px; opacity: 0.9; }
.menu { background: white; border-radius: 16px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.menu-title { font-size: 15px; font-weight: 600; margin-bottom: 14px; color: #555; }
.chapter-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; margin-bottom: 16px; }
.chapter-btn { padding: 12px 16px; border: 2px solid #e0e0e0; border-radius: 10px; background: white; cursor: pointer; font-size: 14px; text-align: left; transition: all 0.2s; }
.chapter-btn:hover { border-color: #1a73e8; background: #f5f8ff; }
.chapter-btn.active { border-color: #1a73e8; background: #e8f0fe; color: #1a73e8; font-weight: 600; }
.chapter-btn .count { font-size: 11px; color: #999; margin-top: 4px; }
.type-filter { display: flex; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }
.type-btn { padding: 8px 20px; border: 2px solid #e0e0e0; border-radius: 20px; background: white; cursor: pointer; font-size: 13px; transition: all 0.2s; }
.type-btn:hover { border-color: #1a73e8; }
.type-btn.active { background: #1a73e8; color: white; border-color: #1a73e8; }
.start-btn { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, #1a73e8, #0d47a1); color: white; border: none; border-radius: 12px; font-size: 17px; font-weight: 600; cursor: pointer; transition: all 0.2s; }
.start-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(26,115,232,0.35); }
.start-btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
.quiz-area { display: none; }
.quiz-header { background: white; border-radius: 16px; padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; justify-content: space-between; align-items: center; }
.quiz-header .progress { font-size: 14px; color: #666; }
.quiz-header .progress span { color: #1a73e8; font-weight: 600; }
.quiz-header .wrong-count { font-size: 13px; color: #e53935; }
.quiz-card { background: white; border-radius: 16px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 16px; }
.quiz-card .q-meta { font-size: 12px; color: #999; margin-bottom: 8px; }
.quiz-card .q-tag { display: inline-block; padding: 2px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; margin-right: 6px; }
.tag-single { background: #e3f2fd; color: #1565c0; }
.tag-multiple { background: #fff3e0; color: #e65100; }
.tag-judge { background: #e8f5e9; color: #2e7d32; }
.quiz-card .q-text { font-size: 16px; line-height: 1.7; margin-bottom: 20px; }
.options { display: flex; flex-direction: column; gap: 10px; }
.option { padding: 14px 18px; border: 2px solid #e8e8e8; border-radius: 12px; cursor: pointer; font-size: 15px; line-height: 1.5; transition: all 0.2s; }
.option:hover { border-color: #90caf9; background: #f5f8ff; }
.option.selected { border-color: #1a73e8; background: #e8f0fe; }
.option.correct { border-color: #43a047; background: #e8f5e9; color: #2e7d32; }
.option.wrong { border-color: #e53935; background: #ffebee; color: #c62828; }
.option.show-correct { border-color: #43a047; background: #e8f5e9; }
.option.disabled { pointer-events: none; opacity: 0.7; }
.feedback { margin-top: 16px; padding: 14px 18px; border-radius: 12px; font-size: 14px; display: none; }
.feedback.correct { display: block; background: #e8f5e9; color: #2e7d32; border: 1px solid #c8e6c9; }
.feedback.wrong { display: block; background: #ffebee; color: #c62828; border: 1px solid #ffcdd2; }
.feedback .answer-text { margin-top: 6px; font-weight: 500; }
.nav-btns { display: flex; gap: 12px; margin-top: 16px; }
.nav-btn { flex: 1; padding: 12px; border: 2px solid #e0e0e0; border-radius: 12px; background: white; cursor: pointer; font-size: 15px; font-weight: 500; transition: all 0.2s; }
.nav-btn:hover { border-color: #1a73e8; }
.nav-btn.primary { background: #1a73e8; color: white; border-color: #1a73e8; }
.nav-btn.primary:hover { background: #1557b0; }
.nav-btn:disabled { opacity: 0.4; cursor: not-allowed; }
.wrong-panel { display: none; background: white; border-radius: 16px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.wrong-panel h3 { font-size: 18px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
.wrong-panel h3 .count { font-size: 14px; color: #999; font-weight: 400; }
.wrong-item { padding: 16px; border: 1px solid #ffcdd2; border-radius: 12px; margin-bottom: 12px; background: #fff5f5; }
.wrong-item .wi-q { font-size: 15px; margin-bottom: 8px; }
.wrong-item .wi-answer { font-size: 13px; }
.wrong-item .wi-answer .wrong-a { color: #e53935; }
.wrong-item .wi-answer .correct-a { color: #43a047; }
.btn-back { padding: 10px 24px; border: 2px solid #e0e0e0; border-radius: 10px; background: white; cursor: pointer; font-size: 14px; margin-top: 12px; }
.btn-back:hover { border-color: #1a73e8; }
.empty-state { text-align: center; padding: 60px 20px; color: #999; }
.empty-state .icon { font-size: 48px; margin-bottom: 16px; }
.summary { display: none; background: white; border-radius: 16px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); text-align: center; }
.summary h2 { font-size: 22px; margin-bottom: 12px; }
.summary .score { font-size: 48px; font-weight: 700; color: #1a73e8; margin: 16px 0; }
.summary .detail { font-size: 15px; color: #666; margin-bottom: 20px; }
.summary .detail span { font-weight: 600; color: #333; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div>
      <h1>""" + chr(128214) + """ 毛概期末练习题库</h1>
      <div class="stats">共 """ + str(total) + """ 道题 """ + chr(183) + """ 单选 """ + str(single_count) + """ """ + chr(183) + """ 多选 """ + str(multi_count) + """ """ + chr(183) + """ 判断 """ + str(judge_count) + """</div>
    </div>
  </div>

  <div id="menuView">
    <div class="menu">
      <div class="menu-title">""" + chr(128194) + """ 选择章节（可多选）</div>
      <div class="chapter-list" id="chapterList"></div>
      <div class="menu-title" style="margin-top:16px;">""" + chr(128203) + """ 题目类型</div>
      <div class="type-filter" id="typeFilter">
        <button class="type-btn active" data-type="all">全部</button>
        <button class="type-btn" data-type="single">单选题</button>
        <button class="type-btn" data-type="multiple">多选题</button>
        <button class="type-btn" data-type="judge">判断题</button>
      </div>
      <div style="margin-top:6px;margin-bottom:16px;font-size:13px;color:#999;" id="selectedInfo">已选：0 道题</div>
      <button class="start-btn" id="startBtn" disabled>""" + chr(128640) + """ 开始答题</button>
    </div>
    <div class="menu" style="margin-top:16px;">
      <div class="menu-title">""" + chr(128214) + """ 其他功能</div>
      <button class="start-btn" id="wrongReviewBtn" style="background: linear-gradient(135deg, #e53935, #b71c1c);margin-top:0;">""" + chr(128221) + """ 查看错题本</button>
    </div>
  </div>

  <div class="quiz-area" id="quizView">
    <div class="quiz-header">
      <div class="progress" id="progressText">第 <span>1</span> / <span id="totalQ">?</span> 题</div>
      <div class="wrong-count" id="wrongCount">""" + chr(10060) + """ 错题：0</div>
    </div>
    <div class="quiz-card" id="quizCard"></div>
    <div class="nav-btns">
      <button class="nav-btn" id="prevBtn" disabled>""" + chr(8592) + """ 上一题</button>
      <button class="nav-btn primary" id="nextBtn">下一题 """ + chr(8594) + """</button>
      <button class="nav-btn" id="submitBtn" style="display:none;background:#43a047;color:white;border-color:#43a047;">""" + chr(9989) + """ 完成答题</button>
    </div>
  </div>

  <div class="summary" id="summaryView">
    <h2>""" + chr(127881) + """ 答题完成！</h2>
    <div class="score" id="finalScore">0%</div>
    <div class="detail" id="finalDetail">正确 <span id="correctCount">0</span> 题 """ + chr(183) + """ 错误 <span id="incorrectCount">0</span> 题 """ + chr(183) + """ 共 <span id="totalCount">0</span> 题</div>
    <button class="start-btn" onclick="location.reload()" style="margin-top:20px;display:inline-block;width:auto;padding:12px 40px;">返回主菜单</button>
    <button class="start-btn" id="reviewWrongBtn" style="margin-top:12px;display:inline-block;width:auto;padding:12px 40px;background:linear-gradient(135deg,#e53935,#b71c1c);">""" + chr(128221) + """ 复习错题</button>
  </div>

  <div class="wrong-panel" id="wrongView">
    <h3>""" + chr(128221) + """ 错题本 <span class="count" id="wrongTotalCount"></span></h3>
    <div id="wrongList"></div>
    <button class="btn-back" onclick="showMenu()">""" + chr(8592) + """ 返回主菜单</button>
  </div>
</div>

<script>
const ALL_QUESTIONS = """ + questions_js + """;
const CHAPTERS = """ + chapters_js + """;

let selectedChapters = new Set();
let selectedTypes = new Set(["all"]);
let currentQuestions = [];
let currentIndex = 0;
let userAnswers = {};
let wrongQuestions = JSON.parse(localStorage.getItem("maogai_wrong") || "[]");
let isReviewing = false;

function init() {
  renderChapters();
  renderTypeFilter();
  updateSelectedInfo();
}

function renderChapters() {
  const list = document.getElementById("chapterList");
  list.innerHTML = "";
  CHAPTERS.forEach((ch, i) => {
    const btn = document.createElement("button");
    btn.className = "chapter-btn";
    const total = ch.single + ch.multiple + ch.judge;
    btn.innerHTML = ch.name + '<div class="count">单选 ' + ch.single + ' ' + String.fromCharCode(183) + ' 多选 ' + ch.multiple + ' ' + String.fromCharCode(183) + ' 判断 ' + ch.judge + ' ' + String.fromCharCode(183) + ' 共 ' + total + ' 题</div>';
    btn.onclick = function() { toggleChapter(i, btn); };
    list.appendChild(btn);
  });
}

function renderTypeFilter() {
  document.querySelectorAll(".type-btn").forEach(function(btn) {
    btn.onclick = function() {
      const type = btn.dataset.type;
      if (type === "all") {
        selectedTypes = new Set(["all"]);
        document.querySelectorAll(".type-btn").forEach(function(b) { b.classList.toggle("active", b.dataset.type === "all"); });
      } else {
        selectedTypes.delete("all");
        if (selectedTypes.has(type)) selectedTypes.delete(type);
        else selectedTypes.add(type);
        btn.classList.toggle("active");
        document.querySelector(".type-btn[data-type=\"all\"]").classList.toggle("active", selectedTypes.size === 0);
        if (selectedTypes.size === 0) {
          selectedTypes.add("all");
          document.querySelectorAll(".type-btn").forEach(function(b) { b.classList.toggle("active", b.dataset.type === "all"); });
        }
      }
      updateSelectedInfo();
    };
  });
}

function toggleChapter(index, btn) {
  const chName = CHAPTERS[index].name;
  if (selectedChapters.has(chName)) {
    selectedChapters.delete(chName);
    btn.classList.remove("active");
  } else {
    selectedChapters.add(chName);
    btn.classList.add("active");
  }
  if (selectedChapters.size === 0) {
    CHAPTERS.forEach(function(ch) { selectedChapters.add(ch.name); });
    document.querySelectorAll(".chapter-btn").forEach(function(b) { b.classList.add("active"); });
  }
  updateSelectedInfo();
}

function updateSelectedInfo() {
  const types = selectedTypes.has("all") ? ["single", "multiple", "judge"] : Array.from(selectedTypes);
  const chs = selectedChapters.size === 0 ? CHAPTERS.map(function(c) { return c.name; }) : Array.from(selectedChapters);
  const filtered = ALL_QUESTIONS.filter(function(q) { return chs.includes(q.chapter) && types.includes(q.type); });
  document.getElementById("selectedInfo").textContent = "已选：" + filtered.length + " 道题";
  document.getElementById("startBtn").disabled = filtered.length === 0;
}

document.getElementById("startBtn").onclick = startQuiz;
document.getElementById("wrongReviewBtn").onclick = showWrongReview;
document.getElementById("submitBtn").onclick = finishQuiz;
document.getElementById("reviewWrongBtn").onclick = reviewWrong;
document.getElementById("prevBtn").onclick = prevQuestion;
document.getElementById("nextBtn").onclick = nextQuestion;

function startQuiz() {
  const types = selectedTypes.has("all") ? ["single", "multiple", "judge"] : Array.from(selectedTypes);
  const chs = selectedChapters.size === 0 ? CHAPTERS.map(function(c) { return c.name; }) : Array.from(selectedChapters);
  currentQuestions = ALL_QUESTIONS.filter(function(q) { return chs.includes(q.chapter) && types.includes(q.type); });
  currentIndex = 0;
  userAnswers = {};
  isReviewing = false;

  document.getElementById("menuView").style.display = "none";
  document.getElementById("quizView").style.display = "block";
  document.getElementById("summaryView").style.display = "none";
  document.getElementById("wrongView").style.display = "none";
  document.getElementById("submitBtn").style.display = "none";
  document.getElementById("totalQ").textContent = currentQuestions.length;
  renderQuestion();
}

function renderQuestion() {
  if (currentIndex >= currentQuestions.length) { finishQuiz(); return; }
  const q = currentQuestions[currentIndex];
  const card = document.getElementById("quizCard");
  const typeMap = {single: "单选题", multiple: "多选题", judge: "判断题"};
  const tagClass = {single: "tag-single", multiple: "tag-multiple", judge: "tag-judge"};

  let optionsHTML = "";
  if (q.type === "judge") {
    optionsHTML = '<div class="options"><div class="option" data-value="' + String.fromCharCode(27491) + '\u786e">' + String.fromCharCode(9989) + ' \u6b63\u786e</div><div class="option" data-value="\u9519\u8bef">' + String.fromCharCode(10060) + ' \u9519\u8bef</div></div>';
  } else {
    optionsHTML = '<div class="options">';
    q.options.forEach(function(o) {
      optionsHTML += '<div class="option" data-value="' + o.letter + '">' + o.letter + '. ' + o.text + '</div>';
    });
    optionsHTML += "</div>";
  }

  card.innerHTML = '<div class="q-meta"><span class="q-tag ' + tagClass[q.type] + '">' + typeMap[q.type] + '</span><span>' + q.chapter + '</span></div><div class="q-text">' + q.num + '. ' + q.question + '</div>' + optionsHTML + '<div class="feedback" id="feedback"></div>';

  const prevAns = userAnswers[currentIndex];
  if (prevAns) {
    const opts = card.querySelectorAll(".option");
    if (q.type === "single" || q.type === "judge") {
      opts.forEach(function(o) { if (o.dataset.value === prevAns) o.classList.add("selected"); });
    } else {
      prevAns.split("").forEach(function(v) {
        opts.forEach(function(o) { if (o.dataset.value === v) o.classList.add("selected"); });
      });
    }
  }

  card.querySelectorAll(".option").forEach(function(o) { o.onclick = function() { selectOption(o); }; });

  document.querySelector("#progressText span").textContent = currentIndex + 1;
  document.getElementById("prevBtn").disabled = currentIndex === 0;
  document.getElementById("nextBtn").textContent = currentIndex === currentQuestions.length - 1 ? "" + String.fromCharCode(128202) + " \u67e5\u770b\u7ed3\u679c" : "\u4e0b\u4e00\u9898 " + String.fromCharCode(8594);
  document.getElementById("submitBtn").style.display = "none";
  updateWrongCount();
}

function selectOption(el) {
  const q = currentQuestions[currentIndex];
  if (q.type === "multiple") {
    el.classList.toggle("selected");
    const selected = Array.from(document.querySelectorAll(".option.selected")).map(function(o) { return o.dataset.value; });
    userAnswers[currentIndex] = selected.sort().join("");
  } else {
    document.querySelectorAll(".option").forEach(function(o) { o.classList.remove("selected"); });
    el.classList.add("selected");
    userAnswers[currentIndex] = el.dataset.value;
    // Auto check for single/judge
    checkAnswer();
  }
}

function checkAnswer() {
  const q = currentQuestions[currentIndex];
  const feedback = document.getElementById("feedback");
  const userAns = userAnswers[currentIndex];
  if (!userAns) return false;

  const isCorrect = q.type === "multiple"
    ? userAns.split("").sort().join("") === q.answer.split("").sort().join("")
    : userAns === q.answer;

  document.querySelectorAll(".option").forEach(function(o) { o.classList.add("disabled"); });

  if (isCorrect) {
    feedback.className = "feedback correct";
    feedback.innerHTML = String.fromCharCode(9989) + " \u56de\u7b54\u6b63\u786e\uff01";
    document.querySelectorAll(".option.selected").forEach(function(o) { o.classList.add("correct"); });
  } else {
    feedback.className = "feedback wrong";
    feedback.innerHTML = String.fromCharCode(10060) + " \u56de\u7b54\u9519\u8bef<div class=\"answer-text\">\u6b63\u786e\u7b54\u6848\uff1a" + q.answer + "</div>";
    document.querySelectorAll(".option.selected").forEach(function(o) { o.classList.add("wrong"); });

    if (q.type === "judge") {
      document.querySelectorAll(".option").forEach(function(o) { if (o.dataset.value === q.answer) o.classList.add("show-correct"); });
    } else {
      q.answer.split("").forEach(function(v) {
        document.querySelectorAll(".option").forEach(function(o) { if (o.dataset.value === v) o.classList.add("show-correct"); });
      });
    }
    addWrongQuestion(q);
  }
  updateWrongCount();
  return isCorrect;
}

function addWrongQuestion(q) {
  const wrongSet = new Set(wrongQuestions.map(function(w) { return w.chapter + w.num + w.type; }));
  const key = q.chapter + q.num + q.type;
  if (!wrongSet.has(key)) {
    var copy = JSON.parse(JSON.stringify(q));
    copy.wrongAnswer = userAnswers[currentIndex];
    wrongQuestions.push(copy);
    localStorage.setItem("maogai_wrong", JSON.stringify(wrongQuestions));
  }
}

function updateWrongCount() {
  document.getElementById("wrongCount").textContent = String.fromCharCode(10060) + " \u9519\u9898\uff1a" + wrongQuestions.length;
}

function prevQuestion() { if (currentIndex > 0) { currentIndex--; renderQuestion(); } }

function nextQuestion() {
  if (currentIndex < currentQuestions.length - 1) {
    currentIndex++;
    renderQuestion();
  } else {
    let allAnswered = true;
    for (let i = 0; i < currentQuestions.length; i++) {
      if (!userAnswers[i]) { allAnswered = false; break; }
    }
    if (allAnswered) {
      finishQuiz();
    } else {
      let found = false;
      for (let i = currentIndex; i < currentQuestions.length; i++) {
        if (!userAnswers[i]) { currentIndex = i; renderQuestion(); found = true; break; }
      }
      if (!found) {
        for (let i = 0; i < currentIndex; i++) {
          if (!userAnswers[i]) { currentIndex = i; renderQuestion(); found = true; break; }
        }
      }
      if (!found) finishQuiz();
    }
  }
}

function finishQuiz() {
  let correct = 0, incorrect = 0;
  currentQuestions.forEach(function(q, i) {
    const ans = userAnswers[i];
    if (!ans) return;
    const isC = q.type === "multiple"
      ? ans.split("").sort().join("") === q.answer.split("").sort().join("")
      : ans === q.answer;
    if (isC) correct++; else incorrect++;
  });

  document.getElementById("quizView").style.display = "none";
  document.getElementById("summaryView").style.display = "block";
  const total = correct + incorrect;
  const score = total > 0 ? Math.round(correct / total * 100) : 0;
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

  const list = document.getElementById("wrongList");
  const typeMap = {single: "单选题", multiple: "多选题", judge: "判断题"};

  if (wrongQuestions.length === 0) {
    list.innerHTML = '<div class="empty-state"><div class="icon">' + String.fromCharCode(127881) + '</div><div>\u8fd8\u6ca1\u6709\u9519\u9898\uff0c\u7ee7\u7eed\u4fdd\u6301\uff01</div></div>';
    document.getElementById("wrongTotalCount").textContent = "(0)";
    return;
  }

  document.getElementById("wrongTotalCount").textContent = "(\u5171 " + wrongQuestions.length + " \u9898)";
  list.innerHTML = "";
  wrongQuestions.forEach(function(q, i) {
    const div = document.createElement("div");
    div.className = "wrong-item";
    const displayAns = q.wrongAnswer || "\u672a\u63d0\u4ea4";
    div.innerHTML = '<div class="wi-q"><strong>' + (i+1) + '.</strong> [' + typeMap[q.type] + '] ' + q.question + '</div><div class="wi-answer"><span class="wrong-a">\u4f60\u7684\u7b54\u6848\uff1a' + displayAns + '</span> ' + String.fromCharCode(183) + ' <span class="correct-a">\u6b63\u786e\u7b54\u6848\uff1a' + q.answer + '</span></div>';
    list.appendChild(div);
  });
}

function reviewWrong() {
  if (wrongQuestions.length === 0) return;
  currentQuestions = wrongQuestions.map(function(q) { var c = JSON.parse(JSON.stringify(q)); c.options = c.options || []; return c; });
  currentIndex = 0;
  userAnswers = {};
  isReviewing = true;

  document.getElementById("summaryView").style.display = "none";
  document.getElementById("totalQ").textContent = currentQuestions.length;
  document.getElementById("submitBtn").style.display = "none";
  document.getElementById("quizView").style.display = "block";
  renderQuestion();
}

function showMenu() {
  document.getElementById("menuView").style.display = "block";
  document.getElementById("quizView").style.display = "none";
  document.getElementById("summaryView").style.display = "none";
  document.getElementById("wrongView").style.display = "none";
  updateSelectedInfo();
}

init();
</script>
</body>
</html>"""

out_path = "C:\\Users\\Ben\\Documents\\Codex\\2026-05-27\\files-mentioned-by-the-user-2025\\maogai_quiz.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Generated: " + out_path)
print("Size: " + str(os.path.getsize(out_path)) + " bytes")
