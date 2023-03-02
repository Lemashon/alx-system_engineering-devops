import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    # Initialize the count dictionary if it's None
    if count_dict is None:
        count_dict = {}

    # Base case: if the word list is empty, print the count dictionary
    if not word_list:
        for word, count in sorted(count_dict.items(), key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(word, count))
        return

    # Recursive case: query the Reddit API and update the count dictionary
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            count = title.count(word)
            if count > 0:
                if word in count_dict:
                    count_dict[word] += count
                else:
                    count_dict[word] = count
    after = data['data']['after']
    if not after:
        count_words(subreddit, [], count_dict=count_dict)
    else:
        count_words(subreddit, word_list, after=after, count_dict=count_dict)
