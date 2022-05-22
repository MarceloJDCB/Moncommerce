from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import userSerializer


class usersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    
    def get_queryset(self):
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self,request):
        #print(User.)
        users = self.serializer_class(self.queryset,many=True)
        return Response(data=users.data)