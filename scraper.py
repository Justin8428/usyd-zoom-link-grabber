import pandas as pd
# import requests
from bs4 import BeautifulSoup
# from canvasapi import Canvas
#import argparse


# scrape the links from table given a html with just the table portion
def scrape_link_zoom(import_data):
    page_content = BeautifulSoup(import_data, 'html5lib')
    data_table = page_content.find("table")
    
    data_rows = data_table.find_all("tr")
    zoom_links = []

    for i, row in enumerate(data_rows):
        # skip the header
        if i == 0:
            continue
        else:
            # handle each column separately
            date = row.find_all("td")[0].get_text()
            topic = row.find_all("td")[1].get_text()
            meetingID = row.find_all("td")[2].get_text()
            link = str('https://applications.zoom.us' + row.find_all("td")[3].a['href'])

            entry = {
                "date": date,
                "topic": topic,
                "meetingID": meetingID,
                "link": link
            }

            zoom_links.append(entry)

    df = pd.DataFrame(zoom_links)
    return df

""" # argument parser
parser = argparse.ArgumentParser(description='Scrape links from Canvas Zoom embedded iframe.')
parser.add_argument('-f', '--file', type=str, required=True, help="File to read in with your html, eg 'file.txt'")
parser.add_argument('-o', '--output', type=str, default="classes.csv", help = "Output csv file to store the results. Defaults to classes.csv")
args = parser.parse_args() # parse argument

if __name__ == "__main__":
    # lets say we 'cheat' and now we have the table
    import_data = open(args.file, 'r')
    df = scrape_link_zoom(import_data)
    df.to_csv(args.output) """