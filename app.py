import streamlit as st
import random
import json
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Science SmartBot",
    page_icon="🔬",
    layout="centered"
)
st.markdown("""
<div style="
    background: linear-gradient(135deg, #063970, #11998e);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
">
    <h1>🔬 SCIENCE SMARTBOT</h1>
    <h3>Explore • Learn • Discover</h3>
    <p>Welcome to the World of Science!</p>
    <p>اردو اور سنڌي ۾ سائنس سکڻ جو دلچسپ طريقو</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.info("🌟 Welcome Young Scientists! Let's discover something amazing today.")

# DESIGN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#e8f5f0,#eaf1ff);
}
h1 {
    color: #12664f;
    text-align: center;
    font-weight: 800;
}
h2, h3 {
    color: #176b55;
}
.stButton > button {
    background: #176b55;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 22px;
    font-weight: bold;
}
.stButton > button:hover {
    background: #104c3d;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# SCIENCE QUESTION AND ANSWER DATABASE

topics = {
    "Plants": [
        {
            "ur": "پودے اپنی خوراک کیسے بناتے ہیں؟",
            "sd": "ٻوٽا پنهنجي خوراڪ ڪيئن ٺاهين ٿا؟",
            "keywords": ["پودے اپنی خوراک", "photosynthesis",
                         "ٻوٽا پنهنجي خوراڪ", "فوٹوسنتھیسز"],
            "a_ur": "پودے سورج کی روشنی، پانی اور کاربن ڈائی آکسائیڈ سے اپنی خوراک بناتے ہیں۔ اس عمل کو فوٹوسنتھیسز کہتے ہیں۔",
            "a_sd": "ٻوٽا سج جي روشني، پاڻي ۽ ڪاربان ڊاءِ آڪسائيڊ سان پنهنجي خوراڪ ٺاهين ٿا۔ هن عمل کي فوٽوسنٿيسس چئبو آهي۔"
        },
        {
            "ur": "پودوں کو سورج کی روشنی کیوں چاہیے؟",
            "sd": "ٻوٽن کي سج جي روشني ڇو گهرجي؟",
            "keywords": ["سورج کی روشنی", "سج جي روشني"],
            "a_ur": "پودوں کو خوراک بنانے کے لیے سورج کی روشنی کی ضرورت ہوتی ہے۔",
            "a_sd": "ٻوٽن کي خوراڪ ٺاهڻ لاءِ سج جي روشني جي ضرورت هوندي آهي۔"
        }
    ],

    "Heart": [
        {
            "ur": "دل کیا کام کرتا ہے؟",
            "sd": "دل ڇا ڪم ڪري ٿو؟",
            "keywords": ["دل کیا کام", "دل ڇا ڪم", "heart"],
            "a_ur": "دل خون کو پورے جسم میں پمپ کرتا ہے۔",
            "a_sd": "دل رت کي سڄي جسم ۾ پمپ ڪري ٿو۔"
        },
        {
            "ur": "دل کس نظام کا حصہ ہے؟",
            "sd": "دل ڪهڙي نظام جو حصو آهي؟",
            "keywords": ["دل کس نظام", "دل ڪهڙي نظام"],
            "a_ur": "دل نظام دورانِ خون کا حصہ ہے۔",
            "a_sd": "دل رت جي گردش واري نظام جو حصو آهي۔"
        }
    ],

    "Water Cycle": [
        {
            "ur": "پانی کا چکر کیا ہے؟",
            "sd": "پاڻي جو چڪر ڇا آهي؟",
            "keywords": ["پانی کا چکر", "پاڻي جو چڪر", "water cycle"],
            "a_ur": "پانی کے بخارات بننے، بادل بننے اور بارش ہونے کے مسلسل عمل کو پانی کا چکر کہتے ہیں۔",
            "a_sd": "پاڻي جي ٻاڦ ٿيڻ، ڪڪر ٺهڻ ۽ مينهن وسڻ جي مسلسل عمل کي پاڻي جو چڪر چئبو آهي۔"
        },
        {
            "ur": "بارش کیسے ہوتی ہے؟",
            "sd": "مينهن ڪيئن وسي ٿو؟",
            "keywords": ["بارش کیسے", "مينهن ڪيئن"],
            "a_ur": "بادلوں میں پانی کے قطرے جمع ہو کر بھاری ہوتے ہیں اور زمین پر بارش کی صورت میں گرتے ہیں۔",
            "a_sd": "ڪڪرن ۾ پاڻي جا ڦڙا گڏ ٿي ڳرا ٿين ٿا ۽ مينهن جي صورت ۾ وسن ٿا۔"
        }
    ],

    "Gravity": [
        {
            "ur": "کشش ثقل کیا ہے؟",
            "sd": "ڪشش ثقل ڇا آهي؟",
            "keywords": ["کشش ثقل کیا", "ڪشش ثقل ڇا", "gravity"],
            "a_ur": "کشش ثقل ایک قوت ہے جو چیزوں کو ایک دوسرے کی طرف کھینچتی ہے۔",
            "a_sd": "ڪشش ثقل هڪ قوت آهي جيڪا شين کي هڪ ٻئي ڏانهن ڇڪي ٿي۔"
        },
        {
            "ur": "چیزیں زمین پر کیوں گرتی ہیں؟",
            "sd": "شيون زمين تي ڇو ڪرن ٿيون؟",
            "keywords": ["زمین پر کیوں", "زمين تي ڇو"],
            "a_ur": "زمین کی کشش ثقل چیزوں کو اپنی طرف کھینچتی ہے۔",
            "a_sd": "زمين جي ڪشش ثقل شين کي پاڻ ڏانهن ڇڪي ٿي۔"
        }
    ],

    "Matter": [
        {
            "ur": "مادہ کیا ہے؟",
            "sd": "مادو ڇا آهي؟",
            "keywords": ["مادہ کیا", "مادو ڇا", "matter"],
            "a_ur": "مادہ وہ چیز ہے جس کی کمیت ہو اور جو جگہ گھیرتی ہو۔",
            "a_sd": "مادو اها شيءِ آهي جنهن جي ڪميت هجي ۽ جيڪا جاءِ والاري۔"
        },
        {
            "ur": "مادے کی تین حالتیں کون سی ہیں؟",
            "sd": "مادي جون ٽي حالتون ڪهڙيون آهن؟",
            "keywords": ["مادے کی تین", "مادي جون ٽي"],
            "a_ur": "مادے کی تین بنیادی حالتیں ٹھوس، مائع اور گیس ہیں۔",
            "a_sd": "مادي جون ٽي بنيادي حالتون ٺوس، پاڻياٺ ۽ گئس آهن۔"
        }
    ],

    "Solar System": [
        {
            "ur": "شمسی نظام کیا ہے؟",
            "sd": "شمسي نظام ڇا آهي؟",
            "keywords": ["شمسی نظام کیا", "شمسي نظام ڇا", "solar system"],
            "a_ur": "شمسی نظام میں سورج اور اس کے گرد گردش کرنے والے سیارے اور دیگر اجسام شامل ہیں۔",
            "a_sd": "شمسي نظام ۾ سج ۽ ان جي چوڌاري گردش ڪندڙ سيارا ۽ ٻيا جسم شامل آهن۔"
        },
        {
            "ur": "سورج کیا ہے؟",
            "sd": "سج ڇا آهي؟",
            "keywords": ["سورج کیا", "سج ڇا"],
            "a_ur": "سورج ایک ستارہ ہے جو ہمیں روشنی اور حرارت دیتا ہے۔",
            "a_sd": "سج هڪ تارو آهي جيڪو اسان کي روشني ۽ گرمي ڏئي ٿو۔"
        }
    ],

    "Planets": [
        {
            "ur": "نظام شمسی میں کتنے سیارے ہیں؟",
            "sd": "شمسي نظام ۾ ڪيترا سيارا آهن؟",
            "keywords": ["کتنے سیارے", "ڪيترا سيارا", "how many planets"],
            "a_ur": "ہمارے نظام شمسی میں آٹھ سیارے ہیں۔",
            "a_sd": "اسان جي شمسي نظام ۾ اٺ سيارا آهن۔"
        },
        {
            "ur": "سب سے بڑا سیارہ کون سا ہے؟",
            "sd": "سڀ کان وڏو سيارو ڪهڙو آهي؟",
            "keywords": ["سب سے بڑا سیارہ", "سڀ کان وڏو سيارو"],
            "a_ur": "مشتری نظام شمسی کا سب سے بڑا سیارہ ہے۔",
            "a_sd": "مشتري شمسي نظام جو سڀ کان وڏو سيارو آهي۔"
        }
    ],

    "Evaporation": [
        {
            "ur": "تبخیر کیا ہے؟",
            "sd": "تبخير ڇا آهي؟",
            "keywords": ["تبخیر کیا", "تبخير ڇا", "evaporation"],
            "a_ur": "مائع کا حرارت حاصل کرکے بخارات میں تبدیل ہونا تبخیر کہلاتا ہے۔",
            "a_sd": "پاڻياٺ جو گرمي حاصل ڪري ٻاڦ ۾ تبديل ٿيڻ تبخير چئبو آهي۔"
        },
        {
            "ur": "پانی بھاپ میں کیسے بدلتا ہے؟",
            "sd": "پاڻي ٻاڦ ۾ ڪيئن بدلجي ٿو؟",
            "keywords": ["بھاپ میں کیسے", "ٻاڦ ۾ ڪيئن"],
            "a_ur": "جب پانی حرارت حاصل کرتا ہے تو اس کے ذرات تیزی سے حرکت کرتے ہیں اور پانی بخارات بن جاتا ہے۔",
            "a_sd": "جڏهن پاڻي گرمي حاصل ڪري ٿو ته ان جا ذرڙا تيزيءَ سان حرڪت ڪن ٿا ۽ پاڻي ٻاڦ بڻجي ٿو۔"
        }
    ],

    "Lungs": [
        {
            "ur": "پھیپھڑوں کا کیا کام ہے؟",
            "sd": "ڦڦڙن جو ڪهڙو ڪم آهي؟",
            "keywords": ["پھیپھڑوں کا", "ڦڦڙن جو", "lungs"],
            "a_ur": "پھیپھڑے سانس لینے میں مدد دیتے ہیں اور خون میں آکسیجن پہنچانے کے عمل میں حصہ لیتے ہیں۔",
            "a_sd": "ڦڦڙ ساهه کڻڻ ۾ مدد ڪن ٿا ۽ رت ۾ آڪسيجن پهچائڻ واري عمل ۾ حصو وٺن ٿا۔"
        },
        {
            "ur": "ہم سانس کیوں لیتے ہیں؟",
            "sd": "اسان ساهه ڇو کڻون ٿا؟",
            "keywords": ["سانس کیوں", "ساهه ڇو"],
            "a_ur": "ہم جسم کو آکسیجن فراہم کرنے اور کاربن ڈائی آکسائیڈ خارج کرنے کے لیے سانس لیتے ہیں۔",
            "a_sd": "اسان جسم کي آڪسيجن ڏيڻ ۽ ڪاربان ڊاءِ آڪسائيڊ خارج ڪرڻ لاءِ ساهه کڻون ٿا۔"
        }
    ],

    "Magnet": [
        {
            "ur": "مقناطیس کیا ہے؟",
            "sd": "مقناطيس ڇا آهي؟",
            "keywords": ["مقناطیس کیا", "مقناطيس ڇا", "magnet"],
            "a_ur": "مقناطیس ایک ایسی چیز ہے جو لوہے جیسی بعض دھاتوں کو اپنی طرف کھینچتی ہے۔",
            "a_sd": "مقناطيس اهڙي شيءِ آهي جيڪا لوهه جهڙين ڪجهه ڌاتن کي پاڻ ڏانهن ڇڪي ٿي۔"
        },
        {
            "ur": "مقناطیس کن چیزوں کو کھینچتا ہے؟",
            "sd": "مقناطيس ڪهڙين شين کي ڇڪي ٿو؟",
            "keywords": ["کن چیزوں کو", "ڪهڙين شين کي"],
            "a_ur": "مقناطیس لوہے، نکل اور کوبالٹ جیسی بعض دھاتوں کو کھینچتا ہے۔",
            "a_sd": "مقناطيس لوهه، نڪل ۽ ڪوبالٽ جهڙين ڪجهه ڌاتن کي ڇڪي ٿو۔"
        }
    ]
}


# APP TITLE

st.markdown("""
# 🔬 Science SmartBot
### Class 6 | Urdu & Sindhi
📚 Learn Science • Ask Questions • Take Quiz
""")

language = st.selectbox(
    "Choose your language / ٻولي چونڊيو",
    ["Urdu", "Sindhi"]
)

lang = "ur" if language == "Urdu" else "sd"


# SCIENCE TOPIC CARDS

st.divider()
st.header("📚 Explore Science Topics")
st.caption("Choose a topic and discover interesting science questions!")

topic_design = {
    "Plants": "🌱",
    "Heart": "❤️",
    "Water Cycle": "💧",
    "Gravity": "🌍",
    "Matter": "🧪",
    "Solar System": "☀️",
    "Planets": "🪐",
    "Evaporation": "💨",
    "Lungs": "🫁",
    "Magnet": "🧲"
}

topic_colors = [
    "#E8F5E9", "#FCE4EC", "#E3F2FD",
    "#FFF3E0", "#F3E5F5"
]

topic_list = list(topics.items())

for row in range(0, len(topic_list), 2):
    cols = st.columns(2)

    for col, (topic_name, items) in zip(
        cols, topic_list[row:row+2]
    ):
        with col:
            emoji = topic_design.get(topic_name, "🔬")

            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #E3F2FD, #E8F5E9);
                padding: 18px;
                border-radius: 15px;
                text-align: center;
                border: 2px solid #11998e;
                margin-bottom: 10px;
            ">
                <h1>{emoji}</h1>
                <h3>{topic_name}</h3>
                <p>{len(items)} Interesting Questions</p>
            </div>
            """, unsafe_allow_html=True)

            with st.expander("Explore Questions"):
                for i, item in enumerate(items, 1):
                    st.write(f"*Q{i}. {item[lang]}*")

# SMARTBOT STATISTICS DASHBOARD

total_topics = len(topics)
total_questions = sum(len(items) for items in topics.values())

st.divider()
st.subheader("📊 Science SmartBot Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Topics", total_topics)

with col2:
    st.metric("❓ Questions", total_questions)

with col3:
    st.metric("🌐 Languages", 2)

with col4:
    st.metric("🎯 Quiz Questions", len(quiz_bank))
    
# ASK SMARTBOT

st.divider()
st.header("💬 Ask Science SmartBot")

question = st.text_input(
    "اپنا سوال لکھیں / پنهنجو سوال لکو"
)

if st.button("Ask SmartBot"):
    answer = None
    user_question = question.lower().strip()

    for items in topics.values():
        for item in items:
            if any(k.lower() in user_question for k in item["keywords"]):
                answer = item["a_" + lang]
                break
        if answer:
            break

    if answer:
        st.success(answer)

        speech_language = "ur-PK" if lang == "ur" else "sd-PK"
        answer_json = json.dumps(answer, ensure_ascii=False)

        html_code = """
        <button onclick="speakAnswer()"
        style="padding:12px 22px;border-radius:12px;
        background:#176B55;color:white;border:none;
        font-size:17px;">
        🔊 جواب سنیں / جواب ٻڌو
        </button>

        <script>
        const answerText = ANSWER_PLACEHOLDER;
        const speechLang = "LANG_PLACEHOLDER";

        function speakAnswer() {
            const speech = new SpeechSynthesisUtterance(answerText);
            speech.lang = speechLang;
            speech.rate = 0.85;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(speech);
        }
        </script>
        """

        html_code = html_code.replace(
            "ANSWER_PLACEHOLDER", answer_json
        ).replace(
            "LANG_PLACEHOLDER", speech_language
        )

        components.html(html_code, height=65)

    elif question.strip():
        st.info(
            "معذرت! یہ سوال میری معلومات میں موجود نہیں۔"
            if lang == "ur"
            else "معاف ڪجو! اهو سوال منهنجي ڄاڻ ۾ موجود ناهي۔"
        )


# RANDOM QUIZ BANK

quiz_bank = [
    {
        "ur": "پودے اپنی خوراک بنانے کے لیے کس کی روشنی استعمال کرتے ہیں؟",
        "sd": "ٻوٽا خوراڪ ٺاهڻ لاءِ ڪنهن جي روشني استعمال ڪن ٿا؟",
        "options_ur": ["چاند", "سورج", "ستارے"],
        "options_sd": ["چنڊ", "سج", "تارا"],
        "answer": 1
    },
    {
        "ur": "خون پورے جسم میں کون پمپ کرتا ہے؟",
        "sd": "رت سڄي جسم ۾ ڪير پمپ ڪري ٿو؟",
        "options_ur": ["دل", "پھیپھڑے", "معدہ"],
        "options_sd": ["دل", "ڦڦڙ", "معدو"],
        "answer": 0
    },
    {
        "ur": "نظام شمسی میں کتنے سیارے ہیں؟",
        "sd": "شمسي نظام ۾ ڪيترا سيارا آهن؟",
        "options_ur": ["7", "8", "9"],
        "options_sd": ["7", "8", "9"],
        "answer": 1
    },
    {
        "ur": "مادے کی بنیادی حالتیں کتنی ہیں؟",
        "sd": "مادي جون بنيادي حالتون ڪيتريون آهن؟",
        "options_ur": ["2", "3", "4"],
        "options_sd": ["2", "3", "4"],
        "answer": 1
    },
    {
        "ur": "زمین چیزوں کو کس قوت سے کھینچتی ہے؟",
        "sd": "زمين شين کي ڪهڙي قوت سان ڇڪي ٿي؟",
        "options_ur": ["حرارت", "کشش ثقل", "روشنی"],
        "options_sd": ["گرمي", "ڪشش ثقل", "روشني"],
        "answer": 1
    },
    {
        "ur": "سب سے بڑا سیارہ کون سا ہے؟",
        "sd": "سڀ کان وڏو سيارو ڪهڙو آهي؟",
        "options_ur": ["زمین", "مشتری", "مریخ"],
        "options_sd": ["ڌرتي", "مشتري", "مريخ"],
        "answer": 1
    },
    {
        "ur": "پھیپھڑے کس کام میں مدد دیتے ہیں؟",
        "sd": "ڦڦڙ ڪهڙي ڪم ۾ مدد ڪن ٿا؟",
        "options_ur": ["سانس", "ہضم", "چلنا"],
        "options_sd": ["ساهه کڻڻ", "هضم", "هلڻ"],
        "answer": 0
    },
    {
        "ur": "پانی گرم ہونے پر کس میں تبدیل ہوتا ہے؟",
        "sd": "پاڻي گرم ٿيڻ تي ڪنهن ۾ تبديل ٿئي ٿو؟",
        "options_ur": ["برف", "بھاپ", "مٹی"],
        "options_sd": ["برف", "ٻاڦ", "مٽي"],
        "answer": 1
    },
    {
        "ur": "مقناطیس کس دھات کو کھینچتا ہے؟",
        "sd": "مقناطيس ڪهڙي ڌاتو کي ڇڪي ٿو؟",
        "options_ur": ["لکڑی", "لوہا", "پلاسٹک"],
        "options_sd": ["ڪاٺ", "لوهه", "پلاسٽڪ"],
        "answer": 1
    },
    {
        "ur": "سورج کیا ہے؟",
        "sd": "سج ڇا آهي؟",
        "options_ur": ["سیارہ", "ستارہ", "چاند"],
        "options_sd": ["سيارو", "تارو", "چنڊ"],
        "answer": 1
    },
    {
        "ur": "فوٹوسنتھیسز کے لیے پودوں کو کیا چاہیے؟",
        "sd": "فوٽوسنٿيسس لاءِ ٻوٽن کي ڇا گهرجي؟",
        "options_ur": ["روشنی", "پلاسٹک", "ریت"],
        "options_sd": ["روشني", "پلاسٽڪ", "ريت"],
        "answer": 0
    },
    {
        "ur": "بارش کس قدرتی عمل کا حصہ ہے؟",
        "sd": "مينهن ڪهڙي قدرتي عمل جو حصو آهي؟",
        "options_ur": ["پانی کا چکر", "مقناطیس", "کشش ثقل"],
        "options_sd": ["پاڻي جو چڪر", "مقناطيس", "ڪشش ثقل"],
        "answer": 0
    }
]


# QUIZ - RANDOM QUESTIONS

st.divider()
st.header("🧠 Science Quiz")

if "quiz_round" not in st.session_state:
    st.session_state.quiz_round = 0

if "quiz_set" not in st.session_state:
    st.session_state.quiz_set = random.sample(quiz_bank, 3)

if st.button("🔄 New Quiz / نئون سوالنامو"):
    st.session_state.quiz_round += 1
    st.session_state.quiz_set = random.sample(quiz_bank, 3)
    st.rerun()

with st.form("science_quiz_form"):

    selected_answers = []

    for i, q in enumerate(st.session_state.quiz_set):
        st.write(f"*Q{i+1}. {q[lang]}*")

        options = q["options_ur"] if lang == "ur" else q["options_sd"]

        selected = st.radio(
            "Choose your answer:",
            options,
            key=f"quiz_{st.session_state.quiz_round}_{i}"
        )

        selected_answers.append(options.index(selected))

    submitted = st.form_submit_button("Submit Quiz")

if submitted:
    score = sum(
        selected_answers[i] == q["answer"]
        for i, q in enumerate(st.session_state.quiz_set)
    )

    st.success(f"🎉 Your Score: {score}/3")
