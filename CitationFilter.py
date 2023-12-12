def find_citations(input_string, found_papers, client):
  out = ""
  messages = []
  for key in found_papers:
    prompt = "Base on the Assesment part of the input for XXXX, find the paper (Title + pdf_url + authors + published_date) which provide best support for XXXX.\
    For terms, focus on finding the term in the provided abstract (In the Abstract).\
    For sentences, focus on messuring the semantic similarity between the sentence and the provided documents.\
    Assure the format stays the same.\
    The results should have similar format, : \
    Title: xxxxxx \n pdf_url: https:xxxxxx.pdf \n authors: Abs \n published_date: July 20, 2019 (replace with the actual published date)"
    prompt = prompt.replace("XXXX", key)
    messages.append({"role": "system", "content": prompt})
    messages.append({"role": "user", "content": input_string})
    papers = ""
    for result in found_papers[key]:
      author_names = [author.name for author in result.authors]
      author_names_str = ', '.join(author_names)
      papers += "Title: " + result.title + "pdf_url: " + result.pdf_url + "\n" + "authors: " + author_names_str + " \n" + "published_date: " + result.published.strftime("%Y-%m-%d") + "\n"
    messages.append({"role": "user", "content": papers})
    completion = client.chat.completions.create(
      model= "gpt-4",
      messages=messages,
      temperature = 1
    )
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})
    response = "Part:"+ key + "\n" + completion.choices[0].message.content
    print(response)
    out += response + "\n"

  return out