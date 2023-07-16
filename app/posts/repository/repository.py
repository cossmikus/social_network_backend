# # from datetime import datetime
# # from typing import Optional
# from typing import Any
# from bson.objectid import ObjectId
# from pymongo.database import Database
# from pymongo.results import UpdateResult, DeleteResult


# class PostRepository:
#     def __init__(self, database: Database):
#         self.database = database
        
#     def create_post_rep(self, user_id: str, data: dict[str, Any]):
#         data["user_id"] = user_id
#         insert_to_the_db = self.database["posts"].insert_one(data)
#         return insert_to_the_db.inserted_id
  
#     def get_tweet_by_user_id(self, post_id: str):
#         return self.database["posts"].find_one({"_id": ObjectId(post_id)})
    
#     def update_tweet_info(self, post_id: str, 
#                           user_id: str, data: dict[str, Any]) -> UpdateResult:
#         return self.database["posts"].update_one(
#             filter={"_id": ObjectId(post_id), "user_id": ObjectId(user_id)},
#             update={"$set": data},
#         )
        
#     def delete_tweet_info(self, post_id: str, 
#                           user_id: str) -> DeleteResult:
#         return self.database["posts"].delete_one(
#             {"_id": ObjectId(post_id), "user_id": ObjectId(user_id)}
#         )



# from typing import Any
# from bson.objectid import ObjectId
# from pymongo.database import Database
# from pymongo.results import UpdateResult, DeleteResult


# class PostRepository:
#     def __init__(self, database: Database):
#         self.database = database
        
#     def create_post_rep(self, user_id: str, data: dict[str, Any]):
#         data["user_id"] = user_id
#         insert_to_the_db = self.database["posts"].insert_one(data)
#         return str(insert_to_the_db.inserted_id)
  
#     def get_tweet_by_post_id(self, post_id: str):
#         return self.database["posts"].find_one({"_id": ObjectId(post_id)})
    
#     def edit_post_info(self, post_id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
#         return self.database["posts"].update_one(
#             filter={"_id": ObjectId(post_id), "user_id": user_id},
#             update={"$set": data},
#         )
        
#     def delete_tweet_info(self, post_id: str, user_id: str) -> DeleteResult:
#         return self.database["posts"].delete_one(
#             {"_id": ObjectId(post_id), "user_id": user_id}
#         )

# from typing import Any
# from bson.objectid import ObjectId
# from pymongo.database import Database
# from pymongo.results import UpdateResult, DeleteResult


# class PostRepository:
#     def __init__(self, database: Database):
#         self.database = database
        
#     def create_post_rep(self, user_id: str, data: dict[str, Any]):
#         data["user_id"] = user_id
#         insert_to_the_db = self.database["posts"].insert_one(data)
#         return str(insert_to_the_db.inserted_id)
  
#     def get_tweet_by_post_id(self, post_id: str):
#         return self.database["posts"].find_one({"_id": ObjectId(post_id)})
    
#     def edit_post_info(self, post_id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
#         return self.database["posts"].update_one(
#             filter={"_id": ObjectId(post_id), "user_id": user_id},
#             update={"$set": data},
#         )
        
#     def delete_tweet_info(self, post_id: str, user_id: str) -> DeleteResult:
#         return self.database["posts"].delete_one(
#             {"_id": ObjectId(post_id), "user_id": user_id}
#         )

from typing import Any
from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import UpdateResult, DeleteResult


class PostRepository:
    def __init__(self, database: Database):
        self.database = database
        
    def create_post_rep(self, user_id: str, data: dict[str, Any]):
        data["user_id"] = user_id
        data["like_count"] = 0  # Initialize like count to 0
        insert_to_the_db = self.database["posts"].insert_one(data)
        return str(insert_to_the_db.inserted_id)
  
    def get_tweet_by_post_id(self, post_id: str):
        return self.database["posts"].find_one({"_id": ObjectId(post_id)})
    
    def edit_post_info(self, post_id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
        return self.database["posts"].update_one(
            filter={"_id": ObjectId(post_id), "user_id": user_id},
            update={"$set": data},
        )
        
    def delete_tweet_info(self, post_id: str, user_id: str) -> DeleteResult:
        return self.database["posts"].delete_one(
            {"_id": ObjectId(post_id), "user_id": user_id}
        )

    def increment_like_count(self, post_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"like_count": 1}},
        )

    def decrement_like_count(self, post_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"like_count": -1}},
        )
        
    def increment_dislike_count(self, post_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"dislike_count": 1}},
        )

    def decrement_dislike_count(self, post_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$inc": {"dislike_count": -1}},
        )
        
    def add_liked_by(self, post_id: str, user_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$addToSet": {"liked_by": user_id}},
        )

    def add_disliked_by(self, post_id: str, user_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$addToSet": {"disliked_by": user_id}},
        )
        
    def delete_liked_by(self, post_id: str, user_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$pull": {"liked_by": user_id}},
        )
        
    def delete_disliked_by(self, post_id: str, user_id: str) -> UpdateResult:
        return self.database["posts"].update_one(
            {"_id": ObjectId(post_id)},
            {"$pull": {"disliked_by": user_id}},
        )
