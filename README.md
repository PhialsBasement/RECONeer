# RECONeer

RECONeer is a Python script that performs reconnaissance tasks by searching for PDF files and social media profiles related to a given search query. It utilizes the Selenium WebDriver to automate web browsing and scraping tasks.
Features
    * Searches for PDF files related to the provided search query on Google
    * Supports two types of search: Wide Lookup and Specific Lookup
    * Downloads the found PDF files and saves them in a directory named "downloaded_pdfs"
    * Searches for social media profiles (Facebook, Twitter, Instagram, LinkedIn) related to the search query
    * Prints the URLs of the found social media profiles

# Prerequisites

Before running the script, make sure you have the following dependencies installed:
    * Python 3.x
    * Selenium WebDriver
    * Chrome WebDriver (chromedriver) executable in the system PATH
    *  Required Python packages: os, requests, selenium, transliterate

# Usage

  1. Clone the repository or download the script file.
  2. Install the required dependencies by running the following command:
  3. Make sure you have the Chrome WebDriver executable (chromedriver) in your system PATH or in the same directory as the script.
  4. Run the script using the following command:
    ```py
    python reconeer.py
    ```
  5. When prompted, enter the name or search query you want to perform reconnaissance on.
  6. Choose the type of search by entering 1 for Wide Lookup or 2 for Specific Lookup.
  7. The script will start the Chrome browser and perform the searches automatically.
  8. The found PDF files will be downloaded and saved in the "downloaded_pdfs" directory.
    The URLs of the found social media profiles will be printed in the console.
    Once the script finishes executing, the browser will be closed automatically.
    
