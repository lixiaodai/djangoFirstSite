#encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Poll, Choise
from django.template import loader
from django.template.context import RequestContext
from django.core.urlresolvers import reverse

# Create your views here.

#定义url的处理逻辑以及返回内容。
def index(request):
    #返回内容
    #返回内容要么是一个HttpResponse对象，要么是一个excption
#    return HttpResponse("Hello, world . You're at the poll index.")
    latest_poll_list = Poll.objects.order_by('-put_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request,{
#        'latest_poll_list':latest_poll_list,
#    })
#    return HttpResponse(template.render(context))
    context = {'latest_poll_list':latest_poll_list}
    return render(request,'polls/index.html',context)

def detail(request,poll_id):
#    try:
#        poll = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
    #get_object_or_404等价于上边的内容，还有一个get_list_or_404的方法
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/detail.html',{'poll':poll})

def results(request,poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})

def vote(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        #request.POST['参数name']用来得到表单提交的参数值，
        #request.POST是一个字典类型，并且其value一般为string类型
        #request.GET得到get类型的提交值
        selected_choice = p.choise_set.get(pk=request.POST['choice'])
    except (KeyError,Choise.DoesNotExist):
        return render(request,'polls/detail.html',{'poll':p,'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #HttpResponseRedirect(),用来进行重定向，其传入的参数值为一个url
        #reverse方法将urls.py中定义的正则和args中定义的参数匹配起来生成一个url，避免硬编码
        return HttpResponseRedirect(reverse('polls:polls-results',args=(p.id,)))
