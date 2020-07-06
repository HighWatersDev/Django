from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_q_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_q_list': latest_q_list}
    return render(request, 'web_api/index.html', context)
# Create your views here.


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'web_api/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
