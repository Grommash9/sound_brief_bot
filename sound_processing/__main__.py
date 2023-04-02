import time

import requests
import os
import pathlib
import db_methods

headers = {
    'Authorization': 'Bearer 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',
}
voice_messages_path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), 'voice_files')


while True:
    for voice_file in os.listdir(voice_messages_path):
        if not voice_file.endswith('.mp3'):
            continue

        input_file = os.path.join(voice_messages_path, voice_file)

        files = {
            'file': open(input_file, 'rb'),
            'model': (None, 'whisper-1'),
        }

        response = requests.post('https://api.openai.com/v1/audio/transcriptions', headers=headers, files=files)

        if response.status_code != 200:
            continue

        os.remove(input_file)
        message_data = voice_file.split('.')[0]
        chat_id, message_id = map(int, message_data.split('_'))
        db_methods.voice_files.update_text(response.json()['text'], chat_id, message_id)

    time.sleep(1)