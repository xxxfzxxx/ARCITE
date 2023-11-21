import requests


class SemanticScholar:
    def __init__(self):
        self.api_key = '1ncDOSkmgv5I9Ud73NCt87jcIBnQgxhb4kPzC8DF'
        self.base_url = "https://api.semanticscholar.org/graph/v1/paper/search"

    def search(self, query, limit=10):
        """
        Search for papers using Semantic Scholar API.
        
        :param query: The search query (string).
        :param limit: Number of results to return (int).
        :return: JSON response containing search results.
        """
        headers = {
            'x-api-key': self.api_key
        }
        params = {
            'query': query,
            'limit': limit
        }
        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"