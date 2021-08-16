from scraper import scrape_link_zoom
import pandas as pd
from bs4 import BeautifulSoup
import os
import argparse


# argument parser
parser = argparse.ArgumentParser(description='Scrape links from Canvas Zoom embedded iframe. Multiple files version')
parser.add_argument('-i', '--input_folder', type=str, required=True, help="Folder to read in with your html files, eg './dir'")
parser.add_argument('-o', '--output', type=str, default="classes.csv", help = "Output csv file to store the results. Defaults to classes.csv")
args = parser.parse_args() # parse argument

if __name__ == "__main__":
    appended_data = []
    subfolder = args.input_folder
    files = [(subfolder + "/" + i) for i in os.listdir(subfolder)] # generate a list of files in the subfolder with the 'full' relative path
    for i, file in enumerate(files):
        import_data = open(file, 'r')
        df = scrape_link_zoom(import_data)
        appended_data.append(df)
        import_data.close()
    appended_data = pd.concat(appended_data)

    appended_data.to_csv(args.output)

# usage: python wrapper.py -i "./data" -o "something.csv"