
import pickle
import streamlit as st

pickle_in = open("diabetes1.pkl", "rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(num_preg, glucose_conc, diastolic_bp, insulin, bmi, diab_pred, age, skin):
    prediction = classifier.predict([[num_preg, glucose_conc, diastolic_bp, insulin, bmi, diab_pred, age, skin]])
    print(prediction)
    return prediction


def main():
    st.title("Diabetes Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    num_preg = st.text_input("number of times pregnant", "Type Here")
    glucose_conc = st.text_input("glucose concentration", "Type Here")
    diastolic_bp = st.text_input("diastolic bp", "Type Here")
    insulin = st.text_input("level of insulin", "Type Here")
    bmi = st.text_input("level of bmi", "Type Here")
    diab_pred = st.text_input("diab_pred", "Type Here")
    age = st.text_input("age", "Type Here")
    skin = st.text_input("skin", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(num_preg, glucose_conc, diastolic_bp, insulin, bmi, diab_pred, age, skin)
    if result==1:
        st.success('You have a chance of diabetes')
    elif result==0:
        st.success('You have no diabetes')


if __name__ == '__main__':
    main()