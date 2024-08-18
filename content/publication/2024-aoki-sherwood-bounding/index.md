---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Bounding Consideration Probabilities in Consider-Then-Choose Ranking Models"
authors: [Ben Aoki-Sherwood, Catherine Bregou, David Liben-Nowell, admin, Thomas Zeng]
date: 2024-01-19T15:58:48-05:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2024-02-12T15:58:48-05:00

# Publication type.
publication_types: ['preprint']

# Publication name and optional abbreviated publication name.
publication: "arXiv (extended abstract at AAMAS '24)"
publication_short: "arXiv"

abstract: "  A common theory of choice posits that individuals make choices in a two-step process, first selecting some subset of the alternatives to consider before making a selection from the resulting consideration set.
  However, inferring unobserved consideration sets (or item consideration probabilities) in this \"consider then choose\" setting poses significant challenges, because even simple models of consideration with strong independence assumptions are not identifiable, even if item utilities are known.
  We consider a natural extension of consider-then-choose models to a top-k ranking setting, where we assume rankings are constructed according to a Plackett-Luce model after sampling a consideration set.
  While item consideration probabilities remain non-identified in this setting, we prove that knowledge of item utilities allows us to infer bounds on the relative sizes of consideration probabilities.
  Additionally, given a condition on the expected consideration set size, we derive absolute upper and lower bounds on item consideration probabilities.
We also provide algorithms to tighten those bounds on consideration probabilities by propagating inferred constraints.
  Thus, we show that we can learn useful information about consideration probabilities despite not being able to identify them precisely.
  We demonstrate our methods on a ranking dataset from a psychology experiment with two different ranking tasks (one with fixed consideration sets and one with unknown consideration sets).
  This combination of data allows us to estimate utilities and then learn about unknown consideration probabilities using our bounds. "

# Summary. An optional shortened abstract.
summary: ""

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

url_pdf: https://arxiv.org/abs/2401.11016
url_code:
url_dataset:
url_poster: aamas-24-poster.pdf
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
