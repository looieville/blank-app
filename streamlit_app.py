import streamlit as st
import random

# test library 
dad_jokes = [
    "I'm afraid for the calendar. Its days are numbered.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I only know 25 letters of the alphabet. I don't know y.",
    "I used to play piano by ear, but now I use my hands.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I would avoid the sushi if I was you. It’s a little fishy.",
    "What do you call a factory that makes good products? A satisfactory.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "What do you call a prostitute who can rap? Araphoe",
    "What's black, white and red all over? A zebra in a blender."
]

# app title
st.set_page_config(page_title="Dad Joke Generator", page_icon="🧔", layout="centered")
st.title("🧔 Dad Joke Dispenser")
st.subheader("Tap the button for a classic cringe-worthy dad joke!")

if st.button("🎲 Tell me a joke"):
    joke = random.choice(dad_jokes)
    st.success(joke)
    st.code(joke, language="markdown")

# footer
st.markdown("---")
st.caption("Warning: excessive use may result in uncontrollabe eye-rolls!")
