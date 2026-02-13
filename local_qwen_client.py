from config import config_obj
import requests
import json


class LocalQwenClient:
    def __init__(self, model="qwen3-vl:235b-cloud", host=config_obj.host_ollama, port=config_obj.port_ollama):
        self.base_url = f"http://{host}:{port}"
        self.model = model

    def get_answer_from_local_qwen(self, prompt: str, system_prompt="Ты полезный ассистент Qwen", max_tokens=1000, temperature=0.5):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": temperature,
            }
        }
        response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=60
            )
        if response.status_code == 200:
            result = response.json()
            return {
                    "success": True,
                    "response": result.get("response", "")
                    }
        else:
            return {
                "success": False,
                "error": response.status_code,
                "details": response.text[:200]
            }


    def check_connection(self):
        response = requests.get(f"{self.base_url}/api/tags", timeout=5)
        if response.status_code != 200:
            print("Ollama сервер не отвечает")
           
qwen = LocalQwenClient()