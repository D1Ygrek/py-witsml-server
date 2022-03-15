from fastapi import (FastAPI, Header, WebSocket, HTTPException, 
                        Depends, Request, Response)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from parsers.request_parser import what_do_you_need

from responsers.get_version import return_version
from responsers.get_cap import return_cap
from responsers.get_base_msg import return_base_msg
from responsers.get_from_store import return_from_store

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

security = HTTPBasic()

@app.websocket('/sapi')
async def connect_client(websocket: WebSocket):
    #print(credentials.username, credentials.password)
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            print(data)
            print('flsdhfikusdhfiuo')
            print(data.decode('ascii'))
    except Exception as exc:
        print('ws closed', exc)

@app.post('/sapi')
async def return_entry(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    responses = {
        'GetVersion': return_version,
        'GetCap': return_cap,
        'GetBaseMsg': return_base_msg,
        'GetFromStore': return_from_store
    }
    ask = await request.body()
    f_name,params = what_do_you_need(ask.decode('utf-8'))
    print(f'<----{f_name}---->')
    #TODO: print(credentials.username, credentials.password)



    data = responses.get(f_name)(params)
    return Response(content=str(data), media_type="text/xml")