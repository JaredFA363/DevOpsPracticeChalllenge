from xml.dom.minidom import getDOMImplementation, Document
from typing import List
import json
import random

def getDom() -> Document:
    impl = getDOMImplementation()
    dt = impl.createDocumentType(
        "html",
        "-//W3C//DTD XHTML 1.0 Strict//EN",
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
    )
    return impl.createDocument("http://www.w3.org/1999/xhtml", "html", dt)

def add_heading_to_html(quote) -> str:
    dom = getDom()
    html = dom.documentElement
    heading = dom.createElement("h1")
    heading.appendChild(dom.createTextNode(quote))
    html.appendChild(heading)
    return dom.toxml()

def get_random_quote():
    # loading json
    with open("content/quotes.json", "r") as f:
        data = json.load(f)
    
    # Obtain random quote
    random_quote = random.randint(0,len(data)-1)
    quote = data[random_quote]["quote"]
    return quote

def add_to_index(html):
    file_path = 'build/index.html'

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            print("HTML file generated")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    html = add_heading_to_html(get_random_quote())
    add_to_index(html)