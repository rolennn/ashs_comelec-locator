import streamlit as st


# page configuration
st.set_page_config(
    page_title="Election",
    initial_sidebar_state="auto",
    page_icon="_data/logo.jpg"
)


text_intro = """
Hello! [Republic Act No. 11935][1] states that the Barangay and Sangguniang Kabataan (SK) Elections will be held on the last Monday of October, 2023. With this, the Commission on Elections (COMELEC) re-opened the registration of voters following the procedures in [COMELEC Resolution No. 10868][2].

[1]: https://www.officialgazette.gov.ph/2022/10/10/republic-act-no-11935/
[2]: https://comelec.gov.ph/?r=VoterRegistration/Resolutions/res10868
"""

text_eligibility1 = """
Any Filipino citizen who is not yet a registered voter may apply for registration, provided they possesses the following qualifications—

**For Barangay Elections:**
- At least eighteen (18) years of age on or before the day of the Barangay Elections;
- A resident of the Philippines for at least one (1) year and in the place wherein he/ she proposes to vote, for at least six (6) months immediately preceding the Barangay and Sangguniang Kabataan Elections; and
- Not otherwise disqualified by law.
"""
text_eligibility2 = """
**For Sangguniang Kabataan Elections:**
- At least fifteen (15) but not more than thirty (30) years of age and residing in the barangay for at least six (6) months on or before Sangguniang Kabataan Elections; and
- Not otherwise disqualified by law.
"""

text_registration = """
##### Traditional Registration
Applications for registration can be **filed personally at the Office of the Election Officer (OEO) of the city/municipality/district where the applicant resides**, during office hours, **from 8:00 AM to 5:00 PM from Mondays to Saturdays** including Holidays, except when declared otherwise by the COMELEC.

The OEOs will receive applications from **December 12, 2022** to **January 31, 2023**, except on December 24 and 31, 2022 (Christmas Eve and last day of the year). 

---

##### Register Anywhere Project (RAP)
To aid in the registration process, the COMELEC launched the Register Anywhere Project (RAP), where applicants can register **in select RAP venues within the country**. The applications processed in these RAP venues will be sent to the applicant’s respective city/municipality/district, and they will be registered as voters in that locality. 

The RAP venues will receive applications from **December 17, 2022** to **January 25, 2023**, except on December 24, 25, 31, and January 1, 2022. 
"""

text_requirements1 = """
##### Required Forms
The applicant must submit an accomplished [Application Form (Revised CEF-1-A)][1] for their registration. Depending on their context and the nature of the application, they (or any accompanying guardian) might be expected to accomplish any of the following forms: 
1. [Supplementary Data Form][2];
2. [Certification for Registration][3] of Applicant whose name is not found in the Local Voter's Registration Database (LVRD), Printed Lists of Voters (PLVs), Printed Lists of Deactivated Voters (PLDVs);
3. [Affidavit under Oath][4] of the Voter's Identification; and
4. [OVF form 1-B: Application for Transfer][5] from Post to Philippine Municipality/City/District. 

[1]: https://comelec.gov.ph/php-tpls-attachments/VoterRegistration/ApplicationsForms/CEF1_Revised_fillable.pdf
[2]: https://comelec.gov.ph/php-tpls-attachments/VoterRegistration/ApplicationsForms/Annex_B_SupplementaryData_Fillable.pdf
[3]: https://comelec.gov.ph/php-tpls-attachments/VoterRegistration/ApplicationsForms/Annex_C_Certification.pdf
[4]: https://comelec.gov.ph/php-tpls-attachments/VoterRegistration/ApplicationsForms/AnnexD.pdf
[5]: https://comelec.gov.ph/php-tpls-attachments/OverseasVoting/2023RegForms/AnnexE.pdf
"""
text_requirements2 = """
##### For registration
The applicant must present an identification document that contains their signature and photograph. The following are the valid documents:
- National identification (ID) card under the Philippine Identification System (PhilSys);
- Employee's ID card, with the signature of the employer or authorized representative;
- Postal ID card;
- PWD ID Card;
- Student's ID card or library card, signed by the school authority;
- Senior Citizen's ID card;
- Driver's license;
- NBI clearance;
- Passport;
- SSS/GSIS or other UMID ID card;
- Integrated Bar of the Philippines (IBP) ID card;
- License issued by the Professional Regulatory Commission (PRC);
- Certificate of Confirmation issued by the National Commission on Indigenous Peoples (NCIP) in case of members of ICCs or IPs;
- Barangay Identification/Certification with photo; and
- Any other valid ID cards.
"""

text_additional = """
The information presented in this page was gathered from the [COMELEC Resolution No. 10868][1]. Procedures for transfer, change/corrections of entries in the registration records, reactivation of registration records, and similar activities can also be found in the resolution. Generally, you may refer to the [COMELEC website][2] for election-related information. 

Additionally, the National Citizens’ Movement for Free Elections (NAFREL) maintains "[Vote For Us][3]", a voter information and outreach platform that aims to educate Filipinos on electoral processes. 

[1]: https://comelec.gov.ph/?r=VoterRegistration/Resolutions/res10868
[2]: https://comelec.gov.ph/
[3]: https://www.voteforus.org.ph/
"""

text_conclusion = """
Good luck with the registration :>
"""

st.subheader("Barangay and Sangguniang Kabataan (SK) Elections")
st.markdown(text_intro)
st.info("We hope that the information below can guide you in your application for registration.")

with st.expander("Who may register to be a voter?", expanded=False):
    st.markdown(text_eligibility1)
    st.markdown("")
    st.markdown(text_eligibility2)
    st.markdown("")
    st.info("Please note that Barangay and Sangguniang Kabataan Elections is expected to be conducted on the last Monday of October, 2023, as per Republic Act No. 11935.")

with st.expander("Where and when can I register?", expanded=False):
    st.markdown(text_registration)
    st.info("You may use the 🔍 Registration Sites portion of this web-app to locate your municipality’s OEO and the nearest RAP venue/s. ")

with st.expander("What are the requirements for registration?", expanded=False):
    st.markdown(text_requirements1)
    st.markdown("")
    st.info("Please note that all of the above-specified forms are available at the registration station free of charge. They may also be downloaded and printed on a long bond paper.")
    st.markdown("---")
    st.markdown(text_requirements2)
    st.markdown("")
    st.info("Please note that failure to establish the applicant's identity will lead to their application not being processed")

with st.expander("Where can I learn more about the registration?", expanded=False):
    st.markdown(text_additional)

# st.markdown(text_conclusion)