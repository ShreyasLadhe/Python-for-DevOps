# import  requests
#
# response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#
# complete_details = response.json()
#
# for element in range(len(complete_details)):
#     print(complete_details[element]["user"]["login"])

import requests

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

response = requests.get(url)  # Add headers=headers inside get() for authentication

if response.status_code == 200:
    pull_requests = response.json()
    pr_creators = {}

    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")