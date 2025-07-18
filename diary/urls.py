from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexVeiw.as_view(), name='index'),
    path('page/create/', views.PageCreateView.as_view(), name='page_create'),
    path('pages/', views.PageListView.as_view(), name='page_list'),
    path('mypages/', views.MypageListView.as_view(), name='mypage_list'),
    path('page/<uuid:id>/', views.PageDetailView.as_view(), name='page_detail'),
    path('page/<uuid:id>/update/', views.PageUpdateView.as_view(), name='page_update'),
    path('page/<uuid:id>/delete/', views.PageDeleteView.as_view(), name='page_delete'),
]