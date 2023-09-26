### Dependencies ###
# pip install --upgrade pip
# pip install --upgrade openai
# pip install --upgrade googlesearch-python
# pip install --upgrade beautifulsoup4
# pip install --upgrade html5lib
# pip install --upgrade html2text
# pip install --upgrade python-dotenv


# Import Stuff
import os
import re
import openai
import requests
import html2text
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file.

# Set your OpenAI API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


def basilar_query_to_openai(query_for_task):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=query_for_task,
        temperature=0.6,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["message"]["content"]


def need_search_on_google(step_title, step_for_task):
    query_for_step = "Do I need to do a Google search to do this? Answer only with yes or no.\n" + step_title + ": " + step_for_task

    query_for_step = [
        {
            "role": "user",
            "content": query_for_step
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=query_for_step,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["message"]["content"]


def need_scraping_on_web(step_title, step_for_task):
    query_for_step = "Do I need to do scraping to do this? Answer only with yes or no.\n" + step_title + ": " + step_for_task

    query_for_step = [
        {
            "role": "user",
            "content": query_for_step
        }
    ]


    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=query_for_step,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["message"]["content"]


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

first_step_response = basilar_query_to_openai(history)

# Define the RegEx
first_step_regex = r"\d+.\s\*\*(.+)\*\*\:\s(.+)\n\n"

# Extract the steps
steps = re.findall(first_step_regex, first_step_response)

# Initialize some variables
dictionary_step = dict()
list_steps = list()
step_number = 0

# Fill a list with the step each in a dictionary
for step in steps:
    dictionary_step = {
        "step_number": step_number,
        "step_title": step[0],
        "step_for_task": step[1],
        "need_search_on_google": need_search_on_google(step[0], step[1]),
        "need_scraping_on_web": need_scraping_on_web(step[0], step[1])
    }

    step_number =+ 1

    print(dictionary_step)
    print("---")


    list_steps.append(dictionary_step)
