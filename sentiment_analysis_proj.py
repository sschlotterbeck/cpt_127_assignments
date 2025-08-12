"""
"Looking Back: Sentiment Analysis of Elon Musk's Wikipedia Page Over 10+ Years"
"Intro to Sentiment Analysis with Python" assignment - CPT 127 - Summer 2025 Term
Sylvia Schlotterbeck - August 10, 2025

The following is the code I wrote for the "Intro to Sentiment Analysis with Python" assignment
for CPT 127 during the summer of 2025. The program takes a csv file that contains 22 URLs from the Wayback
Machine on archive.org which contain archived versions of the Wikipedia entry for Elon Musk in six month intervals
starting in January of 2015 and continuing until June of 2025, and parses the body of the text for each entry 
from the html code. it then runs that through a Natural Language Processing pipeline for sentiment analysis
using the TextBlob library, calculating the polarity score (ranges from -1.0 to 1.0, which -1.0 signifying
very negative sentiment, 1.0 signifying very positive sentiment, and 0 signifying neutral sentiment) and
subjectivity score (ranges from 0.0 to 1.0 -- 0.0 being extremely objective and 1.0 being extremely subjective)
of each version, adding the data to a pandas DataFrame, and plotting the scores to visual the changes of each
over the timeframe analyzed. This code accompanies a write-up of my process and a discussion of the results that
is not posted here on GitHub.
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt

# read the list of urls to request and do sentiment analysis on.
# each url in this list is an archived version of Elon Musk's
# Wikipedia page saved to the Wayback Machine on archive.org.
# The the archived versions start with January, 2015, and proceed
# with every six months until June of 2025 (Jan and June of each year)
url_list = pd.read_csv("sentiment_analysis_urls.csv")

# create a list of the url addresses where each element
# in the list is one url address
addresses = []
for address in url_list['URL']:
    addresses.append(address)

# create two empty lists to be appended to with sentiment
# data from TextBlob
polarities = []
subjectivities = []

# creates a counter to keep track of the count of web pages processed
counter = 0

# runs a loop for each url in the list of url addresses,
# which will import the address, parse its contents,
# run its contents through NLP processing for sentiment
# analysis with TextBlob, and append that sentiment data into the two
# preceding lists
for address in addresses:
    url = address
    # requests the current url address and assigns the contents to a variable
    page_code = requests.get(url)
    html_doc = page_code.text
    # parses the text from the main html_doc so it can be 
    # passed along for NLP/sentiment analysis in the following step
    soup = BeautifulSoup(html_doc, "html.parser")
    page_text = BeautifulSoup.get_text(soup)
    # creates a blob object with TextBlob
    page_blob = TextBlob(page_text)
    # returns polarity score of page_blob (ranges between -1
    # and 1, with most negative being -1, most positive 
    # being 1, and 0 being neutral)
    page_polarity = page_blob.sentiment.polarity 
    # appends polarity score of the page to the polarities list
    polarities.append(page_polarity)
    # returns subjectivity score of the page (where 0.0 is
    # very objective, and 1.0 is very subjective)
    page_subjectivity = page_blob.sentiment.subjectivity
    # appends subjectivity score of the page to the subjectivities list
    subjectivities.append(page_subjectivity)
    # increments the counter by one
    counter += 1
    # lets the user know how many web pages out of the total have been processed.
    print(counter, "of 22 web pages processed.")
    # prompts user to hit the Enter key after each web page is requested and processed,
    # in order not to overload the server being requested
    input('please hit "Enter" to process the next web page')

# renames url_list DataFrame to be clearer as to what it is
url_list_sentiments_df = url_list

# creates two new columns in the url_list DataFrame, adding a column each
# for polarity scores and subjectivity scores
url_list_sentiments_df['Polarity Score'] = polarities
url_list_sentiments_df['Subjectivity Score'] = subjectivities

# creates a new DataFrame and modifies it to be ready to plot as a 
# line graph
url_list_sentiments_to_plot_df = url_list_sentiments_df
del url_list_sentiments_to_plot_df['URL']
url_list_sentiments_to_plot_df.set_index('Date')

# draws graph plotting the change in polarity and subjectivity scores
# on Elon Musk's Wikipedia page over the past 10 years
url_list_sentiments_to_plot_df.plot(kind='line', x='Date', xlabel = 'Date (in six month increments)', title="Polarity and Subjectivity Score of Elon Musk's Wikipedia entry (2015-2025)", marker='o', markersize=8)

