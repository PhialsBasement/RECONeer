# RECONeer

RECONeer is a Python program that automates the process of searching for PDF documents and social media profiles related to a given search query. It utilizes web scraping techniques to extract relevant information from Google search results.

# Features

Search for PDF documents based on a user-provided search query
Option to perform a wide lookup or a specific lookup for PDF documents
Download and save the found PDF files locally
Search for social media profiles (Facebook, Twitter, Instagram, LinkedIn) related to the search query
Display the URLs of the found social media profiles
Analyze the downloaded PDF documents using an AI-powered chat interface

# Prerequisites

Before running the program, make sure you have the following dependencies installed:

Python (version 3.x)
Selenium WebDriver
Chrome browser
Required Python libraries: requests, PyPDF2, colorama, ascii_magic, anthropic

# Installation

 Clone the repository:

    shell

    git clone https://github.com/your-username/RECONeer.git

# Install the required Python libraries:

    shell

    pip install -r requirements.txt

# Set up the Anthropic API key:
 Sign up for an Anthropic API account and obtain an API key.
 Replace "your-api-key" in the RECONeerChat.py file with your actual API key.

# Usage

Run the RECONeer.py script:

    shell

    python RECONeer.py

   Enter the search query when prompted.
    Choose the type of search:
        Enter 1 for a wide lookup (searches for the query along with "filetype:pdf").
        Enter 2 for a specific lookup (searches for the exact query within quotes along with "filetype:pdf").
    The program will search for PDF documents and social media profiles based on the provided query.
    The found PDF files will be downloaded and saved in the downloaded_pdfs directory.
    The URLs of the found social media profiles will be displayed in the console.
    After the search is complete, the AI-powered chat interface (RECONeerChat.py) will open automatically.
    In the chat interface, you can select a downloaded PDF document to analyze or input your own PDF body text as a string.
    Provide a prompt or question to guide the AI in analyzing the selected PDF document.
    The AI will generate a summary or analysis based on your prompt and display the output in the console.
    You can continue analyzing additional PDF documents or exit the program.

# License

This project is licensed under the MIT License.
Acknowledgements

  Anthropic for providing the AI-powered chat interface.
    Selenium for web scraping functionality.
    PyPDF2 for PDF extraction and manipulation.
    colorama for color output in the console.
    ascii_magic for displaying ASCII art.

# Disclaimer

Please use this program responsibly and respect the terms of service of the websites being scraped. The authors of this program are not responsible for any misuse or illegal activities conducted using this tool.
