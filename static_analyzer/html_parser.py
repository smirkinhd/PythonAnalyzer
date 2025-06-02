from bs4 import BeautifulSoup

def extract_scripts(html_content: str):
    soup = BeautifulSoup(html_content, "html.parser")
    inline_scripts = [script.string for script in soup.find_all("script") if script.string]
    external_scripts = [script.get("src") for script in soup.find_all("script") if script.get("src")]
    return inline_scripts, external_scripts
