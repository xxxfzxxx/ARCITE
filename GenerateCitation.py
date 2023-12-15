import openai
import arxiv
from ArxivSearchQueries import generate_arxiv_search_queries
from ArxivSearch import arxiv_search
from CitationFilter import find_citations
from AnalysisText import analyze_text_for_citations
from MatchStyle import match_style
from openai import OpenAI

def GenerateCitation(input_text, citation_style = "APA style"):
    
    messages = []

    # Client initialization or configuration goes here
    client = OpenAI(api_key="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")
    print("client initialized")

    # Step 1: Analyze text for citations
    step_1_out = analyze_text_for_citations(input_text, client, citation_style=citation_style)
    print("step 1 output:")
    print(step_1_out)
    
    messages.append("Step 1 completed: " + str(step_1_out))

    # Step 2: Generate arXiv search queries
    queries_arxiv = generate_arxiv_search_queries(step_1_out, client)
    print("queries_arxiv generated")

    # Step 3: Search arXiv
    out_dic = arxiv_search(queries_arxiv)
    print("arxiv search finished")

    # Step 4: Find citations
    citations = find_citations(step_1_out, out_dic, client)
    print("find citations finished")

    # Step 5: Match style
    response = match_style(client, input_text, step_1_out, citations, citation_style=citation_style)

    return response, messages