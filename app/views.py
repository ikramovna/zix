from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.utils.translation import get_language
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.template.loader import render_to_string

from app.serializers import *
from root import settings


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        email_body = (
            f"New Contact Form Submission:\n\n"
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Country: {contact.country}\n"
            f"Message: {contact.message}"
        )
        subject = "New Contact Form Submission"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["muslimazokirjonova2004@gmail.com"]

        self.email_sent = False

        try:
            send_mail(
                subject,
                email_body,
                from_email,
                recipient_list,
                fail_silently=False
            )
            self.email_sent = True
        except Exception as e:
            print(f"Failed to send email: {e}")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Contact saved successfully.",
            "email_sent": getattr(self, 'email_sent', False),
            "data": response.data
        }, status=status.HTTP_201_CREATED)


class AboutListAPIView(ListAPIView):
    serializer_class = AboutTranslatableModelSerializer

    def get_queryset(self):
        language_code = self.kwargs.get('language_prefix', get_language())
        return About.objects.filter(
            translations__language_code=language_code,
            translations__title__isnull=False,
            translations__description__isnull=False
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['language_code'] = self.kwargs.get('language_prefix', get_language())
        return context


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(ListAPIView):
    serializer_class = ProductListTranslatableModelSerializer

    def get_queryset(self):
        language_code = self.kwargs.get('language_prefix', get_language())
        return Product.objects.filter(
            translations__language_code=language_code,
            translations__name__isnull=False,
            translations__description__isnull=False
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['language_code'] = self.kwargs.get('language_prefix', get_language())
        return context


class FaqListAPIView(ListAPIView):
    serializer_class = FaqTranslatableModelSerializer

    def get_queryset(self):
        language_code = self.kwargs.get('language_prefix', get_language())
        return Faq.objects.filter(
            translations__language_code=language_code,
            translations__question__isnull=False,
            translations__answer__isnull=False
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['language_code'] = self.kwargs.get('language_prefix', get_language())
        return context
