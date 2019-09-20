from django.contrib import admin
from .models import MenuModel, HeaderModel,FooterModel, FooterIcon, ArticlesModel, ContactModel, ProfileModel, PostModel, Default_Profile, Date



# Register your models here.

admin.site.register(MenuModel)
admin.site.register(HeaderModel)
admin.site.register(FooterModel)
admin.site.register(FooterIcon)
admin.site.register(ArticlesModel)
admin.site.register(ContactModel)
admin.site.register(ProfileModel)
admin.site.register(PostModel)
admin.site.register(Default_Profile)
admin.site.register(Date)