from .views import index

urlpatterns = [
    path('', index, name='index')
]