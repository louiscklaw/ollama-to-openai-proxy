#!/usr/bin/env python
import requests
import json


def test_tags_endpoint():
    """Test the /api/tags endpoint equivalent to test_tags.http"""

    base_url = "http://192.168.10.1:11434"

    print("Testing /api/tags endpoint...")

    try:
        # Test 1: List available models (Ollama-compatible endpoint)
        print("\n1. Testing GET /api/tags")
        response = requests.get(f"{base_url}/api/tags")

        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("Response:")
            try:
                data = response.json()
                print(json.dumps(data, indent=2))
            except json.JSONDecodeError:
                print(response.text)
        else:
            print(f"Error: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_tags_endpoint()
