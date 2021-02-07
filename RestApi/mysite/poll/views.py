from django.views import generic

from .models import Question
from .mixins import RequiredLoginMixin

class IndexView(RequiredLoginMixin, generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'


class DeleteView(generic.DeleteView):
    model = Question
    success_url = "/poll/"
