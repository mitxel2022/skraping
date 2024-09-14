import platform
import requests
import os


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service



if platform.system() == "Windows":
    firefox_profile_path = os.path.expanduser("~") + os.sep + 'AppData' + os.sep + 'Local' + os.sep + 'Mozilla' + os.sep + 'Firefox' + os.sep + 'Profiles' + os.sep + 'fedk3ctb2.default-release'
else:
    firefox_profile_path = os.path.expanduser("~") + "/snap/firefox/common/.mozilla/firefox/inmersprofile.default-release"

# Create a FirefoxOptions object with your profile path
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--profile')
firefox_options.add_argument(firefox_profile_path)

# service = Service(log_path=os.devnull)

# Create a new Firefox driver with your options
try:
    # driver = webdriver.Firefox(options=firefox_options, service=service)
    driver = webdriver.Firefox(options=firefox_options)
except:
    print("ERROR")
    driver.quit()

def extract_youtube_trending_titles():
    url = "https://www.youtube.com/feed/trending"
    driver.get(url)
    content = driver.page_source
    #driver.quit()

    soup = BeautifulSoup(content, 'html.parser')
    titles = soup.find_all('h3', {'class': 'title-and-badge style-scope ytd-video-renderer'})
    return [title.text.strip() for title in titles]

def get_browser_content(url):
    driver = webdriver.Chrome()
    driver.get(url)
    content = driver.page_source
    driver.quit()
    return content


def extract_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h1')
    return [title.text for title in titles]

def fetch_webpage(url):
    response = requests.get(url)
    return response.text

def main():
    # Example usage
    trending_titles = extract_youtube_trending_titles()
    print(trending_titles)


if __name__ == '__main__':
    main()
