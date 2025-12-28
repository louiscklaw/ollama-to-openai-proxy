#!/usr/bin/env python
import requests
import json


def test_generate_endpoint():
    """Test the /api/generate endpoint equivalent to test_generate.http"""

    base_url = "http://192.168.10.1:11434"

    print("Testing /api/generate endpoint...")

    try:
        # Test POST /api/generate
        print("\n1. Testing POST /api/generate")

        payload = {
            "model": "tngtech/deepseek-r1t2-chimera:free",
            "prompt": "[pass|fali]Hi, this is a sanity test. Can you hear me ?",
        }

        headers = {"Content-Type": "application/json"}

        print(f"Request URL: {base_url}/api/generate")
        print(f"Request Headers: {headers}")
        print(f"Request Payload: {json.dumps(payload, indent=2)}")

        response = requests.post(
            f"{base_url}/api/generate", headers=headers, json=payload
        )

        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("Response:")
            try:
                data = response.json()
                print(json.dumps(data, indent=2))
            except json.JSONDecodeError:
                print(response.text)
        else:
            print(f"Error Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    test_generate_endpoint()
