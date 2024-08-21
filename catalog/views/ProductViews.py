import logging

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema, extend_schema_view
from ..models import Product
from ..serializer import ProductSerializer, ProductDetailSerializer
from enums.ResponseStatus import ResponseStatus
from utils.utils import is_uuid
from structs.Response import BaseResponse
from ..filters.ProductFilters import ProductFilter
from drf_spectacular.utils import OpenApiParameter
logger = logging.getLogger('management')
#list=extend_schema(parameters=[
#        OpenApiParameter(name='name__icontains', description="some help text")
#    ])
@extend_schema(responses=list[dict],summary='получить список товаров')
@api_view(['GET'])
def get_products(request: Request) -> Response:
    """получить список товаров
    """
    try:

        products = Product.objects.all()
        filterset = ProductFilter(request.GET, queryset=products)

        if filterset.is_valid():
            products = filterset.qs
        data = BaseResponse(msg=ResponseStatus.SUCCESS, data=ProductSerializer(products, many=True).data)
        return Response(status=status.HTTP_200_OK, data=data.__dict__)

    except Exception as e:
        logger.exception(e)
        raise

@extend_schema(responses=ProductDetailSerializer, summary='информацию о товаре')
@api_view(['GET'])
def get_product_detail(request: Request, id: str) -> Response:
    """получить информацию о товаре
        id (str): Идентификатор товара.
    """
    try:
        if not is_uuid(id):
            return Response(status=status.HTTP_400_BAD_REQUEST, data=BaseResponse(msg=ResponseStatus.INCORRECT_PARAMETER))

        product = Product.objects.get(id=id)
        data = BaseResponse(msg=ResponseStatus.SUCCESS, data=ProductDetailSerializer(product).data)

        return Response(status=status.HTTP_200_OK, data=data.__dict__)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_200_OK, data=BaseResponse(msg=ResponseStatus.OBJECT_DOES_NOT_EXIST))

    except Exception as e:
        logger.exception(e)
        raise








