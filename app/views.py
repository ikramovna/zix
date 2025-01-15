from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import get_language
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from django.template.loader import render_to_string

from app.serializers import *
from root import settings


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        email_message = render_to_string('contact_form.html', {'contact': contact})
        subject = "New Contact Form Submission"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["muslimazokirjonova2004@gmail.com"]

        try:
            send_mail(subject, email_message, from_email, recipient_list, fail_silently=False,
                      html_message=email_message)
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Contact saved and email sent successfully.",
            "data": response.data
        }, status=status.HTTP_201_CREATED)



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryTranslatableModelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['language_code'] = self.kwargs.get('language_prefix', get_language())
        return context

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductTranslatableModelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['language_code'] = self.kwargs.get('language_prefix', get_language())
        return context
