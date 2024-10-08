import argparse
import os
import re
import json
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from pathlib import Path

from typing import List, Set, Union, Dict, Optional, Any
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from PIL import Image
from io import BytesIO
from urllib import request
def getGenerator():
    return Pipeline()
from fastapi import FastAPI
app = FastAPI()

# Dynamically set CORS origins based on environment
if os.environ.get("ENVIRONMENT") == "PRODUCTION":
    origins = ["https://google.com"]
else:
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HashableBaseModel(BaseModel):
    def __hash__(self):
        return hash(self.json())
    
class FormPayload(HashableBaseModel):
    coherence: float
    clarity: float
    creativity: float
    freeForm: str
    html: str

class GoodbyePayload(HashableBaseModel):
    firstname: str
# API routes
@app.get("/")
def index():
    return RedirectResponse(url="client/index.html")

@app.get("/api/docs")
async def docs():
    return RedirectResponse(url="/docs")

@app.get("/api/get-a-hi", response_model=str)
async def hello(firstname: str):
    return f"Hello {firstname}"

@app.post("/api/post-a-bye", response_model=str)
async def goodbye(payload: GoodbyePayload):
    return f"Goodbye {payload.firstname}"

# CLI and entry point
def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--port", default=8000, type=int, help="Port to run the app.")
    args = parser.parse_args()
    uvicorn.run(app, host="0.0.0.0", port=args.port)

    # Testing app
    client = TestClient(app)
    response = client.get(make_url("/api/get-a-hi", {"firstname": "bob"}))
    assert response.status_code == 200
    assert response.json() == "Hello bob"
    
    request = {"firstname": "bob"}
    response = client.post("/api/post-a-bye", json=request)
    assert response.status_code == 200
    assert response.json() == "Goodbye bob"

def make_url(baseurl, to_send: Dict[str, Any]):
    return baseurl + "?" + urlencode(to_send)

if __name__ == "__main__":
    main()