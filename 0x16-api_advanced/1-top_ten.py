import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if not data['data']['children']:
            print(None)
        else:
            for post in data['data']['children']:
                print(post['data']['title'])
    else:
        print(None)
