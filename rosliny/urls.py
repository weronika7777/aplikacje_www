from django.urls import path
from .views import RoslinyList
from .views import RynekList
from .views import RynekDetail
from .views import RoslinyDetail
from .views import ApiRoot
from .views import UserList
from .views import UserDetail

urlpatterns =[
    path('rosliny', RoslinyList.as_view(), name=RoslinyList.name),
    path('rynek', RynekList.as_view(), name=RynekList.name),
    path('rynek/<int:pk>', RynekDetail.as_view(), name=RynekDetail.name),
    path('rosliny/<int:pk>', RoslinyDetail.as_view(), name=RoslinyDetail.name),
    path('users', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
]
