import requests
import os
import json
import base64
from datetime import datetime

# =========================
# ZekeGPT CLI
# official by ZekeLabs
# =========================

BASE_URL = "https://zekegpt.pikastudio.dpdns.org/devapi/v1"

chat_url = f"{BASE_URL}/chat"
image_url = f"{BASE_URL}/image"

chat_history = []

# clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("""
============================================
                ZekeGPT
         official cli by ZekeLabs
============================================

Commands:
/help       show commands
/clear      clear chat history
/savechat   save chat to txt
/image      generate image
/exit       quit
""")

# token
token = "PUT_YOUR_TOKEN_HERE"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def save_chat():
    if not chat_history:
        print("No chat history to save")
        return

    filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for msg in chat_history:
            f.write(f"{msg['role']}: {msg['content']}\n")

    print(f"Saved chat to {filename}")


def generate_image():
    prompt = input("Image prompt: ")

    print("Generating image...")

    try:
        response = requests.post(
            image_url,
            headers=headers,
            json={
                "prompt": prompt,
                "size": "1024x1024"
            },
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()

            image_base64 = result["data"][0]["b64_json"]

            image_bytes = base64.b64decode(image_base64)

            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

            with open(filename, "wb") as f:
                f.write(image_bytes)

            print(f"Saved image as {filename}")

        else:
            print(f"HTTP {response.status_code}")
            print(response.text)

    except Exception as e:
        print("Image generation failed:", e)


def send_chat(message):
    global chat_history

    chat_history.append({
        "role": "user",
        "content": message
    })

    print("ZekeGPT is thinking...\n")

    try:
        response = requests.post(
            chat_url,
            headers=headers,
            json={
                "message": message,
                "history": chat_history
            },
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()

            ai_response = result.get("response", "No response")

            print("ZekeGPT:", ai_response)

            chat_history.append({
                "role": "assistant",
                "content": ai_response
            })

        else:
            print(f"HTTP {response.status_code}")
            print(response.text)

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# =========================
# main loop
# =========================

while True:
    user_input = input("\nYou: ")

    if not user_input.strip():
        continue

    # commands

    if user_input == "/help":
        print("""
Commands:
/help       show commands
/clear      clear chat history
/savechat   save chat to txt
/image      generate image
/exit       quit
""")
        continue

    if user_input == "/clear":
        chat_history = []
        print("Chat history cleared")
        continue

    if user_input == "/savechat":
        save_chat()
        continue

    if user_input == "/image":
        generate_image()
        continue

    if user_input == "/exit":
        print("Goodbye!")
        break

    # normal chat
    send_chat(user_input)
