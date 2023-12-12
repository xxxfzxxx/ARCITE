def match_style(client, original_input, step1_result, citations, citation_style = "APA style citation"):
  messages = []
  messages.append({"role": "system", "content": "original text: " + original_input})
  messages.append({"role": "system", "content": "step1 result: " + step1_result})
  messages.append({"role": "system", "content": "selected paper: " + citations})
  prompt = f"For the corresponding Term/Sent in the step1_result, complete the {citation_style} in-text citation to the original text. Also generate a reference list. "
  messages.append({"role": "system", "content": prompt})
  completion = client.chat.completions.create(
    model= "gpt-3.5-turbo-1106",
    messages = messages,
    temperature = 0
  )
  messages.append({"role": "assistant", "content": completion.choices[0].message.content})
  response = completion.choices[0].message.content
  return response