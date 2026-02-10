from openai import OpenAI
from config import config_obj

client = OpenAI(
    api_key= config_obj.deepseek_API_key,
    base_url= config_obj.deepseek_base_url
)

def chat_with_deepseek(prompt: str, model: str = "deepseek-chat") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            stream=False 
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    result = chat_with_deepseek("Привет! Как дела?")
    print(result)