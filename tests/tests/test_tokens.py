from django.test import TestCase
from toconline.services import toconline


class TokenTestCase(TestCase):
    def test_token(self):
        token = toconline.get_token()

        self.assertIsNotNone(token)        
        self.assertEqual(token.token_type, "Bearer")
        self.assertIsNotNone(token.access_token)
        self.assertIsNotNone(token.refresh_token)
        self.assertIsNotNone(token.acquired_at)
        self.assertIsNotNone(token.refreshed_at)
        self.assertIsNotNone(token.expires_in)
        self.assertGreater(token.expires_in, 0)
        self.assertFalse(token.is_expired)
        self.assertFalse(token.is_expiring_soon)

    def test_refresh_token(self):
        token = toconline.get_token()
        old_access_token = token.access_token

        toconline.refresh_token(token)
        new_access_token = token.access_token

        self.assertNotEqual(old_access_token, new_access_token)

    def test_auto_refresh_token(self):
        token = toconline.get_token()
        old_access_token = token.access_token

        token.expires_in = 300  # 5 minutes - should be expiring soon
        token.save()

        self.assertFalse(token.is_expired)
        self.assertTrue(token.is_expiring_soon)

        # should auto-refresh
        new_access_token = toconline.get_token().access_token

        self.assertNotEqual(old_access_token, new_access_token)

    def test_expired_token(self):
        token = toconline.get_token()
        old_access_token = token.access_token

        token.expires_in = 30  # 30 seconds - should be expired
        token.save()

        self.assertTrue(token.is_expired)

        # should get a new token
        new_access_token = toconline.get_token().access_token

        self.assertNotEqual(old_access_token, new_access_token)
