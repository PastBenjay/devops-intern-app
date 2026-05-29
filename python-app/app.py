import os
import time
from dotenv import load_dotenv
from requests import Request

load_dotenv()

def build_greeting(name: str) -> str:
    return f"Hello, {name}! This is a simple Python app running in Docker."

def prepare_request() -> str:
    req = Request("GET", "https://example.com")
    return f"Prepared {req.method} request to {req.url}"

def main() -> None:
    name = os.getenv("NAME", "Intern")
    message = build_greeting(name)
    print(message)

    while True:
        time.sleep(3600)