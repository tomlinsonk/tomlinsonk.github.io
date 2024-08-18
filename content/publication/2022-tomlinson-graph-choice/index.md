---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Graph-based Methods for Discrete Choice"
authors: [admin, Austin R. Benson]
date: 2023-08-17T08:00:00-04:00
doi: "10.1017/nws.2023.20"

# Schedule page publish date (NOT publication's date).
publishDate: 2022-05-23T00:12:36-04:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: "Network Science"
# publication_short: ""

abstract: "Choices made by individuals have widespread impacts—-for instance, people choose between political candidates to vote for, between social media posts to share, and between brands to purchase—-moreover, data on these choices are increasingly abundant. Discrete choice models are a key tool for learning individual preferences from such data. Additionally, social factors like conformity and contagion influence individual choice. Existing methods for incorporating these factors into choice models do not account for the entire social network and require hand-crafted features. To overcome these limitations, we use graph learning to study choice in networked contexts. We identify three ways in which graph learning techniques can be used for discrete choice: learning chooser representations, regularizing choice model parameters, and directly constructing predictions from a network. We design methods in each category and test them on real-world choice datasets, including county-level 2016 US election results and Android app installation and usage data. We show that incorporating social network structure can improve the predictions of the standard econometric choice model, the multinomial logit. We provide evidence that app installations are influenced by social context, but we find no such effect on app usage among the same participants, which instead is habit-driven. In the election data, we highlight the additional insights a discrete choice framework provides over classification or regression, the typical approaches. On synthetic data, we demonstrate the sample complexity benefit of using social information in choice models."

# Summary. An optional shortened abstract.
summary: "We adapt graph learning methods to incorporate network structure into discrete choice models."

tags: []
categories: [Discrete Choice]
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: 2022-tomlinson-graph-choice.pdf
url_code: https://github.com/tomlinsonk/graph-based-discrete-choice
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
