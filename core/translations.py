from modeltranslation.translator import translator, TranslationOptions
from core.models import (
    Setting,
    Category,
    News,
    Products,
    Testimonial,
    Contact,
)


class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "content", "category")


class ProductsTranslationOptions(TranslationOptions):
    fields = ("title", "content", "category")


class TestimonialTranslationOptions(TranslationOptions):
    fields = ("content", "position")


class ContactTranslationOptions(TranslationOptions):
    fields = "message"


translator.register(News, NewsTranslationOptions)
translator.register(Products, ProductsTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
