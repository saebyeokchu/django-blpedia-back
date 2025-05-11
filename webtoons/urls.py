from django.urls import path
from . import views

urlpatterns = [
    path('webtoons/create/', views.WebtoonCreateView.as_view(), name='webtoon-make'),
    path('webtoons/', views.WebtoonListView.as_view(), name='webtoon-list'),
    path('webtoons/<slug:slug>/', views.WebtoonDetailView.as_view(), name='webtoon-detail'),
    path('webtoons/<uuid:pk>/delete/', views.WebtoonDeleteView.as_view(), name='webtoon-delete'),
    path('search/', views.WebtoonSearchView.as_view(), name='webtoon-search'),

    path('themes/', views.ThemeTagListView.as_view(), name='theme-list'),
    path('themes/<slug:slug>/', views.ThemeTagDetailView.as_view(), name='theme-detail'),
    path('themes/<slug:slug>/webtoons/', views.WebtoonByThemeView.as_view(), name='webtoon-by-theme'),
    path('status/<str:status>/webtoons/', views.WebtoonByStatusView.as_view(), name='webtoon-by-status'),
    path('companies/', views.CompanyListView.as_view(), name='theme-list'),

    path('testme/', views.WebtoonTestView.as_view(), name='webtoon-testme'),
    path('test-token/', views.TestTokenView.as_view()),
]
