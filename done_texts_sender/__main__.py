import time
from done_texts_sender import config
import db_methods
import requests

while True:
    voice_files_ids_to_send_list = db_methods.voice_files.get_info_for_send()

    for voice_file_id in voice_files_ids_to_send_list:
        resp = requests.get(f"{config.WEBHOOK_HOST}/{config.ROUTE_URL}/send_message?voice_file_id={voice_file_id}")
        db_methods.voice_files.update_as_sent(voice_file_id)
        time.sleep(1)
    time.sleep(1)
