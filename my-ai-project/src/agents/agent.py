# src/agents/agent.py
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Function to load OpenAI API key
def load_api_key():
    api_key = os.getenv("your api key")
    print(f"Loaded API Key: {api_key}")
    if not api_key:
        raise ValueError("OpenAI API key is missing.")
    return api_key

class MultiUserAIAgent:
    def __init__(self):
        self.api_key = load_api_key()
        openai.api_key = self.api_key
        self.user_sessions = {}

    def generate_response(self, user_id, prompt):
        if user_id not in self.user_sessions:
            self.user_sessions[user_id] = []
        
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )

            # Store interaction
            self.user_sessions[user_id].append({
                'prompt': prompt,
                'response': response.choices[0].text.strip()
            })

            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def get_user_history(self, user_id):
        return self.user_sessions.get(user_id, [])

# Example usage
if __name__ == "__main__":
    agent = MultiUserAIAgent()
    print(agent.generate_response("user_1", "What is the weather today?"))
    print(agent.generate_response("user_2", "What is the capital of France?"))
    print(agent.get_user_history("user_1"))
