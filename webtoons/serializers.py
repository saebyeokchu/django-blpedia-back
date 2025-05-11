from rest_framework import serializers
from .models import Review, Webtoon, Company, ThemeTag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'content', 'created_at']

class WebtoonWriteSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    themes = serializers.PrimaryKeyRelatedField(queryset=ThemeTag.objects.all(), many=True, required=False)
    review = ReviewSerializer(required=False)

    class Meta:
        model = Webtoon
        fields = '__all__'

    def create(self, validated_data):
        review_data = validated_data.pop('review', None)
        themes = validated_data.pop('themes', [])
        webtoon = Webtoon.objects.create(**validated_data)
        webtoon.themes.set(themes)

        if review_data:
            Review.objects.create(webtoon=webtoon, **review_data)

        return webtoon
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class ThemeTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeTag
        fields = ['id', 'name', 'slug']


class WebtoonReadSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    themes = ThemeTagSerializer(many=True)

    class Meta:
        model = Webtoon
        fields = '__all__'

class ThemeTagDetailSerializer(serializers.ModelSerializer):
    webtoons = WebtoonReadSerializer(many=True, read_only=True)

    class Meta:
        model = ThemeTag
        fields = ['id', 'name', 'slug', 'webtoons']

