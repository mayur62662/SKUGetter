from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location, Department,Category, SubCategory
from .serializers import *
import json


# Location section

@api_view(['GET'])
def get_location(request):
    data_objects = Location.objects.all()
    serializer = LocationSerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_location(request, name):
    data_objects = Location.objects.filter(name = name)
    serializer = LocationSerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_location_detail(request, pk):

    data_object = get_object_or_404(Location, pk=pk)
    serializer = LocationSerializer(data_object)
    return Response(serializer.data)


@api_view(['POST'])
def post_location(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return a 201 Created status for successful POST
    return Response(serializer.errors, status=400)  # Return a 400 Bad Request status for invalid data


@api_view(['PUT'])
def put_location(request, pk):
    data_object = get_object_or_404(Location, pk=pk)
    serializer = LocationSerializer(data_object, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_location(request, pk):
    data_object = get_object_or_404(Location, pk=pk)
    data_object.delete()
    return Response(status=204)  # Return a 204 No Content status for successful DELETE


# Department section


@api_view(['GET'])
def get_department(request):
    data_objects = Department.objects.all()
    serializer = DepartmentSerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_department(request, name):
    data_objects = Department.objects.filter(name = name)
    serializer = DepartmentSerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_department_detail(request, pk):

    data_object = get_object_or_404(Department, pk=pk)
    serializer = DepartmentSerializer(data_object)
    return Response(serializer.data)


@api_view(['POST'])
def post_department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return a 201 Created status for successful POST
    return Response(serializer.errors, status=400)  # Return a 400 Bad Request status for invalid data


@api_view(['PUT'])
def put_department(request, pk):
    data_object = get_object_or_404(Department, pk=pk)
    serializer = DepartmentSerializer(data_object, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_department(request, pk):
    data_object = get_object_or_404(Department, pk=pk)
    data_object.delete()
    return Response(status=204)  # Return a 204 No Content status for successful DELETE


# Category section


@api_view(['GET'])
def get_category(request):
    data_objects = Category.objects.all()
    serializer = CategorySerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category_detail(request, pk):

    data_object = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(data_object)
    return Response(serializer.data)


@api_view(['GET'])
def search_category(request, name):
    data_objects = Category.objects.filter(name = name)
    serializer = CategorySerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return a 201 Created status for successful POST
    return Response(serializer.errors, status=400)  # Return a 400 Bad Request status for invalid data


@api_view(['PUT'])
def put_category(request, pk):
    data_object = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(data_object, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_category(request, pk):
    data_object = get_object_or_404(Category, pk=pk)
    data_object.delete()
    return Response(status=204)  # Return a 204 No Content status for successful DELETE


# Subcategory section

@api_view(['GET'])
def get_subcategory(request):
    data_objects = SubCategory.objects.all()
    serializer = SubCategorySerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_subcategory_detail(request, pk):

    data_object = get_object_or_404(SubCategory, pk=pk)
    serializer = SubCategorySerializer(data_object)
    return Response(serializer.data)


@api_view(['GET'])
def search_subcategory(request, name):
    data_objects = SubCategory.objects.filter(name = name)
    serializer = SubCategorySerializer(data_objects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_subcategory(request):
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return a 201 Created status for successful POST
    return Response(serializer.errors, status=400)  # Return a 400 Bad Request status for invalid data


@api_view(['PUT'])
def put_subcategory(request, pk):
    data_object = get_object_or_404(SubCategory, pk=pk)
    serializer = SubCategorySerializer(data_object, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_subcategory(request, pk):
    data_object = get_object_or_404(SubCategory, pk=pk)
    data_object.delete()
    return Response(status=204)  # Return a 204 No Content status for successful DELETE