from django.test import TestCase
from io import StringIO
from django.core.management import call_command

# Create your tests here.


class PopulateDBTest(TestCase):
    """
    Unit test case for custom management command to populate database.

    """

    def test_command_output(self):
        out = StringIO()
        call_command('populate_db', stdout=out)
        self.assertIn('Successfully populated the database', out.getvalue().strip())
