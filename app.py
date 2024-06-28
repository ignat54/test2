import streamlit as st

def calculate_risk(form_data):
    total_score = sum(form_data.values())

    if total_score <= 3:
        risk_level = "Низкий риск ССЗ"
    elif total_score <= 9:
        risk_level = "Средний риск ССЗ"
    else:
        risk_level = "Высокий риск ССЗ"

    return total_score, risk_level

st.title("Тест для выявления риска развития ССЗ")

form_data = {}

form_data['gender'] = st.radio("1) Пол:", [("", -1), ("Мужчина", 1), ("Женщина", 0)], format_func=lambda x: x[0], index=0)[1]
form_data['age'] = st.radio("2) Возраст:", [("", -1), ("Больше 40 лет", 1), ("Меньше 40 лет", 0)], format_func=lambda x: x[0], index=0)[1]
form_data['smoking'] = st.radio("3) Курение:", [("", -1), ("Да", 1), ("Нет", 0)], format_func=lambda x: x[0], index=0)[1]
form_data['waist'] = st.radio("4) Ваш обхват талии в норме? (Для мужчин < 94, для женщин < 80):", [("", -1), ("Да", 0), ("Нет", 1)], format_func=lambda x: x[0], index=0)[1]
form_data['familyHistory'] = st.radio("5) Имеются ли ССЗ у ближайших родственников:", [("", -1), ("Да", 1), ("Нет", 0)], format_func=lambda x: x[0], index=0)[1]
form_data['cholesterol'] = st.radio("6) Уровень холестерина:", [("", -1), ("Менее 3,0", 0), ("3,0-3,9", 1), ("4,0-4,9", 2), ("5,0-5,9", 3), ("6,0-6,9", 4), ("Неизвестно", 1)], format_func=lambda x: x[0], index=0)[1]
form_data['bloodPressure'] = st.radio("7) Систолическое артериальное давление (верхнее):", [("", -1), ("Менее 140", 0), ("140-159", 1), ("Более 160", 2), ("Неизвестно", 1)], format_func=lambda x: x[0], index=0)[1]
form_data['chestPain'] = st.radio("8) Бывают ли у вас боли в груди, возникающие после стресса или повышенной физической активности:", [("", -1), ("Да", 1), ("Нет", 0)], format_func=lambda x: x[0], index=0)[1]
form_data['palpitations'] = st.radio("9) Бывают ли у вас приступы учащенного сердцебиения, возникающие без причины:", [("", -1), ("Да", 1), ("Нет", 0)], format_func=lambda x: x[0], index=0)[1]
form_data['physicalActivity'] = st.radio("10) Занимаетесь ли вы физической активностью:", [("", -1), ("Да", 0), ("Нет", 1)], format_func=lambda x: x[0], index=0)[1]

if st.button("Рассчитать риск"):
    if -1 in form_data.values():
        st.write("Пожалуйста, заполните все поля.")
    else:
        total_score, risk_level = calculate_risk(form_data)
        st.write(f"Ваш общий риск: {total_score} баллов. {risk_level}")
        if total_score <= 3:
            st.write("Продолжайте вести здоровый образ жизни!")
        elif total_score <= 9:
            st.write("Вам стоит пересмотреть свой образ жизни и обратиться за консультацией к врачу-терапевту.")
        else:
            st.write("Вам следует как можно скорее обратиться за консультацией к врачу-терапевту!")