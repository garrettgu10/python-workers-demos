from js import Response
from langchain.chat_models import ChatOpenAI

def on_fetch(request, env):
    ChatOpenAI(openai_api_key=env.API_KEY)
    print("Constructed OpenAI object")

    return Response.new("hello world")

