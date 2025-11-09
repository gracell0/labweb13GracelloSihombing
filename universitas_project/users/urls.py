from django.urls import path
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    StudentDashboardView,
    InstructorDashboardView,
    UpdateStudentGradeView,
    UserProfileView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User Profile
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    # Student
    path('student/dashboard/', StudentDashboardView.as_view(), name='student-dashboard'),
    
    # Instructor
    path('instructor/dashboard/', InstructorDashboardView.as_view(), name='instructor-dashboard'),
    path('instructor/grade/<int:student_id>/', UpdateStudentGradeView.as_view(), name='update-grade'),
]