import streamlit as st
import pandas as pd

import find_offices


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def process_data():
    offices_data = pd.read_csv("_data/offices_data.tsv", sep="\t", header=0)

    return offices_data


def setup_page(data):
    # prepare the layout of the page by providing containers and separators
    introduction = st.container()
    st.markdown("---")
    input_location = st.container()
    st.markdown("---")
    output_data = st.container()

    # `introduction` contains preliminary information re. the project 
    with introduction:
        st.title("TITLE")  
        st.markdown("Project description. _(feel free to suggest what to put here or on any part of the web-app, thank you -rolen)_")
    
    # `input_location` contains a space for the user to input their location
    with input_location:
        st.info("Please input your your current place of residence to identify the nearest polling station.")

        loc = st.columns(2)
        submit =  st.columns([1, 4, 1])

        province = loc[0].selectbox(
            "Province",
            options=data["PROV"].dropna().unique()
        )
        municipality = loc[1].selectbox(
            "Municipality",
            options=data[data["PROV"] == province]["MUN"].unique()
        )

        submit[0].markdown("**Location:**")
        submit[1].markdown(f"{province}, {municipality}")
        search = submit[2].button("Find Office")

    # output_data
    with output_data:
        if search:
            try:
                st.info("You may register in any of the following locations.")
                find_offices.search(data, province, municipality)
            except:
                st.error("Unfortunately, we encountered difficulties searching for an office. Please try again later.")


if __name__ == "__main__":
    setup_page(process_data())
