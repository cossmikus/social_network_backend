# from typing import Any
# from fastapi import Depends, Response
# from pydantic import Field

# from app.auth.adapters.jwt_service import JWTData
# from app.auth.router.dependencies import parse_jwt_user_data
# from app.utils import AppModel

# from ..service import Service, get_service
# from . import router


# class GetMyTweetsTweet(AppModel):
#     id: Any = Field(alias="_id")
#     type: str
#     price: int
#     address: str
#     area: float
#     rooms_count: int
#     description: str
#     longitude: float  # Add longitude field
#     latitude: float  # Add latitude field


# class GetMyTweetsResponse(AppModel):
#     id: Any = Field(alias="_id")
#     type: str
#     price: int
#     address: str
#     area: float
#     rooms_count: int
#     description: str
#     user_id: Any 
#     longitude: float  # Added longitude field
#     latitude: float  # Added latitude field


# @router.get("/{post_id:str}", response_model=GetMyTweetsResponse)
# def view_post(
#     post_id: str,
#     jwt_data: JWTData = Depends(parse_jwt_user_data),
#     svc: Service = Depends(get_service),
# ) -> dict[str, str]:
#     # user_id = jwt_data.user_id
#     # tweets = svc.repository.get_tweet_by_user_id(user_id)
#     the_tweet = svc.repository.get_tweet_by_user_id(post_id)
#     if the_tweet is None:
#         return Response(status_code=404, content="Tweet not found")
#     return GetMyTweetsResponse(**the_tweet)


from typing import Any, List
from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class LocationDict(AppModel):
    latitude: float
    longitude: float
    
    
class GetMyTweetsResponse(AppModel):
    id: Any = Field(alias="_id")
    content: str
    caption: str
    hashtags: List[str]
    mentions: List[str]
    links: List[str]
    emojis: List[str]
    address: str
    call_to_action: str
    user_id: Any 
    location: LocationDict  # Added latitude field


@router.get("/{post_id:str}", response_model=GetMyTweetsResponse)
def view_post(
    post_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetMyTweetsResponse:
    the_tweet = svc.repository.get_tweet_by_post_id(post_id)
    if the_tweet is None:
        return Response(status_code=404, content="Tweet not found")
    return GetMyTweetsResponse(**the_tweet)
