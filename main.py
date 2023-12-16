from typing import AsyncGenerator, NoReturn

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from chat_gpt import user_query , process_user_query , converse_with_chatGPT
load_dotenv()
import openai

# app = FastAPI()

openai.api_key = "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"
# with open("index.html") as f:
#     html = f.read()


# def get_ai_response(message: str) :
#     """
#     OpenAI Response
#     """
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a helpful assistant, skilled in explaining "
#                     "complex concepts in simple terms."
#                 ),
#             },
#             {
#                 "role": "user",
#                 "content": message,
#             },
#         ],
#         stream=True,
#     )

#     all_content = ""
#     for chunk in response:
#         content = chunk.choices[0].delta.content
#         if content:
#             all_content += content
#             yield all_content
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Slideoo Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        data_2 = process_user_query(data)
        await websocket.send_text(f"Response from GPT: {data_2}")

# @app.get("/")
# def web_app() -> HTMLResponse:
#     """
#     Web App
#     """
#     return HTMLResponse(html)

# @app.get("/conversation")
# def hello():
#     return "hello"


# @app.websocket("/ws")
# def websocket_endpoint(websocket: WebSocket) -> NoReturn:
#     """
#     Websocket for AI responses
#     """
#     websocket.accept()
#     while True:
#         message = websocket.user_query()
#         websocket.send_text(text)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        
        port=8000,
        log_level="debug",
        reload=True,
    )
