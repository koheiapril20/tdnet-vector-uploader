from dotenv import load_dotenv
from openai import OpenAI
import time
from typing_extensions import override
import os

load_dotenv(override=True)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

vectorstore_id = os.getenv("OPENAI_TARGET_VS_ID")

def upload_new_files():
    existing_files = []
    for f in client.files.list():
        existing_files.append(f.filename)

    data_dir = './data'
    file_list = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]

    new_files = []
    for f in file_list:
        if not f in existing_files:
            print(f"New file {f} found in directory {data_dir}")
            new_files.append(f)

    file_streams = [open(os.path.join(data_dir, path), "rb") for path in new_files]

    if new_files:
        print("Executing Batch upload...")
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vectorstore_id, files=file_streams
        )
        print(file_batch.status)
        print(file_batch.file_counts)
    else:
        print(f"No new files found in directory {data_dir}")
