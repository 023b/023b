<!-- GitHub README.md for 023b with embedded workflow information -->

<div align="center">
  <h1>Arun Prakash</h1>
  <p><i>BCA in Artificial Intelligence & Data Science | Aspiring Developer</i></p>
  
  ![GitHub Profile Views](https://komarev.com/ghpvc/?username=023b&color=blueviolet&style=flat-square)
  
  <hr>
</div>

<div align="center">
  <h2>🐍 Contribution Snake</h2>
  <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg" alt="Snake animation" />
</div>

```python
class Developer:
    def __init__(self):
        self.name = "Arun Prakash"
        self.education = "BCA in AI & Data Science"
        self.institution = "Dr MGR Educational and Research Institute"
        self.timeline = "Sep 2022 - Jul 2025"
        self.interests = ["AI", "NLP", "Named Entity Recognition"]
        
    def get_skills(self):
        return {
            "languages": ["Python", "HTML", "SQL", "R"],
            "ai_tools": ["Large Language Models", "A3C", "Q-Learning"],
            "data": ["Data Mining", "Data Science", "Microsoft Excel"]
        }
        
    def get_projects(self):
        return [
            {
                "name": "Comment_classifier",
                "tech": ["Python", "Google API Client", "VaderSentiment"],
                "desc": "Categorizes YouTube comments with sentiment analysis"
            },
            {
                "name": "Multi-Layered Web Page",
                "tech": ["HTML", "CSS", "JavaScript", "Node.js"],
                "desc": "Dynamic interactive web interface with error handling"
            }
        ]

arun = Developer()
```

<div align="center">
  <h2>⚡ Technologies & Skills</h2>
</div>

<table>
  <tr>
    <td align="center" width="96">
      <div style="height: 24px">Python</div>
    </td>
    <td align="center" width="96">
      <div style="height: 24px">HTML</div>
    </td>
    <td align="center" width="96">
      <div style="height: 24px">SQL</div>
    </td>
    <td align="center" width="96">
      <div style="height: 24px">R Studio</div>
    </td>
    <td align="center" width="96">
      <div style="height: 24px">Node.js</div>
    </td>
  </tr>
</table>

<div align="center">
  <h2>📚 Projects</h2>
</div>

<details>
<summary><b>📊 Comment Classifier</b></summary>
<br>
<p>Python program that uses Google API Client and VaderSentiment to analyze and categorize YouTube comments by sentiment, providing overall percentages of positive, negative, and neutral comments.</p>

```python
# Example sentiment analysis with VaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build

def analyze_comments(video_id, api_key):
    # Setup YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Get comments
    comments = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    ).execute()
    
    # Analyze sentiment
    analyzer = SentimentIntensityAnalyzer()
    results = {'positive': 0, 'negative': 0, 'neutral': 0}
    
    for item in comments['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        score = analyzer.polarity_scores(comment)
        
        if score['compound'] >= 0.05:
            results['positive'] += 1
        elif score['compound'] <= -0.05:
            results['negative'] += 1
        else:
            results['neutral'] += 1
    
    return results
```
</details>

<details>
<summary><b>🌐 Multi-Layered Web Page</b></summary>
<br>
<p>A dynamic web application that leverages HTML, CSS, and JavaScript to create an interactive user interface, with Node.js integration for robust error handling and backend functionality.</p>

```javascript
// Example error handling in Node.js
const express = require('express');
const app = express();

app.use(express.static('public'));

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send({
    status: 500,
    message: 'Internal Server Error',
    error: process.env.NODE_ENV === 'production' ? null : err.message
  });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```
</details>

<div align="center">
  <h2>📈 GitHub Stats</h2>
</div>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=023b&theme=tokyonight" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=023b&show_icons=true&count_private=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" width="400"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=023b&layout=compact&theme=tokyonight&hide_border=true" alt="Most Used Languages" width="400"/>
</p>

<div align="center">
  <a href="https://github.com/023b">
    <img src="https://github-profile-trophy.vercel.app/?username=023b&theme=tokyonight&no-frame=true&column=7" alt="trophy">
  </a>
</div>

<div align="center">
  <h2>🧠 AI Expertise</h2>
</div>

```text
┌─────────────────────────────────────────────────┐
│                                                 │
│  LLM Implementation  ███████████░░░░░  70%      │
│  Reinforcement (A3C) ████████████░░░░  75%      │
│  Q-Learning          ██████████████░░  85%      │
│  Data Mining         ███████████████░  90%      │
│  NLP Processing      █████████░░░░░░░  55%      │
│                                                 │
└─────────────────────────────────────────────────┘
```

<div align="center">
  <h2>🎓 Education & Certifications</h2>
</div>

<details>
<summary><b>🎓 Academic Education</b></summary>
<br>

```css
/* Education */
.degree {
  institution: "Dr MGR Educational and Research Institute";
  program: "BCA (AI & DS)";
  duration: "Sep 2022 - Jul 2025";
  focus: "Artificial Intelligence, Data Science, Programming";
}
```
</details>

<details>
<summary><b>🏆 Professional Certifications</b></summary>
<br>

#### Great Learning
- Data Mining
- AI with Python
- Data Science with Python

#### IBM
- Introduction to Python

#### Udemy
- Artificial Intelligence A-Z (2023)
</details>

<details>
<summary><b>💼 Professional Experience</b></summary>
<br>

#### Pantech Solutions
- **Role**: AI Intern
- **Duration**: 2023
- **Responsibilities**: Worked on AI implementation projects utilizing Python and machine learning frameworks
</details>

<div align="center">
  <h2>📊 Coding Activity</h2>
</div>

```text
Python       ███████████████▓░░░░░░░░░  65.42 % 
HTML/CSS     ████████▒░░░░░░░░░░░░░░░░  30.25 % 
R            ████░░░░░░░░░░░░░░░░░░░░░  15.12 % 
JavaScript   ███▒░░░░░░░░░░░░░░░░░░░░░  10.75 % 
SQL          ██▓░░░░░░░░░░░░░░░░░░░░░░   9.46 % 
```



<div align="center">
  <h2>📫 Connect With Me</h2>
  
  <a href="mailto:arunsabapathi@outlook.com">Email</a> •
  <a href="https://www.linkedin.com/in/arun-prakash-s-739881230/">LinkedIn</a>
  
  <p>+91 9342439528</p>
</div>

<!-- 
FOR SNAKE ANIMATION:
The snake animation shown above is provided by a third-party service. 
If you want your own personalized snake animation, you can:

1. Fork the repository: https://github.com/platane/snk
2. Go to the Actions tab in your forked repository
3. Enable GitHub Actions
4. Run the workflow manually
5. Then, update the snake animation URL in this README to point to your own repository's output

For example, replace the URL with:
https://raw.githubusercontent.com/YOUR_USERNAME/snk/output/github-contribution-grid-snake.svg

This will create a snake animation based on your own GitHub contribution graph.
-->
