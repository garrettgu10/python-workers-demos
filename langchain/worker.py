from js import Response
from langchain.chat_models import ChatOpenAI
import openai

API_KEY = "sk-abcdefgh"

def fetch(request):
    ChatOpenAI(openai_api_key=API_KEY)
    print("OK?")

    return Response.new("hello world")
