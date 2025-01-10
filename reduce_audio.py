import os
import subprocess

def compress_wav(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.replace(".wav", "_compressed.mp3"))
            
            compress_command = f'ffmpeg -i "{input_file}" -codec:a libmp3lame -b:a 128k "{output_file}"'
            try:
                subprocess.run(compress_command, shell=True, check=True)
                print(f"Compressed {file_name} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error during compression of {file_name}: {e}")
