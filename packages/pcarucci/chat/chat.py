import os
import requests as req
"""
args = {}
inp = "Come ti chiami"
"""
MODEL = "llama3.1:8b"
def chat(args):

  host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
  auth = args.get("AUTH", os.getenv("AUTH"))
  url = f"https://{auth}@{host}/api/generate"
  inp = args.get("input", "")
  out = f"Welcome to {MODEL}"
  if inp != "":
    msg = { 
      "model": MODEL,
      "prompt": inp,
      "stream": False
      }
    res = req.post(url, json=msg).json()
    out = res.get("response", "No response")
  return { "output": out }
