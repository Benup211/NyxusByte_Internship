from django.db import models
from django.contrib.auth.models import User
class Comment(models.Model):
    comment_val=models.TextField()
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_val
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_author")
    pub_date=models.DateTimeField(auto_now=True)
    post_comment=models.ManyToManyField(Comment,blank=True)
    post_tag = models.ManyToManyField(User, blank=True, related_name='tagged_posts')
    def __str__(self):
        return self.title