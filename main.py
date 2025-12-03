"""
Fast run server file 
Файл был сделан для тестирования сайта на мобилках :3

Made with ❤️ by @snowlover4ever
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/", StaticFiles(directory='.'))

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)