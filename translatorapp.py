#App Created by Rutwik Deshmukh

# I used streamlit to create a WebApp using Python
# This app basically a simple text translator
# To run this app type the command "streamlit run translatorapp.py"
import streamlit as st
from translate import Translator

st.write('''
    # Language Translator using Python
    '''
)

#Input the text to convert from the user
translated_text = st.text_input("Enter Text to Convert"," ")

if translated_text=="":
    st.warning("Please enter some text to convert")
    


#Creating a selectbox
languages = ['Arabic', 'Belarusian', 'Chewa', 'Chinese',  'Croatian', 'Czech','Danish', 'Dutch', 'English', 
            'Estonian', 'Finnish', 'French', 'German', 'Greek', 'Hebrew', 'Hindi', 'Hungarian', 'Indonesian',
            'Italian', 'Japanese', 'Javanese', 'Korean', 'Latvian', 'Lithuanian','Malay', 'Maltese', 'Norwegian',
            'Persian', 'Polish', 'Portuguese',  'Romanian', 'Russian', 'Slovenian','Spanish',
            'Swedish', 'Thai', 'Turkish', 'Ukrainian', 'Vietnamese', 'Welsh',]


from_= st.selectbox("Convert from Language",languages)
to_ = st.selectbox("Convert to Language",languages)


translator = Translator(from_lang=from_, to_lang=to_)

#Printing the translated text
try:
    if st.button("Submit"):
        result = "The translated text is: " + translator.translate(translated_text)
        st.success(result)

except:
    st.exception("Enter valid Text")


# To create the list of languages supported by translate package used 
# "https://en.wikipedia.org/wiki/Google_Translate#:~:text=The%20Google%20Translate%20app%20for,
# in%20%22augmented%20reality%20mode%22." website