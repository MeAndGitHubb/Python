from django.shortcuts import render
from .models import Question,Choice
from django.http import HttpResponse
# Create your views here.


def index(request):
    myname = "Van Quan"
    taisan =["Dien thoai", "Laptop", " May Bay", "Nhieu tien"]
    context= {"name": myname, "taisan":taisan}

    return render(request, "polls/index.html", context)

def viewlist(request):

    list_question=Question.objects.all()
    context={"dsquest": list_question}
    return render(request, "polls/question_list.html", context)
def detailView(request,question_id):
    q=Question.objects.get(pk=question_id)
    context_detail={"qs":q}
    return render(request, 'polls/detail_question.html',context_detail )
def vote(request,question_id):
    q=Question.objects.get(pk=question_id)
    try:
        dulieu=request.POST["choice"]
        c= q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Lỗi không có choice")
    c.vote = c.vote+1
    c.save()
    return render(request, "polls/result.html",{"q":q})