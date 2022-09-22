import uvicorn
import json

from fastapi import (FastAPI, Header, WebSocket, HTTPException, 
                        Depends, Request, Response)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from sqlalchemy import text
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from annotations.project_settings import Settings

from parsers.request_parser import what_do_you_need

from responsers.get_version import return_version
from responsers.get_cap import return_cap
from responsers.get_base_msg import return_base_msg
from responsers.get_from_store import return_from_store

settings = Settings()

app = FastAPI()

origins = [
    "*"
]

engine = engine.create_async_engine(settings.pg_config, echo = False)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

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

@app.post("/getNameWellByUidWell")
async def get_well_name_by_id(
    request: Request, 
    credentials: HTTPBasicCredentials = Depends(security), 
    session: AsyncSession = Depends(get_session)
    ):
    ask = await request.body()
    ask_id = json.loads(ask)['id']
    sql_text = text(f"""
        SELECT name FROM main.well WHERE id = {ask_id}
    """)
    res = await session.execute(sql_text)
    await session.commit()
    return (res.all()[0].name)

@app.post("/getNameWellboreByUidWellbore")
async def get_well_name_by_id(
    request: Request, 
    credentials: HTTPBasicCredentials = Depends(security), 
    session: AsyncSession = Depends(get_session)
    ):
    ask = await request.body()
    ask_id = json.loads(ask)['id']
    sql_text = text(f"""
        SELECT name FROM main.borehole WHERE id = {ask_id}
    """)
    res = await session.execute(sql_text)
    await session.commit()
    return (res.all()[0].name)

@app.post("/getListActiveWells")
async def get_well_name_by_id( 
    credentials: HTTPBasicCredentials = Depends(security), 
    session: AsyncSession = Depends(get_session)
    ):
    sql_text = text(f"""
        SELECT * FROM main.well WHERE well_type = 1
    """)
    res = await session.execute(sql_text)
    await session.commit()
    return (res.all())
    

if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port=3335, reload = True)