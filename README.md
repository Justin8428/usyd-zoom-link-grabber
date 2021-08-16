# Grab links from Zoom Integration within Canvas
This is a short program designed to grab all Zoom links from a Canvas course webpage (e.g. at USyd, for pages that look like the below):

![image](https://user-images.githubusercontent.com/24475790/129573103-b68d9d36-6d06-47c3-ba60-b35ba82238ed.png)

## Dependencies
 - Python3
 - pandas
 - BeautifulSoup

## How to use ?!?!?!
Sit tight, because this might give you an aneurysm...

1. Clone this repo to your computer, and in that folder create a new subfolder called `data`.
2. Login to your course webpage in your web browser and go to the Zoom tab
3. Right click --> inspect
4. Find the **second** `<!DOCTYPE html>` present in the Inspect Element popout
5. In the line *underneath* that (shown below), right click --> Copy --> Copy outerHTML (for Chromium-based web browsers e.g. Microsoft Edge)

![image](https://user-images.githubusercontent.com/24475790/129575168-24c68e90-697e-4c20-9e8c-c0849a42eea5.png)

6. Within your newly created `data` subfolder create a new text file (e.g. `page1.txt`) and paste the contents in it.
7. In your computer's terminal, navigate to the cloned repo folder and run the `wrapper.py` Python script.
Usage: `python wrapper.py -i "./data" -o "classes.csv"` where `-i` is the folder to read in with your html files, eg './data' and `-o` is the output csv file to store the results, defaults to classes.csv.


## What if Zoom has more than one page?

![image](https://user-images.githubusercontent.com/24475790/129574340-aea0008d-ac3a-4473-9ea7-bc9e9517bbbd.png)

Repeat steps 3 to 6 for each page. Name each file sequentially alphabetically in the order you want them to be arranged in the final csv. (e.g. `page1.txt`, `page2.txt`, etc)

## Todo
 - Scrape it automatically so user does not have to manually copy html
 - Figure out OAuth (this is already giving me a headache....)
 - Maybe figure out CanvasAPI and/or Zoom API


(This is a public repo)

