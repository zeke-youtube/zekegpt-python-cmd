import requests

url = "https://zekegpt.pikastudio.dpdns.org/devapi/v1/chat"

print("============================================")
print("                ZekeGPT                     ")
print("  tool by ZekeLabs (official zekegpt owner) ")
print("============================================")

token = input("Enter your token: ")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def loop():
    while True:
        message = input("You: ")

        data = {
            "message": message
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                result = response.json()
                print("ZekeGPT:", result["response"])
            else:
                print("Error:", response.status_code)
                print(response.text)

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)


loop()