# YouTube Summarizer

A command-line tool to summarize YouTube videos using Large Language Models (LLMs). Provide a YouTube video URL, and get a concise summary of its content. You can also specify a topic to focus the summary on.

## Features

- **Video Summarization**: Get a summary of any YouTube video by providing its URL or video ID.
- **Topic-focused Summaries**: Guide the summarization process by providing an optional topic.
- **Flexible LLM Configuration**: Leverages various LLM providers.
- **Easy-to-use CLI**: Simple and straightforward command-line interface.

## Installation

You can install the package directly from the source code.

1.  Clone the repository:
    ```bash
    git clone https://github.com/AlexanderSlivinskiy/youtubeSummarizer.git
    cd youtubeSummarizer
    ```

2.  Install the package. It's recommended to do this in a virtual environment.
    ```bash
    pip install .
    ```

## Configuration

This tool uses Large Language Models to generate summaries, which may require API keys for services like OpenAI, Google Gemini, OpenRouter or LiteLLM.

1.  In the root directory of the project, create a file named `.env` by copying the template:
    ```bash
    cp .env.template .env
    ```

2.  Open the `.env` file and add your API keys and other configuration details.

    ```
    # API key for OpenRouter. See https://openrouter.ai/keys
    OPENROUTER_API_KEY = "your-openrouter-api-key"
    
    # API key for OpenAI.
    OPENAI_API_KEY = "your-openai-api-key"
    
    # Generic API key for LiteLLM.
    LITELLM_API_KEY = ""
    
    # The base URL for the LiteLLM API.
    LITELLM_BASE_URL = ""
    
    # Optional proxy server settings.
    PROXY = ""
    PROXY_AUTH = ""
    ```
    
    **Note**: You only need to provide the keys for the services you intend to use. A proxy is only necessary for servers usually.

3.  The application supports various models through LiteLLM. You can configure the model used for summarization in `litellm_model_list.yaml`.

## Usage

The tool is designed to be run from the command line.

### Basic Usage
To get a general summary of a video, use the `youtube-summarizer` command followed by the video URL or video ID.

```bash
youtube-summarizer https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Topic-focused Summary
To focus the summary on a specific topic, add the topic as a second argument. This will guide the LLM to generate a summary relevant to the given topic.

```bash
youtube-summarizer https://www.youtube.com/watch?v=some-tech-talk-video "machine learning"
```

The script will fetch the video's transcript, send it to the configured LLM, and print the resulting summary to the console.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
