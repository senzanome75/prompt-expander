# Import Stuffs
import os
import re
import openai
import requests
import html2text
import time
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Take environment variables from .env file
load_dotenv()

# Set OpenAI API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


def reply_boolean_to_assertion(assertion):
    if assertion.lower() == "yes":
        return True
    elif assertion.lower() == "no":
        return False


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


def is_the_prompt_correct(prompt):
    prompt = "Does this text need to be corrected semantically or syntactically? Answer exclusively with yes or no.\n" + prompt

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


def prompt_corrector(prompt):
    prompt = "Correct semantically and syntactically this text: " + prompt

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


def is_it_geolocalizable(prompt):
    prompt = "Does this text refer to a geographic location? Answer exclusively with yes or no.\n" + prompt

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


def geolocalize(prompt):
    prompt = "To which geographic location does the following text refer? Reply only with a geographic location." + prompt

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


def need_search_on_google(step_for_task):
    query_for_step = "Do I need to do a Google search to do this? Answer exclusively with yes or no.\n" + step_for_task

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


def need_scraping_on_web(step_for_task):
    query_for_step = "Do I need to do scraping on the web to do this? Answer exclusively with yes or no.\n" + step_for_task

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

    return response["choices"][0]["message"]["content"].lower()


def search_google(query, query_language):
    try:
        # Search on Google
        results = search(query, num_results=10, advanced=True, lang=query_language)
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


def it_contains_url(prompt):
    prompt = "Does this text contain a URL? Reply exclusively with yes or no.\n" + prompt

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


def contains_url(prompt):
    prompt = "Extract the URL contained in this text; reply to this query with a URL only.\n" + prompt

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


### The script starts here ###
# Input the task
task = input("Please enter the task to be performed: ")
print("---")

# Examine if input task is semantically and syntactically correct
need_corrections = is_the_prompt_correct(task)
need_corrections_boolean = reply_boolean_to_assertion(need_corrections)

# Debug print
print("Does this text need to be corrected semantically or syntactically? " + need_corrections)


if need_corrections_boolean:
    task = prompt_corrector(task)

    # Debug Print
    print("The task after correction is: " + task)

print("---")


the_prompt_is_geolocalizable = is_it_geolocalizable(task)

# Debug Print
print("Does the task talk about a geographic location? " + the_prompt_is_geolocalizable)


if reply_boolean_to_assertion(the_prompt_is_geolocalizable):
    place = geolocalize(task)

    # Debug Print
    print("The geographic location in the task is: " + place)
print("---")


the_prompt_contain_url = it_contains_url(task)

# Debug Print
print("Does the prompt contains URL? " + the_prompt_contain_url)


if reply_boolean_to_assertion(the_prompt_contain_url):
    url = contains_url(task)

    # Debug Print
    print("The URL in the task is: " + url)
print("---")


# Extract language from task in ISO 639-1 code
language = what_language_is_it_written_in(task)

# Debug Print
print("ISO 639-1 language code: " + language)
print("---")


# Build the first prompt expansion
history = [
    {
        "role": "user",
        "content": "Task to perform: " + task
    },
    {
        "role": "assistant",
        "content": "Decide how many steps are needed to accomplish the task and list them in a numbered list. The list must consisting of one line for each step; format the response at this query in markdown."
    }
]


# Debug Print
print("Now wait 61 seconds for avoid exceeding 10,000 tokens/min")
print("---")

# To avoid exceeding 10,000 tokens/min
time.sleep(61)


# First query to OpenAI
first_step_response = basilar_query_to_openai(history)

# Debug Print
print("First step raw response from OpenAI")
print(first_step_response)
print("---")


# Define the RegEx
# To extract the steps from numbered list in markdown - It may cause problems and not capture the query output correctly
numbered_list_regex = r"\d+\.\s(.+)\n+"
# To extract the points from bulleted list in markdown - It may cause problems and not capture the query output correctly
bulleted_list_regex = r"-\s(.+)\n+"

# Extract the steps from numbered list in markdown
steps = re.findall(numbered_list_regex, first_step_response + "\n")

# Initialize some variables
dictionary_step = dict()
list_steps = list()
step_number = 1

# Debug Print
print(steps)
print(type(steps))

# Fill a list with the step each in a dictionary
for step in steps:
    # Debug Print
    print("Now wait 61 seconds for avoid exceeding 10,000 tokens/min")
    print("---")

    # To avoid exceeding 10,000 tokens/min
    time.sleep(61)

    # Each step in a dictionary
    dictionary_step = {
        "step_number": step_number,
        "step_for_task": step,
        "need_search_on_google": reply_boolean_to_assertion(need_search_on_google(step)),
        "need_scraping_on_web": reply_boolean_to_assertion(need_scraping_on_web(step)),
        "contains_geographic_location": reply_boolean_to_assertion(is_it_geolocalizable(step)),
        "contains_url": reply_boolean_to_assertion(it_contains_url(step))
    }

    step_number += 1

    # Debug Print
    print(dictionary_step)
    print("---")

    # Add the dictionary to the list
    list_steps.append(dictionary_step)

# To be continued...
