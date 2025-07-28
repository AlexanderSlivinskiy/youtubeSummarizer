from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.proxies import GenericProxyConfig

from youtube_summarizer.config import PROXY, PROXY_AUTH

ytt_api = YouTubeTranscriptApi(
    proxy_config=(
        GenericProxyConfig(
            http_url=f"http://{PROXY_AUTH}@{PROXY}",
            https_url=f"http://{PROXY_AUTH}@{PROXY}",
        )
        if PROXY and PROXY_AUTH
        else None
    )
)


def get_transcript(video_id):
    """
    Fetch and format transcript for a YouTube video.

    Args:
        video_id (str): YouTube video ID

    Returns:
        str: Formatted transcript text
    """
    x = ytt_api.fetch(video_id, languages=["en", "de"])
    formatter = TextFormatter()
    try:
        formatted = formatter.format_transcript(x)
    except Exception as e:
        print(f"Error formatting transcript: {e}")
        print(f"Transcript data: {x}")
        raise e
    return formatted


def summary_prompt(transcript: str, optional_topic: str = None) -> str:
    prompt = (
        """
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
    ).strip()

    optional_topic = (
        "Focus specifically on the topic of: {optional_topic}\n"
        if optional_topic
        else ""
    )
    prompt = prompt.format(transcript=transcript, optional_topic=optional_topic)
    return prompt
