import requests

def get_random_wiki_article():
    """"Get a random Wikipedia article"""
    r = requests.get('https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json')

    # Get articles
    r_json = r.json()
    random_wiki_articles = r_json['query']['random']

    return random_wiki_articles

def display_articles(wiki_articles):
    
    for article in wiki_articles:
        print(article['title'])

        # Ask the user if the title of the article interest them
        answer = input('Does this interest you? ') 
        if answer == "yes":
            page_id= article['id']
            # Get the URL of the full article using the ID
            r = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids={page_id}&inprop=url&format=json") 
 
            r_json = r.json()

            full_url = r_json['query']['pages'][f'{page_id}']['fullurl'] 
            print("Here is the URL: " + full_url)
            print("Have a nice day!")

            break
        else:
            print('moving on')

if __name__ == "__main__":
    articles = get_random_wiki_article()
    display_articles(articles)
