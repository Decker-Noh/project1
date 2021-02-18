from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, AnimalSerializer, PostListSerializer
from .models import Photo, Post, Animal
from models_ import detect
import glob
from PIL import Image
import datetime
from pathlib import Path
# detection model
import argparse
from models_.models import *  # set ONNX_EXPORT in models.py
from models_.utils import datasets
from models_.utils import utils
from .models import Post, Animal
from .serializers import PostSerializer, AnimalSerializer
# Create your views here.
from accounts.models import User

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def upload_photo(request):
    image = request.FILES['image']
    # 유저 가져온것 (request.user에서 나온거랑 같음)
    userId = request.data.get('userId')
    user = get_object_or_404(User, id=userId)

    photo = Photo()
    photo.image = image
    photo.save()
    # print(image,'사진 저장 완료')

    image_name = str(image) 
    animal_list = detect.detect_start(image_name)
    animal_list.sort()
    # print('인식 성공')

    animal_dic = {
        'bird': 1, 'cat': 2, 'dog': 3, 'horse': 4, 'sheep': 5, 'cow': 6,
        'elephant': 7, 'bear': 8, 'zebra': 9, 'giraffe': 10,
    }
    # images = glob.glob('output/*.jpg')
    ### 만약 원본 사진이 jpg가 아닐경우 jpg만 가져오기로 하면 인덱스 에러 발생
    images = glob.glob('output/*') # output 폴더에 있는거 다 가져오기
    # print(images)
    query_lst = []
    # print(f'애니멀리스트: {animal_list}')
    ### 만약 애니멀리스트가 빈 리스트라면 객첸인식실패(동물없음!! 이므로 예외처리 해줘야 함)
    if len(animal_list) > 0:
      

        for i in range(len(animal_list)):
            name = animal_list[i][0]
            animal_pk = animal_dic[name]
            animal = get_object_or_404(Animal, pk=animal_pk)

            now = str(datetime.datetime.now())[:10]
            tmp_img = Image.open(images[i+1])
            image_p = str(Path(images[i+1]))[7:]
            static_p = str(Path('media'))
            p = static_p + '\\' + now +'_'+ image_p
            tmp_img.save(p)

            res_image = p[6:]
            post = Post()
            post.image = res_image
            post.animal = animal
            print(animal.info)
            post.info = animal.info
            post.name = animal.name
            print(post.name)

            post.user = user
            post.save()
            query_lst.append(post)
        
    print(query_lst)
    serializer = PostListSerializer(query_lst, many=True)
    return Response(serializer.data)

    
# 동물 종류 보기용
@api_view(['GET'])
def animal_list(request):
    animal = Animal.objects.all()
    serializer = AnimalSerializer(animal, many=True)
    return Response(serializer.data)

# 잡은 동물
@api_view(['GET'])
def post_list(request):
    user = request.GET.get('id')
    post = Post.objects.filter(user=user)
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

# 동물 놓아주기
# @permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete(request, post_pk):
    # if user.is_authenticated:
    post_delete = get_object_or_404(Post, pk=post_pk)
    post_delete.delete()
    return Response("삭제완료")
