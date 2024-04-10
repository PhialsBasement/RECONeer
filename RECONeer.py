import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import transliterate
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from ascii_magic import AsciiArt
import pygame as pg
pg.mixer.init()
colorama_init()
# Function to download PDF files
my_art = AsciiArt.from_image('untitled-f000056.png')
my_art.to_terminal(columns=80)
print({Fore.YELLOW})
def download_pdf(url, filename):
    try:
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
    except:
        print("Lol")
pg.mixer.music.load("LifeGameAnonCode.mp3")
pg.mixer.music.play(99)
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Prompt the user for the search query
search_query = input("Enter the name ")
# Ask for type of search
TSearch = input("Enter 1 for Wide Lookup, 2 for Specific Lookup")
social_media_search_url = f'''https://www.google.com/search?q=%22{search_query}%22+site%3Afacebook.com+OR+site%3Atwitter.com+OR+site%3Ainstagram.com+OR+site%3Alinkedin.com'''
# Construct the Google search URL with the PDF dork
if int(TSearch) == 1:
    search_url = f"https://www.google.com/search?q={search_query}+filetype:pdf"
else:
    search_url = f'''https://www.google.com/search?q="{search_query}"+filetype:pdf'''
try:
    # Navigate to the Google search URL
    driver.get(search_url)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
    div_element = driver.find_elements(By.ID,"topstuff")
    elements_inside_div = div_element[0].find_elements(By.XPATH, ".//*")
    if len(elements_inside_div) == 0:
        

        # Find all the PDF links on the first page
        pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")

        # Create a directory to store the downloaded PDFs
        os.makedirs("downloaded_pdfs", exist_ok=True)
        dlpdfs = []
        # Download each PDF file
        for link in pdf_links:
            pdf_url = link.get_attribute("href")
            if not dlpdfs.__contains__(pdf_url):

                filename = os.path.join("downloaded_pdfs", f"{search_query}_{pdf_links.index(link) + 1}.pdf")
                download_pdf(pdf_url, filename)
                print(f"Downloaded: {filename}")
                dlpdfs.append(pdf_url)
    else:
        print("NO RESULTS FOUND")

    # Navigate to the Google search URL for social media profiles
    driver.get(social_media_search_url)
    
    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
    
    # Find all the social media profile links on the first page
    profile_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='facebook.com/'], a[href*='twitter.com/'], a[href*='instagram.com/'], a[href*='linkedin.com/in/']")
    div_element = driver.find_elements(By.ID,"topstuff")
    elements_inside_div = div_element[0].find_elements(By.XPATH, ".//*")
    if len(elements_inside_div) == 0:
        # Print the social media profile URLs
        print("Social Media Profiles:")
        for link in profile_links:
            profile_url = link.get_attribute("href")
            print(profile_url)
    else:
        print("NO RESULTS FOUND")
finally:
    input("Continue to AI Chat")
    print("OPENING AI CHAT")
    os.system('python RECONeerChat.py')
    # Close the browser
    driver.quit()
    input()