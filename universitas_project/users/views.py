from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import (
    RegisterSerializer, 
    CustomTokenObtainPairSerializer,
    StudentGradeSerializer,
    InstructorStudentListSerializer,
    UpdateGradeSerializer
)

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            'message': 'User registered successfully',
            'user': {
                'email': user.email,
                'username': user.username,
                'full_name': user.full_name,
                'major': user.major,
                'role': user.role,
            }
        }, status=status.HTTP_201_CREATED)

# Custom Login View dengan JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Student Dashboard - Melihat grade sendiri
class StudentDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Pastikan yang akses adalah student
        if request.user.role != 'student':
            return Response(
                {'error': 'Only students can access this endpoint'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = StudentGradeSerializer(request.user)
        return Response(serializer.data)

# Instructor Dashboard - Melihat semua student dan gradenya
class InstructorDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Pastikan yang akses adalah instructor
        if request.user.role != 'instructor':
            return Response(
                {'error': 'Only instructors can access this endpoint'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Ambil semua student
        students = CustomUser.objects.filter(role='student').order_by('full_name')
        serializer = InstructorStudentListSerializer(students, many=True)
        return Response(serializer.data)

# Instructor Update Grade
class UpdateStudentGradeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, student_id):
        # Pastikan yang akses adalah instructor
        if request.user.role != 'instructor':
            return Response(
                {'error': 'Only instructors can update grades'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Cari student berdasarkan ID
        try:
            student = CustomUser.objects.get(id=student_id, role='student')
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Student not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Update grade
        serializer = UpdateGradeSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Grade updated successfully',
                'student': InstructorStudentListSerializer(student).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Profile (Optional - untuk get current user info)
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'full_name': user.full_name,
            'major': user.major,
            'role': user.role,
            'final_grade': user.final_grade,
        })