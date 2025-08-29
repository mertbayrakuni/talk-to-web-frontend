"""
uvicorn ws_main:app --reload
"""
import uuid
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from chatbot.config import Config
from chatbot.bot import ChatBot
from chatbot.prompt_loader import PromptLoader
from chatbot.gemini_client import GeminiClient

app = FastAPI(title="Chatbot WebSocket API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Backend ----------
class SessionManager:
    """Basit in-memory store: {session_id: [history...]}"""
    def __init__(self):
        self.store: dict[str, list[dict]] = {}

    def get_history(self, sid: str) -> list[dict]:
        return self.store.setdefault(sid, [])

    def add_turn(self, sid: str, role: str, text: str):
        self.store[sid].append({"role": role, "text": text})

manager = SessionManager()

def make_client():
    cfg = Config()
    prompts = PromptLoader.load(cfg.system_prompt_files)
    return GeminiClient(model=cfg.model, system_prompts=prompts)

# ---------- WebSocket ----------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, client_id: str | None = None):
    await websocket.accept()
    sid = str(uuid.uuid4())
    history = manager.get_history(sid)  # load or create
    client = make_client()
    bot = ChatBot(client)

    try:
        while True:
            user_msg = await websocket.receive_text()
            answer = bot.send(user_msg)
            
            #if "oneri" in answer:
            #    answer = bot.handle_suggestions(answer)

            #await websocket.send_json(
            #    {"session_id": sid, "reply": answer}
            #)
             
            await websocket.send_json(answer)


            #manager.add_turn(sid, "user", user_msg)

            # Geçmişi Gemini’ye “konuşma zinciri” olarak gönder
            #prompt = "\n".join(
            #    f"{turn['role']}: {turn['text']}" for turn in history
            #)
            #prompt += f"\nuser: {user_msg}\nassistant:"

            #answer = client.send(user_msg)
            #manager.add_turn(sid, "assistant", answer)

            #await websocket.send_json(
            #    {"session_id": sid, "reply": answer, "history": history}
            #)
            #await websocket.send_json(
            #    {"session_id": sid, "reply": answer}
            #)
    except WebSocketDisconnect:
        pass  # client kapandı; history RAM’de kalır
