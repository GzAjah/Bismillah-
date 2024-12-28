
import time
from instagrapi import Client
from config import USERNAME, PASSWORD, OPENAI_API_KEY
import openai

# Login ke Instagram
def login_to_instagram():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    return cl

# Membuat balasan AI dengan OpenAI
def generate_ai_response(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response['choices'][0]['text'].strip()

# Membaca dan membalas pesan DM
def reply_to_dms(cl):
    inbox = cl.direct_threads()
    for thread in inbox:
        last_message = thread.messages[0]
        if not last_message.user_id == cl.user_id:
            print(f"Membalas pesan dari {last_message.user.username}: {last_message.text}")
            reply = generate_ai_response(f"Balas pesan ini: {last_message.text}")
            cl.direct_message(thread.id, reply)
            print(f"Balasan: {reply}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        client = login_to_instagram()
        print("Login berhasil!")
        reply_to_dms(client)
        print("Semua pesan sudah dibalas.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
