# from fastapi import Depends, Response

# from app.auth.adapters.jwt_service import JWTData
# from app.auth.router.dependencies import parse_jwt_user_data
# from app.utils import AppModel

# from ..service import Service, get_service
# from . import router
# from typing import List


# class LocationDict(AppModel):
#     latitude: float
#     longitude: float
    
    
# class UpdateMyTweetsTweet(AppModel):
#     content: str
#     caption: str
#     hashtags: List[str]
#     mentions: List[str]
#     links: List[str]
#     emojis: List[str]
#     address: str
#     call_to_action: str    
#     location: LocationDict  # Added latitude field


# @router.patch("/{post_id:str}")
# def edit_post(
#     post_id: str,
#     input: UpdateMyTweetsTweet,
#     jwt_data: JWTData = Depends(parse_jwt_user_data),
#     svc: Service = Depends(get_service),
# ) -> dict[str, str]:
#     update_temp = svc.repository.edit_post_info(
#         post_id, jwt_data.user_id, input.dict()
#     )
#     if update_temp.modified_count == 1:
#         return Response(status_code=200, content="OK")
#     return Response(status_code=404)


from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from ..service import Service, get_service
from . import router
from typing import List


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
    location: LocationDict  # Added latitude field


@router.patch("/{post_id:str}")
def edit_post(
    post_id: str,
    input: UpdateMyTweetsTweet,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    existing_post = svc.repository.get_tweet_by_post_id(post_id)
    if existing_post is None:
        return Response(status_code=404, content="Tweet not found")
    update_data = input.dict(exclude_unset=True)
    update_temp = svc.repository.edit_post_info(
        post_id, jwt_data.user_id, update_data
    )
    if update_temp.modified_count == 1:
        return Response(status_code=200, content="OK")
    return Response(status_code=404)
