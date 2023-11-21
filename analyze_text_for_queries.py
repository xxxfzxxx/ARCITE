
def AnalyzeTextForQueries(input_text, client):
    """
    Analyzes the provided text to prepare for generating search queries.
    
    :param input_text: String containing the text to be analyzed.
    :param client: The OpenAI API client object.
    :param model_engine: The model engine used for the OpenAI API call.
    :return: The response from the API after processing the input text.
    """
    messages = [{"role": "system", "content": "Step 1\
    Conduct a thorough analysis of the provided text. \
    Search for specific sentences or terms that need further citations to support, and assign an index to each, starting from 0.\
    For each selected sentence/term (e.g., Term 0, Term 1, Sent 0 etc.), \
    identify and highlight parts that lack citations. \
    Assess the content critically to determine where additional references are necessary to substantiate the claims or information. \
    This approach aims to ensure that every significant claim or statement in each selected sentence/term is adequately supported by relevant and reliable sources\
    The output should also include the original input with in-text citation position. \
    Example input: Emerging strategies, such as the utilization of ChatGPT Plugins, offer promise.\
    While these plugins are undeniably beneficial, they primarily source citations from expansive paper data APIs, encompassing millions of documents. \
    Consequently, while the generated citations may exhibit accuracy, they may not invariably align with the specific references the author intends.\
    Example output : Emerging strategies, such as the utilization of ChatGPT [Term 0] Plugins, offer promise.\
    While these plugins are undeniably beneficial, they primarily source citations from expansive paper data APIs,[Sent 1] encompassing millions of documents. \
    Consequently, while the generated citations may exhibit accuracy, they may not invariably align with the specific references the author intends.[Sent 2]\
    Assesement: [Term 0]: The reason why term 0 needs citations, [Sent 0]: The reason why sentence 0 needs citations, [Sent 1]: The reason why sentence 1 needs citations, [Sent 2]: The reason why sentence 2 needs citations \
    Step 2\
    Combine the results from the following two analysis steps to formulate a python list (code) of comprehensive query strings for each subsection from step1 for arXiv searches.\
    The query string should be formatted using 'abs' for abstract keywords and 'cat' for category.\
    Ensure the string is concise and accurately reflects the key elements derived from each step: \
    From Citation Category Determination (Index 2.1): Extract the main category or categories identified as relevant to the desired citations (arXiv categories like cs.CL).\
    Use the 'cat' parameter to represent these categories in the query string.\
    From Possible Keywords Abstracts (Index 2.2): Compile a list of essential keywords and phrases identified from the abstracts of potential resources.\
    These keywords should be incorporated into the query string using the 'abs' parameter.\
    The final output should be a single, well-structured query string that synergizes these elements, facilitating targeted and efficient searches on arXiv.\
    The string should be clear, precise, and tailored to yield the most relevant and authoritative academic papers pertinent to the subject matter of the text.\
    Don't use quote marks/double quote marks in the query string. Present the output in the similar format as below:\
    Output list: Term 0: (cat:cs.CL) AND (abs: New-Bing), Term 1:(cat:cs.CL) AND (abs: BARD)\
    The number of terms/sentences in step one should align with the number of elements in the output list of step2"}]  # The full system message goes here

    messages.append({"role": "user", "content": input_text})

    completion = client.chat.completions.create(
        model='gpt-4',
        messages=messages,
        temperature=0
    )
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})
    return response