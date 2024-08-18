---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Workplace Recommendation with Temporal Network Objectives"
authors: [admin, Jennifer Neville, Longqi Yang, Mengting Wan, Cao Lu]
date: 2023-08-09T12:27:24-04:00
doi: "10.1145/3580305.3599932"

# Schedule page publish date (NOT publication's date).
publishDate: 2023-08-09T12:27:24-04:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining"
publication_short: "KDD"

abstract: "Workplace communication software such as Microsoft Teams, Slack, and Google Workspace have become integral to workplace collaboration, especially due to the rise of remote work. By making it easier to access relevant or useful information, recommender systems for these platforms have the potential to improve efficient cross-team information flow through a company's communication network. While there has been some recent work on recommendation approaches that optimize network objectives, these have focused on static graphs. In this work, we focus on optimizing information flow, which is highly temporal and presents a number of novel algorithmic challenges. To overcome these, we develop tractable measures of temporal information flow and design efficient online recommendation algorithms that jointly optimize for relevance and cross-team information flow. We demonstrate the potential for impact of these approaches on a rich multi-modal dataset capturing one month of communication between 180k Microsoft employees through email, chats and posts on Microsoft Teams, and file sharing on SharePoint. We design an offline model-based evaluation pipeline to estimate the effects of recommendations on the temporal communication network. We show that our recommendation algorithms can significantly improve cross-team information flow with only a small decrease in traditional relevance metrics."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: [Recommendation]
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: 2023-tomlinson-workplace-recommendation.pdf
url_code:
url_dataset:
url_poster: kdd-2023-poster.pdf
url_project:
url_slides: kdd-23-network-rec-slides.pdf
url_source:
url_video: https://youtu.be/5OWlKb81NlE

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
