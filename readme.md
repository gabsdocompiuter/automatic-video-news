# Automatic Video News


## Modules Usage

### news_reader

```python
from news_reader import JornalDoPovo

jp = JornalDoPovo()
jp.get_headlines(limit=5)
```

### text_to_speech

```python
from text_to_speech import Speech

sp = Speech()
sp.add_phrase('heeey')
sp.add_phrase('i am an audio file')
audio_file = sp.save('file', extension='mp3')
```

### video_maker

```python
from video_maker import VideoMaker

image = 'image.jpg'
audio = 'audio.mp3'

vk = VideoMaker()
vk.create_clip(image, audio)

video = vk.save_video('video', extension='mp4')
```