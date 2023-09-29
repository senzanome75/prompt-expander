# Prompt Expander

## A Prompt Expander OpenAI-Based.


This repository concerns a **Prompt Expander**: a **Proof of Concept Software** that uses **OpenAI API** itself to improve the performance of a **Task** requested in input.

In my view **an initial expansion of the prompt should be the first task an agent should perform**. Optimizing the initial prompt (with something like Grammarly) could also help generate a better response.

---

The fundamental features will be:
- Expansion of a task into a number of intermediate steps necessary to carry out the task (implemented)
- Language correction (grammar, etc.) of the prompt and (maybe) translation into English (todo) 
- Understand whether a Google search is necessary to carry out a step and, if the answer is positive, carry it out (partially implemented)
- Understand whether scraping from a web page is necessary to carry out a step (partially implemented)
- Understand the language of task and reply with ISO 639-1 code (implemented)
- Use of Markdown as a standard for processing (both for **predictability of OpenAI GPT 3.5/4 output** and for **simplicity of manage** the format itself)
- Saving detailed logs to disk (in Markdown format), necessary later to reconstruct the inputs/prompts/outputs chain (to do)

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
6) enjoy? ;)

---

#### Please note that no milestones are provided and no guarantees that this software will be completed.

---

## Please note that, currently, the software has to be slowed down because it requires more than 10,000 tokens per minute... I'm working on it :/
