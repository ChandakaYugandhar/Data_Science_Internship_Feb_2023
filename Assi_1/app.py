import streamlit as st

st.title("Innomatics Data App")
st.subheader("If if want to know about the App")
btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :heart_eyes:")
    st.write("This Page Contains Information about the Ben 10 versions")
    st.balloons()