import os
import yt_dlp

def download_youtube_audio_as_mp3(youtube_url, output_path, ffmpeg_location=None):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Use video title as filename
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        if ffmpeg_location:
            ydl_opts['ffmpeg_location'] = ffmpeg_location

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print(f"Download and conversion complete: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # YouTube video URL
    youtube_url = input("Enter the YouTube video URL: ")
    
    # Output directory
    output_path = input("Enter the output directory path: ")
    
    # Optional FFmpeg location
    ffmpeg_location = input("Enter the FFmpeg location (leave blank if in PATH): ")
    
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Download and convert
    download_youtube_audio_as_mp3(youtube_url, output_path, ffmpeg_location if ffmpeg_location else None)
