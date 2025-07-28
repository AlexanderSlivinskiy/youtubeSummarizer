"""
Command line interface for the YouTube Summary package.
"""

import time
import argparse

from youtube_summarizer.transcript import get_transcript
from youtube_summarizer.prompts import summary_prompt
from youtube_summarizer.llm import model

CHOICES = ["summary"]

def get_video_id(video_url):
    if "v=" in video_url:
        video_id = video_url.split("v=")[1]
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[1]
        video_id = video_id.split("?si=")[0]
    elif "youtube.com/live" in video_url:
        video_id = video_url.split("youtube.com/live/")[-1]
    elif "youtube.com" in video_url and "watch" not in video_url:
        video_id = video_url.split("youtube.com/")[-1]
    else:
        video_id = video_url
    video_id = video_id.split("?feature=")[0]
    return video_id

def main():
    """Main CLI entry point."""
    # Add command line argument parsing
    parser = argparse.ArgumentParser(description="Process a YouTube video ID.")
    parser.add_argument("video_url", type=str, help="YouTube video URL or ID")
    parser.add_argument(
        "optional_topic",
        type=str,
        default=None,
        help="Optional topic to focus the analysis on",
        nargs="?",
    )
    parser.add_argument(
        "type",
        type=str,
        choices=CHOICES,
        help="Type of analysis to perform: summary",
        nargs="?",
        default="summary",
    )
    args = parser.parse_args()

    topic = args.optional_topic

    video_url = args.video_url.strip()
    video_id = get_video_id(video_url)
    print(f"Video ID: {video_id}")

    # Get transcript
    for attempt in range(3):
        try:
            transcript = get_transcript(video_id)
            break
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            time.sleep(5)
            if attempt < 2:
                print("Retrying...")
            else:
                print("Failed after 3 attempts.")
                return

    # Select prompt function
    prompt = summary_prompt

    optional_topic = (
        "Focus specifically on the topic of: {optional_topic}\n"
        if optional_topic
        else ""
    )
    prompt = prompt.format(transcript=transcript, optional_topic=optional_topic)

    # Make LLM call with retries
    response = model.invoke(prompt)
    print(response.content)


if __name__ == "__main__":
    main()
