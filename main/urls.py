from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ProfileView, JournalView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'journal/',JournalView,basename='journal')

urlpatterns =[path('',include(router.urls)),
              path('register/',RegisterView.as_view(),name='register'),
              path('profile/',ProfileView.as_view(),name='profile'),
              path('token/',TokenObtainPairView.as_view(),name='token'),
              path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
]
