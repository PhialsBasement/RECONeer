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
    ```
    python reconeer.py
    ```
  5. When prompted, enter the name or search query you want to perform reconnaissance on.
  6. Choose the type of search by entering 1 for Wide Lookup or 2 for Specific Lookup.
  7. The script will start the Chrome browser and perform the searches automatically.
  8. The found PDF files will be downloaded and saved in the "downloaded_pdfs" directory.
    The URLs of the found social media profiles will be printed in the console.
    Once the script finishes executing, the browser will be closed automatically.

# Notes
   The script uses the Chrome WebDriver by default. If you prefer to use a different browser, you need to install the corresponding WebDriver and update the code accordingly.
    The script handles exceptions and prints "NO RESULTS FOUND" if no PDF files or social media profiles are found for the given search query.
    The downloaded PDF files are named in the format "searchquery_number.pdf" to avoid overwriting files with the same name.
    The script waits for a maximum of 10 seconds for the search results to load. If the results take longer to load, you may need to increase the timeout value in the WebDriverWait function.

# Disclaimer

Please use this script responsibly and in compliance with the terms of service of the websites being scraped. Respect the privacy and intellectual property rights of others.

# License

This project is licensed under the MIT License.

Feel free to contribute to the project by submitting pull requests or reporting issues on the GitHub repository.
    
