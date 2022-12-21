from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup as bs

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello From Converter"}


@app.get("/api/rates")
async def convert(_from: str, _to: str, value: int):
    t = requests.get(f'https://www.google.com/search?q={value}+{_from}+to+{_to}')
    soup = bs(t.text, 'lxml')
    for i in soup.find_all('div', class_="BNeawe iBp4i AP7Wnd"):
        res = i.text.split(" ")[0]
    return {"result": f"{res}"}
