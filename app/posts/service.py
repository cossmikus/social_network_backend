from pydantic import BaseSettings

from app.config import database

from .adapters.here_service import HereService
from .repository.repository import PostRepository


class Config(BaseSettings):
    HERE_API_KEY: str


class Service:
    def __init__(self):
        config = Config()        
        self.repository = PostRepository(database)
        self.here_service = HereService(config.HERE_API_KEY)


def get_service():
    svc = Service()
    return svc
