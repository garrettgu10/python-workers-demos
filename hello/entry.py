from js import Response

async def fetch(request, env):
    return Response.new("Hello world!")