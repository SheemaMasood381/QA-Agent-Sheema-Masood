import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, VideoUnavailable

def get_youtube_transcript(video_url: str, save_path: str):
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "w", encoding="utf-8") as f:
            for entry in transcript:
                f.write(f"{entry['text']}\n")
        return save_path
    except NoTranscriptFound:
        print("🚫 No transcript found for this video (maybe no captions available).")
    except VideoUnavailable:
        print("🚫 Video is unavailable (private, deleted, or region blocked).")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def chunk_transcript(transcript_path: str, chunk_size: int = 600):
    with open(transcript_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks
