# youtube 字幕取得API
# google cloud run


- Dify、coze、vercelからyoutube_transcript_apiを使って
youtubeにアクセスすると、youtubeから拒否されます。

- 対策として、google cloud runでyoutube_transcript_apiを使って
字幕を取得します。

- アクセス方法はこちら
http://127.0.0.1:8000/transcript?videoId=SQVGzBLoi1M

- 結果はこちら
"{\"text\": \"リモト研究所えとですこの動画ではパプレキシティ最強のAI検索術と.....\"}"

- 解説はこちら
https://qiita.com/sinzy0925/items/7010478f680ea4e29ecd
