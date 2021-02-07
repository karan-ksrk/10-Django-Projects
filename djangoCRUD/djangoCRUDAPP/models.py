from djongo import models

class Posts(models.Model):
    id = models.ObjectIdField()
    post_title = models.CharField(max_length=255)
    post_description= models.TextField()
    comment = models.JSONField()
    tags = models.JSONField()
    user_details = models.JSONField()
    objects = models.DjongoManager()