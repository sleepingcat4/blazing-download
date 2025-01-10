I had trying to solve a problem of downloading audio files without risking large file storage commitment and how it can be scaled. Obviously, it is not an one person activity since it is dependent on the libraries being used and infrastructure as well. 
In this repository, I tried to make it look simple by writing and sharing just the functions and how these can be used by anyone to download audios and then compress them in a state so that 12M videos become 31GB storage headache. 

I've nothing aganist if you are storing them in original format and need close to 500 (terabytes) to store the same audio without any compression. That's your freedom. 

To use this repository:

headover and download:
```
pip install yt-dlp
```

Additionally make sure you have ffmpeg installed on your system. and you're done. Btw if you want to download 12M videos without batching them and without using 50-100 servers, I think you will be on wheelchair before the download is done, haha!

You need very fast connection speed, proxies and routing infrastructure to sustain such large operations. Don't get me wrong but I won't share my tricks with you.

Filenames are simple
1. `get_audio.py` - downloads the audio (very large files)
2. `reduce_audio.py` - makes them very small like 1-2MB
