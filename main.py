# Importing necessary modules
import logic as lg
import streamlit as st

# Front end with Streamlit
st.title("Quiz Generator")
st.subheader("Generate your multiple-choice quiz questions with AI")

# Input about the quiz topic with a maximum of 50 characters
quiz_topic = st.text_input("Enter the topic you want to be asked about", max_chars=50)

# Input about the number of questions with a minimum of 1
num_of_questions = st.number_input("Enter the number of questions", min_value=1)

if quiz_topic and num_of_questions:
    # Button to generate quiz
    st_button = st.button("Generate Quiz")

    if st_button:
        # Generating quiz questions using logic.py
        response = lg.generate_questions(quiz_topic=quiz_topic, num_of_questions=num_of_questions)
        questions = response['question_format']

        # Split questions into individual questions
        question_list = questions.split('Q')[1:]

        # Counter for correct answers
        correct_answers = 0

        # Loop through each question
        for i, question in enumerate(question_list):
            # Display question
            st.subheader(f"Question {i + 1}")
            st.write(question)

            # Extract options
            options_start_index = question.find("a.")
            options_end_index = question.find("Answers:")
            options_text = question[options_start_index:options_end_index].strip()
            options_list = options_text.split("\n")[1:]

            # Create radio buttons for each option
            user_answer = st.radio(f"Select your answer for Question {i + 1}", options_list)

            # Check if the user's answer is correct
            correct_option = options_list[options_text.find("^")]
            if user_answer == correct_option:
                st.success("Correct! 🎉")
                correct_answers += 1

        # Display the summary at the end
        st.subheader("Quiz Summary")
        st.write(f"Number of correct answers: {correct_answers}/{num_of_questions}")

        st.markdown("### MCQ Finished")
