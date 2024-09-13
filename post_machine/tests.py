from django.test import TestCase
# Create your tests here.

from .models import PostMachine, Locker
class PostMachineModelTest(TestCase):

    def setUp(self):
        self.post_machine = PostMachine.objects.create(
            adress="123 Main St",
            city="Kyiv"
        )

    def test_post_machine_creation(self):
        self.assertEqual(self.post_machine.adress, "123 Main St")
        self.assertEqual(self.post_machine.city, "Kyiv")
        self.assertIsInstance(self.post_machine, PostMachine)

    def test_post_machine_str(self):
        self.assertEqual(str(self.post_machine), "PostMachine object (1)")

class LockerModelTest(TestCase):

    def setUp(self):
        self.post_machine = PostMachine.objects.create(
            adress="123 Main St",
            city="Kyiv"
        )
        self.locker = Locker.objects.create(
            size=5,
            post_machine_recipient_id=self.post_machine,
            status=False
        )

    def test_locker_creation(self):
        self.assertEqual(self.locker.size, 5)
        self.assertEqual(self.locker.post_machine_recipient_id, self.post_machine)
        self.assertFalse(self.locker.status)
        self.assertIsInstance(self.locker, Locker)

    def test_locker_str(self):
        expected_str = f"size: 5 - PM {self.post_machine.id} - status: False"
        self.assertEqual(str(self.locker), expected_str)
