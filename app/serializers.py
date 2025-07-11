from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import *
from .models import SubCategory


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'country', 'message')


class TelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'telegram')


class AboutTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=About)

    class Meta:
        model = About
        fields = ('id', 'translations', 'image')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            representation['translations'] = {
                language_code: representation['translations'].get(language_code)
            }
        return representation


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('image') is None:
            representation.pop('image')
        return representation


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    subcategory = serializers.CharField(source='subcategory.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'features', 'category', 'image1', 'image2', 'image3', 'image4', 'subcategory')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        image_fields = ['image1', 'image2', 'image3', 'image4']

        images = []
        for field in image_fields:
            image_url = representation.pop(field, None)
            if image_url:
                if request:
                    images.append(request.build_absolute_uri(image_url))
                else:
                    images.append(image_url)

        representation['images'] = images
        return representation


class ProductListTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'translations', 'name', 'description', 'image1', 'category', 'subcategory')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            translated_fields = representation['translations'].get(language_code, {})
            representation.pop('translations', None)
            representation.update(translated_fields)
        return {
            "id": representation.get("id"),
            "name": representation.get("name"),
            "description": representation.get("description"),
            "image1": representation.get("image1"),
            "category": representation.get("category"),
        }


class FaqTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Faq)

    class Meta:
        model = Faq
        fields = ('id', 'translations')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            representation['translations'] = {
                language_code: representation['translations'].get(language_code)
            }
        return representation


class SubCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubCategory)
    children = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ('id', 'translations', 'parent', 'children')

    def get_children(self, instance):
        children = instance.get_children()
        return SubCategorySerializer(children, many=True, context=self.context).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            translated_fields = representation['translations'].get(language_code, {})
            representation.pop('translations', None)
            representation.update(translated_fields)
        return {
            "id": representation.get("id"),
            "name": representation.get("name"),
            "parent": representation.get("parent"),
            "children": representation.get("children", []),
        }
