from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Comment, Article


class CommentLikes(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        result = 0
        if request.user not in comment.like.all():
            comment.like.add(request.user)
            result = 1
        else:
            comment.like.remove(request.user)

        like = comment.get_like_count()

        data = {
            'like': like,
            'pk': comment.pk,
            'result': result,
        }
        response = JsonResponse(data)
        return response


class ArticleCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comment/update.html'
    form_class = CommentForm
    context_object_name = 'comment'
    # permission_required = 'webapp.change_comment'

    def has_permission(self):
        return self.request.user.has_perm('webapp.change_comment') or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})

class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_comment') or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk })


