#To view the webapp run the following command in the terminal 
#streamlit run "file path"

import pickle
import streamlit as st
import pandas as pd
import numpy as np
import spacy

from extra_features import Extras 
nlp = spacy.load("en_core_web_sm")


def clean_doc(sent):
    doc = nlp(sent)
    lemma_out = [token.lemma_ for token in doc]
    lemma_out = " ".join(lemma_out)
    return lemma_out


with open('tfidfvec.pkl', 'rb') as f:
  vec = pickle.load(f)

from joblib import dump, load
#clf= pickle.load(open('spam_classifier_model.pkl','rb'))
clf=load('spam_classifier_model.joblib')

def main():
    st.title("Spam Mail Detector")
    st.write("Enter the text of mail to check if it's spam or not")
    
    mail=st.text_input("Enter text here: ")

    extra_features=Extras(mail) 
    
    if mail or st.button('Check'):
        clean_mail=clean_doc(mail)
        vector=vec.transform([clean_mail]).toarray()
        extra_cols=np.array([extra_features.count_digits(),extra_features.count_upppercase(),extra_features.count_special_characters(),extra_features.count_hyperlinks()])
        vector=np.append(vector, extra_cols)

        prediction=clf.predict(vector.reshape(1,-1))[0]
        #st.write(prediction)
        if prediction=='spam':
            st.text_area(label ="Prediction",value='SPAM', height =10)
        else:
            st.text_area(label ="Prediction",value='Not SPAM', height =10)

main()


