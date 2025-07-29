summary_prompt = """
    Summarize the following youtube transcript.
    It's an automatically generated transcript of a video, so it may contains errors in grammar, spelling and punctuation.
    Start with a short summary of the video, then provide a detailed summary of the content.
    {optional_topic}


    TRANSCRIPT:
    ```
    {transcript}
    ```
"""