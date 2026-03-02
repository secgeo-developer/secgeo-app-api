"""
Django'da veritabanının kullanılabilir olmasını beklemek için kullanılan komut.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django'da veritabanının yüklenmesini beklemek için kullanılan komut."""

    def handle(self, *args, **options):
        self.stdout.write('Veritabanı bekleniyor...')

        timeout = 60
        start_time = time.time()

        while True:
            try:
                self.check(databases=['default'])
                self.stdout.write(
                    self.style.SUCCESS('Veritabanı mevcut.!')
                    )
                return

            except (Psycopg2OpError, OperationalError):
                if time.time() - start_time > timeout:
                    raise Exception("Veritabanı bağlantı zaman aşımı")

                self.stdout.write('Veritabanı kullanılamıyor, 1 saniye bekleniyor...')
                time.sleep(1)