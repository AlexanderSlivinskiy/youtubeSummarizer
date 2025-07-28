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
