from django.test import TestCase
from .models import Factories, Measurers
from faker import Faker


class MyTests(TestCase):
    def setUp(self):
        fake = Faker()

        # Создаем 5 случайных заводов
        for _ in range(5):
            factory = fake.company()
            Factories.objects.create(factory=factory)

        # Создаем 5 случайных замерщиков
        for _ in range(5):
            measurer = fake.name()
            Measurers.objects.create(measurer=measurer)

    def test_factories_count(self):
        factories_count = Factories.objects.count()
        self.assertEqual(factories_count, 5)

    def test_measurers_count(self):
        measurers_count = Measurers.objects.count()
        self.assertEqual(measurers_count, 5)
