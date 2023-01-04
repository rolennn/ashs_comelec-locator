import streamlit as st


# page configuration
st.set_page_config(
    page_title="About Us",
    initial_sidebar_state="auto",
    page_icon="_data/logo.jpg"
)


content = """
This web-app and other related promotional materials are under the “Para Saan Ka Boboto?” project of the [ASHS Commission on Elections][1] (ASHS ComElec). For any concerns or inquiries about this project or the information presented in this web-app, please feel free to contact us through our email (comelec.ashs@ateneo.edu). 

We do not store data about the locations inputted in this web-app. Additionally, the source code is publicly hosted on the following repository: https://github.com/rolennn/ashs_comelec-locator 

[1]: https://www.facebook.com/ASHSCOMELEC:
"""

st.subheader("About Us")
st.markdown(content)
