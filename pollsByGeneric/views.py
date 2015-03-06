#encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name='pollsByGeneric/index.html'
    context_object_name='latest_poll_list'
    
    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name='pollsByGeneric/detail.html'
    
class ResultsView(generic.DeleteView):
    model = Poll
    template_name='pollsByGeneric/results.html'
    
def vote(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        #request.POST['参数name']用来得到表单提交的参数值，
        #request.POST是一个字典类型，并且其value一般为string类型
        #request.GET得到get类型的提交值
        selected_choice = p.choise_set.get(pk=request.POST['choice'])
    except (KeyError,Choise.DoesNotExist):
        return render(request,'pollsByGeneric/detail.html',{'poll':p,'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #HttpResponseRedirect(),用来进行重定向，其传入的参数值为一个url
        #reverse方法将urls.py中定义的正则和args中定义的参数匹配起来生成一个url，避免硬编码
        return HttpResponseRedirect(reverse('polls:polls-results',args=(p.id,)))