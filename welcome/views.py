from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext
# Create your views here.
def index(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('welcome/index.html')
    context = RequestContext(request, {
        'latest_questions':latest_questions
    })
    return HttpResponse(template.render(context.flatten()))


def detail(request, question_id):
    question = get_object_or_404(Question , pk=question_id)
    template = loader.get_template('welcome/detail.html')
    context = RequestContext(request, {
        'question':question
    })
    return HttpResponse(template.render(context.flatten()))

def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)

def vote(request,question_id):
    return HttpResponse("Vote on question: %s" % question_id)