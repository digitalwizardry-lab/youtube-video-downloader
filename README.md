# YouTube Video Downloader

A command-line tool to download YouTube videos using `yt-dlp`. Supports downloading single videos or multiple videos from a list, with options for automatic download confirmation and quality selection.

## Features

- Download a single YouTube video
- Download multiple YouTube videos from a list
- Choose video quality (best, worst, or specific resolution)
- Automatic download confirmation option

## Requirements

- Python 3.6+
- `yt-dlp` package

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/digitalwizardry-lab/youtube-video-downloader.git
   cd youtube-video-downloader
   ```

2. Install the required packages:

   ```sh
   pip install yt-dlp
   ```

## Usage

### Download a Single Video

To download a single video with the highest quality:

```sh
python download_youtube_video.py <video_url> -p <save_path> -a -q best
```

### Download a Single Video with Specific Quality

To download a single video with a specific resolution (e.g., 720p):

```sh
python download_youtube_video.py <video_url> -p <save_path> -a -q 720
```

### Download Multiple Videos from a List

To download videos from a list in a text file:

```sh
python download_youtube_video.py -l video_list.txt -p <save_path> -a -q best
```

### Options

- `url`: The URL of the YouTube video.
- `-p, --path`: The path where you want to save the video (default is current directory).
- `-a, --auto-confirm`: Automatically confirm the download without asking.
- `-l, --list`: Path to a text file containing YouTube video URLs (one URL per line).
- `-q, --quality`: Set the quality of the video (best, worst, or specify a resolution like 720).

## Examples

1. **Download a single video with the highest quality:**

   ```sh
   python download_youtube_video.py https://www.youtube.com/watch?v=lnpQ-d-3xOQ -p /path/to/save -a -q best
   ```

2. **Download a single video with the lowest quality:**

   ```sh
   python download_youtube_video.py https://www.youtube.com/watch?v=lnpQ-d-3xOQ -p /path/to/save -a -q worst
   ```

3. **Download a single video with a specific resolution (e.g., 720p):**

   ```sh
   python download_youtube_video.py https://www.youtube.com/watch?v=lnpQ-d-3xOQ -p /path/to/save -a -q 720
   ```

4. **Download videos from a list in a text file:**

   ```sh
   python download_youtube_video.py -l video_list.txt -p /path/to/save -a -q best
   ```

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure you have the latest version of `yt-dlp`:

  ```sh
  pip install --upgrade yt-dlp
  ```

- Verify the YouTube URL is correct.
- Make sure you have an active internet connection.
If the problem persists, feel free to open an issue on the [GitHub repository](https://github.com/digitalwizardry-lab/youtube-video-downloader/issues).
