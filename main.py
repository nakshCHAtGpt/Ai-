
from fastapi import FastAPI, Form
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

app = FastAPI()

@app.post("/generate-image/")
async def generate_image(prompt: str = Form(...)):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        response_format="b64_json"
    )
    image_data = response['data'][0]['b64_json']
    return {"image_base64": image_data}
