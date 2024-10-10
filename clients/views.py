# clients/views.py
from typing import List
from ninja import Router
from clients import models
from clients.forms import ClientForm
from django.shortcuts import get_object_or_404
from clients.schemas import ClientSchema, ClientCreateSchema, ClientUpdateSchema

## from ninja.security import django_auth
from ninja.security import HttpBearer
import jwt
from django.conf import settings
from jwt.exceptions import InvalidTokenError
from django.contrib.auth import get_user_model
from django.forms import model_to_dict

User = get_user_model()


class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            # Decode the JWT token
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            username = decoded_token.get("username")
            if username:
                # Fetch the user based on the username in the token
                try:
                    user = User.objects.get(username=username)
                    return user
                except User.DoesNotExist:
                    return None
        except InvalidTokenError:
            return None


client_router = Router()


@client_router.get("", response=List[ClientSchema], auth=JWTAuth())
def get_clients(request):
    clients = models.Client.objects.all()
    return clients


@client_router.post(
    "add", response={201: ClientSchema, 400: dict, 401: dict}, auth=JWTAuth()
)
def add_client(request, payload: ClientCreateSchema):
    user = request.auth  # JWTAuth sets the authenticated user here
    if user is not None:
        form = ClientForm(payload.dict())
        if form.is_valid():
            client = form.save(commit=False)
            client.user = user
            client.save()
            return 201, model_to_dict(client)
        return 400, {"error": "Invalid data", "details": form.errors}
    return 401, {"error": "Unauthorized"}


@client_router.get("{pk}", response=ClientSchema, auth=JWTAuth())
def view_client(request, pk: int):
    client = get_object_or_404(models.Client, id=pk)
    return client


@client_router.put("edit/{pk}", response={200: ClientSchema, 400: str}, auth=JWTAuth())
def update_client(request, pk: int, payload: ClientUpdateSchema):
    client = get_object_or_404(models.Client, id=pk)
    form = ClientForm(payload.dict(), instance=client)
    if form.is_valid():
        client = form.save()
        return 200, client
    return 400, "Invalid data"


@client_router.delete("delete/{pk}", response={200: str, 404: str}, auth=JWTAuth())
def delete_client(request, pk: int):
    client = get_object_or_404(models.Client, id=pk)
    client.delete()
    return 200, "successful deleted"
