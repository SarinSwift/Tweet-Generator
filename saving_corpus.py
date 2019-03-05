
import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = 'e4f36c08ee8edf1d4951c7bdfdfb0a93'
def get_article(article_url):
    # set request params for API request
    params = { 'token': DIFFBOT_DEV_TOKEN,
               'url': article_url,
               'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params) # hit the Diffbot API
    res_obj = res.json()['objects'][0]          # parse the response object

    return res_obj['text']                      # pull out the text


if __name__ == '__main__':
    import sys
    urls_file = open('/Users/sarinswift/Desktop/Designs/pages.txt')
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip() # remove leading/trailing whitespace
        article = get_article(url)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
