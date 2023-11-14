# ARCITE: Augmented Retrieval and Citation Integration using arXiv and GPT-4 Enhancements

## Introduction

ARCITE addresses the challenge of citation hallucination in Large Language Models (LLMs). This project proposes a novel citation generation approach, leveraging semantic analysis and term-specific searches to enhance citation accuracy. The method involves direct content analysis and semantic matching to identify citation-worthy content, generating accurate citations and reference lists.

<img width="1405" alt="diagram" src="https://github.com/Carstin520/CS546-ARCITE/assets/78332064/76220b26-d392-4c0d-91ff-7d9297f677f4">

## Related Work

The emergence of LLMs has been notable in augmenting scholarly writing, although challenges in citation accuracy persist. Our study falls into the post-hoc citation category, focusing on generating citations after content creation.

## Methodology
<img width="641" alt="initial_process" src="https://github.com/Carstin520/CS546-ARCITE/assets/78332064/a7558eac-e8be-49aa-8a91-9aaad813b7ce">

Identification of Citation-worthy Content: Discerning domain-specific terms and explicit references to identify potential citation cues.

Paper Retrieval: Categorizing terms and ideas to guide reference search, employing arXiv search and Semantic Scholar API for retrieval.

<img width="729" alt="selected_citations" src="https://github.com/Carstin520/CS546-ARCITE/assets/78332064/a7a251d7-0fb8-4b4f-9b00-6298c52039df">

Semantic Selection Using GPT-4: Conducting semantic analysis to ensure the relevance and accuracy of citations.

<img width="728" alt="final_result" src="https://github.com/Carstin520/CS546-ARCITE/assets/78332064/48918de9-4d22-4ee0-a1d9-480950f9b2a8">

Citation and Reference List Generation: Integrating citations in the required style and creating a reference list accordingly.
Experimental Setup

We use the CORWA dataset for our study, focusing on the related works sections from papers within the Microsoft Academic Graph. Our evaluations include insert position, semantic similarity, keyword matching, citation generation, and formatting.

## Experimental Results

The research showed progress in identifying citation-worthy terms and matching the original paper. We also noticed improvements in retrieval accuracy and semantic matching.

## Discussion

We address the GPT-4 model's token limitation by developing improved search strategies and optimizing input text.

## Future Directions

The project aims to integrate the GPT-4 model more effectively, focusing on developing approaches that accommodate the model's token limits.

## Contributions

Dongheng Li: Framework implementation for the NLP model and dataset integration.

Zongxian Feng & Hang Yu: Reference hallucination control and method improvement.

Qiannian Liang: Documentation of the experimental process and error analysis.

Mohammad Shoaib Abbas: Background research and investigation of prior approaches.
