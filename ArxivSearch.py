import arxiv

def arxiv_search(queries_arxiv):
    num_results = 5
    out_dic = {}

    for key in queries_arxiv:
        search = arxiv.Search(
            query=queries_arxiv[key],
            max_results=num_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        out_dic[key] = list(search.results())
    
    return out_dic