# scrap-youtube-comments-with-python

YouTube Comment Scraper
This script allows you to scrape comments from a YouTube video using Selenium and Chrome WebDriver.

Prerequisites
Before running the script, make sure you have the following installed:

Python 3.x
Selenium library (pip install selenium)
Chrome WebDriver
Download the appropriate Chrome WebDriver for your system and update the webdriver_path variable in the script with the correct path to the WebDriver executable.

Usage
Clone this repository or copy the script to your local machine.

Run the script using the following command:

Copy code
python youtube_comment_scraper.py
Enter the URL of the YouTube video when prompted.

Wait for the script to scrape the comments from the video.

The extracted comments will be displayed on the console and saved to a file named youtube_comments.txt.

Note
The script scrolls down the page multiple times to load more comments. Adjust the scroll_pause_time variable if needed to control the scroll speed.

In case of any exceptions or errors, they will be displayed on the console.

Make sure you comply with YouTube's terms of service and respect the privacy of the users when using this script.

