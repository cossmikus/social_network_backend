
from typing import Any
from fastapi import Depends
from typing import List
from pydantic import Field, BaseModel

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class LocationDict(BaseModel):
    latitude: float = 0.0
    longitude: float = 0.0


class CreateTweetRequest(AppModel):
    content: str
    caption: str
    hashtags: List[str]
    mentions: List[str]
    links: List[str]
    emojis: List[str]
    address: str
    call_to_action: str
    
    
class CreateTweetResponse(AppModel):
    id: Any = Field(alias="post_id")


class CreateTweetDBModel(CreateTweetRequest):
    location: LocationDict


@router.post("/", response_model=CreateTweetResponse)
def create_post(
    inpu: CreateTweetRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> CreateTweetResponse:
    get_address = inpu.address
    result = svc.here_service.get_coordinates(get_address)
    latitude = result.get('lat', 0.0)
    longitude = result.get('lng', 0.0)
    db_input = CreateTweetDBModel(**inpu.dict(), location=LocationDict(latitude=latitude, longitude=longitude))
    post_id = svc.repository.create_post_rep(jwt_data.user_id, db_input.dict())
    return CreateTweetResponse(id=post_id, result=result)

