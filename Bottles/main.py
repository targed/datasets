# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import os

# URL of the Google Image Search API
url = "https://www.google.com/search?q=nalgene+wide+mouth+water+bottle&rlz=1C1GCEU_enUS832US832&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJ5J6Y5J_iAhXOyDgGHQGzDZQQ_AUIEigB&biw=1366&bih=657"

# Sending request to the URL
response = requests.get(url)

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Creating a directory to store the images
if not os.path.exists("nalgene_images"):
    os.makedirs("nalgene_images")

# Finding all the image tags
img_tags = soup.find_all("img")

# Downloading the images
for i, img in enumerate(img_tags):
    try:
        img_url = img["src"]
        img_data = requests.get(img_url).content
        with open(f"nalgene_images/nalgene_{i}.jpg", "wb") as handler:
            handler.write(img_data)
    except:
        pass
