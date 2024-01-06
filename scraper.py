import requests
from bs4 import BeautifulSoup

from url_list import websites

custom_headers = {
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,kn;q=0.7",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
}


def fetch_page(url):
    try:
        response = requests.get(url, headers=custom_headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()


def write_to_file(content, filename):
    with open(f"txt_files/{filename}", 'w', encoding='utf-8') as file:
        file.write(content)


def save_html(html_content, url):
    filename = url.split('//')[-1].split('/')[0] + "_raw.html"
    with open(f"html_files/{filename}", 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML saved to {filename}")


def scrape_website(url):
    print(f"Scraping {url}")
    html_content = fetch_page(url)
    if html_content:
        save_html(html_content, url)
        parsed_content = parse_content(html_content)
        filename = url.split('//')[-1].split('/')[0] + ".txt"  # Generating filename from URL
        write_to_file(parsed_content, filename)
        print(f"Content saved to {filename}")


if __name__ == "__main__":
    # url = websites[3]
    for url in websites:
        scrape_website(url)
