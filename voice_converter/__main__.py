import os
import pathlib
import subprocess

voice_messages_path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), 'voice_files')


for voice_file in os.listdir(voice_messages_path):
    if not voice_file.endswith('.oga'):
        continue
    input_file = os.path.join(voice_messages_path, voice_file)

    output_file = os.path.join(voice_messages_path, voice_file.split('.')[0] + '.mp3')

    # subprocess.call(['/Users/oleksandr/Downloads/ffmpeg', '-i', input_file, '-acodec', 'libmp3lame', '-ab', '192k', output_file])
    subprocess.call(['ffmpeg', '-i', input_file, '-acodec', 'libmp3lame', '-ab', '192k', output_file])
    os.remove(input_file)
