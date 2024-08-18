---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Summarizing Diverging String Sequences, with Applications to Chain-Letter Petitions"
authors: [Patty Commins, David Liben-Nowell, Tina Liu, admin]
date: 2020-06-09
doi: "10.4230/LIPIcs.CPM.2020.11"
math: true

# Schedule page publish date (NOT publication's date).
publishDate: 2020-04-16T18:46:32-04:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: "31st Annual Symposium on Combinatorial Pattern Matching"
publication_short: "CPM"

abstract: "Algorithms to find optimal alignments among strings, or to find a parsimonious summary of a collection of strings, are well studied in a variety of contexts, addressing a wide range of interesting applications.  In this paper, we consider *chain letters*, which contain a growing sequence of signatories added as the letter propagates.  The unusual constellation of features exhibited by chain letters (one-ended growth, divergence, and mutation) make their propagation, and thus the corresponding reconstruction problem, both distinctive and rich.  Here, inspired by these chain letters, we formally define the problem of computing an optimal summary of a set of diverging string sequences.  From a collection of these sequences of names, with each sequence noisily corresponding to a branch of the unknown tree $T$ representing the letter's true dissemination, can we efficiently and accurately reconstruct a tree $T' \\approx T$?  In this paper, we give efficient exact algorithms for this summarization problem when the number of sequences is small; for larger sets of sequences, we prove hardness and provide an efficient heuristic algorithm.  We evaluate this heuristic on synthetic data sets chosen to emulate real chain letters, showing that our algorithm is competitive with or better than previous approaches, and that it also comes close to finding the true trees in these synthetic datasets."

# Summary. An optional shortened abstract.
summary: "We examine the problem of reconstructing the history of diverging string sequences, inspired by chain email petitions."

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code: https://github.com/tomlinsonk/diverging-string-seqs
url_dataset:
url_poster:
url_project:
url_slides: 2020-CPM-slides.pdf
url_source:
url_video: https://youtu.be/qScA12VBDQk

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
