from django.test import TestCase
from .models import Factory, Measurer
from faker import Faker


class MyTests(TestCase):
    def setUp(self):
        fake = Faker()

        # Создаем 5 случайных заводов
        for _ in range(5):
            factory = fake.company()
            Factory.objects.create(factory=factory)

        # Создаем 5 случайных замерщиков
        for _ in range(5):
            measurer = fake.name()
            Measurer.objects.create(measurer=measurer)

    def test_factories_count(self):
        factories_count = Factory.objects.count()
        self.assertEqual(factories_count, 5)

    def test_measurers_count(self):
        measurers_count = Measurer.objects.count()
        self.assertEqual(measurers_count, 5)
