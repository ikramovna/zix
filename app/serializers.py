from django.utils.translation import override
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app.models import *


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


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


class CategoryTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = ('id', 'translations', 'image')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            representation['translations'] = {
                language_code: representation['translations'].get(language_code)
            }
        return representation


class ProductTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'translations', 'category', 'quantity', 'price', 'image1', 'image2', 'image3', 'image4')

    def get_category(self, obj):
        language_code = self.context.get('language_code')
        with override(language_code):
            return obj.category.safe_translation_getter('name', language_code)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            representation['translations'] = {
                language_code: representation['translations'].get(language_code)
            }
        return representation


class ProductListTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = ('id', 'translations', 'name', 'description', 'image1')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            translated_fields = representation['translations'].get(language_code, {})
            representation.pop('translations', None)
            representation.update(translated_fields)
        return {
            "name": representation.get("name"),
            "description": representation.get("description"),
            "image1": representation.get("image1"),
        }
