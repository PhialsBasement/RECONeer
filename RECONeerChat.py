import anthropic
import os
import PyPDF2
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import pyglet, sys, time
import Gif_Ascii_Animator as anim
from ascii_magic import AsciiArt
colorama_init()
pdf_directory = "./downloaded_pdfs"
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]

while True:
    my_art = AsciiArt.from_image('untitled-f000056.png')
    my_art.to_terminal(columns=80)
    print("Available PDF documents:")
    for i, pdf in enumerate(pdf_files, start=1):
        print(f"{i}. {pdf}")
    print("99. Input your own PDF body text as a string")

    s = input("Select a PDF document you wish to import into the API (enter the number): ")

    if s == "99":
        text = input()
    elif s.isdigit() and 1 <= int(s) <= len(pdf_files):
        selected_pdf = pdf_files[int(s) - 1]
        pdf_path = os.path.join(pdf_directory, selected_pdf)

        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

        print("Extracted text from the PDF:")
        print(text)
    else:
        print("Invalid input. Please try again.")
    client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="",
    )
    lf = input("What are you looking for in this file: ")
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0,
        system="You are a PDF analysis bot. You analyze PDF docs and do your best to summirize them according to the users request. You may analyze PDF documents in other languages, however all output must be in ENGLISH",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"ALL output must be in ENGLISH EVEN IF THE PDF IS IN ANOTHER LANGUAGE, Analyze this PDF file for {lf} BODY: {text}"
                    }
                ]
            }
        ]
    )
    print(message.content[0].text)
    input("Press Enter to Analyse another doc")














