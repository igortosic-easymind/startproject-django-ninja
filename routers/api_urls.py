# routers/api.py
from ninja import NinjaAPI
from users.views import user_router
from clients.views import client_router

api = NinjaAPI()

api.add_router("/users/", user_router, tags=["Users API"])
api.add_router("/clients/", client_router, tags=["Clients API"])
