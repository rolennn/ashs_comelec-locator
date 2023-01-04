import streamlit as st
import pandas as pd

import find_offices


# page configuration
st.set_page_config(
    page_title="Registration",
    initial_sidebar_state="auto",
    page_icon="_data/logo.jpg"
)


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
    text_intro = """
    Please input your current place of residence to identify the nearest polling station. Note that the Register Anywhere Project (RAP) venues within your municipality will be prioritized (if there are any), followed by the Office of the Election Officer (OEO) for your municipality/district, followed by the RAP venues within your province (if there are any). RAP venues outside your province will be displayed last. 
    """

    with introduction:
        st.title("Registration Sites")  
        st.markdown(text_intro)
    
    # `input_location` contains a space for the user to input their location
    with input_location:
        st.info("Please input your your current place of residence to identify the nearest polling station.")

        loc = st.columns(2)
        submit =  st.columns([1, 4, 1])

        province = loc[0].selectbox(
            "Province",
            options=data["PROV"].unique()
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
                st.info("You may register in any of the following locations:")
                find_offices.search(data, province, municipality)
            except:
                st.error("Unfortunately, we encountered difficulties searching for an office. Please try again later.")


if __name__ == "__main__":
    setup_page(process_data())

