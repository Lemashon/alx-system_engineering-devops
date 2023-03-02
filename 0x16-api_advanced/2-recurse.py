import requests

def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if not data['data']['children']:
            return hot_list
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        return None
    else:
        print(f'Error {response.status_code}')
