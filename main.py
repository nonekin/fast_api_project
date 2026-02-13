from fastapi import FastAPI, Body
from local_qwen_client import qwen

app = FastAPI()

@app.get("/requests")
def get_my_requests():
    return "Hello world!"


@app.post("/requests")
def send_promt(promt:str = Body(embed = True)):
    answer = qwen.get_answer_from_local_qwen(promt)

    return ({"answer": answer["response"]} if answer["success"] else {"answer": "Проблемы на стороне сервера. Приносим свои извинения!\nПопробуйте еще раз"})

