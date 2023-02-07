from django.urls import path, include
from api_v1.views import ArticleView, ArticleViewPK, CommentView, CommentViewPK
app_name = 'api_v1'

ArticleUrl = [
    path('', ArticleView.as_view()),
    path('<int:pk>/', ArticleViewPK.as_view()),
]

CommentUrl = [
    path('', CommentView.as_view()),
    path('<int:pk>/', CommentViewPK.as_view()),
]

urlpatterns = [
    path('article/', include(ArticleUrl)),
    path('comment/', include(CommentUrl)),
]
