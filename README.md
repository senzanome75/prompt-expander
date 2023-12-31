# Prompt Expander

## A Prompt Expander OpenAI-Based.

### Introduction
This repository concerns a **Prompt Expander**: a **Proof of Concept Software** that uses **OpenAI API** itself to improve the performance of a **Task** requested in input for a hypothetical **Agent**.

In my view **an initial expansion of the prompt should be the first task an Agent should perform**. Optimizing the initial prompt (with something Grammarly-like) could also help generate a better response.

In addition to this, an Agent should extract as much information as possible from the input task such as: **geographical locations**, **ISO 639-1 language codes**, **URLs**, etc. for possible later use.

---

IMPORTANT: using **Markdown** as the format in which to request responses to **prompts** opens up the possibility of using common **regexes** to manage the output from GPT 3.5/4 by taking advantage of the **predictability of the output**.

---

### The features will:
- Expansion of a task into a number of intermediate steps necessary to carry out the task (implemented)
- Language correction (grammar, etc.) of the prompt (implemented)
- Understand if the task includes a geographical locations and extract it (implemented)
- Understand the language of task and reply with ISO 639-1 language code (implemented)
- Understand if the task includes a URL and extract it (implemented)
- Understand whether a Google search is necessary to carry out a step and, if the answer is positive, carry it out (partially implemented)
- Understand whether scraping from a web page is necessary to carry out a step (partially implemented)
- Saving detailed logs to disk (in Markdown format), necessary later to reconstruct the inputs/prompts/outputs chain (to do)
- Use of Markdown as a standard for processing (both for **predictability of OpenAI GPT 3.5/4 output** and for **simplicity of manage** the format itself with common regexes)


If you want more insight you could read this post blog: https://ingegnerealbano.com/prompt-expansion-con-openai-potrebbe-essere-una-nuova-idea/

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

### To Run Just
1) clone the repository: git clone ...
2) create and activate a venv
3) install dependencies or use requirements.txt
4) put a .env file with your OpenAI API Key into the project root
5) python3 main.py
6) enjoy? ;)

---

#### Please note that no milestones are provided and no guarantees that this software will be completed.

---

## Please note that, currently, this software has to be slowed down because it requires more than 10,000 tokens per minute...
