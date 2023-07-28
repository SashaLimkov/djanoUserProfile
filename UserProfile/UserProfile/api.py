from ninja import NinjaAPI, Schema

from api.routers import profile_router

api = NinjaAPI()

api.add_router("/profile/", profile_router)