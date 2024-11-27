import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import json

load_dotenv()

app = FastAPI()

# CORSミドルウェアを追加して、他のドメインからのリクエストを受け入れられるように設定
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "https://youtube01-791673075181.asia-northeast2.run.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 字幕を取得する関数
def get_transcript(video_id: str):
    try:
        # 字幕を取得 (日本語字幕を優先)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja'])

        text = ""
        if transcript:
            for item in transcript:
                text += item["text"]
        else:
            print("字幕が見つかりませんでした。")

        text1 = {"text": text}
        # 字幕のリストを返す
        return json.dumps(text1, ensure_ascii=False)
    except Exception as e:
        print(f"字幕の取得に失敗しました: {e}")
        return {"error": "字幕の取得に失敗しました"}

# videoIdをクエリパラメータとして受け取るエンドポイント
@app.get("/transcript")
async def get_video_transcript(videoId: str):
    res = get_transcript(videoId)
    return res

@app.get("/")
async def aaa():
    return 'Hello!'
