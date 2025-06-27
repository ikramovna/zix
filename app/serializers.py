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

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'features', 'category', 'image1', 'image2', 'image3', 'image4')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        images = [
            {"image1": representation.pop('image1')},
            {"image2": representation.pop('image2')},
            {"image3": representation.pop('image3')},
            {"image4": representation.pop('image4')}
        ]
        representation['images'] = [img for img in images if list(img.values())[0] is not None]
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
            "id": representation.get("id"),
            "name": representation.get("name"),
            "description": representation.get("description"),
            "image1": representation.get("image1"),
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
