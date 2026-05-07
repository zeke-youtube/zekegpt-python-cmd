import requests
import os
from colorama import Fore, Style, init

init(autoreset=True)

URL = "https://zekegpt.pikastudio.dpdns.org/devapi/v1/chat"

os.system("cls" if os.name == "nt" else "clear")

print(Fore.CYAN + """
============================================
                ZekeGPT
      official cli by ZekeLabs
============================================
""")

token = input(Fore.YELLOW + "Enter token: ")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

chat_history = []

while True:
    message = input(Fore.GREEN + "\nYou: ")

    if message.lower() in ["exit", "quit"]:
        break

    chat_history.append({
        "role": "user",
        "content": message
    })

    try:
        response = requests.post(
            URL,
            headers=headers,
            json={
                "message": message,
                "history": chat_history
            },
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()

            ai = result.get("response", "No response")

            print(Fore.CYAN + "\nZekeGPT:", ai)

            chat_history.append({
                "role": "assistant",
                "content": ai
            })

        else:
            print(Fore.RED + f"\nHTTP {response.status_code}")
            print(response.text)

    except requests.exceptions.Timeout:
        print(Fore.RED + "\nRequest timed out")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\nRequest failed: {e}")
