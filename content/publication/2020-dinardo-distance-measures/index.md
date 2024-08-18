---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Distance Measures for Tumor Evolutionary Trees"
authors: [Zach DiNardo, admin, Anna Ritz, Layla Oesper]
date: 2020-04-01
doi: "10.1093/bioinformatics/btz869"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-03-06T16:42:25-05:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: "Bioinformatics (early version presented at RECOMB-CCB '19)"
publication_short: "Bioinformatics"

abstract: "There has been recent increased interest in using algorithmic methods to infer the evolutionary tree underlying the developmental history of a tumor. Quantitative measures that compare such trees are vital to a num- ber of different applications including benchmarking tree inference methods and evaluating common inheritance patterns across patients. However, few appropriate distance measures exist, and those that do have low resolution for differentiating trees or do not fully account for the complex relationship between tree topology and the inherit- ance of the mutations labeling that topology. Here, we present two novel distance measures, Common Ancestor Set distance (CASet) and Distinctly Inherited Set Comparison distance (DISC), that are specifically designed to account for the subclonal mutation inheritance patterns characteristic of tumor evolutionary trees. We apply CASet and DISC to multiple simulated datasets and two breast cancer datasets and show that our distance measures allow for more nuanced and accurate delineation between tumor evolutionary trees than existing distance measures."

# Summary. An optional shortened abstract.
summary: "We introduce distance metrics on tumor evolutionary trees to use for benchmmarking inference methods or clustering trees."

tags: []
categories: ["Computational Biology"]
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code: https://bitbucket.org/oesperlab/stereodist
url_dataset:
url_poster:
url_project:
url_slides: 2019-RECOMB-CCB-slides.pdf
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
