from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()

# Create your models here.

class MenuModel(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class HeaderModel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    background_img = models.ImageField(upload_to='header/')
    background_color = models.CharField(max_length=50, null=True, blank=True)
    name = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    text = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name.name

class FooterModel(models.Model):
    text=models.CharField(max_length=400)

    def __str__(self):
        return self.text


class FooterIcon(models.Model):
    icon=models.CharField(max_length=255)
    url=models.URLField()
    section=models.ForeignKey('FooterModel', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.icon}'


class ArticlesModel(models.Model):
    title = models.CharField(max_length=455)
    subtitle = models.CharField(max_length=455, blank=True, null=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='user', null = True, blank=True)
    background_image = models.ImageField(upload_to='user', null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(ProfileModel, self).save(*args, **kwargs)


class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    text = RichTextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    background_image = models.ImageField(upload_to='post/', blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subtitle)
        super(PostModel, self).save(*args, **kwargs)


class Default_Profile(models.Model):
    profile_image = models.ImageField(upload_to='default')
    background_image = models.ImageField(upload_to='default')

    def __str__(self):
        return 'default'


class Date(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    # create_date = models.DateTimeField()
    name =  models.CharField(max_length=255, null=True, blank=True)



