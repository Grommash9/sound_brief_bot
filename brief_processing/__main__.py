import time
import db_methods
import requests
import json


while True:
    voice_files_ids = db_methods.voice_files.get_all_to_make_short()

    for voice_file_id in voice_files_ids:
        voice_message_text = db_methods.voice_files.get_text(voice_file_id)

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer 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",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "можешь выделить из текста суть и написать коротко о чем в нем сказано пиши на языке на котором записан текст"},
                {"role": "user",
                 "content": voice_message_text}]
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            continue

        short_text = response.json()['choices'][0]['message']['content']

        db_methods.voice_files.update_short_text(short_text, voice_file_id)

    time.sleep(1)
