# Import Stuff
import os
import re
import openai
import requests
import html2text
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Take environment variables from .env file
load_dotenv()

# Set OpenAI API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


def basilar_query_to_openai(query_for_task):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=query_for_task,
        temperature=0.6,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["message"]["content"]


def need_search_on_google(step_title, step_for_task):
    query_for_step = "Do I need to do a Google search to do this? Answer exclusively with yes or no.\n" + step_title + ": " + step_for_task

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
    query_for_step = "Do I need to do scraping on the web to do this? Answer exclusively with yes or no.\n" + step_title + ": " + step_for_task

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


def what_language_is_it_written_in(prompt):
    prompt = "In what language is the following text? Reply exclusively with an ISO 639-1 code.\n" + prompt

    prompt = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=prompt,
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
# Input the task
task = input("Please enter the task to be performed: ")

# Build the first prompt expansion
history = [
    {
        "role": "user",
        "content": "Task to perform: " + task
    },
    {
        "role": "assistant",
        "content": "Decide how many steps are needed to accomplish the task and list them in a numbered list. The list must consisting of one line for each step, separating each steps with a blank line; format the response at this query in markdown."
    }
]

# First query to OpenAI
first_step_response = basilar_query_to_openai(history)

# Debug Print
print("---")
print("First step raw response from OpenAI")
print(first_step_response)
print("---")

# Extract language from task in ISO 639-1 code
language = what_language_is_it_written_in(task)

# Debug Print
print("---")
print("ISO 639-1 language code")
print(language)
print("---")

# Define the RegEx
first_step_regex = r"\d+.\s\*\*(.+)\*\*\:\s(.+)\n\n"

# Extract the steps
steps = re.findall(first_step_regex, first_step_response)

# Initialize some variables
dictionary_step = dict()
list_steps = list()
step_number = 0

# Debug Print
print(steps)
print(type(steps))

# Fill a list with the step each in a dictionary
for step in steps:
    dictionary_step = {
        "step_number": step_number,
        "step_title": step[0],
        "step_for_task": step[1],
        "need_search_on_google": need_search_on_google(step[0], step[1]),
        "need_scraping_on_web": need_scraping_on_web(step[0], step[1])
    }

    step_number += 1

    # Debug Print
    print(dictionary_step)
    print("---")

    list_steps.append(dictionary_step)
