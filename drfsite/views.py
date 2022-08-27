from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet

from shop.models import Product, Category
from .serialesers import productserialers

class any(BasePermission):
    def has_permission(self, request, view):
        return True

class Listrest(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,

                   GenericViewSet):

    serializer_class = productserialers
    permission_classes = (IsAdminUser,)
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        if not pk:
            return Product.objects.all()[:10]

        return Product.objects.filter(pk=pk)
    @action(methods=['get','post'],detail=True)
    def category(self,request,pk=None):
        cat=Category.objects.get(pk=pk)
        return Response({"category":cat.name})








    # def get(self,request):
    #
    #     data = Product.objects.all()
    #
    #     return Response({'get':productserialers(data,many=True).data})
    # def post(self,request):
    #
    #    serilazater=productserialers(data=request.data)
    #    serilazater.is_valid(raise_exception=True)
    #    serilazater.save()
    #    return Response({"post":serilazater.data})
    #
    # def put(self,request,*args,**kwargs):
    #
    #     pk=kwargs.get('pk')
    #     print(kwargs.get("pk"))
    #     if  pk:
    #         instance=Product.objects.get(pk=pk)
    #
    #     else:
    #         return Response("id yoq")
    #
    #     serilazer=productserialers(data=request.data,instance=instance)
    #     serilazer.is_valid(raise_exception=True)
    #     serilazer.save()
    #     return Response(serilazer.data)
    #
    # def delete(self,request,*args,**kwargs):
    #     pk=kwargs.get("pk")
    #     delete=Product.objects.get(pk=pk).delete()
    #     return Response(delete)
