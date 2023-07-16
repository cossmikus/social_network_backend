from fastapi import Depends, Response
from typing import List
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class LocationDict(AppModel):
    latitude: float
    longitude: float


class UpdateMyTweetsTweet(AppModel):
    content: str
    caption: str
    hashtags: List[str]
    mentions: List[str]
    links: List[str]
    emojis: List[str]
    address: str
    call_to_action: str
    location: LocationDict
    

@router.delete("/{post_id:str}")
def delete_post(
    post_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    # user_id = jwt_data.user_id
    delete_temp = svc.repository.delete_tweet_info(
        post_id, jwt_data.user_id
    )
    if delete_temp.deleted_count == 1:
        return Response(status_code=200, content="OK")
    return Response(status_code=404)
