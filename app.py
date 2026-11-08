import streamlit as st
import json
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Science SmartBot",
    page_icon="🔬",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e8f5f0, #eaf1ff);
}

h1 {
    color: #12664f;
    text-align: center;
    font-weight: 800;
}

h3 {
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

.stTextInput input {
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

science_data = {
    "plants": {
        "keywords": ["plants", "photosynthesis", "پودے", "ٻوٽا"],
         "ur": "پودے سورج کی روشنی، پانی اور کاربن ڈائی آکسائیڈ سے اپنی خوراک بناتے ہیں۔",
        "sd": "ٻوٽا سج جي روشني، پاڻي ۽ ڪاربان ڊاءِ آڪسائيڊ سان پنهنجي خوراڪ ٺاهين ٿا۔"
    },
    "heart": {
        "keywords": ["heart", "دل"],
        "ur": "دل پورے جسم میں خون پمپ کرتا ہے۔",
        "sd": "دل سڄي جسم ۾ رت پمپ ڪري ٿو۔"
    },
    "water": {
        "keywords": ["water cycle", "پانی کا چکر", "پاڻي جو چڪر"],
        "ur": "پانی بخارات بنتا ہے، بادل بنتے ہیں اور بارش ہوتی ہے۔",
        "sd": "پاڻي ٻاڦ بڻجي ٿو، ڪڪر ٺهن ٿا ۽ مينهن وسي ٿو۔"
    },
    "gravity": {
        "keywords": ["gravity", "کشش ثقل"],
        "ur": "کشش ثقل چیزوں کو زمین کی طرف کھینچتی ہے۔",
        "sd": "ڪشش ثقل شين کي زمين ڏانهن ڇڪي ٿي۔"
    },
    "matter": {
        "keywords": ["matter", "مادہ", "مادو"],
        "ur": "مادہ وہ چیز ہے جس کا وزن ہو اور جو جگہ گھیرتی ہو۔",
        "sd": "مادو اها شيءِ آهي جنهن جو وزن هجي ۽ جيڪا جاءِ والاري۔"
    },
    "solar": {
        "keywords": ["solar system", "شمسی نظام", "شمسي نظام"],
        "ur": "شمسی نظام میں سورج اور اس کے گرد گردش کرنے والے سیارے شامل ہیں۔",
        "sd": "شمسي نظام ۾ سج ۽ ان جي چوڌاري گردش ڪندڙ سيارا شامل آهن۔"
    },
    "planets": {
        "keywords": ["planet", "planets", "سیارے", "سيارا"],
        "ur": "ہمارے نظامِ شمسی میں آٹھ سیارے ہیں۔",
        "sd": "اسان جي شمسي نظام ۾ اٺ سيارا آهن۔"
    },
    "evaporation": {
        "keywords": ["evaporation", "بخارات", "ٻاڦ"],
        "ur": "پانی گرم ہو کر بھاپ میں تبدیل ہوتا ہے۔",
        "sd": "پاڻي گرم ٿي ٻاڦ ۾ تبديل ٿئي ٿو۔"
    },
    "lungs": {
        "keywords": ["lungs", "پھیپھڑے", "ڦڦڙ"],
        "ur": "پھیپھڑے سانس لینے میں مدد دیتے ہیں۔",
        "sd": "ڦڦڙ ساهه کڻڻ ۾ مدد ڏين ٿا۔"
    },
    "magnet": {
        "keywords": ["magnet", "مقناطیس"],
        "ur": "مقناطیس لوہے جیسی بعض دھاتوں کو اپنی طرف کھینچتا ہے۔",
        "sd": "مقناطيس لوهه جهڙين ڪجهه ڌاتن کي پاڻ ڏانهن ڇڪي ٿو۔"
    }
}

st.markdown("""
# 🔬 Science SmartBot
### Class 6 | Urdu & Sindhi
Learn Science • Ask Questions • Take Quiz
""")

language = st.selectbox(
    "Choose your language / ٻولي چونڊيو",
    ["Urdu", "Sindhi"]
)

lang = "ur" if language == "Urdu" else "sd"
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e8f5f0, #eaf1ff);
}

h1 {
    color: #12664f;
    text-align: center;
    font-weight: 800;
}

h3 {
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

.stTextInput input {
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.header("📚 Science Question Library")

topic_questions = {
    "Plants": {
        "ur": [
            "پودے اپنی خوراک کیسے بناتے ہیں؟",
            "فوٹوسنتھیسز کیا ہے؟",
            "پودوں کو سورج کی روشنی کیوں چاہیے؟"
        ],
        "sd": [
            "ٻوٽا پنهنجي خوراڪ ڪيئن ٺاهين ٿا؟",
            "فوٽوسنٿيسس ڇا آهي؟",
            "ٻوٽن کي سج جي روشني ڇو گهرجي؟"
        ]
    },
    "Heart": {
        "ur": ["دل کیا کام کرتا ہے؟", "دل خون کہاں پمپ کرتا ہے؟"],
        "sd": ["دل ڇا ڪم ڪري ٿو؟", "دل رت ڪٿي پمپ ڪري ٿو؟"]
    },
    "Water Cycle": {
        "ur": ["پانی کا چکر کیا ہے؟", "بارش کیسے ہوتی ہے؟"],
        "sd": ["پاڻي جو چڪر ڇا آهي؟", "مينهن ڪيئن وسي ٿو؟"]
    },
    "Gravity": {
        "ur": ["کشش ثقل کیا ہے؟", "چیزیں زمین پر کیوں گرتی ہیں؟"],
        "sd": ["ڪشش ثقل ڇا آهي؟", "شيون زمين تي ڇو ڪرن ٿيون؟"]
    },
    "Matter": {
        "ur": ["مادہ کیا ہے؟", "مادے کی تین حالتیں کون سی ہیں؟"],
        "sd": ["مادو ڇا آهي؟", "مادي جون ٽي حالتون ڪهڙيون آهن؟"]
    },
    "Solar System": {
        "ur": ["شمسی نظام کیا ہے؟", "سورج کیا ہے؟"],
        "sd": ["شمسي نظام ڇا آهي؟", "سج ڇا آهي؟"]
    },
    "Planets": {
        "ur": ["ہمارے نظام شمسی میں کتنے سیارے ہیں؟", "سب سے بڑا سیارہ کون سا ہے؟"],
        "sd": ["اسان جي شمسي نظام ۾ ڪيترا سيارا آهن؟", "سڀ کان وڏو سيارو ڪهڙو آهي؟"]
    },
    "Evaporation": {
        "ur": ["تبخیر کیا ہے؟", "پانی بھاپ میں کیسے بدلتا ہے؟"],
        "sd": ["تبخير ڇا آهي؟", "پاڻي ٻاڦ ۾ ڪيئن بدلجي ٿو؟"]
    },
    "Lungs": {
        "ur": ["پھیپھڑوں کا کیا کام ہے؟", "ہم سانس کیوں لیتے ہیں؟"],
        "sd": ["ڦڦڙن جو ڪهڙو ڪم آهي؟", "اسان ساهه ڇو کڻون ٿا؟"]
    },
    "Magnet": {
        "ur": ["مقناطیس کیا ہے؟", "مقناطیس کن چیزوں کو کھینچتا ہے؟"],
        "sd": ["مقناطيس ڇا آهي؟", "مقناطيس ڪهڙين شين کي ڇڪي ٿو؟"]
    }
}

for topic, data in topic_questions.items():
    with st.expander("🔬 " + topic):
        for i, q in enumerate(data[lang], 1):
            st.write(f"*Q{i}. {q}*")
st.subheader("💬 Ask Science SmartBot")

question = st.text_input("Type your science question:")

if st.button("Ask SmartBot"):
    answer = None

    for topic in science_data.values():
        if any(
            k.lower() in question.lower()
            for k in topic["keywords"]
        ):
            answer = topic[lang]
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
        )
        html_code = html_code.replace(
            "LANG_PLACEHOLDER", speech_language
        )

        components.html(html_code, height=65)

    else:
        st.info(
            "معذرت! یہ سوال میری معلومات میں موجود نہیں۔"
            if lang == "ur"
            else "معاف ڪجو! اهو سوال منهنجي ڄاڻ ۾ موجود ناهي۔"
        )

st.divider()
st.subheader("🧠 Science Quiz")

questions = [
    {
        "ur": "پودے اپنی خوراک بنانے کے لیے کس کی روشنی استعمال کرتے ہیں؟",
        "sd": "ٻوٽا خوراڪ ٺاهڻ لاءِ ڪنهن جي روشني استعمال ڪن ٿا؟",
        "options": ["چاند", "سورج", "ستارے"],
        "answer": 1
    },
    {
        "ur": "خون پورے جسم میں کون پمپ کرتا ہے؟",
        "sd": "رت سڄي جسم ۾ ڪير پمپ ڪري ٿو؟",
        "options": ["دل", "پھیپھڑے", "معدہ"],
        "answer": 0
    },
    {
        "ur": "نظامِ شمسی میں کتنے سیارے ہیں؟",
        "sd": "شمسي نظام ۾ ڪيترا سيارا آهن؟",
        "options": ["7", "8", "9"],
        "answer": 1
    }
]

answers = []

for i, q in enumerate(questions):
    st.write(f"*Q{i+1}. {q[lang]}*")

    option = st.radio(
        "Choose your answer:",
        q["options"],
        key=f"quiz_{i}"
    )

    answers.append(q["options"].index(option))

if st.button("Submit Quiz"):
    score = sum(
        answers[i] == q["answer"]
        for i, q in enumerate(questions)
    )

    st.success(f"Your score: {score}/3")
