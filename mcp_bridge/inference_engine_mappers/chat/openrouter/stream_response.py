from lmos_openai_types import (
    CreateChatCompletionStreamResponse
)

def chat_completion_openrouter_stream_response(data: dict) -> CreateChatCompletionStreamResponse:
    return CreateChatCompletionStreamResponse.model_validate(data)
