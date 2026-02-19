import streamlit as st
import pickle

st.title("Addiction_prediction")

st.set_page_config(page_title="Addiction_prediction", page_icon=":smiley:", layout="wide")


def load_model():
    return pickle.load(open('er_model.pkl', 'rb'))

model=load_model()

# Age                            -0.166396
# Gender                         -0.049692
# Academic_Level                  0.075543
# Country                         0.221383
# Avg_Daily_Usage_Hours           0.832000
# Most_Used_Platform              0.209653
# Affects_Academic_Performance    0.866049
# Sleep_Hours_Per_Night          -0.764858
# Mental_Health_Score            -0.945051
# Relationship_Status            -0.016517
# Conflicts_Over_Social_Media     0.933586
# Addicted_Score                  1.000000

value1=st.number_input("Avg_Daily_Usage_Hours")
st.write("Value entered: ", value1)
value2=st.selectbox("Affects_Academic_Performance", [1,0])
st.write("Value entered: ", value2)
value3=st.number_input("Sleep_Hours_Per_Night")
st.write("Value entered: ", value3)
value4=st.selectbox("Mental_Health_Score", [4, 5, 6, 7, 8, 9])
st.write("Value entered: ", value4)
value5=st.selectbox("Conflicts_Over_Social_Media", [0,1,2,3,4,5])
st.write("Value entered: ", value5)

if st.button("predict"):
    input_data=[[value1, value2, value3, value4, value5]]
    prediction=model.predict(input_data)
    st.write("Prediction: ", prediction[0])