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

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
    )
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = 'category'

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

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
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = 'product'

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)


