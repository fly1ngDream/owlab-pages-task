from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Page, VersionsThread
from .serializers import PageSerializer, VersionsThreadSerializer


class PageListView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(generics.RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageVersionListView(generics.ListAPIView):
    model = Page
    serializer_class = PageSerializer

    def get_queryset(self):
        obj = self.model.objects.get(id=self.kwargs.get('pk'))

        return obj.versions


class PageVersionDetailView(generics.RetrieveAPIView):
    model = Page
    serializer_class = PageSerializer

    def get_object(self):
        obj = self.model.objects.get(id=self.kwargs.get('pk'))
        version = float(self.kwargs.get('version'))

        return obj.versions.get(version=version)


class PageVersionCurrentDetailView(generics.RetrieveAPIView):
    model = Page
    serializer_class = PageSerializer

    def get_object(self):
        obj = self.model.objects.get(id=self.kwargs.get('pk'))

        return obj.versions.get(is_current=True)


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)
