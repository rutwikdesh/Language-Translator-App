#App Created by Rutwik Deshmukh

#To install streamlit use the command: "pip install streamlit"
#To install translate use the command: "pip install translate"
#To Run the code use the command: "streamlit run app.py"


#Importing Relevant Libraries
import streamlit as st
from translate import Translator


#Title
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
            'Swedish', 'Thai', 'Turkish', 'Ukrainian', 'Vietnamese', 'Welsh']


#Creating SelectBoxes
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
