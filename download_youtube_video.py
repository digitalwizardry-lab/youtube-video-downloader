import argparse
import yt_dlp
from yt_dlp.utils import DownloadError, ExtractorError

def download_youtube_video(url, save_path=".", auto_confirm=False, quality="best"):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }
        if quality == "worst":
            ydl_opts['format'] = 'worst'
        elif quality == "best":
            ydl_opts['format'] = 'best'
        else:
            ydl_opts['format'] = f'best[height<={quality}]'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            print(f"Title: {info_dict.get('title')}")
            print(f"Number of views: {info_dict.get('view_count')}")
            print(f"Length of video: {info_dict.get('duration')} seconds")

            if not auto_confirm:
                confirm = input("Do you want to download this video? (Y/n): ").strip().lower()
                if confirm == 'n':
                    print("Download canceled.")
                    return

            print("Downloading...")
            ydl.download([url])
            print("Download completed!")
    except DownloadError as e:
        print(f"DownloadError: {e}")
    except ExtractorError as e:
        print(f"ExtractorError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def download_from_list(file_path, save_path=".", auto_confirm=False, quality="best"):
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()
        
        for url in urls:
            url = url.strip()
            if url:
                download_youtube_video(url, save_path, auto_confirm, quality)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    parser.add_argument("url", nargs='?', help="The URL of the YouTube video.")
    parser.add_argument("-p", "--path", default=".", help="The path where you want to save the video (default is current directory).")
    parser.add_argument("-a", "--auto-confirm", action="store_true", help="Automatically confirm the download without asking.")
    parser.add_argument("-l", "--list", help="Path to a text file containing YouTube video URLs (one URL per line).")
    parser.add_argument("-q", "--quality", default="best", help="Set the quality of the video (best, worst, or specify a resolution like 720).")

    args = parser.parse_args()

    if args.list:
        download_from_list(args.list, args.path, args.auto_confirm, args.quality)
    elif args.url:
        download_youtube_video(args.url, args.path, args.auto_confirm, args.quality)
    else:
        print("Please provide a YouTube video URL or a file containing URLs.")
