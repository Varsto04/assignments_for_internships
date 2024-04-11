from django.db import models


class MenuElement(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name_menu = models.CharField(max_length=100)

    def __str__(self):
        return self.title
