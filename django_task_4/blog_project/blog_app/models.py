from django.db import models
from django.contrib.auth.models import User
class Comment(models.Model):
    comment_val=models.TextField()
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_val
class Tag(models.Model):
    tag_user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.tag_user)
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    post_comment=models.ManyToManyField(Comment)
    post_tag=models.ManyToManyField(Tag)
    def __str__(self):
        return self.title