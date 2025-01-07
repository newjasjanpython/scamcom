from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.


UserModel = get_user_model()


class BaseModel(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CodeSet(BaseModel):
    created_users = models.ManyToManyField(UserModel, related_name='tasks_created_by_u')
    title = models.CharField(max_length=256)
    description = models.TextField()


class GithubManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(file_type='github')


class FileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(file_type='file')


class TextManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(file_type='text')


class File(BaseModel):
    codeset = models.ForeignKey(to=CodeSet, on_delete=models.CASCADE, related_name='files_attached_to_c')
    file_type = models.CharField(max_length=256, choices=(
        ('github', 'Github'),
        ('file', 'File'),
        ('text', 'Text')
    ))

    github_url = models.CharField(max_length=1024, null=True, blank=True)
    file = models.FileField(upload_to='files', null=True, blank=True)
    text = models.TextField(max_length=1024 * 64, null=True, blank=True)

    objects = models.Manager()
    githubs = GithubManager()
    files = FileManager()
    texts = TextManager()

