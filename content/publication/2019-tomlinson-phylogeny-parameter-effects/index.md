---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Parameter, Noise, and Tree Topology Effects in Tumor Phylogeny Inference"
authors: [admin, Layla Oesper]
date: 2019-12-23
doi: "10.1186/s12920-019-0626-0"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-03-06T16:52:41-05:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: "BMC Medical Genomics"
publication_short: ""

abstract: "Accurate inference of the evolutionary history of a tumor has important implications for understanding and potentially treating the disease. While a number of methods have been proposed to reconstruct the evolutionary history of a tumor from DNA sequencing data, it is not clear how aspects of the sequencing data and tumor itself affect these reconstructions. We investigate when and how well these histories can be reconstructed from multi-sample bulk sequencing data when considering only single nucleotide variants (SNVs). Specifically, we examine the space of all possible tumor phylogenies under the infinite sites assumption (ISA) using several approaches for enumerating phylogenies consistent with the sequencing data. On noisy simulated data, we find that the ISA is often violated and that low coverage and high noise make it more difficult to identify phylogenies. Additionally, we find that evolutionary trees with branching topologies are easier to reconstruct accurately. We also apply our reconstruction methods to both chronic lymphocytic leukemia and clear cell renal cell carcinoma datasets and confirm that ISA violations are common in practice, especially in lower-coverage sequencing data. Nonetheless, we show that an ISA-based approach can be relaxed to produce high-quality phylogenies. Consideration of practical aspects of sequencing data such as coverage or the model of tumor evolution (branching, linear, etc.) is essential to effectively using the output of tumor phylogeny inference methods. Additionally, these factors should be considered in the development of new inference methods."

# Summary. An optional shortened abstract.
summary: "An extended journal version of our 2018 BIBM paper. We examine how aspects of sequencing data and patterns of tumor evolution affect phylogeny inference."

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
url_code:
url_dataset: https://bitbucket.org/oesperlab/inference-effects-data
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
