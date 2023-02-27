import streamlit as st

st.title("Innomatics Data App")
st.subheader("Hello Everyone")
btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.write("This Page Contains Information about the Ben 10 versions")
    st.balloons()
