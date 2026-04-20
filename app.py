# app.py - твой тест по анатомии для публикации в интернете
import streamlit as st
from PIL import Image

# --- НАСТРОЙКИ СТРАНИЦЫ (должны быть самой первой командой Streamlit) ---
st.set_page_config(
    page_title="Тест по анатомии",  # Название вкладки в браузере
    page_icon="🧠",                 # Иконка вкладки
    layout="centered"              # Центрируем содержимое
)

# --- ВОПРОСЫ ТЕСТА ---
# (Твои вопросы, картинки должны лежать в той же папке, что и app.py)
questions = [
    {
        "question": "Какие системы изображены?",
        "options": ["Артерии, Вены, Лимфа", "Органы, Нервы", "Протоки, Вены, Лимфа", "Артерии, Вены, Нервы"],
        "correct": 0,
        "image": "v1.jpg"
    },
    {
        "question": "Какая кость выделена?",
        "options": ["Лучевая кость", "Логтевая кость", "Плечевая кость", "Бедреная кость"],
        "correct": 2,
        "image": "v2.jpg"
    },
    {
        "question": "Какая системаорганов изображена?",
        "options": ["Половая", "Дыхательная", "Пищеварительная", "Нервная"],
        "correct": 2,
        "image": "v3.jpg"
    },
    {
        "question": "Что выделено на изображении?",
        "options": ["Селезная железа", "Око", "Ухо", "Зрачек"],
        "correct": 0,
        "image": "v4.jpg"
    },
    {
        "question": "Какая артерия выделена?",
        "options": ["Подключичная артерия", "Общая сонная артерия", "Бедренная артерия", "Подмышечная артерия"],
        "correct": 1,
        "image": "v5.jpg"
    },
    {
        "question": "Какая кость выделена?",
        "options": ["Лобная", "Нижнечелюстная", "Височная", "Теменная"],
        "correct": 3,
        "image": "v6.jpg"
    },
    {
        "question": "Как называется выделенная мышца?",
        "options": ["Малая грудная", "Поперечная", "Большая грудная", "Подключичная"],
        "correct": 2,
        "image": "v7.jpg"
    },
    {
        "question": "Как называется выделенный элемент?",
        "options": ["Женские клетки", "Матка", "Яичник", "Подматочник"],
        "correct": 2,
        "image": "v8.jpg"
    },
    {
        "question": "Проекция чего изображена?",
        "options": ["Головной мозг", "Гортань", "Глазые орбитры", "Височная кость"],
        "correct": 0,
        "image": "v9.jpg"
    },
    {
        "question": "Какой уровень мышц на изображении?",
        "options": ["Головные", "Подножные", "Внешние", "Внутренние"],
        "correct": 3,
        "image": "v10.jpg"
    }
]

# --- ЛОГИКА ТЕСТА (работа с памятью браузера) ---
def main():
    # Инициализируем переменные в session_state (как в "кармане" браузера)
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answered = False

    q = questions[st.session_state.question_index]
    total = len(questions)

    # --- ВИЗУАЛЬНАЯ ЧАСТЬ ВЕБ-СТРАНИЦЫ ---
    st.title("🧠 Тест по анатомии")
    st.progress((st.session_state.question_index) / total) # Полоска прогресса

    st.subheader(f"Вопрос {st.session_state.question_index + 1} из {total}")
    st.write(q["question"])

    # Показываем картинку
    try:
        image = Image.open(q["image"])
        st.image(image, width=300) # Подпись под картинкой
    except:
        st.warning("(картинка не загружена)", icon="⚠️")

    # Варианты ответов (radio-кнопки)
    answer = st.radio("Выбери ответ:", q["options"], key="answer", disabled=st.session_state.answered)

    # Кнопка "Ответить"
    if st.button("Ответить", disabled=st.session_state.answered):
        st.session_state.answered = True
        if answer == q["options"][q["correct"]]:
            st.session_state.score += 1
            st.success("✅ Правильно!")
        else:
            correct_text = q["options"][q["correct"]]
            st.error(f"❌ Неправильно. Правильный ответ: {correct_text}")

    # Кнопка "Следующий вопрос"
    if st.button("Следующий вопрос"):
        if st.session_state.question_index + 1 < total:
            # Переходим к следующему вопросу
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.rerun()
        else:
            # Тест закончен, показываем результат
            st.balloons()
            st.success(f"✨ Тест завершён! ✨\n\nТвой результат: {st.session_state.score} из {total} ({int((st.session_state.score/total)*100)}%)")
            st.balloons()
            # Кнопка, чтобы начать заново
            if st.button("Пройти тест заново"):
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.rerun()

if __name__ == "__main__":
    main()
