## ARCITE: Augmented Retrieval and Citation Integration using arXiv and GPT-4 Enhancements

# Introduction

ARCITE addresses the challenge of citation hallucination in Large Language Models (LLMs). This project proposes a novel citation generation approach, leveraging semantic analysis and term-specific searches to enhance citation accuracy. The method involves direct content analysis and semantic matching to identify citation-worthy content, generating accurate citations and reference lists.

# Related Work

The emergence of LLMs has been notable in augmenting scholarly writing, although challenges in citation accuracy persist. Our study falls into the post-hoc citation category, focusing on generating citations after content creation.

# Methodology

Identification of Citation-worthy Content: Discerning domain-specific terms and explicit references to identify potential citation cues.
Paper Retrieval: Categorizing terms and ideas to guide reference search, employing arXiv search and Semantic Scholar API for retrieval.
Semantic Selection Using GPT-4: Conducting semantic analysis to ensure the relevance and accuracy of citations.
Citation and Reference List Generation: Integrating citations in the required style and creating a reference list accordingly.
Experimental Setup

We use the CORWA dataset for our study, focusing on the related works sections from papers within the Microsoft Academic Graph. Our evaluations include insert position, semantic similarity, keyword matching, citation generation, and formatting.

# Experimental Results

The research showed progress in identifying citation-worthy terms and matching the original paper. We also noticed improvements in retrieval accuracy and semantic matching.

# Discussion

We address the GPT-4 model's token limitation by developing improved search strategies and optimizing input text.

# Future Directions

The project aims to integrate the GPT-4 model more effectively, focusing on developing approaches that accommodate the model's token limits.

# Contributions

Dongheng Li: Framework implementation for the NLP model and dataset integration.
Zongxian Feng & Hang Yu: Reference hallucination control and method improvement.
Qiannian Liang: Documentation of the experimental process and error analysis.
Mohammad Shoaib Abbas: Background research and investigation of prior approaches.
