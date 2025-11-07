# CS50 Project: Quote Generator
#### Video Demo:  <URL HERE>
#### Description: ####

A CS50 project: a Python shell GUI that fetches and displays quotes containing a specific keyword from user input. Uses JSON data, ZenQuotes API, and NLTK for text processing.

## Features:
- Interactive shell interface for entering keywords  
- Different quotes returned for the same keyword each time  
- Filters quotes using NLTK to validate English words  
- Minimal API overhead with ZenQuotes JSON caching

_Example Usage:_<br>

```bash
python quote_shell.py
```

_Quote with exact word included:_ 

***time*** <br>
_("Don't spend time beating on a wall, hoping to transform it into a door.", 'Coco Chanel')_ <br>

```bash
python quote_shell.py
```

_Quote with exact word included:_

***time*** <br>
_('Mastery is not a function of genius or talent, it is a function of time and intense focus applied to a particular field of knowledge.', 'Robert Greene')_

Best words to use for a variety of quotes: man, love, past

Worst words/(categories): joy, death, (specific foods ex. coffee), (specific animals ex. penguin)

## Directory Structure
### `Project`
- **`project/`**: Directory of Final Project for CS50P
    - **`project_dev_py3.12.2/`**: venv folder
    - `project.py`: Project Quote Generator main code
    - `README.md`: Description/instructions for Quote Generator project
    - `requirements.txt`: Quote Generator project dependencies list
    - `test_project.py`: Tests for Quote Generator project

## Design Decisions:
<!-- if you debated certain design choices, explaining why you made them -->
#### Virtual Environment
Included virtual environment instructions for accessability in README.md

Utilized Virtual Environtmnet:
- stable/reproduceable environment
- isolate dependencies between projects

#### User Input Validation
Utilized to enforce correct syntax (text/string input) and semantic value (English words).

- must be a string/text
- must be more than 2 letters
- must be a valid English word

#### NLTK Library
Utilized:
- tokenize to parse the user input keyword from quotes for efficiency/reduce error probability

- NTLK library to help filter English words from nonsense

#### User Input
Chose to allow users to type in their own keyword for search compared to a set category/genre/mood.

Pros:
- generate quotes from specific search word

Cons:
- difficult/unrefined validation compared to pre-set category/words

- limited quotes available at a time with the API utilized + the variety of user input words available create such a large scope that it limits successful quote generation

#### Zenquotes API
decided to use zenquotes API due to it's ability to cache a small JSON response of quotes on a changing/rotating basis for a wider variety of quotes with efficiency compared to large data sets

## Installation
Virtual Environment Setup:
utilize virtual environments to isolate dependencies

#### 1. Install Python
>[!NOTE]
>NLTK requires Python versions 3.7, 3.8, 3.9, 3.10 or 3.11

[Official Python download documentation](https://www.python.org/downloads/)


#### 2. Setting up Virtual Environment
Create a virtual environment.

[Python Virtual Environment Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)

Before installing NLTK; [NLTK documentation for installation](https://www.nltk.org/install.html)

#### 3. Installing Dependencies
Activate virtual environment.


Unix/macOS:
```
source my_venv/bin/activate
```
Windows:
```
my_venv\Scripts\activate
```

Install project dependencies using the `requirements.txt` file:
```
pip install -r requirements.txt
```
#### Dependencies Notes
Punkt tokenizer only needs to be downloaded once; **already implemented with download check in project.py code**

NLTK requires Punkt tokenizer:<br>
```
import nltk
nltk.download('punkt')
```

# Citations:
## WordNet
Princeton University "About WordNet." WordNet. Princeton University. 2010.

### Description
WordNet is an English database concerning words, their meanings, semantic relationships, and properties in linguistics.

### Source
- Website: [WordNet Homepage](https://wordnet.princeton.edu/)
- Repository: [WordNet GitHub Repository](https://github.com/wordnet/wordnet)
- Authors: Princeton University Cognitive Science Laboratory

### License
WordNet is distributed under the [WordNet License](https://wordnet.princeton.edu/license-and-commercial-use).

## NLTK
Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O'Reilly Media Inc.

## Python
Python Software Foundation. (2024). Download Python. Retrieved from https://www.python.org/downloads/

## ZenQuotes
Inspirational quotes provided by <a href="https://zenquotes.io/" target="_blank">ZenQuotes API</a>
