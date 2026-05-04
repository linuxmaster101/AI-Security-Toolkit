import requests

API_URL = "https://api.example.com/chat"  # غيره حسب الهدف

def load_payloads():
    with open("payloads.txt") as f:
        return f.read().splitlines()

def test_payload(payload):
    data = {
        "message": payload
    }

    try:
        r = requests.post(API_URL, json=data)
        return r.text
    except Exception as e:
        return str(e)

def main():
    payloads = load_payloads()

    for p in payloads:
        print(f"\n[+] Testing: {p}")
        response = test_payload(p)
        print(f"[Response]: {response[:200]}")

if __name__ == "__main__":
    main()
