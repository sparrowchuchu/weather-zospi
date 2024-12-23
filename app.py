from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI(debug=True)

# 設置靜態文件目錄
app.mount("/static", StaticFiles(directory="static"), name="static")
    
# 設置模板目錄
templates = Jinja2Templates(directory="templates")

# Mount the static files directory to serve CSS, JS, and images
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

  
# CMD運行指令
# vicorn app:app --reload
# uvicorn app:app --host 0.0.0.0 --port 8000 --reload
