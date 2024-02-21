from typing import Any
import requests
from flask import Flask, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        return "Hello world service!"

    @app.route("/service_output", methods=["POST"])
    def inference() -> dict[str, Any]:
        input = request.json
        url = 'http://host.docker.internal:8081/api/v1/functions/execute'
        payload = {
            "function_id": "bafybeiaugwh3mktzbnudurzk7jcyvmdhyy6jnairiu2phuf2t7c7orowjq",
            "method": "footest.wasm",
            "parameters": None,
            "config": {
                "env_vars": [
                    {"name": "BLS_REQUEST_PATH", "value": "/api"},
                ],
                "number_of_nodes": -1,
                "timeout": 2
            }
        }


        # Set the Content-Type header
        headers = {'Content-Type': 'application/json'}

        # Make the POST request
        response = requests.post(url, json=payload, headers=headers)

        return {"output": f"hello, world!, your input was: {input}", "response" : response.text}

    return app