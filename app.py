import streamlit as st

st.set_page_config(
    page_title="Science SmartBot",
    page_icon="🔬",
    layout="centered"
)

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
*Learn Science • Ask Questions • Take Quiz*
""")

language = st.selectbox(
    "Choose your language / ٻولي چونڊيو",
    ["Urdu", "Sindhi"]
)

lang = "ur" if language == "Urdu" else "sd"

st.divider()
st.subheader("💬 Ask Science SmartBot")

question = st.text_input("Type your science question:")

if st.button("Ask SmartBot"):
    answer = None
    for topic in science_data.values():
        if any(k.lower() in question.lower()
               for k in topic["keywords"]):
            answer = topic[lang]
            break

    if answer:
        st.success(answer)
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
