from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from rest_framework.serializers import ModelSerializer

from app.models import *

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


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

    class Meta:
        model = Product
        fields = ('id', 'translations', 'category', 'image1', 'image2', 'image3', 'image4', 'price')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        language_code = self.context.get('language_code')
        if language_code and 'translations' in representation:
            representation['translations'] = {
                language_code: representation['translations'].get(language_code)
            }
        return representation
