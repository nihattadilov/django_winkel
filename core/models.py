from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Setting(BaseModel):
    logo = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    site = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    location = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settings")

    def __str__(self):
        return "Settings"


class Category(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.title


class News(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="news", null=True, blank=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="news"
    )

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return "News"


class Products(BaseModel):
    title = models.CharField(max_length=250)
    content = RichTextField()
    image = models.ImageField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    discount = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = _("Products")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    @property
    def discount_price(self):
        return self.price - (self.price * self.discount / 100)


class Testimonial(BaseModel):
    content = models.TextField()
    image = models.ImageField()
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonial")

    def __str__(self):
        return self.position


class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contact")

    def __str__(self):
        return self.name
