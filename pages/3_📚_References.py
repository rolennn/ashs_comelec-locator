import streamlit as st


# page configuration
st.set_page_config(
    page_title="References",
    initial_sidebar_state="auto",
    page_icon="_data/logo.jpg"
)


text_ref = """
The information on registration offices was processed using data from: 
* Republic of the Philippines, Commission on Elections. (January, 2022). Field Offices. https://comelec.gov.ph/?r=ContactInformation/FieldOffices 

* Republic of the Philippines, Philippine Statistics Authority. (November, 2022). Third Quarter 2022 PSGC Updates: Division of the Province of Maguindanao, Conversion of One (1) Municipality into New City, Creation of One (1) Barangay, and Correction of the Names of 44 Barangays. Philippine Standard Geographic Code (PSGC). https://psa.gov.ph/classification/psgc/ 

---

The general processes of registration and election schedule were summarized from:
* Republic of the Philippines, Commission on Elections. (November 29, 2022). Resolution No. 10868. RULES AND REGULATIONS ON THE CONDUCT OF THE SYSTEM OF CONTINUING REGISTRATION OF VOTERS FOR THE BARANGAY AND SANGGUNIANG KABATAAN ELECTIONS. https://comelec.gov.ph/?r=VoterRegistration/Resolutions/res10868 

* Republic of the Philippines, The Official Gazette. (October 10, 2022). Republic Act No. 11935. AN ACT POSTPONING THE DECEMBER 2022 BARANGAY AND SANGGUNIANG KABATAAN ELECTIONS, AMENDING FOR THE PURPOSE REPUBLIC ACT NO. 9164, AS AMENDED, APPROPRIATING FUNDS THEREFOR, AND FOR OTHER PURPOSES. https://www.officialgazette.gov.ph/2022/10/10/republic-act-no-11935/ 

---

The information about the Register Anywhere Project were gathered from:
* Casilao, Joahna. (December 5, 2022). Comelec names 5 NCR malls for 'register anywhere' drive. GMA News. https://www.gmanetwork.com/news/topstories/regions/853520/comelec-names-5-ncr-malls-for-register-anywhere-drive/story/ 

* GMA Integrated News. (December 12, 2022). Voter registration starts for barangay, Sangguniang Kabataan polls. GMA News. https://www.gmanetwork.com/news/topstories/nation/854196/voter-registration-starts-for-barangay-sangguniang-kabataan-polls/story/ 

* Noriega, Richa. (December 10, 2022). More sites included in Register Anywhere Project — Comelec. GMA News. https://www.gmanetwork.com/news/topstories/nation/854115/more-sites-included-in-register-anywhere-project-comelec/story/ 
"""


st.title("References")
st.markdown(text_ref)