import codecs
import sys
from bs4 import BeautifulSoup as Soup

def parse_html(file_name, framework="flask", supported_ext=["js", "css"]):
    framework = framework.lower()
    
    def parse_tags(tag):
        def parse_doc(doc):
            if doc == None:
                return doc
            else:
                if framework == "flask":
                    doc = "{{ url_for('static', filename = '" + doc + "') }}"
                else:
                    doc = "{% static '" + doc + "' %}"
                return doc

        if tag.name == "link":
            doc_link = tag["href"]
        else:
            doc_link = tag["src"]
        return str(tag).replace(doc_link, parse_doc(doc_link))

    html = open(file_name, "r").read()
    html_soup = Soup(html, "html.parser")

    for i in html_soup.find_all(["script", "link"]):
        i.replace_with(Soup(parse_tags(i), "html.parser"))

    clean_html = html_soup.prettify()
    if framework == "django":
        clean_html = "{% load static %}\n\n" + clean_html

    codecs.open(file_name, "w", "utf-8").write(clean_html)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""python restatic.py <file.html> <flask|django>""")
    else:
        parse_html(sys.argv[1], sys.argv[2])
