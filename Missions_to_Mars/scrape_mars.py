# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import libraries
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


# %%
## NASA Mars News


# %%
#created path to mars new website
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# establish url
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)


# %%
# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = bs(html, 'html.parser')


# %%



# %%
# Extract title text
section = soup.find('li', class_='slide')
news_title= section.find('div', class_='content_title').text
print(news_title)


# %%
# extract paragraph text
news_paragraph = section.find('div', class_='article_teaser_body').text
print(news_paragraph)


# %%
## JPL Mars Space Images - Featured Image


# %%
url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)


# %%
html = html = browser.html
soup = bs(html, 'html.parser')


# %%
# click on full image
browser.click_link_by_partial_text('Jan 12')


# %%
# download jpg
# used partial text because 'click link by text' has to be exact and it didn't work
browser.click_link_by_partial_text('Download JPG')


# %%
# save a complete url string for this image
featured_image_url = 'https://d2pn8kiwq2w21t.cloudfront.net/original_images/jpegPIA24362.jpg'


# %%
## Mars Facts


# %%
mars_facts_url = 'https://space-facts.com/mars/'
browser.visit(mars_facts_url)


# %%
html = html = browser.html
soup = bs(html, 'html.parser')


# %%
# scrape the table containing facts about the planet including Diameter, Mass, etc.
tables = pd.read_html(mars_facts_url)
tables


# %%
## Mars Hemispheres


# %%
# Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres
mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
cerberus_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
schiaparelli_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
syrtis_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
valles_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'


# %%
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url},
]


# %%



