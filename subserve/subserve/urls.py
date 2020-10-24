from django.contrib import admin
from django.urls import path, include
import main.urls
import detail.urls
from customer import views
from detail import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('search/', main.views.search, name="search"),
    path('mylocation/', main.views.mylocation, name="mylocation"),
    path('customer/', include('customer.urls')),
    path('store/', include ('detail.urls')),
    path('loadMoreDataAPI', main.views.loadMoreData, name="loadmoredata"),
    path('sidebarDataAPI', main.views.sidebarData, name="sidebardata"),
    path('weekrank', main.views.weekrank, name='weekrank'),
    path('menu/', include('menu.urls')),
    path('manager/', main.views.manager, name='manager'),
    path('checkAvailableAPI', detail.views.checkAvailable, name='checkAvailableAPI')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
