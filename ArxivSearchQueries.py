def generate_arxiv_search_queries(analysis_result, client):
    """
    Generates search queries for arXiv based on the analysis result.

    :param analysis_result: The output from analyze_text_for_citations.
    :return: A dictionary of search queries for each term/sentence.
    """
    queries = {}
    # GPT-4 prompt for analyzing text
    max_attempts = 3  # Set a maximum number of attempts to avoid infinite loops

    for attempt in range(max_attempts):
      prompt = f"""
        Analyze the following text and determine the appropriate arXiv.search categories for citations.
        The arXiv.search categories and the keywords should be relevant to the subjects mentioned in the text.
        List the arXiv.search categories for each term or sentence that requires a citation. (e.g., cs.AI, cs.CC, eess.AS)
        List the keywords for each term or sentence that requires a citation:

        Text: {analysis_result}

        Please format the output as follows:
        [Term/Sentence Index] Categories: List of valid arXiv.search categories ; Keywords: list of relevant keywords
      """
      print(prompt)
      # Call GPT-4 API for analysis
      response = client.chat.completions.create(
          model="gpt-4",
          messages=[{"role": "system", "content": prompt}],
          temperature=0
      )

      # Extracting the response text
      analysis_result = response.choices[0].message.content.strip()
      print(analysis_result)

      # Parsing logic (to be adapted based on actual format of GPT-4 response)
      queries = {}

      # Process the analysis_result line by line
      for line in analysis_result.split('\n'):
          if  'Categories:' in line and 'Keywords:' in line:
              try:
                  index, rest = line.split('] Categories:', 1)
                  categories_str, keywords_str = rest.split('; Keywords:', 1)
                  categories = [cat.strip() for cat in categories_str.split(',')]
                  keywords = [keyword.strip() for keyword in keywords_str.split(',')]

                  category_query = ' OR '.join(f"(cat:{cat})" for cat in categories)
                  keywords_query = ' OR '.join(f"(abs:{keyword})" for keyword in keywords)
                  query = f"{category_query} AND {keywords_query}"
                  queries[index.strip('[')] = query
              except ValueError:
                  # If parsing fails, break and try again
                  break
      else:
          # If parsing is successful, return the queries
          return queries

      # If we reach here, the output format was not as expected, retry

    # If all attempts fail, return an error or a default value
    return {"error": "Failed to parse GPT-4 response in the required format."}