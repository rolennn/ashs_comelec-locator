import streamlit as st
import numpy as np 


# dirty try-catch hack, but ehhh
def check_nan(data_pt):
    try: 
        if np.isnan(data_pt):
            return "No data provided"
    except:
        return data_pt
        

def create_card(marker, title, tel, email, loc):
    with st.expander(marker, expanded=False):
        st.markdown(f"#### {title}")
        
        c11, c12 = st.columns([1, 12])
        with c11:
            st.markdown("**Loc.:**")
        with c12:
            st.markdown(loc)
        
        c21, c22, c23, c24 = st.columns([1,5,1,5])
        with c21:
            st.markdown("**Tel.:**")
        with c22:
            st.markdown(tel)
        with c23:
            st.markdown("**Email:**")
        with c24:
            st.markdown(email)

        
def show_data(filtered):
    for i in range(len(filtered.index)):
        row = filtered.iloc[i]

        office_type = row["MEO-LOC_1"]
        telephone = check_nan(row["MEO-TEL"])
        email = check_nan(row["MEO-EML"])
        location = row["MEO-LOC_2"]

        create_card(
            marker=office_type,
            title=office_type,
            tel=telephone,
            email=email,
            loc=location
        )


def search(data, prov, mun): 
    # every data received will be presented in an expander
    
    # prioritize RAP locations within a MUN, PROV
    rap_mun = data[
        (data["PROV"] == prov) &
        (data["MUN"] == mun) &
        (data["MEO-POS"] == "Register Anywhere Project")
    ]
    show_data(rap_mun)

    # display OEO locations within a MUN, PROV
    # note that this must exclude the RAP locations already shown
    oeo_mun = data[
        (data["PROV"] == prov) &
        (data["MUN"] == mun) &
        (data["MEO-POS"] != "Register Anywhere Project")
    ]
    show_data(oeo_mun)

    # display the RAP locations within the PROV
    # note that this must exclude the RAP locations already shown
    rap_prov = data[
        (data["PROV"] == prov) &
        (data["MUN"] != mun) &
        (data["MEO-POS"] == "Register Anywhere Project")
    ]
    show_data(rap_prov)

    # present the rest of the RAP locations (not within MUN, PROV)
    st.info("Alternatively, you may register in the following satellite offices through COMELEC's Register Anywhere Project (RAP)")

    rap_rest = data[
        (data["PROV"] != prov) &
        (data["MUN"] != mun) &
        (data["MEO-POS"] == "Register Anywhere Project")
    ]
    show_data(rap_rest)


