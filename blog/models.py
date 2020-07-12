from django.db import models

from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class BlogAuthor(models.Model):
	"""
	部落主
	"""
	# OneToOneField--一對一,只有一個po文者
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
	
	# class Meta定義model;ordering:按訂單升序排列
	class Meta:
		ordering = ["user", "bio"]
	
	def get_absolute_url(self):
	    """
	    用url 登入
	    """
	    
	    # reverse: 傳回views內的blog-by-author
	    return reverse('blog-by-author', args=[str(self.id)])

	def __str__(self):
	    """
	    String for representing the Model object
	    """	    
	    return self.user.username


class Blog(models.Model):
	"""
	PO文
	"""
	name = models.CharField(max_length=200)
	# ForeignKey:多對一,po者有很多po文;SET_NULL:如果po文者被刪除，就會顯示anonymous or deleted
	author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
	description = models.TextField(max_length=2000, help_text="Enter your blog text here.")
	post_date = models.DateField(default=date.today)
	
	# 按訂單降序排列
	class Meta:
		ordering = ["-post_date"]
		
	def get_absolute_url(self):
		return reverse('blog-detail', args=[str(self.id)])

	
	def __str__(self):
		return self.name

class BlogComment(models.Model):
	description = models.TextField(max_length=1000, help_text="Enter comment about blog here..")
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	post_date = models.DateTimeField(auto_now_add=True)
	# CASADE:post_date = models.DateField(default=date.today)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	
	class Meta:
		ordering = ["post_date"]
	
	def __str__(self):
		len_title=75
		if len(self.description) > len_title:
			titlestring=self.description[:len_title] + '...'
		else:
			titlestring=self.description
		return titlestring



		
	
	
