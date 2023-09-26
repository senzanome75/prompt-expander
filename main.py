### Dependencies ###
# pip install --upgrade pip
# pip install --upgrade openai
# pip install --upgrade googlesearch-python
# pip install --upgrade beautifulsoup4
# pip install --upgrade html5lib
# pip install --upgrade html2text


# Import Stuff
import os
import re
import openai
import requests
import html2text
from googlesearch import search
from bs4 import BeautifulSoup

# Set your OpenAI API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


def basilar_query_to_openai(history):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history,
        temperature=0.6,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    history.append({
        "role": "assistant",
        "content": response["choices"][0]["message"]["content"]
    })

    return history


def search_google(query):
    try:
        # Search on Google
        results = search(query, num_results=20, advanced=True, lang="it")
        return results

    except Exception as e:
        return False


def extract_text_from_html_page(url):
    # Request to webpage
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML of the page
    soup = BeautifulSoup(response.text, "html5lib")

    # Use html2text to convert HTML to Markdown
    text_maker = html2text.HTML2Text()
    # text_maker.ignore_links = True

    markdown_text = text_maker.handle(soup.prettify())

    return markdown_text





### The script starts here ###

task = input("Please enter the task to be performed: ")

history = [
    {
        "role": "user",
        "content": "Task to perform: " + task
    },
    {
        "role": "assistant",
        "content": "Decide how many steps are needed to accomplish the task and list them in a numbered list consisting of one line for each step, separating each steps with blank lines; format the response at this query in markdown."
    }
]

first_step_history = basilar_query_to_openai(history)



# steps = first_step_prompt[2]["content"].split("\n\n")


# Define the RegEx
first_step_regex = r"\d+.\s\*\*(.+)\*\*\:\s(.+)\n\n"

# Extract the steps
steps = re.findall(first_step_regex, first_step_history[2]["content"])

