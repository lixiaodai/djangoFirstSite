#encoding:utf-8
from django.db import models
from django.utils import timezone
import datetime
from django.views.static import was_modified_since

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    put_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.put_date >= timezone.now() - datetime.timedelta(days=1)
    #这些属性用于定义was_published_recently在list页面显示的某些内容
    was_published_recently.admin_order_field = 'put_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    def __unicode__(self):
        return str(self.id)+","+self.question+","+str(self.put_date)


class Choise(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.poll.__str__()+","+self.choice_text+","+str(self.votes)
    