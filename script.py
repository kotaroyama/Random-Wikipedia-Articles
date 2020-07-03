"""Suggests random Wikipedia Articles to the user"""
import re
import webbrowser
import requests

def get_random_wiki_articles():
    """"Get random Wikipedia articles"""
    res = requests.get('https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json')

    # Get articles in JSON format
    r_json = res.json()
    random_wiki_articles = r_json['query']['random']

    return random_wiki_articles

def display_articles(wiki_articles):
    """Suggest random Wikipedia articles"""
    for article in wiki_articles:
        print(article['title'])

        # Forever while loop until the user enters an answer in correct form
        while True:
            # Ask the user if the title of the article interest them
            answer = input('Does this interest you? ')

            # Use regular expression to match user's answer
            yes_pattern = re.compile("yes|y+|Yes|YES|Y+")
            no_pattern = re.compile("no|n+|No|NO|N+")

            # Answer is yes
            if yes_pattern.match(answer):
                page_id = article['id']
                # Get the URL of the full article using the ID
                res = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids={page_id}&inprop=url&format=json')
                r_json = res.json()

                full_url = r_json['query']['pages'][f'{page_id}']['fullurl']
                print("\nHere is the URL: " + full_url)
                print("Have a nice day!")

                # Open the URL in the default browser
                webbrowser.open(full_url)

                return

            # Answer is no
            if no_pattern.match(answer):
                print("\nmoving on...\n")
                break

            # Answer is not valid
            print('\nPlease enter a valid response...\n')
            continue

    print("No more articles left")

if __name__ == "__main__":
    ARTICLES = get_random_wiki_articles()
    display_articles(ARTICLES)
