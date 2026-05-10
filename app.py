import streamlit as st
from openai import OpenAI
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="LLM Prompt Evaluator", page_icon="⚖️", layout="wide")
st.title("⚖️ LLM Prompt Evaluator (PM Toolkit)")
st.markdown("A lightweight tool to A/B test prompts using an LLM-as-a-Judge.")

# --- SIDEBAR (API Key Management) ---
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("OpenAI API Key", type="password", help="Never hardcode your API key!")
    st.markdown("---")
    st.markdown("**Criteria for the Judge:**")
    eval_criteria = st.text_area("What makes a good prompt here?", 
                                 "1. Accuracy\n2. Tone (Professional yet conversational)\n3. Conciseness")

# --- MAIN UI ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🅰️ Baseline Prompt")
    prompt_a = st.text_area("Enter your current/baseline prompt:", height=150, key="prompt_a")

with col2:
    st.subheader("🅱️ Candidate Prompt")
    prompt_b = st.text_area("Enter the new prompt you want to test:", height=150, key="prompt_b")

st.markdown("---")
st.subheader("🧪 Test Data")
test_case = st.text_area("Enter a sample user input or test scenario:", height=100)

# --- EXECUTION LOGIC ---
if st.button("🚀 Run Evaluation", use_container_width=True):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not prompt_a or not prompt_b or not test_case:
        st.warning("Please fill in all prompt and test case fields.")
    else:
        # Initialize OpenAI Client
        client = OpenAI(api_key=api_key)
        
        with st.spinner("Running evaluation... (this might take a few seconds)"):
            try:
                # 1. Generate Output A
                response_a = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "system", "content": prompt_a}, {"role": "user", "content": test_case}]
                )
                output_a = response_a.choices[0].message.content
                
                # 2. Generate Output B
                response_b = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "system", "content": prompt_b}, {"role": "user", "content": test_case}]
                )
                output_b = response_b.choices[0].message.content
                
                # 3. LLM-as-a-Judge (The Secret Sauce)
                judge_prompt = f"""
                You are an expert AI Product Manager evaluating two different LLM outputs based on a test case.
                
                Evaluation Criteria:
                {eval_criteria}
                
                Test Case: {test_case}
                
                Output A (Baseline): {output_a}
                Output B (Candidate): {output_b}
                
                Which output is better based on the criteria? Provide a brief justification, then clearly declare a winner (Output A or Output B).
                """
                
                judge_response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "You are an objective AI evaluator."},
                              {"role": "user", "content": judge_prompt}]
                )
                evaluation = judge_response.choices[0].message.content

                # --- DISPLAY RESULTS ---
                st.success("Evaluation Complete!")
                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.info("**Output A:**\n\n" + output_a)
                with res_col2:
                    st.info("**Output B:**\n\n" + output_b)
                
                st.markdown("### 🧑‍⚖️ The Judge's Verdict")
                st.write(evaluation)

            except Exception as e:
                st.error(f"An error occurred: {e}")
