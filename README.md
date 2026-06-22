# LLM Prompt Evaluator (PM/ Builder Toolkit)

A lightweight Streamlit application designed for Product Managers/ Builders to A/B test and objectively evaluate LLM prompts using "LLM-as-a-Judge" methodology.

## The Problem
When iterating on GenAI features, Product Managers/ Builders and Engineers constantly tweak prompts to improve output quality, reduce hallucinations, or adjust tone. However, evaluating if "Prompt B" is actually better than "Prompt A" is usually done via vibe checks, i.e., manual, tedious reading of a few outputs. This lack of quantitative evaluation prevents scaling AI products reliably.

## 💡 The Solution
This tool allows PMs to:
1. Input a **Baseline Prompt** and a **Candidate Prompt**.
2. Upload a small dataset of test cases (e.g., user queries).
3. Use a stronger LLM (like GPT-4o) as an objective "Judge" to score the outputs of both prompts against specific criteria (Accuracy, Tone, Helpfulness).
4. View a side-by-side comparison and win-rate to make data-driven decisions on prompt deployments.

## 🏗️ Architecture & Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) for rapid UI prototyping.
* **Orchestration:** Python (with potential integration of LangChain/LiteLLM for model routing).
* **Evaluator:** OpenAI API (GPT-4o) used as the judge model.
* **Data Handling:** Pandas for processing test case CSVs.

## 🚀 Future Roadmap
- [ ] Add support for custom evaluation rubrics (defining specific grading criteria).
- [ ] Export evaluation reports to CSV/Markdown for engineering hand-off.
- [ ] Add support for local open-source models (via Ollama) to reduce API costs.

----
*Built by [Sadasib]. This is a personal project using cosmetic data and has no affiliation with my employer*
