prompt = """
    Summarize the following youtube transcript.
    It's an automatically generated transcript of a video, so it may contains errors in grammar, spelling and punctuation.
    Create bullet points and use markdown formatting.
    Answer in the language of the transcript.
    {optional_topic}


    TRANSCRIPT:
    ```
    {transcript}
    ```
"""