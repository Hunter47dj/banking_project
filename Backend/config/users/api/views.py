from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.services.user_service import UserService

class UserAPI(APIView):
    
    def post(self, request):
        try:
            user = UserService.create_user(request.data)
            return Response({
                "id": str(user.id),
                "name": user.name,
                "email": user.email,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }, status=status.HTTP_201_CREATED)
            
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def get(self, request):
        users = UserService.list_users()
        data = [{
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        } for user in users]
        return Response(data, status=status.HTTP_200_OK)