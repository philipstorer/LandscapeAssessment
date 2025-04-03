import streamlit as st
import openai

# Securely access your API key from Streamlit's secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Insert your GPT prompt securely in Streamlit secrets as well
GPT_SYSTEM_PROMPT = st.secrets["GPT_SYSTEM_PROMPT"]

st.title("🩺 Pharma Market Landscape Analysis GPT")

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
            response = openai.ChatCompletion.create(
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
