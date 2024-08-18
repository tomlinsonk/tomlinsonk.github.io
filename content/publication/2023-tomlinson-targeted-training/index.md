---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Targeted Training for Multi-Organization Recommendation"
authors: [admin, Mengting Wan, Cao Lu, Brent Hecht, Jaime Teevan, Longqi Yang]
date: 2023-06-08T15:54:01-05:00
doi: "10.1145/3603508"

# Schedule page publish date (NOT publication's date).
publishDate: 2023-06-08T15:54:01-05:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: "ACM Transactions on Recommender Systems"
publication_short: "ACM TORS"

abstract: "Making recommendations for users in diverse organizations (orgs) is a challenging task for workplace social platforms such as Microsoft Teams and Slack. The current industry-standard model training approaches either use data from all organizations to maximize information or train organization-specific models to minimize noise. Our real-world experiments show that both approaches are poorly suited for the multi-org recommendation setting where different organizations’ interaction patterns vary in their generalizability. We introduce targeted training, which improves on standard practices by automatically selecting a subset of orgs for model development whose data are cleanest and best represent global trends. We demonstrate how and when targeted training improves over global training through theoretical analysis and simulation. Our experiments on large-scale datasets from Microsoft Teams, SharePoint, Stack Exchange, DBLP, and Reddit show that in many cases targeted training can improve mean average precision across orgs by 10-15% over global training, is more robust to orgs with lower data quality, and generalizes better to unseen orgs. Our training framework is applicable to a wide range of inductive recommendation models, from simple regression models to graph neural networks."

# Summary. An optional shortened abstract.
summary: "We investigate the challenge of recommending items in multiple non-overlapping organizations and develop targeted training, a surprising simple and effective transfer-learning approach."

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

url_pdf: 2023-tomlinson-targeted-training.pdf
url_code:
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
