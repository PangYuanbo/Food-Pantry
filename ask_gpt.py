import openai
import schedule
from dotenv import load_dotenv
import os

# 配置您的OpenAI API密钥
openai.api_key =os.getenv("OPENAI_API_KEY")