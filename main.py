# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("liuhaotian/llava-v1.6-mistral-7b")