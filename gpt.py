import base64
from openai import OpenAI

client = OpenAI()

messages = []

prompt = f"""
Analyze this architectural drawing, How many doors are there in the drawing? Use your knowledge in professional architectural design to find correct symbols
"""

# prompt = "What is in this image?"
filename = "floorplan_page-0007"
with open(f"sample/{filename}.jpg", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

messages.append(
{
    "role": "user",
    "content": [
        {"type": "input_text", "text": prompt},
        {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
    ],
}
)
response = client.responses.create(
    model="gpt-4o-mini",
    input=messages,
)

response_text = response.output[0].content[0].text


# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "developer", "content": "Translate japanese to english with high accuracy"},
#         {
#             "role": "user",
#             "content": f"Translate the japanese texts below to english. Retain the formatting, just do translation. Heres the text: {response_text}",
#         },
#     ],
# )

# response_text = completion.choices[0].message.content

with open(f"{filename}.md", "w", encoding="utf-8") as f:
    f.write(response_text)