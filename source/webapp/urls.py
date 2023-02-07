from django.urls import path, include
from webapp.views import IndexViews, ArticleCreateView, ArticleView, MyRedirectView, ArticleUpdateView, \
    ArticleDeleteView, ArticleCommentCreateView, CommentUpdateView, CommentDeleteView, ArticleLikes, CommentLikes

app_name = 'webapp'

ArticleUrl = [
    path('like/<int:pk>', ArticleLikes.as_view(), name='article_like'),
    path('<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('<int:pk>/comment/add/', ArticleCommentCreateView.as_view(), name='article_comment_add'),
    path('add/', ArticleCreateView.as_view(), name='article_add'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
]


CommentUrl = [
    path('<int:pk>/update', CommentUpdateView.as_view(), name='comment_update'),
    path('<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path('like/<int:pk>', CommentLikes.as_view(), name='comment_like'),
]


urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('redirect_view/', MyRedirectView.as_view()),
    path('article/', include(ArticleUrl)),
    path('comment/', include(CommentUrl)),
]