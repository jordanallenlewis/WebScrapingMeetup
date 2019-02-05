# import request & beautiful soup
# request is for getting content from a URL
# beautiful soup is used to parse through the HTML we get from requests
import requests
# import Regex
import re
from bs4 import BeautifulSoup


# Make the request to a url
r = requests.get('https://sageelliott.com/scrape/')

# Lets look at what the request content looks like
#print(r.content)

# use Beautifulsoup on content from request
c = r.content
soup = BeautifulSoup(c)

# Look at the content formatted with Beautifulsoup
print(soup)

# using prettify() in Beautiful soup indents HTML like it should be in the web page
# This can make reading teh HTML a little be easier
print(soup.prettify())
#
# # get elements within the 'main-content' tag
# main_content = soup.find('div', attrs = {'class': 'main-content'})
# #print(main_content)
#
# # get the list items inside of a unorded list
# content = main_content.find('ul')
# #print(content)
#
# # get elements within the 'main-content' tag
# list_content = soup.find('div', attrs = {'class': 'main-content'}).ul
# #print(list_content)
#
# # get the list items inside of a unorded list
# list_text_content = main_content.find('ul').text
# #print(list_text_content)
#
# # Try to get h2 elements
# content = main_content.find('h2').text
# #print(content)
#
# # get all the h2s on the page and display each one
# content = main_content.find_all('h2')
# #print(content)
#
# # Iterate content list and print out text inside each h2 element
# for h2 in content:
#     print(h2.text)
#
# # Get all links(a) in the main_content div.
# # for each link in list print link text and the link URL(href)
# content = main_content.find_all('a')
# for link in content:
#     print(link.text+":")
#     print(link['href'])
#
# # Get all links(a) in the main_content div.
# # for each link in list print link text and the link URL(href)
#
# content = main_content.find_all('a')
#
# for link in content:
#     print(link.text+":")
#     print(link['href'])
#
#
# # get the list items inside of a unorded list
# list_text_content = main_content.find('ul').text
# print(list_text_content)
#
# # Pattern to match the salaries | does this line start with a dollar sign?
# salary_pattern = re.compile(r'\$.+')
# salaries = salary_pattern.findall(list_text_content)
# print(salaries)
#
# # Convert to numbers
# num_salaries = [int(''.join(s[1:].split(','))) for s in salaries]
# num_salaries
#
#
# # combined networth
# combined_worth = sum(num_salaries)
# print(combined_worth)
#
# print ("Combined worth is: ${:,}".format(combined_worth))
#
# # Even More readable format
# worth_billions = float(combined_worth /1000000000)
# print ("Combined worth is: ${:.2f} billion".format(worth_billions))
#
# # Create a pattern to match the names
# name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:is)', flags = re.M)
# names = name_pattern.findall(list_text_content)
# print(names)
#

