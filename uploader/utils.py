from firebase_admin import auth
from django.http import JsonResponse

def verify_firebase_token(request):
    auth_header = request.headers.get("Authorization") or request.META.get("HTTP_AUTHORIZATION")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise Exception("Authorization header missing or invalid")

    token = auth_header.replace("Bearer ", "")

    decoded_token = auth.verify_id_token(token)
    return decoded_token["uid"]
