from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class Settings(BaseSettings):
    # run_configuration
    run: RunConfig = RunConfig()

    # db
    # db_url: str

    # prefix
    api_prefix: str = "/api"


settings = Settings()
