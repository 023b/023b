# Arun Prakash

<div align="center">
  <img src="https://i.imgur.com/jQstgKI.png" alt="Quantum AI Banner" width="800">
</div>

<p align="center">
  <a href="https://www.linkedin.com/in/arun-prakash-s-739881230/"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin" alt="LinkedIn"></a>
  <a href="mailto:arunsabapathi@outlook.com"><img src="https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail" alt="Email"></a>
  <img src="https://img.shields.io/badge/AI & DS-Student-green?style=flat-square" alt="AI & DS Student">
  <img src="https://komarev.com/ghpvc/?username=yourusername&style=flat-square&color=brightgreen" alt="Profile Views">
</p>

## About Me

I am an ambitious undergraduate student pursuing Bachelor's in Computer Application with a specialization in Artificial Intelligence and Data Science. My research interests primarily revolve around explorations in the field of AI, encompassing named entity recognition and natural language processing.

```javascript
const arun = {
  education: "BCA with AI & DS specialization",
  interests: ["Artificial Intelligence", "NLP", "Quantum Computing"],
  currentlyLearning: "Advanced Neural Network Architectures",
  lookingToCollaborate: "AI and Quantum Computing projects"
};
```

## Education

| Degree | Institution | Timeline |
|--------|-------------|----------|
| Bachelor of Computer Application (AI & DS) | Dr MGR Educational and Research Institute | Sep 2022 - Jul 2025 |

## Skills

```python
class Skills:
    def __init__(self):
        self.programming = ["Python", "HTML", "R", "SQL"]
        self.ai_ml = ["Large Language Models", "A3C", "Q-Learning"]
        self.data_science = ["Data Mining", "Data Analysis", "Microsoft Excel"]
        
    def constantly_improving(self):
        return True
```

### Programming Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### AI & Data Science Skills
- Large Language Models
- A3C Reinforcement Learning
- Q-Learning
- R Studio
- Data Mining
- Data Science
- Microsoft Excel

## Projects

<table>
  <tr>
    <td width="50%">
      <h3 align="center">Comment Classifier</h3>
      <div align="center">
        <a href="#" target="_blank">
          <img src="https://www.researchgate.net/publication/349569902/figure/fig2/AS:995462872711168@1614399754057/YouTube-comments-sentiment-analysis-methodology.jpg" width="100%" alt="Comment Classifier"/>
        </a>
        <p>
          <strong>Python | VaderSentiment | Google API</strong> - A Python program using Google API Client and VaderSentiment to categorize YouTube comments, providing overall sentiment percentages (Positive, Negative, Neutral).
        </p>
      </div>
    </td>
    <td width="50%">
      <h3 align="center">Multi-Layered Web Page</h3>
      <div align="center">
        <a href="#" target="_blank">
          <img src="https://raw.githubusercontent.com/danielgatis/rembg/master/examples/car-1.png" width="100%" alt="Web Project"/>
        </a>
        <p>
          <strong>HTML | CSS | JavaScript | Node.js</strong> - A dynamic Web-page that utilizes HTML, CSS, and JavaScript to create an interactive user Interface. The project is integrated with Node.js for error handling.
        </p>
      </div>
    </td>
  </tr>
</table>

## Certificates

| Provider | Certificate |
|----------|-------------|
| Great Learning | Data Mining |
| Great Learning | AI with Python |
| Great Learning | Data Science with Python |
| IBM | Introduction to Python |
| Udemy | Artificial Intelligence A-Z (2023) |

## Experience

**AI Internship** at Pantech Solutions
- Applied machine learning techniques to real-world problems
- Worked with cutting-edge AI technologies and frameworks

## Quantum Computing Interest

```
     ┌──────────┐┌──────────┐┌────────────┐┌────────────┐
q_0: ┤ Hadamard ├┤ Rx(π/64) ├┤ Phase(π/2) ├┤ Measure[0] ├
     ├──────────┤├──────────┤└──────┬─────┘└────────────┘
q_1: ┤ Hadamard ├┤ Rx(π/32) ├───────┼───────────────────
     └──────────┘└──────────┘       │                    
c_0: ════════════════════════════════════════════════════
                                     ▲                    
                                     │                    
                                 Classical               
                                  Control                
```

## GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true&theme=tokyonight&count_private=true&hide_border=true" alt="GitHub Stats" height="170">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=yourusername&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" height="170">
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=yourusername&theme=tokyonight&hide_border=true" alt="GitHub Streak" width="700">
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/yourusername/yourusername/output/github-contribution-grid-snake.svg" alt="Snake animation">
</div>

## Let's Connect!

If you're interested in AI, quantum computing, or just want to collaborate on interesting projects, feel free to reach out!

<div align="center">
  <a href="https://www.linkedin.com/in/arun-prakash-s-739881230/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:arunsabapathi@outlook.com">
    <img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="Email">
  </a>
</div>

<!-- Don't forget to create the GitHub Action workflow for the snake animation! -->
<!-- Create .github/workflows/snake.yml with the content below -->

<!--
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 0 * * *" # Runs at 12 am UTC everyday
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: Platane/snk@master
        id: snake-gif
        with:
          github_user_name: yourusername
          svg_out_path: dist/github-contribution-grid-snake.svg
      - uses: crazy-max/ghaction-github-pages@v2.5.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
-->
