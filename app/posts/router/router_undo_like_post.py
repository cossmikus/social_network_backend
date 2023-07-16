
from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from ..service import Service, get_service
from . import router


class LikePostRequest(AppModel):
    post_id: str


@router.post("/undo_like")
def undo_like_post(
    request: LikePostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    post_id = request.post_id
    post = svc.repository.get_tweet_by_post_id(post_id)
    if post is None:
        return Response(status_code=404, content="Post not found")
    user_id = jwt_data.user_id
    if user_id == post["user_id"]:
        return Response(status_code=400, content="Cannot undo like your own post")

    if user_id in post.get("liked_by", []):
        svc.repository.decrement_like_count(post_id)
        svc.repository.delete_liked_by(post_id, user_id) 
        return Response(status_code=200, content="Undid the like successfully")
    else:
        return Response(status_code=400, content="Error, maybe you did not like the post, that is why you cannot undo it")
