import os
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Example URL
url_basic = 'https://fearnation.club'  # https://fearnation.club/page/3/
url_page = 'https://fearnation.club/page/'


def fetch_and_parse_url(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        # Handle errors (e.g., page not found, server error)
        print(f"Error {response.status_code}: Unable to fetch the page")
        return None


def fetch_news(save_folder: str = r"data\news", interval_time=0.3):
    print(f"== Downloading news ==")
    for i in range(1, 1000):
        # do not fetch too frequently
        time.sleep(interval_time)

        # Fetch and parse the URL
        url_fear_nation = url_basic if i == 1 else url_page + str(i)
        soup = fetch_and_parse_url(url_fear_nation)
        if not soup:
            print(f"Network ERROR STOPS")
            break

        # Find all 'a' tags with class 'u-permalink'
        link_posts = soup.find_all('article', class_='feed post')

        # Print the href attribute of each link
        for post in link_posts:
            post_date_raw = post.find('time', class_='feed-date').text.strip()
            post_date = datetime.strptime(post_date_raw, '%b %d, %Y').strftime('%Y-%m-%d')
            post_save_name = post_date + ".txt"
            # Check already downloaded
            if os.path.isdir(save_folder):
                list_downloaded = os.listdir(save_folder)
                if post_save_name in list_downloaded:
                    print(f"{post_save_name} already exists")
                    continue
            else:
                os.mkdir(save_folder)

            print(f"fetching {post_save_name}")
            post_url = url_basic + post.find('a', class_='u-permalink').get('href')

            lines = [f"以下为{post_date}的新闻"]
            soup_article = fetch_and_parse_url(post_url)
            # Using CSS selector to find the target parent element
            contents_parent = soup_article.find('div', class_='single-content gh-content gh-canvas')

            is_started = False
            if contents_parent:
                # Iterate over the child elements
                for content in contents_parent.contents:
                    content_text = content.text
                    if content_text.startswith(r"• "):
                        is_started = True
                        lines.append(content_text.replace(r"• ", ""))
                    elif is_started and content_text == "":
                        break

            # save txt
            save_path = os.path.join(save_folder, post_save_name)
            with open(save_path, 'w', encoding="utf-8") as file:
                file.write("\n".join(lines))


if __name__ == '__main__':
    fetch_news()
