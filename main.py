from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(debug=True)

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}


# 設定靜態文件目錄（假設你的網頁放在 'static' 資料夾中）
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_index():
    # 這裡返回你的 HTML 文件
    with open("static/index.html") as f:
        return f.read()