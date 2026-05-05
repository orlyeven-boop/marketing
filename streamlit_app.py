import streamlit as st
from datetime import datetime

# הגדרות כותרת
st.title("📚 מנהל התוכן: האמת שהסתרתי")
st.subheader("התכנית השיווקית של אורלי גולדשטיין")

# לוח הזמנים המתוכנן
schedule = {
    "Sunday": {"type": "הומור / מאחורי הקלעים", "content": "פוסט הומור: 'הפרצוף שלי כשמישהו אומר שאין לו זמן לקרוא'"},
    "Tuesday": {"type": "הכר את הדמות", "content": "הכירו את יובל עדן: סופר מצליח עם סוד גדול"},
    "Thursday": {"type": "מסר או ציטוט", "content": "ציטוט: 'יש אמיתות שמסתירים מאהבה'"}
}

# בדיקת היום הנוכחי
today = datetime.now().strftime("%A")
date_display = datetime.now().strftime("%d/%m/%Y")

st.info(f"היום: {today}, {date_display}")

if today in schedule:
    st.success(f"🚀 **היום מעלים פוסט!**")
    st.write(f"**סוג הפוסט:** {schedule[today]['type']}")
    st.write(f"**התוכן המוצע:** {schedule[today]['content']}")
    if st.button("העתק תוכן לפוסט"):
        st.write("התוכן הועתק! (דמיוני, פשוט סמני והעתיקי)")
else:
    st.warning("היום אין פוסט מתוכנן. זמן מצוין לענות לתגובות!")

# תצוגת הגאנט המלאה
with st.expander("צפי בלוח החודשי המלא"):
    st.table([
        {"יום": "ראשון", "נושא": "הומור", "תיאור": "מאחורי הקלעים וצחוק"},
        {"יום": "שלישי", "נושא": "דמויות", "תיאור": "יובל, אולגה ושירלי"},
        {"יום": "חמישי", "נושא": "מסר", "תיאור": "ציטוטים מרגשים"}
    ])
