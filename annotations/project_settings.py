from pydantic import BaseSettings

class Settings(BaseSettings):
    pg_config: str
    token_key: str
    redis_sentinels: str
    self_url: str
    holder_url: str
    rigserver_url: str
    mongo_cn_string: str
    class Config:
        env_file = '.env'