
from django.contrib import admin
from django.urls import path
from . import views
from customer import views as customerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('contractForm/' , customerViews.contractForm , name='contractForm'),
    path('contractSave/' , customerViews.contractSave , name='contractSave'),
    path('manageContract/' , customerViews.manageContract , name='manageContract'),
    path('deleteContract/<int:id>' , customerViews.deleteContract , name='deleteContract'),
    path('editContract/<int:id>' , customerViews.editContract , name='editContract'),
    path('submitEditContract/<int:id>' , customerViews.submitEditContract , name='submitEditContract'),

]




from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)