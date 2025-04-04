import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Load GPT prompt configuration securely
GPT_SYSTEM_PROMPT = st.secrets["GPT_SYSTEM_PROMPT"]

# Inline CSS for Sidebar Navigation and Footer
st.markdown(
    """
    <style>
    /* Sidebar style */
    [data-testid="stSidebar"] {
        background-color: #f0f0f0;
        width: 240px !important;
        padding: 10px;
    }
    /* Navigation styling */
    .custom-nav ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }
    .custom-nav li {
        margin: 0;
        padding: 2px 0;
        text-align: left;
    }
    .custom-nav li a {
        text-decoration: none;
        color: inherit;
        display: block;
        padding: 2px 5px;
    }
    .custom-nav li.active a {
        background-color: #d3d3d3;
        border-radius: 4px;
        padding: 2px 5px;
        width: 100%;
        box-sizing: border-box;
    }
    /* Footer styling */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100vw;
        background-color: #444444;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 20px;
        font-size: 0.9em;
        z-index: 99999;
    }
    .custom-footer a {
        color: #dddddd;
        margin: 0 10px;
        text-decoration: none;
    }
    .custom-footer a:hover {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation Pane
with st.sidebar:
    st.markdown(
        """
        <div class="custom-nav">
          <ul>
            <li><a href="#">Find Real Patients</a></li>
            <li><a href="https://full-site-demo-rtvuylvub3w6fbvdurdgbx.streamlit.app/">Tactical Plans</a></li>
            <li><a href="https://costcalculator-5zcyncr2pzv4baam2w54e6.streamlit.app/">Cost Calculator</a></li>
            <li class="active"><a href="https://landscapeassessment-dnjxq2mzzamu4ekog5y2ew.streamlit.app/">Landscape Analysis</a></li>
            <li><a href="#">Pipeline Outlook</a></li>
            <li><a href="#">Create Messaging</a></li>
            <li><a href="#">Campaign Concepts</a></li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# App Main Content
st.title("🩺 Market Landscape Analysis")

with st.form("analysis_form"):
    brand = st.text_input("Brand Name (optional)", placeholder="e.g., Keytruda")
    indication = st.text_input("Indication (Disease/Condition)", placeholder="e.g., NSCLC")
    geography = st.text_input("Geography", value="U.S.")
    competitive_focus = st.text_input("Specific Competitive Focus (optional)", placeholder="e.g., Patient Marketing")

    submit = st.form_submit_button("Generate Analysis")

if submit:
    if not indication:
        st.error("Please enter an indication (Disease/Condition).")
    else:
        user_prompt = f"""
        Brand Name: {brand or 'None'}
        Indication: {indication}
        Geography: {geography or 'U.S.'}
        Specific Competitive Focus: {competitive_focus or 'General'}
        """

        with st.spinner('Generating analysis...'):
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": GPT_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.5,
                max_tokens=1200
            )

            analysis = response.choices[0].message.content
            st.subheader("Market Landscape Analysis")
            st.write(analysis)

# Footer
footer_html = """
<footer class="custom-footer">
  <div style="text-align: left; flex: 1;">© Philip Storer 2025</div>
  <div>
    <a href="#">Terms of Use</a> |
    <a href="#">Privacy Policy</a> |
    <a href="#">Cookie Settings</a> |
    <a href="#">Contact Us</a>
  </div>
</footer>
"""
st.markdown(footer_html, unsafe_allow_html=True)
