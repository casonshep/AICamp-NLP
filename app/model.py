import requests
import json

API_URL = "https://api-inference.huggingface.co/models/casonshep/NLP-TaylorSwift"
headers = {"Authorization": "Bearer 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"}


def query(payload):
  data = json.dumps(payload)
  response = requests.request("POST", API_URL, headers=headers, data=data)
  return json.loads(response.content.decode("utf-8"))
