from django.urls import path
from .views import testRequest,ImageList,ImageUpload,ImageDetail,UpdateImage,DeleteImage
urlpatterns = [
    path('error/',testRequest,name='error'), # Testing Purposes !!
    path('',ImageList.as_view(),name = 'main'),
    path('image-detail/<int:pk>',ImageDetail.as_view(), name='detail'),
    path('image-upload/',ImageUpload.as_view(), name = 'upload'),
    path('edit-task/<int:pk>',UpdateImage.as_view(),name='edit'),
    path('delete-task/<int:pk>',DeleteImage.as_view(),name='delete'),
    ]