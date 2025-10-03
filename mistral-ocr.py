import os
import base64
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

# Replace with your local PDF file path
pdf_file_path = "test.pdf"

# Read and encode the PDF file to base64
with open(pdf_file_path, "rb") as pdf_file:
    pdf_content = pdf_file.read()
    pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_base64",
        "document_base64": pdf_base64
    },
    include_image_base64=True
)