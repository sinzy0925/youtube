# Pythonのベースイメージを作成
FROM python:3.11.3
# 作業ディレクトリを指定
WORKDIR /app
# 依存関係ファイルをコピー
COPY requirements.txt .
# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt
# アプリケーションファイルのコピー
COPY . .
# Uvicornを使用してアプリケーションを実行（JSON形式に修正）
CMD ["uvicorn", "app.youtube_api:app", "--host", "0.0.0.0", "--port", "8080"]
