from django.shortcuts import render
from . import models
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    p = Paginator(models.QUESTIONS, 3)
    page = request.GET.get('page')
    questions = p.get_page(page)
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    context = {'items': questions,
               'tags': tags, 'members': models.MEMBERS}
    return render(request, 'index.html', context)


def hot(request):
    p = Paginator(models.QUESTIONS, 3)
    page = request.GET.get('page')
    questions = p.get_page(page)
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    context = {'items': questions,
               'tags': tags, 'members': models.MEMBERS}
    return render(request, 'hot.html', context)


def login(request):
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    context = {'tags': tags, 'members': models.MEMBERS}
    return render(request, 'login.html', context)


def ask(request):
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    context = {'tags': tags, 'members': models.MEMBERS}
    return render(request, 'ask.html', context)


def signup(request):
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    context = {'tags': tags, 'members': models.MEMBERS}
    return render(request, 'signup.html', context)


def settings(request):
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    context = {'tags': tags, 'members': models.MEMBERS}
    return render(request, 'settings.html', context)


def question(request, question_id):
    if (question_id > len(models.QUESTIONS)):
        return HttpResponseNotFound("Error 404")
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    p = Paginator(models.ANSWERS, 3)
    page = request.GET.get('page')
    answers = p.get_page(page)
    context = {'question': models.QUESTIONS[question_id],
               'items': answers, 'answer_amounts': len(models.ANSWERS),
               'tags': tags, 'members': models.MEMBERS}
    return render(request, 'question.html', context)


def tag(request, tag_name):
    tags = set()
    for question in models.QUESTIONS:
        for tag in question['tags']:
            tags.add(tag)
    for tag in tags:
        if tag == tag_name:
            tagged_questions = list()
            for question in models.QUESTIONS:
                for tag in question['tags']:
                    if tag == tag_name:
                        tagged_questions.append(question)
                        break
            p = Paginator(tagged_questions, 3)
            page = request.GET.get('page')
            questions = p.get_page(page)
            context = {'tag': tag_name, 'items': questions,
                       'members': models.MEMBERS, 'tags': tags}
            return render(request, 'tag.html', context)
    return HttpResponseNotFound("Error 404")
