from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=50, blank=True, null=True)
    course_code = models.CharField(max_length=10)
    condition = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title', 'author', 'edition', 'condition')

    def __str__(self):
        return f"{self.title} by {self.author} ({self.course_code})"