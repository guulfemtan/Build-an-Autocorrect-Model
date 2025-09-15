!pip install streamlit -q
import streamlit as st
import textdistance
import pickle

with open("/content/autocorrect_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

dictionary = loaded_model["dictionary"]
word_freq = loaded_model["word_freq"]

def autocorrect(word):
    word = word.lower()
    if word in dictionary:
        return word
    candidates = sorted(dictionary, key=lambda w: textdistance.levenshtein(word, w))[:5]
    best_match = max(candidates, key=lambda w: word_freq.loc[word_freq["word"]==w, "count"].values[0])
    return best_match

st.title("Autocorrect App")
st.write("Enter a word and see the autocorrected result:")

user_input = st.text_input("Type a word:")
if user_input:
    corrected = autocorrect(user_input)
    st.success(f"Corrected Word: {corrected}")
