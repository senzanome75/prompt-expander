# Prompt Expander

## A Prompt Expander OpenAI-Based.

---

This repository concerns a **Prompt Expander**: a proof of concept software that uses **OpenAI API** itself to improve the performance of a **Task** requested in input.

The fundamental features will be:
1) Expansion of a task into a number of intermediate steps necessary to carry out the task (partially implemented)
2) Understand whether a Google search is necessary to carry out a step and, if the answer is positive, carry it out (partially implemented)
3) Understand whether scraping from a web page is necessary to carry out a step (partially implemented)
4) Use of Markdown as a standard for intermediate processing (both for the predictability of GPT output and for the simplicity of managing the format itself)
5) Saving detailed logs to disk (in Markdown format), necessary later to reconstruct the input/prompt/output chain.

---

### Dependencies
- pip install --upgrade pip
- pip install --upgrade openai
- pip install --upgrade googlesearch-python
- pip install --upgrade beautifulsoup4
- pip install --upgrade html5lib
- pip install --upgrade html2text
- pip install --upgrade python-dotenv

But requirements.txt is provided.

---

### To Run
Just:
1) clone the repository: git clone ...
2) create and activate a venv
3) install dependencies or use requirements.txt
4) put a .env file with your OpenAI API Key into the project root
5) python3 main.py


#### Please note that no milestones are provided and no guarantees that this software will be completed.
