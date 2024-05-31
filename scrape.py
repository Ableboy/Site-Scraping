import requests # This lib allows us to download and get data
from bs4 import BeautifulSoup # This lib allows us to use the data inform of scraping(e.g cleaning up, etc)
import pprint # This helps to beautify our code output.


res = requests.get("https://news.ycombinator.com/") # getting webpage
res2 = requests.get("https://news.ycombinator.com/?p=2") # getting second webpage
soup = BeautifulSoup(res.text, 'html.parser') # modifying webpage from str to html as obj
soup2 = BeautifulSoup(res2.text, 'html.parser') # modifying second webpage from str to html as obj

links = soup.select('.titleline > a') # This carries all title of hacker_new(hn) on pg 1 with accessible link func
subtext = soup.select('.subtext') # This carries points view in title
links2 = soup2.select('.titleline > a') # This carries all title of hacker_new(hn) on pg 2 with accessible link func
subtext2 = soup2.select('.subtext') # This carries points view in title

mega_link = links + links2
mega_subtext = subtext + subtext2


def sort_votes(hnlist): # This func sort vote points and use lam func to specialised the points
    return sorted(hnlist, key= lambda k: k['vote'], reverse= True)


def create_custom_hn(links, subtext): # This func helps to checkout point > 100 
    regenerat_list = [] # New list of data file
    for index, item in enumerate(links): # This loop over all the data
        title = item.getText() # This is used to get the title of the data
        href = item.get('href', None) # This is used to get link related to title
        vote  = subtext[index].select('.score') # This carries point of title check
        if len(vote): # This shows if point is more than 0
            points = int(vote[0].getText().replace(' points', ' ')) # seperated checker: convert to space_string
            if points > 99:
                regenerat_list.append({'title' : title, 'link' : href, 'vote' : points}) # This combine using dict append
    return sort_votes(regenerat_list)

# Display the results
pprint.pprint(create_custom_hn(mega_link, mega_subtext))