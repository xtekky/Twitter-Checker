
url = "https://twitter.com/i/api/i/users/username_available.json"

querystring = {
    "full_name": "tekkytok",
    "suggest": "false",
    "username": "tekkyto"
}

headers = {
    "host": "twitter.com",
    "connection": "keep-alive",
    "sec-ch-ua": "".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"",
    "x-twitter-client-language": "en",
    "x-csrf-token": "122340a1f7ae3ef954ebd0d498f1eef96f6862e4621a6ecc4e1d98a6a923ecab59f377294eed9471f3d25d7443bca8934c896ef408a07f1470ce623a7a2b3a81ecd2557ad76d4b4529fd7c8e6198ea75",
    "sec-ch-ua-mobile": "?0",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "x-guest-token": "1541486022587998209",
    "x-twitter-active-user": "yes",
    "sec-ch-ua-platform": ""Windows"",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://twitter.com/i/flow/signup",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "guest_id=v1%3A165635387392696399; gt=1541486022587998209; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A165635387392696399; guest_id_marketing=v1%3A165635387392696399; personalization_id="v1_8Ro1mYznsLWXxkqAynZU5w=="; _ga=GA1.2.1391310238.1656353889; _gid=GA1.2.703708330.1656353889; _sl=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoHaWQiJTliNzJkMzJmNjc2NDQ3ZDg1N2U0NDU1%250AOTUzNmE2OGRjOg9jcmVhdGVkX2F0bCsIstpkpoEBOgxjc3JmX2lkIiViYzY2%250ANDM2Mjk0ZWIyNjE2NTg0NWE2MWNhOWExN2ZhMA%253D%253D--3e17c1ff9af8ca369353110f1bcc6968446b5532; att=1-BRVe8grunzQYlw13h2XtD2eiBPryUCAye46qTsAP; kdt=8thj0NlZcd6drkjpUlJP7UZqzEyrVz6jNXaDIbR4; auth_token=d851f4b5bc6fe0e20ce11b3c3352e8256a2212c4; ct0=122340a1f7ae3ef954ebd0d498f1eef96f6862e4621a6ecc4e1d98a6a923ecab59f377294eed9471f3d25d7443bca8934c896ef408a07f1470ce623a7a2b3a81ecd2557ad76d4b4529fd7c8e6198ea75; twid=u%3D1541486942533177347"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.text)
