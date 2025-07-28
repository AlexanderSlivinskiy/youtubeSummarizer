from enum import Enum
from typing import Optional
from pydantic import Field, SecretStr
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_litellm import ChatLiteLLMRouter
from litellm import Router

from youtube_summarizer.config import (
    GEMINI_API_KEY,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
    litellm_model_list,
)


OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"


class ModelSource(Enum):
    LITELLM = "litellm"
    OPENROUTER = "openrouter"
    GOOGLE = "google"
    OPENAI = "openai"


class ChatOpenRouter(ChatOpenAI):
    openai_api_key: Optional[SecretStr] = Field(
        alias="api_key",
        default_factory=OPENROUTER_API_KEY,
    )

    def __init__(self, openai_api_key: Optional[str] = None, **kwargs):
        openai_api_key = OPENROUTER_API_KEY
        super().__init__(
            base_url="https://openrouter.ai/api/v1",
            openai_api_key=openai_api_key,
            **kwargs,
        )


if GEMINI_API_KEY:
    google_model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        max_retries=2,
    ).with_retry()
    print(f"Using Google Gemini model: {google_model.model_name}")

if OPENAI_API_KEY:
    model = ChatOpenAI(model="gpt-4o", temperature=0)

if OPENROUTER_API_KEY:
    model = ChatOpenRouter(
        model_name="google/gemini-2.5-flash",
    ).with_retry()
    print(f"Using OpenRouter model: {model.model_name}")

if litellm_model_list:
    litellm_router = Router(model_list=litellm_model_list)
    model = ChatLiteLLMRouter(
        router=litellm_router,
        model_name=litellm_model_list[0]["model_name"],
        temperature=0,
    )
    print(f"Using LiteLLM model: {model.model_name}")
