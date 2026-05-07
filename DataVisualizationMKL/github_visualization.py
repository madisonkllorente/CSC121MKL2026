# Github Visualization MKL

import requests
import matplotlib.pyplot as plt

# API URL
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Make API request
response = requests.get(url)

# Convert response to dictionary
response_dict = response.json()

# Process repository information
repo_dicts = response_dict['items']

repo_names = []
stars = []

for repo_dict in repo_dicts[:10]:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(repo_names, stars)

# Add labels and title
plt.title("Most-Starred Python Projects on GitHub")
plt.xlabel("Repository")
plt.ylabel("Stars")

# Rotate labels
plt.xticks(rotation=45)

# Display chart
plt.tight_layout()
plt.show()