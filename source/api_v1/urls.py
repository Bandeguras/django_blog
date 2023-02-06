from django.urls import path
from .views import ArticleView, ArticleViewPK
app_name = 'api_v1'

urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('article/<int:pk>/', ArticleViewPK.as_view()),
]
