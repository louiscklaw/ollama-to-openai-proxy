#!/usr/bin/env python
import requests
import json


def test_chat_endpoint():
    """Test the /api/chat and /api/chat/completions endpoints equivalent to test_chat.http"""

    base_url = "http://192.168.10.1:11434"

    print("Testing chat endpoints...")

    try:
        # Test 1: Chat completion using OpenAI-compatible endpoint (/api/chat)
        print("\n1. Testing POST /api/chat")

        payload1 = {
            "model": "tngtech/deepseek-r1t2-chimera:free",
            "messages": [
                {"role": "user", "content": "[pass|fail]This is a sanity test, can you hear me?"}
            ],
            "stream": False,
            "temperature": 0.7,
            "max_tokens": 512,
        }

        headers = {"Content-Type": "application/json"}

        print(f"Request URL: {base_url}/api/chat")
        print(f"Request Headers: {headers}")
        print(f"Request Payload: {json.dumps(payload1, indent=2)}")

        response1 = requests.post(
            f"{base_url}/api/chat", headers=headers, json=payload1
        )

        print(f"\nStatus Code: {response1.status_code}")
        print(f"Response Headers: {dict(response1.headers)}")

        if response1.status_code == 200:
            print("Response:")
            try:
                data = response1.json()
                print(json.dumps(data, indent=2))
            except json.JSONDecodeError:
                print(response1.text)
        else:
            print(f"Error Response: {response1.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    test_chat_endpoint()
