
# Synchronous Example
from mistralai import Mistral
import os


with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
) as mistral:

    res = mistral.files.upload(file={
        "file_name": "test.pdf",
        "content": open("test.pdf", "rb"),
    })

    # Handle response
    print(res)