# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

#作者：Andrew_liu
#链接：http://www.jianshu.com/p/dbc4193b4f95
#來源：简书
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
