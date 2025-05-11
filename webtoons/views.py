from rest_framework import permissions
from rest_framework import generics
from .models import Company, Review, Webtoon, ThemeTag
from .serializers import CompanySerializer, ReviewSerializer, ThemeTagDetailSerializer, ThemeTagSerializer, WebtoonReadSerializer, WebtoonWriteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]  # or IsAuthenticated
 
class WebtoonTestView(APIView):
    def post(self, request):
        print("✅ REACHED POST")
        return Response({"message": "POST received!"})
    
class WebtoonListView(generics.ListAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonReadSerializer

class WebtoonCreateView(generics.CreateAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonWriteSerializer
    permission_classes = [permissions.IsAdminUser]

    # def create(self, request, *args, **kwargs):
    #     print("📩 Incoming POST:", request.data)

    #     serializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid():
    #         print("❌ Validation errors:", serializer.errors)  # 🧠 Inspect this!
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class WebtoonDeleteView(generics.DestroyAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonReadSerializer
    permission_classes = [permissions.IsAdminUser]

class WebtoonDetailView(generics.RetrieveAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonReadSerializer
    lookup_field = 'slug'

class WebtoonSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        if not query:
            return Response([])

        keywords = query.split()

        qs = Webtoon.objects.all()
        for word in keywords:
            qs = qs.filter(
                Q(title__icontains=word) |
                Q(company__name__icontains=word) |
                Q(themes__name__icontains=word)
            )

        qs = qs.distinct()
        serializer = WebtoonReadSerializer(qs, many=True)
        return Response(serializer.data)


class ThemeTagListView(generics.ListAPIView):
    queryset = ThemeTag.objects.all()
    serializer_class = ThemeTagSerializer

class ThemeTagDetailView(generics.RetrieveAPIView):
    queryset = ThemeTag.objects.all()
    serializer_class = ThemeTagDetailSerializer
    lookup_field = 'slug'

class WebtoonByThemeView(generics.ListAPIView):
    serializer_class = WebtoonReadSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Webtoon.objects.filter(themes__slug=slug)

class WebtoonByStatusView(generics.ListAPIView):
    serializer_class = WebtoonReadSerializer

    def get_queryset(self):
        status = self.kwargs['status']
        return Webtoon.objects.filter(status=status)

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TestTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'detail': 'token valid'})