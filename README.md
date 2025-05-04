# YouTube Audio Player

A Python script that allows users to input a list of YouTube URLs, download their audio tracks, convert them to MP3, and play them sequentially using `pygame`. The script uses `yt_dlp` for downloading and `FFmpeg` for audio conversion, with asynchronous execution handled by `asyncio`.

## Features
- **Input Multiple URLs**: Collect up to 100 YouTube URLs (or fewer if the user chooses to stop early).
- **Audio Extraction**: Downloads and converts YouTube audio to MP3 format using `yt_dlp` and `FFmpeg`.
- **Sequential Playback**: Plays each audio file in sequence using `pygame.mixer`.
- **Temporary File Management**: Automatically deletes temporary MP3 files after playback.
- **Cross-Platform Support**: Runs on Windows, macOS, Linux, and potentially in WebAssembly environments (e.g., Emscripten).

## Prerequisites
To run this script, ensure you have the following installed:
- **Python 3.7+**: Download from [python.org](https://www.python.org/downloads/).
- **FFmpeg**: A command-line tool for audio conversion.
- A working internet connection for downloading YouTube audio.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/youtube-audio-player.git
cd youtube-audio-player
```

### 2. Install Python Dependencies
Install the required Python libraries using `pip`:
```bash
pip install yt_dlp pygame
```

### 3. Install FFmpeg
FFmpeg is required for audio extraction and conversion.

#### On Windows
1. Download FFmpeg from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) or the [official website](https://ffmpeg.org/download.html).
2. Extract the archive and add the `bin` folder to your system PATH:
   - Go to System Properties > Advanced > Environment Variables.
   - Edit the `Path` variable and add the path to the FFmpeg `bin` folder (e.g., `C:\ffmpeg\bin`).
3. Verify installation:
   ```bash
   ffmpeg -version
   ```

#### On macOS
1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install FFmpeg:
   ```bash
   brew install ffmpeg
   ```
3. Verify installation:
   ```bash
   ffmpeg -version
   ```

#### On Linux
Install FFmpeg using your package manager:
- **Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **Fedora**:
  ```bash
  sudo dnf install ffmpeg
  ```
- **Arch Linux**:
  ```bash
  sudo pacman -S ffmpeg
  ```
Verify installation:
```bash
ffmpeg -version
```

## Usage
1. Run the script:
   ```bash
   python youtube_audio_player.py
   ```
2. Follow the prompts to enter YouTube URLs:
   - Enter up to 100 URLs, one at a time.
   - Type `done` to finish early.
   - Empty inputs will prompt for a valid URL or `done`.
3. The script will:
   - Download the audio from each URL.
   - Convert it to MP3.
   - Play each track sequentially.
   - Delete the temporary MP3 file after playback.

### Example
```
Enter list of song you need to listen
Enter URLs (max 100). Type 'done' to finish early.
Enter URL #1 (or 'done' to finish): https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter URL #2 (or 'done' to finish): done
```

The script will download and play the audio from the provided URL, then clean up the temporary file.

## Dependencies
- **Python Libraries**:
  - `yt_dlp`: For downloading and extracting audio from YouTube.
  - `pygame`: For audio playback.
  - Install with: `pip install yt_dlp pygame`
- **System Dependency**:
  - `FFmpeg`: For audio conversion (must be in system PATH).
- **Built-in Python Libraries** (no installation needed):
  - `asyncio`
  - `platform`
  - `os`
  - `tempfile`

## Notes
- **Temporary Files**: The script stores temporary MP3 files in the system's temporary directory (accessed via `tempfile.gettempdir()`). Ensure write permissions are available.
- **Internet Connection**: Required for downloading audio from YouTube.
- **Emscripten Support**: The script includes a platform check for Emscripten (WebAssembly). This is primarily for browser-based execution (e.g., via Pyodide). For standard desktop use, this does not affect functionality.
- **Error Handling**: The script catches and displays errors during download, conversion, or playback.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [yt_dlp](https://github.com/yt-dlp/yt-dlp) for YouTube audio downloading.
- [pygame](https://www.pygame.org/) for audio playback.
- [FFmpeg](https://ffmpeg.org/) for audio conversion.