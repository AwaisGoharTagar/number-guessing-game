import random
import streamlit as st

def number_guessing_game():
    st.title("🎯 Number Guessing Game")
    
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 7
    
    guess = st.number_input("Guess the number (between 1 and 100):", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        if st.session_state.attempts > 0:
            st.session_state.attempts -= 1
            if guess < st.session_state.secret_number:
                st.warning("📉 Too low! Try again.")
            elif guess > st.session_state.secret_number:
                st.warning("📈 Too high! Try again.")
            else:
                st.success("🎉 Congratulations! You guessed the correct number.")
                st.session_state.secret_number = random.randint(1, 100)
                st.session_state.attempts = 7
        
        if st.session_state.attempts == 0:
            st.error(f"❌ You've run out of attempts! The correct number was {st.session_state.secret_number}.")
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 7

if __name__ == "__main__":
    number_guessing_game()