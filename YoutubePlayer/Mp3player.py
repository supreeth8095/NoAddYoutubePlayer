import asyncio
import platform
import yt_dlp
import pygame
import os
import tempfile

FPS = 60

def setup():
    pygame.mixer.init()

async def play_youtube_audio(url, i):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(tempfile.gettempdir(), 'temp_audio'+str(i)+'.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            mp3_file = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')

        pygame.mixer.music.load(mp3_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(2.0 / FPS)

        os.remove(mp3_file)
        print("Temporary file deleted")

    except Exception as e:
        print(f"Error: {e}")


def collect_urls(max_urls=100):
    urls = []
    print(f"Enter URLs (max {max_urls}). Type 'done' to finish early.")

    while len(urls) < max_urls:
        user_input = input(f"Enter URL #{len(urls) + 1} (or 'done' to finish): ").strip()

        if user_input.lower() == 'done':
            break

        if user_input:  # Ensure the input is not empty
            urls.append(user_input)
        else:
            print("Empty input, please enter a valid URL or 'done'.")

    return urls

async def main():
    setup()
    print("Enter list of song you need to listen")
    collected_urls = collect_urls()
    i = 0
    while (i < len(collected_urls)):
        await play_youtube_audio(collected_urls[i],i)
        i+=1

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())