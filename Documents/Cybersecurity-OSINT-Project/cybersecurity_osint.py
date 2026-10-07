import requests
import json
import xml.etree.ElementTree as ET
from datetime import datetime


# Public cybersecurity RSS feed
RSS_URL = "https://www.cisa.gov/cybersecurity-advisories/all.xml"

# Number of articles to collect
MAX_ARTICLES = 10

# Output file
OUTPUT_FILE = "cybersecurity_news.json"


def fetch_feed(url):
    """
    Download the RSS feed from the specified URL.
    """

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Cybersecurity-OSINT-Student-Project/1.0"
            }
        )

        response.raise_for_status()

        return response.content

    except requests.exceptions.Timeout:
        print("ERROR: The request timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to the website.")
        return None

    except requests.exceptions.HTTPError as error:
        print(f"ERROR: HTTP request failed: {error}")
        return None

    except requests.exceptions.RequestException as error:
        print(f"ERROR: Request failed: {error}")
        return None


def parse_feed(xml_data):
    """
    Parse the RSS/XML data and extract article information.
    """

    if xml_data is None:
        return []

    try:
        root = ET.fromstring(xml_data)

    except ET.ParseError:
        print("ERROR: Could not parse the RSS/XML data.")
        return []

    articles = []

    for item in root.findall(".//item")[:MAX_ARTICLES]:

        title_element = item.find("title")
        link_element = item.find("link")
        date_element = item.find("pubDate")
        description_element = item.find("description")

        title = (
            title_element.text.strip()
            if title_element is not None and title_element.text
            else "No title available"
        )

        link = (
            link_element.text.strip()
            if link_element is not None and link_element.text
            else "No link available"
        )

        publication_date = (
            date_element.text.strip()
            if date_element is not None and date_element.text
            else "Date unavailable"
        )

        description = (
            description_element.text.strip()
            if description_element is not None and description_element.text
            else "No description available"
        )

        article = {
            "title": title,
            "link": link,
            "publication_date": publication_date,
            "description": description
        }

        articles.append(article)

    return articles


def save_results(articles):
    """
    Save collected cybersecurity information to a JSON file.
    """

    output = {
        "collection_time": datetime.now().isoformat(),
        "source": RSS_URL,
        "article_count": len(articles),
        "articles": articles
    }

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(output, file, indent=4, ensure_ascii=False)

        print(f"\nData successfully saved to {OUTPUT_FILE}")

    except OSError as error:
        print(f"ERROR: Could not save the output file: {error}")


def display_results(articles):
    """
    Display collected articles in the terminal.
    """

    if not articles:
        print("No cybersecurity articles were collected.")
        return

    print("\n" + "=" * 70)
    print("CYBERSECURITY OSINT NEWS RESULTS")
    print("=" * 70)

    for number, article in enumerate(articles, start=1):

        print(f"\nArticle {number}")
        print("-" * 70)
        print(f"Title: {article['title']}")
        print(f"Date: {article['publication_date']}")
        print(f"Link: {article['link']}")

        description = article["description"]

        if len(description) > 250:
            description = description[:250] + "..."

        print(f"Description: {description}")


def main():
    """
    Main program function.
    """

    print("=" * 70)
    print("Cybersecurity OSINT Automated Data Collector")
    print("=" * 70)

    print("\nConnecting to public cybersecurity information source...")

    xml_data = fetch_feed(RSS_URL)

    if xml_data is None:
        print("\nThe program could not collect data.")
        return

    print("Data successfully downloaded.")

    articles = parse_feed(xml_data)

    print(f"Collected {len(articles)} cybersecurity articles.")

    display_results(articles)

    save_results(articles)

    print("\nCollection completed.")


if __name__ == "__main__":
    main()