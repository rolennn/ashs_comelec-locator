import streamlit as st
# import numpy as np
# import pandas as pd
# import os

def setup_page():
    introduction = st.container()
    st.markdown("---")
    input_location = st.container()
    output_data = st.container()
    st.markdown("---")
    additionals = st.container()

    with introduction:
        st.title("TITLE")  
        st.markdown("Project description.")
    
    with input_location:
        st.info("Please input your your current place of residence to identify the nearest polling station.")

        province, city, barangay = st.columns(3)
        location, search = st.columns([7.8, 1])

        province.selectbox(
            "Province",
            ("a", "b", "c")
        )
        city.selectbox(
            "City",
            ("a", "b", "c")
        )
        barangay.selectbox(
            "Barangay",
            ("a", "b", "c")
        )

        location.markdown("Output result here.")
        search.button("Search")

    with additionals:
        with st.expander("Notes on Privacy", expanded=False):
            st.markdown("""
            Additional notes
            """)

        with st.expander("Credits", expanded=False):
            st.markdown("""
            Additional Credits
            """)


if __name__ == "__main__":
    setup_page()