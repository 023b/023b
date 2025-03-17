import os
import re
import requests
import json

# GitHub API configuration
github_username = "023b"
token = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"token {token}"}

# Fetch language data
languages_url = f"https://api.github.com/users/{github_username}/repos"
response = requests.get(languages_url, headers=headers)
repos = response.json()

# Collect language statistics
language_stats = {}
for repo in repos:
    if repo.get("fork"):
        continue  # Skip forked repositories
        
    languages_url = repo["languages_url"]
    lang_response = requests.get(languages_url, headers=headers)
    languages = lang_response.json()
    
    for language, bytes_count in languages.items():
        if language in language_stats:
            language_stats[language] += bytes_count
        else:
            language_stats[language] = bytes_count

# Calculate percentages
total_bytes = sum(language_stats.values())
for language in language_stats:
    language_stats[language] = round((language_stats[language] / total_bytes) * 100, 2)

# Sort languages by percentage
sorted_languages = sorted(language_stats.items(), key=lambda x: x[1], reverse=True)
top_languages = sorted_languages[:5]  # Get top 5 languages

# Update the README
with open("README.md", "r") as file:
    readme_content = file.read()

# Create new language stats section that matches your current format
language_section = "```text\n"
for language, percentage in top_languages:
    language_section += f"{language.ljust(12)} {'█' * int(percentage/5)}{'░' * (20-int(percentage/5))}  {percentage} % \n"
language_section += "```"

# Replace existing language stats section
pattern = r"```text\n(?:.*\n){1,10}```"
updated_readme = re.sub(pattern, language_section, readme_content, flags=re.DOTALL)

with open("README.md", "w") as file:
    file.write(updated_readme)

print("README updated with current language statistics")
