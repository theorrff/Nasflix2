import os

def scan_videos(directory):
    video_extensions = ['.mp4', '.mkv', '.avi']
    videos = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in video_extensions):
                videos.append(os.path.join(root, file))
    return videos

video_list = scan_videos("home/theo/test/films")
print(video_list)
