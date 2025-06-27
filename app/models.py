from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Model
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class Contact(Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        db_table = 'contact'

    def __str__(self):
        return self.name


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(blank=True, null=True),
    )
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        db_table = 'about'

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class Category(Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = 'category'

    def __str__(self):
        return str(self.name) if self.name else ''

class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description=models.TextField(blank=True, null=True),
        features=RichTextField(blank=True, null=True),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='product/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product/', null=True, blank=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = 'product'

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

class Faq(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(max_length=255),
        answer=models.TextField(blank=True, null=True),
    )

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        db_table = 'faq'