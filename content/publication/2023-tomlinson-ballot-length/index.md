---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Ballot Length in Instant Runoff Voting"
authors: [admin, Johan Ugander, Jon Kleinberg]
date: 2023-02-07T00:00:00-05:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-07-19T20:34:46-05:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: "Thirty-Seventh AAAI Conference on Artificial Intelligence"
publication_short: "AAAI"

abstract: "Instant runoff voting (IRV) is an increasingly-popular alternative to traditional plurality voting in which voters submit rankings over the candidates rather than individual votes. In practice, municipalities often restrict the ballot length, the number of candidates a voter is allowed to rank on their ballot. We theoretically and empirically analyze how ballot length can influence the outcome of an election, given fixed voter preferences. We show that there exist preference profiles over k candidates such that up to k−1 different candidates win at different ballot lengths. We derive exact lower bounds on the number of voters required for such profiles and provide constructions matching these bounds. Additionally, we fully characterize which sequences of winners are possible over ballot lengths and provide explicit profile constructions achieving any feasible winner sequence. Finally, we analyze a collection of 168 real-world elections, where we truncate rankings to simulate shorter ballots. We find that shorter ballots could have changed the outcome in one quarter of these elections and that longer ballots can favor particular candidates. Our results highlight ballot length as a consequential degree of freedom in the design of IRV elections."

# Summary. An optional shortened abstract.
summary: "We theoretically and empirically investigate the impact of ballot length in instant runoff voting elections."

tags: []
categories: [Voting]
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: https://arxiv.org/abs/2207.08958
url_code: https://github.com/tomlinsonk/irv-ballot-length
url_dataset:
url_poster: aaai-ballot-length-poster.pdf
url_project:
url_slides: aaai-ballot-length-slides.pdf
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
