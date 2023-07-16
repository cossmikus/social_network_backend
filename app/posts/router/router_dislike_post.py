from fastapi import Depends, Response
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from ..service import Service, get_service
from . import router


class LikePostRequest(AppModel):
    post_id: str


@router.post("/dislike")
def dislike_post(
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
        return Response(status_code=400, content="Cannot dislike your own post")
    if user_id in post.get("disliked_by", []):
        return Response(status_code=400, content="You have already disliked this post")

    # Increment the like count in the database
    svc.repository.increment_dislike_count(post_id)
    svc.repository.add_disliked_by(post_id, user_id)
    return Response(status_code=200, content="Post disliked successfully")
