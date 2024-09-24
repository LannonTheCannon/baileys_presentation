# material_game.py
import streamlit as st


def material_game():
    st.subheader("Guess the best material for each situation!")
    st.caption("Questions made by the Material Selection AI :thumbsup:")
    # initialize session state variables for the quiz
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    # create a variable using state called score
    if "score" not in st.session_state:
        st.session_state.score = 0
    # and another one called quiz_complete
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False

    quiz_data = [
        {
            "question": "What material is commonly used for making lightweight yet strong structures, including aircraft and bicycles?",
            "options": ["Steel","Aluminum","Wood"],
            "correct_answer": 1,
        },
        {
            "question": "Which of the following materials is best known for its thermal insulation properties and is often used in building construction?",
            "options": ["Polystyrene foam"," Glass","Concrete"],
            "correct_answer": 0,
        },
        {
            "question": "Which material is commonly used for making surgical instruments due to its resistance to corrosion and ability to be sterilized?",
            "options": ["Copper","Plastic","Stainless Steel"],
            "correct_answer": 2,
        }
    ]

    # quiz logic
    if not st.session_state.quiz_complete:
        question = quiz_data[st.session_state.current_question]
        st.write(f'Question {st.session_state.current_question + 1} of {len(quiz_data)}')
        st.write(question["question"])

        answer = st.radio("Choose your answer", question["options"], key = f'sb_q{st.session_state.current_question}')

        if st.button("Submit Answer",key = "sb_submit"):
            if question["options"].index(answer) == question["correct_answer"]:
                st.session_state.score += 1
                st.success("Correct")
##                    st.rerun()
            else:
                st.error(f'Wrong. The correct answer was "{question["options"][question["correct_answer"]]}"')
            if st.session_state.current_question < len(quiz_data) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.quiz_complete = True
        if st.button("Next"):
            pass
        if st.button("Skip"):
            st.session_state.current_question += 1
            if st.session_state.current_question > len(quiz_data) -1:
                st.session_state.current_question = len(quiz_data)
                st.session_state.quiz_complete = True
##            st.rerun()
\
    else:
        st.success("You completed the quiz!")
        st.write(f'Your score is: {st.session_state.score}/{len(quiz_data)}')
        
##        if st.button("Restart"):
##            st.session_state.current_question = 0
##            st.session_state.score = 0
##            st.session_state.quiz_complete = False
##            st.rerun()
    st.sidebar.write('''
______________________________
''')
    st.sidebar.write(f'Current score: {st.session_state.score}/{len(quiz_data)}')

