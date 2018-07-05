#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The goal is to scrape baseline stats on stories from https://medium.com/me/stats
       in order to get a better understanding of how readers engage with a writers work.
       At the moment, this script will only be functional if you have set up your 
       Medium login through Google, though Facebook, Twitter, etc. would be similar
       requiring only a few tweaks on your part. The output will be produced in your
       curent directory as file called mystats.csv. It's also worth noting that this is 
       a personal project and is in no way associated with Medium."""

# Imports 
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# Insert Google login info for Medium entry
USER = ''
PASS = ''	

# Goes through splash and login process
def splash_process(driver, email, password):
    
    # Goes to sign in page
    driver.get('https://medium.com/m/signin')

    # Clicks sign in button
    driver.find_element_by_xpath(".//button[contains(.,'Sign in')]").click()

    # Clicks sign in with Google
    driver.find_element_by_xpath(".//button[contains(.,'Sign in with Google')]").click()

    # Finds email field
    email_field = driver.find_element_by_id("identifierId")

    # Types in email
    email_field.send_keys(email)

    # Clicks next button
    driver.find_element_by_id("identifierNext").click()

    # Wait a sec
    time.sleep(1)

    # Finds password field
    pass_field = driver.find_element_by_name("password")

    # Types in password
    pass_field.send_keys(password)

    # Click next button
    driver.find_element_by_id("passwordNext").click()
    
    # Wait a sec
    time.sleep(3)
    
    # Go to stats page and return it 
    driver.get('https://medium.com/me/stats')


# Scrolls to bottom to get all posts into view
def scroll(driver):

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(6)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def get_info(driver):
    # Grab the main table html from Medium stats 
    table = driver.find_element_by_class_name('js-statsTableBody')

    # Get the raw html from our table element
    raw_html = table.get_attribute('innerHTML')

    # Quit our driver
    driver.quit()

    # Clean html  
    soup = BeautifulSoup(raw_html, 'html.parser')

    # Story titles
    titles = [item.text for i, item in enumerate(soup.select('h2'))]
    #print('---------------------')
    #print('Title:', titles[0])

    # Reading times
    read_times = [item.get('title') for i, item in enumerate(soup.findAll('span', 
        {'class':'readingTime'}))]
    #print('Read Time:', read_times[0])

    # Publication names
    pubs = []
    h2tags = soup.find_all('h2')
    for h2tag in h2tags:
        page = [str(h2tag)]
        elem = h2tag.next_sibling
        while elem and elem.name != 'h2':
            if elem.text.split('View story')[0] == '':
                pubs.append('None')
            else:
                pubs.append(elem.text.split('View story')[0][3::])
            elem = elem.next_sibling
    #print('Publication:', pubs[0])

    # Get all numerical metrics
    nums = [item.text for i, item in enumerate(soup.findAll('span', 
        {'class':'sortableTable-value'})) if (len(item.text) < 13 or '.' in item.text)]

    # Views
    views = nums[::4]
    #print('Views:', views[0])

    # Reads
    reads = nums[1::4]
    #print('Reads:', reads[0])

    # Read ratio
    ratio = nums[2::4]
    #print('Read Ratio:', ratio[0])

    # Fans
    fans = nums[3::4]
    #print('Fans:', fans[0])

    # Create dataframe
    df = pd.DataFrame(data={'Title': titles, 'Read Time': read_times, 'Publication': pubs, 'Views': views, 
                            'Reads': reads, 'Read Ratio': ratio, 'Fans': fans})

    # Reorder columns
    df = df[['Title', 'Publication', 'Read Time', 'Views', 'Reads', 'Read Ratio', 'Fans']]

    # Convert numerical features to floats
    df = df.apply(pd.to_numeric, errors='ignore')
    df['Read Time'] = df['Read Time'].apply(lambda x: int(x.split()[0]))
    #print('---------------------')

    # Return DataFrame
    return df

# Print results in terminal
def print_results(df):
    for index, row in df.iterrows():
        if index == 0:
            print('---------------------')
        print('Title:', row['Title'])
        print('Read Time:', row['Read Time'])
        print('Publication:', row['Publication'])
        print('Views:', row['Views'])
        print('Reads:', row['Reads'])
        print('Read Ratio:', row['Read Ratio'])
        print('Fans:', row['Fans'])
        print('---------------------')
        time.sleep(.2)

# Run main
if __name__ == "__main__":
    
    # Start the driver
    driver = webdriver.Chrome('../chromedriver')

    # Log in!
    splash_process(driver, USER, PASS)
    scroll(driver)

    # Export as csv
    df = get_info(driver)
    print_results(df)
    df.to_csv('mystats.csv', index=False)
    print('Created mystats.csv')
