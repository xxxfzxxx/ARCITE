

def analyze_text_for_citations(input_text, client, citation_style="APA style"):
    """
    Analyzes the text to identify parts that need citations.

    :param input_text: String containing the text to be analyzed.
    :param client: The OpenAI API client object.
    :return: Modified text with indexed terms/sentences and an assessment.
    """
    # Prepare message for GPT-4
    messages = [
        {
            "role": "system",
            "content": f"""
                Analyze the provided text. ONLY Identify specific terminologies and sentences that ABSOLUTELY require citations to support their claims or information.
                Treat each term separately, ensuring that different terms are not mixed together when determining the need for citations.
                If a term is an acronym, include an explanation of what it stands for in the assessment.
                Assign a unique index to each, distinguishing between 'Term' and 'Sentence' (e.g., [Term 0], [Sent 0]).
                For each identified term and sentence, provide a brief explanation of why a citation is necessary to validate or support the information or claim.

                TThe output should include the original text with {citation_style} in-text citation placeholders for each identified term and sentence, and a separate assessment section detailing the reasoning behind the citation requirements.


                Text: {input_text}

                Please format the output as follows:
                1. Modified Text with Citation Placeholders:
                  [The text with in-text placeholders like [Term 0] or [Sent 0] at relevant positions.]

                2. Assessment of Citation Requirements:
                  For each Term/Sentence:
                  [Term/Sentence Index] : Brief explanation of why a citation is necessary for the term or sentence.
            """
        },
        {"role": "user", "content": input_text}
    ]

    # Call GPT-4 for analysis
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )

    # Extract the response
    response = completion.choices[0].message.content
    return response