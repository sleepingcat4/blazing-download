import subprocess
import os

def yt_download(url, proxy=None, batch_file=None, output_dir='.'):
    command = [
        'yt-dlp', 
        '-f', 'bestaudio', 
        '--extract-audio', 
        '--audio-format', 'wav', 
        '--concurrent-fragments', '30',
        '-o', f'{output_dir}/audio%(autonumber)s.%(ext)s'
    ]
    
    if proxy:
        command.extend(['--proxy', proxy])
    
    if batch_file:
        command.extend(['-a', batch_file])
    else:
        command.append(url)
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")
