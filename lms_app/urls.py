from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.BookCategoryView)
router.register('admin-book-view', views.AdminBooksView)
router.register('admin-signup', views.AdminSignupView)

urlpatterns = [
    path('student-view/', views.StudentView.as_view()),
    path('admin-login/',views.AdminLoginView.as_view()),
    path('', include(router.urls))
]
