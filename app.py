import streamlit as st
import random
import json
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Science SmartBot",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eaf7f2 0%, #eef3ff 55%, #f8f1ff 100%);
}
.block-container {padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1150px;}
.hero {
    background: linear-gradient(120deg, #063970, #087f78, #16a085);
    padding: 30px 22px; border-radius: 22px; color: white;
    text-align: center; box-shadow: 0 8px 24px rgba(5,55,80,.18);
    margin-bottom: 16px;
}
.hero h1 {color:white !important; font-size:2.35rem; margin:0;}
.hero p {color:#f0fffb; margin:7px 0 0 0; font-size:1.05rem;}
.section-title {color:#12664f; font-weight:800; font-size:1.45rem; margin:8px 0;}
.topic-card {
    background: linear-gradient(145deg, #ffffff, #e9f7f2);
    border:1px solid #b9ded3; border-radius:18px; padding:16px;
    text-align:center; min-height:145px; box-shadow:0 4px 13px rgba(20,80,70,.08);
}
.topic-icon {font-size:2.1rem;}
.topic-name {font-size:1.05rem; font-weight:800; color:#135c4c;}
.topic-count {font-size:.85rem; color:#54766d;}
.answer-box {
    background:#ffffff; border-left:6px solid #11998e;
    border-radius:12px; padding:17px; color:#174d43;
}
.small-note {color:#53746b; font-size:.9rem;}
.stButton > button, .stFormSubmitButton > button {
    background:#176b55; color:white; border:0; border-radius:12px;
    padding: .55rem 1rem; font-weight:700;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background:#0d5141; color:white; border:0;
}
div[data-testid="stExpander"] {
    background:rgba(255,255,255,.78); border-radius:12px;
    border:1px solid #d4e9e2;
}
</style>
""", unsafe_allow_html=True)

# ---------- SCIENCE CONTENT ----------
topics = {
    "Plants": {
        "icon": "🌱",
        "questions": [
            {"ur":"پودے اپنی خوراک کیسے بناتے ہیں؟","sd":"ٻوٽا پنهنجي خوراڪ ڪيئن ٺاهين ٿا؟",
             "keywords":["پودے اپنی خوراک","photosynthesis","ٻوٽا پنهنجي خوراڪ","فوٹوسنتھیسز","فوٽوسنٿيسس"],
             "a_ur":"پودے سورج کی روشنی، پانی اور کاربن ڈائی آکسائیڈ سے اپنی خوراک بناتے ہیں۔ اس عمل کو فوٹوسنتھیسز کہتے ہیں۔",
             "a_sd":"ٻوٽا سج جي روشني، پاڻي ۽ ڪاربان ڊاءِ آڪسائيڊ سان پنهنجي خوراڪ ٺاهين ٿا. هن عمل کي فوٽوسنٿيسس چئبو آهي۔"},
            {"ur":"پودوں کو سورج کی روشنی کیوں چاہیے؟","sd":"ٻوٽن کي سج جي روشني ڇو گهرجي؟",
             "keywords":["سورج کی روشنی","سج جي روشني"],
             "a_ur":"پودوں کو خوراک بنانے کے لیے سورج کی روشنی کی ضرورت ہوتی ہے۔",
             "a_sd":"ٻوٽن کي خوراڪ ٺاهڻ لاءِ سج جي روشني جي ضرورت هوندي آهي۔"}
        ]
    },
    "Heart": {
        "icon":"❤️",
        "questions":[
            {"ur":"دل کیا کام کرتا ہے؟","sd":"دل ڇا ڪم ڪري ٿو؟","keywords":["دل کیا کام","دل ڇا ڪم","heart"],
             "a_ur":"دل خون کو پورے جسم میں پمپ کرتا ہے۔","a_sd":"دل رت کي سڄي جسم ۾ پمپ ڪري ٿو۔"},
            {"ur":"دل کس نظام کا حصہ ہے؟","sd":"دل ڪهڙي نظام جو حصو آهي؟","keywords":["دل کس نظام","دل ڪهڙي نظام"],
             "a_ur":"دل نظامِ دورانِ خون کا اہم حصہ ہے۔","a_sd":"دل رت جي گردش واري نظام جو اهم حصو آهي۔"}
        ]
    },
    "Water Cycle": {
        "icon":"💧",
        "questions":[
            {"ur":"پانی کا چکر کیا ہے؟","sd":"پاڻي جو چڪر ڇا آهي؟","keywords":["پانی کا چکر","پاڻي جو چڪر","water cycle"],
             "a_ur":"پانی کے بخارات بننے، بادل بننے اور بارش ہونے کے مسلسل عمل کو پانی کا چکر کہتے ہیں۔",
             "a_sd":"پاڻي جي ٻاڦ ٿيڻ، ڪڪر ٺهڻ ۽ مينهن وسڻ جي مسلسل عمل کي پاڻي جو چڪر چئبو آهي۔"},
            {"ur":"بارش کیسے ہوتی ہے؟","sd":"مينهن ڪيئن وسي ٿو؟","keywords":["بارش کیسے","مينهن ڪيئن"],
             "a_ur":"بادلوں میں پانی کے قطرے جمع ہو کر بھاری ہوتے ہیں اور بارش کی صورت میں زمین پر گرتے ہیں۔",
             "a_sd":"ڪڪرن ۾ پاڻي جا ڦڙا گڏ ٿي ڳرا ٿين ٿا ۽ مينهن جي صورت ۾ زمين تي وسن ٿا۔"}
        ]
    },
    "Gravity": {
        "icon":"🌍",
        "questions":[
            {"ur":"کشش ثقل کیا ہے؟","sd":"ڪشش ثقل ڇا آهي؟","keywords":["کشش ثقل کیا","ڪشش ثقل ڇا","gravity"],
             "a_ur":"کشش ثقل ایک قوت ہے جو چیزوں کو ایک دوسرے کی طرف کھینچتی ہے۔",
             "a_sd":"ڪشش ثقل هڪ قوت آهي جيڪا شين کي هڪ ٻئي ڏانهن ڇڪي ٿي۔"},
            {"ur":"چیزیں زمین پر کیوں گرتی ہیں؟","sd":"شيون زمين تي ڇو ڪرن ٿيون؟","keywords":["زمین پر کیوں","زمين تي ڇو"],
             "a_ur":"زمین کی کشش ثقل چیزوں کو اپنی طرف کھینچتی ہے۔",
             "a_sd":"زمين جي ڪشش ثقل شين کي پاڻ ڏانهن ڇڪي ٿي۔"}
        ]
    },
    "Matter": {
        "icon":"🧪",
        "questions":[
            {"ur":"مادہ کیا ہے؟","sd":"مادو ڇا آهي؟","keywords":["مادہ کیا","مادو ڇا","matter"],
             "a_ur":"مادہ وہ چیز ہے جس کی کمیت ہو اور جو جگہ گھیرتی ہو۔",
             "a_sd":"مادو اها شيءِ آهي جنهن جي ڪميت هجي ۽ جيڪا جاءِ والاري۔"},
            {"ur":"مادے کی تین حالتیں کون سی ہیں؟","sd":"مادي جون ٽي حالتون ڪهڙيون آهن؟","keywords":["مادے کی تین","مادي جون ٽي"],
             "a_ur":"مادے کی تین بنیادی حالتیں ٹھوس، مائع اور گیس ہیں۔",
             "a_sd":"مادي جون ٽي بنيادي حالتون ٺوس، پاڻياٺ ۽ گئس آهن۔"}
        ]
    },
    "Solar System": {
        "icon":"☀️",
        "questions":[
            {"ur":"شمسی نظام کیا ہے؟","sd":"شمسي نظام ڇا آهي؟","keywords":["شمسی نظام کیا","شمسي نظام ڇا","solar system"],
             "a_ur":"شمسی نظام میں سورج اور اس کے گرد گردش کرنے والے سیارے اور دیگر اجسام شامل ہیں۔",
             "a_sd":"شمسي نظام ۾ سج ۽ ان جي چوڌاري گردش ڪندڙ سيارا ۽ ٻيا جسم شامل آهن۔"},
            {"ur":"سورج کیا ہے؟","sd":"سج ڇا آهي؟","keywords":["سورج کیا","سج ڇا"],
             "a_ur":"سورج ایک ستارہ ہے جو ہمیں روشنی اور حرارت دیتا ہے۔",
             "a_sd":"سج هڪ تارو آهي جيڪو اسان کي روشني ۽ گرمي ڏئي ٿو۔"}
        ]
    },
    "Planets": {
        "icon":"🪐",
        "questions":[
            {"ur":"نظام شمسی میں کتنے سیارے ہیں؟","sd":"شمسي نظام ۾ ڪيترا سيارا آهن؟","keywords":["کتنے سیارے","ڪيترا سيارا","how many planets"],
             "a_ur":"ہمارے نظام شمسی میں آٹھ سیارے ہیں۔","a_sd":"اسان جي شمسي نظام ۾ اٺ سيارا آهن۔"},
            {"ur":"سب سے بڑا سیارہ کون سا ہے؟","sd":"سڀ کان وڏو سيارو ڪهڙو آهي؟","keywords":["سب سے بڑا سیارہ","سڀ کان وڏو سيارو"],
             "a_ur":"مشتری نظام شمسی کا سب سے بڑا سیارہ ہے۔","a_sd":"مشتري شمسي نظام جو سڀ کان وڏو سيارو آهي۔"}
        ]
    },
    "Evaporation": {
        "icon":"💨",
        "questions":[
            {"ur":"تبخیر کیا ہے؟","sd":"تبخير ڇا آهي؟","keywords":["تبخیر کیا","تبخير ڇا","evaporation"],
             "a_ur":"مائع کا سطح سے بخارات میں تبدیل ہونا تبخیر کہلاتا ہے۔","a_sd":"پاڻياٺ جو سطح تان ٻاڦ ۾ تبديل ٿيڻ تبخير چئبو آهي۔"},
            {"ur":"پانی بھاپ میں کیسے بدلتا ہے؟","sd":"پاڻي ٻاڦ ۾ ڪيئن بدلجي ٿو؟","keywords":["بھاپ میں کیسے","ٻاڦ ۾ ڪيئن"],
             "a_ur":"حرارت ملنے پر پانی کے ذرات تیزی سے حرکت کرتے ہیں اور پانی بخارات بن سکتا ہے۔",
             "a_sd":"گرمي ملڻ سان پاڻي جا ذرڙا تيزيءَ سان حرڪت ڪن ٿا ۽ پاڻي ٻاڦ بڻجي سگهي ٿو۔"}
        ]
    },
    "Lungs": {
        "icon":"🫁",
        "questions":[
            {"ur":"پھیپھڑوں کا کیا کام ہے؟","sd":"ڦڦڙن جو ڪهڙو ڪم آهي؟","keywords":["پھیپھڑوں کا","ڦڦڙن جو","lungs"],
             "a_ur":"پھیپھڑے سانس لینے میں مدد دیتے ہیں اور جسم میں آکسیجن پہنچانے کے عمل میں حصہ لیتے ہیں۔",
             "a_sd":"ڦڦڙ ساهه کڻڻ ۾ مدد ڪن ٿا ۽ جسم ۾ آڪسيجن پهچائڻ واري عمل ۾ حصو وٺن ٿا۔"},
            {"ur":"ہم سانس کیوں لیتے ہیں؟","sd":"اسان ساهه ڇو کڻون ٿا؟","keywords":["سانس کیوں","ساهه ڇو"],
             "a_ur":"ہم جسم کو آکسیجن فراہم کرنے اور کاربن ڈائی آکسائیڈ خارج کرنے کے لیے سانس لیتے ہیں۔",
             "a_sd":"اسان جسم کي آڪسيجن ڏيڻ ۽ ڪاربان ڊاءِ آڪسائيڊ خارج ڪرڻ لاءِ ساهه کڻون ٿا۔"}
        ]
    },
    "Magnet": {
        "icon":"🧲",
        "questions":[
            {"ur":"مقناطیس کیا ہے؟","sd":"مقناطيس ڇا آهي؟","keywords":["مقناطیس کیا","مقناطيس ڇا","magnet"],
             "a_ur":"مقناطیس ایک ایسی چیز ہے جو لوہے جیسی بعض دھاتوں کو اپنی طرف کھینچتی ہے۔",
             "a_sd":"مقناطيس اهڙي شيءِ آهي جيڪا لوهه جهڙين ڪجهه ڌاتن کي پاڻ ڏانهن ڇڪي ٿي۔"},
            {"ur":"مقناطیس کن چیزوں کو کھینچتا ہے؟","sd":"مقناطيس ڪهڙين شين کي ڇڪي ٿو؟","keywords":["کن چیزوں کو","ڪهڙين شين کي"],
             "a_ur":"مقناطیس لوہے، نکل اور کوبالٹ جیسی بعض دھاتوں کو کھینچتا ہے۔",
             "a_sd":"مقناطيس لوهه، نڪل ۽ ڪوبالٽ جهڙين ڪجهه ڌاتن کي ڇڪي ٿو۔"}
        ]
    }
}

quiz_bank = [
    {"ur":"پودے اپنی خوراک بنانے کے لیے کس کی روشنی استعمال کرتے ہیں؟","sd":"ٻوٽا خوراڪ ٺاهڻ لاءِ ڪنهن جي روشني استعمال ڪن ٿا؟","options_ur":["چاند","سورج","ستارے"],"options_sd":["چنڊ","سج","تارا"],"answer":1},
    {"ur":"خون پورے جسم میں کون پمپ کرتا ہے؟","sd":"رت سڄي جسم ۾ ڪير پمپ ڪري ٿو؟","options_ur":["دل","پھیپھڑے","معدہ"],"options_sd":["دل","ڦڦڙ","معدو"],"answer":0},
    {"ur":"نظام شمسی میں کتنے سیارے ہیں؟","sd":"شمسي نظام ۾ ڪيترا سيارا آهن؟","options_ur":["7","8","9"],"options_sd":["7","8","9"],"answer":1},
    {"ur":"مادے کی بنیادی حالتیں کتنی ہیں؟","sd":"مادي جون بنيادي حالتون ڪيتريون آهن؟","options_ur":["2","3","4"],"options_sd":["2","3","4"],"answer":1},
    {"ur":"زمین چیزوں کو کس قوت سے کھینچتی ہے؟","sd":"زمين شين کي ڪهڙي قوت سان ڇڪي ٿي؟","options_ur":["حرارت","کشش ثقل","روشنی"],"options_sd":["گرمي","ڪشش ثقل","روشني"],"answer":1},
    {"ur":"سب سے بڑا سیارہ کون سا ہے؟","sd":"سڀ کان وڏو سيارو ڪهڙو آهي؟","options_ur":["زمین","مشتری","مریخ"],"options_sd":["ڌرتي","مشتري","مريخ"],"answer":1},
    {"ur":"پھیپھڑے کس کام میں مدد دیتے ہیں؟","sd":"ڦڦڙ ڪهڙي ڪم ۾ مدد ڏين ٿا؟","options_ur":["سانس","ہضم","چلنا"],"options_sd":["ساهه کڻڻ","هضم","هلڻ"],"answer":0},
    {"ur":"پانی گرم ہونے پر کس میں تبدیل ہو سکتا ہے؟","sd":"پاڻي گرم ٿيڻ تي ڪنهن ۾ تبديل ٿي سگهي ٿو؟","options_ur":["برف","بھاپ","مٹی"],"options_sd":["برف","ٻاڦ","مٽي"],"answer":1},
    {"ur":"مقناطیس کس دھات کو کھینچتا ہے؟","sd":"مقناطيس ڪهڙي ڌاتو کي ڇڪي ٿو؟","options_ur":["لکڑی","لوہا","پلاسٹک"],"options_sd":["ڪاٺ","لوهه","پلاسٽڪ"],"answer":1},
    {"ur":"سورج کیا ہے؟","sd":"سج ڇا آهي؟","options_ur":["سیارہ","ستارہ","چاند"],"options_sd":["سيارو","تارو","چنڊ"],"answer":1},
    {"ur":"فوٹوسنتھیسز کے لیے پودوں کو کیا چاہیے؟","sd":"فوٽوسنٿيسس لاءِ ٻوٽن کي ڇا گهرجي؟","options_ur":["روشنی","پلاسٹک","ریت"],"options_sd":["روشني","پلاسٽڪ","ريت"],"answer":0},
    {"ur":"بارش کس قدرتی عمل کا حصہ ہے؟","sd":"مينهن ڪهڙي قدرتي عمل جو حصو آهي؟","options_ur":["پانی کا چکر","مقناطیس","کشش ثقل"],"options_sd":["پاڻي جو چڪر","مقناطيس","ڪشش ثقل"],"answer":0}
]

# ---------- LANGUAGE ----------
language = st.selectbox("🌐 Choose language / ٻولي چونڊيو", ["Urdu", "Sindhi"])
lang = "ur" if language == "Urdu" else "sd"
speech_language = "ur-PK" if lang == "ur" else "sd-PK"

# ---------- HERO ----------
st.markdown("""
<div class="hero">
  <h1>🔬 SCIENCE SMARTBOT</h1>
  <h3 style="color:#eafffa;margin:8px 0;">Explore • Learn • Discover</h3>
  <p>Class 6 | Urdu & Sindhi Science Learning</p>
  <p>خوش آمدید! سائنس سیکھیں، سوال پوچھیں اور کوئز کھیلیں۔</p>
</div>
""", unsafe_allow_html=True)

# ---------- NAVIGATION ----------
page = st.radio(
    "Choose a section",
    ["🏠 Home", "💬 Ask SmartBot", "📚 Topics", "🧠 Quiz", "ℹ️ About"],
    horizontal=True,
    label_visibility="collapsed"
)

if page == "🏠 Home":
    st.markdown('<div class="section-title">🌟 Welcome, Young Scientist!</div>', unsafe_allow_html=True)
    st.write("Explore science in your own language. Select a section above to start learning.")
    st.markdown("""
    <div class="topic-card">
      <div class="topic-icon">🔭 🧪 🌱 🪐</div>
      <div class="topic-name">A world of discovery is waiting!</div>
      <div class="topic-count">Ask questions • Explore topics • Test your knowledge</div>
    </div>
    """, unsafe_allow_html=True)
    st.subheader("🚀 Explore these science areas")
    cols = st.columns(5)
    for col, (name, info) in zip(cols, topics.items()):
        with col:
            st.markdown(f"""
            <div class="topic-card">
              <div class="topic-icon">{info['icon']}</div>
              <div class="topic-name">{name}</div>
            </div>
            """, unsafe_allow_html=True)
    st.info("Tip: Open *Ask SmartBot* to type a science question, or choose *Quiz* to test yourself.")

elif page == "💬 Ask SmartBot":
    st.markdown('<div class="section-title">💬 Ask Science SmartBot</div>', unsafe_allow_html=True)
    st.write("Type one of the science questions from the Topics section.")
    question = st.text_input("اپنا سوال لکھیں / پنهنجو سوال لکو", placeholder="مثلاً: پودے اپنی خوراک کیسے بناتے ہیں؟")
    if st.button("Ask SmartBot / سوال پوچھیں"):
        normalized = question.lower().strip()
        answer = None
        if normalized:
            for info in topics.values():
                for item in info["questions"]:
                    if normalized == item[lang].lower().strip() or any(k.lower() in normalized for k in item["keywords"]):
                        answer = item["a_" + lang]
                        break
                if answer:
                    break
        if answer:
            st.markdown(f'<div class="answer-box"><b>🤖 SmartBot:</b><br>{answer}</div>', unsafe_allow_html=True)
            answer_json = json.dumps(answer, ensure_ascii=False)
            html_code = """
            <button onclick="speakAnswer()" style="padding:12px 20px;border-radius:12px;background:#176B55;color:white;border:none;font-size:16px;cursor:pointer;">
            🔊 جواب سنیں / جواب ٻڌو
            </button>
            <script>
            const answerText = ANSWER_PLACEHOLDER;
            const speechLang = "LANG_PLACEHOLDER";
            function speakAnswer() {
              if (!("speechSynthesis" in window)) { alert("Speech is not supported in this browser."); return; }
              const speech = new SpeechSynthesisUtterance(answerText);
              speech.lang = speechLang; speech.rate = 0.85;
              window.speechSynthesis.cancel(); window.speechSynthesis.speak(speech);
            }
            </script>
            """
            html_code = html_code.replace("ANSWER_PLACEHOLDER", answer_json).replace("LANG_PLACEHOLDER", speech_language)
            components.html(html_code, height=65)
        elif normalized:
            st.warning("معذرت! یہ سوال ابھی میری معلومات میں موجود نہیں۔" if lang == "ur" else ".معاف ڪجو! هي سوال اڃا منهنجي ڄاڻ ۾ موجود ناهي")
        else:
            st.info("Please type a question first.")

elif page == "📚 Topics":
    st.markdown('<div class="section-title">📚 Explore Science Topics</div>', unsafe_allow_html=True)
    st.caption("Choose a topic to reveal its questions. Answers stay hidden in this library.")
    topic_names = list(topics.keys())
    cols = st.columns(2)
    for idx, name in enumerate(topic_names):
        with cols[idx % 2]:
            info = topics[name]
            st.markdown(f"""
            <div class="topic-card">
              <div class="topic-icon">{info['icon']}</div>
              <div class="topic-name">{name}</div>
              <div class="topic-count">{len(info['questions'])} questions</div>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("Explore Questions / سوال ڏسو"):
                for number, item in enumerate(info["questions"], 1):
                    st.write(f"*Q{number}. {item[lang]}*")

elif page == "🧠 Quiz":
    st.markdown('<div class="section-title">🧠 Science Challenge Quiz</div>', unsafe_allow_html=True)
    st.write("Answer 3 random questions and check your score.")
    if "quiz_round" not in st.session_state:
        st.session_state.quiz_round = 0
    if "quiz_set" not in st.session_state:
        st.session_state.quiz_set = random.sample(quiz_bank, 3)
    if st.button("🔄 New Quiz / نئون سوالنامو"):
        st.session_state.quiz_round += 1
        st.session_state.quiz_set = random.sample(quiz_bank, 3)
        st.session_state.pop("last_quiz_score", None)
        st.rerun()

    with st.form("science_quiz_form"):
        selected_answers = []
        for i, q in enumerate(st.session_state.quiz_set):
            st.markdown(f"*Q{i+1}. {q[lang]}*")
            options = q["options_ur"] if lang == "ur" else q["options_sd"]
            selected = st.radio("Choose your answer:", options, key=f"quiz_{st.session_state.quiz_round}_{i}")
            selected_answers.append(options.index(selected))
        submitted = st.form_submit_button("Submit Quiz / جواب جمع ڪريو")

    if submitted:
        score = sum(selected_answers[i] == q["answer"] for i, q in enumerate(st.session_state.quiz_set))
        st.session_state.last_quiz_score = score
        st.session_state.last_quiz_round = st.session_state.quiz_round

    if st.session_state.get("last_quiz_round") == st.session_state.quiz_round:
        score = st.session_state.last_quiz_score
        if score == 3:
            st.success(f"🏆 Excellent! Full marks: {score}/3")
        elif score == 2:
            st.success(f"👏 Very good! Your score: {score}/3")
        else:
            st.info(f"🌱 Good effort! Your score: {score}/3. Keep learning!")

elif page == "ℹ️ About":
    st.markdown('<div class="section-title">ℹ️ About Science SmartBot</div>', unsafe_allow_html=True)
    st.write("Science SmartBot is a bilingual learning assistant designed to help Class 6 students explore basic science concepts in Urdu and Sindhi.")
    st.markdown("""
    - 🔬 10 science topics
    - 💬 Typed question-and-answer chatbot
    - 🔊 Browser-based spoken answers
    - 🧠 Random three-question quiz
    - 🌐 Urdu and Sindhi language options
    """)
    st.caption("Made for learning, curiosity and school science exhibitions.")

st.divider()
st.markdown("<p style='text-align:center;color:#5d7d73;font-size:0.85rem;'>🔬 Science SmartBot | Learn Something New Every Day</p>", unsafe_allow_html=True)
