from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load your fine-tuned model
model = pipeline("text-generation", model="./my_health_guru_model")

@app.get("/")
async def root():
    return {"message": "Health Model API"}

@app.post("/generate")
async def generate(prompt: str):
    result = model(prompt, max_length=100, temperature=0, do_sample=False)
    return {"response": result[0]["generated_text"]}
