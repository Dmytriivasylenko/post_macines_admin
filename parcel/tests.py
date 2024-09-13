from datetime import timezone, datetime
from django.test import TestCase
from django.contrib.auth.models import User
from post_machine.models import PostMachine, Locker
from parcel.models import Parcel


class ParcelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.post_machine = PostMachine.objects.create(adress='Test Address', city='Test City')

        self.locker = Locker.objects.create(size=1, post_machine_recipient=self.post_machine, status=True)

        self.parcel = Parcel.objects.create(
            recipient=self.user,
            sender='Test Sender',
            size=5,
            post_machine_recipient=self.post_machine,
            locker=self.locker,
            order_datetime=datetime.now(timezone.utc),
            update_datetime=datetime.now(timezone.utc),
            status=False
        )

    def test_parcel_creation(self):
        self.assertEqual(Parcel.objects.count(), 1)
        self.assertEqual(self.parcel.sender, 'Test Sender')
        self.assertEqual(self.parcel.size, 5)
        self.assertEqual(self.parcel.post_machine_recipient, self.post_machine)
        self.assertEqual(self.parcel.locker, self.locker)
        self.assertFalse(self.parcel.status)

    def test_parcel_update_status(self):
        self.parcel.status = True
        self.parcel.save()
        updated_parcel = Parcel.objects.get(id=self.parcel.id)
        self.assertTrue(updated_parcel.status)

    def test_locker_status_update_on_parcel(self):
        self.parcel.status = True
        self.parcel.save()
        updated_locker = Locker.objects.get(id=self.locker.id)
        self.assertFalse(updated_locker.status)
