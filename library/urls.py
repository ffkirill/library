"""lib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from rest_framework import routers
from django.urls import include, path
import book.views
import bookshelf.views


urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'author', book.views.AuthorViewSet)
router.register(r'book', book.views.BooksViewSet)
router.register(r'bookshelf', bookshelf.views.BookshelfViewSet)
router.register(r'bookshelfitem', bookshelf.views.BookshelfItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    path('api/', include(router.urls)),]

# Append static serve in debug mode:
if settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>', serve_static,
            {'document_root': settings.STATIC_ROOT}),
        path('ui/<path:path>', serve_static,
            {'document_root': settings.BASE_DIR / 'ui' / 'dist'})
]
