import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the Chrome WebDriver executable
webdriver_path = '/usr/local/bin/chromedriver'  # Update with the correct path

# YouTube video URL
url = input("Enter Your Youtube Video URL: ")

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=Service(webdriver_path))

# Open the YouTube video URL
driver.get(url)

# Wait for the comments section to load
wait = WebDriverWait(driver, 10)
comments_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-comments')))
driver.execute_script("arguments[0].scrollIntoView();", comments_section)

# Scroll down the page multiple times to load more comments
scroll_pause_time = 2
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all the comment elements
comment_elements = driver.find_elements(By.CSS_SELECTOR, 'ytd-comment-renderer')

# Extract the commenter names, comments, time, and date
comments = []
for comment in comment_elements:
    try:
        commenter_name = "@" + comment.find_element(By.CSS_SELECTOR, '#author-text span').text.strip()
        comment_text = comment.find_element(By.CSS_SELECTOR, '#content-text').text.strip()
        comments.append({"Commenter Name": commenter_name, "Comment": comment_text})
    except Exception as e:
        print("Exception occurred:", str(e))

# now Print the extracted comments
if comments:
    for comment in comments:
        print(f"Commenter Name: {comment['Commenter Name']}")
        print(f"Comment: {comment['Comment']}")
else:
    print("No comments found.")

# Save the comments to a file
filename = "youtube_comments.txt"
with open(filename, "w") as file:
    if comments:
        for comment in comments:
            file.write(f"Commenter Name: {comment['Commenter Name']}\n")
            file.write(f"Comment: {comment['Comment']}\n")
    else:
        file.write("No comments found.")

print(f"Comments saved to {filename}")

# Quit the WebDriver
driver.quit()
