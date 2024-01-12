import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from url_list import websites

custom_headers = {
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,kn;q=0.7",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
}


def extract_md(soup, **options):
    converter = MarkdownConverter(**options).convert_soup(soup)
    return converter


def get_html_content(url, use_selenium=False):
    if use_selenium:
        return fetch_html_with_selenium(url)
    else:
        return fetch_html_with_requests(url)


def fetch_html_with_selenium(url, headless=True):
    options = uc.ChromeOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
    driver = uc.Chrome(options=options, enable_cdp_events=True, version_main=114)

    try:
        driver.get(url)
        driver.save_screenshot("tempDir/temp.png")
        return driver.page_source
    finally:
        driver.quit()


def fetch_html_with_requests(url):
    try:
        response = requests.get(url, headers=custom_headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def get_soup(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


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
    html_content = get_html_content(url, use_selenium=True)
    if html_content:
        save_html(html_content, url)
        parsed_content = get_soup(html_content)
        md_content = extract_md(parsed_content, heading_style='ATX')
        print(md_content)
        # filename = url.split('//')[-1].split('/')[0] + ".txt"
        # write_to_file(parsed_content, filename)
        # print(f"Content saved to {filename}")


if __name__ == "__main__":
    urls = websites[0]
    # for urls in websites:
    scrape_website(urls)
