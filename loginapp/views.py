from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User

class GoogleLogin(APIView):
    def post(self, request):
        token = request.data.get('token')
        client_id = settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id']  # Get client ID from settings

        try:
            user_info = id_token.verify_oauth2_token(token, requests.Request(), client_id)

            email = user_info["email"]
            username = email.split("@")[0]

            # Get or create the user
            user, created = User.objects.get_or_create(
                email=email,
                defaults={"username": username, "first_name": user_info.get("given_name", username)}
            )

            return Response({
                'status': 'success',
                'user': {
                    'email': user.email,
                    'name': user.username,
                }
            })

        except ValueError:
            return Response({'status': 'invalid token'}, status=400)

