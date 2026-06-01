import unittest
import json
from app import app


class TestWalletRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_app_routes_exist(self):
        """Test that the Flask app has the expected routes defined."""
        rules = [rule.rule for rule in app.url_map.iter_rules()]
        self.assertIn('/generate_wallet', rules)
        self.assertIn('/send_transaction', rules)
        self.assertIn('/check_balance', rules)

    def test_send_transaction_invalid_amount(self):
        """Test that send_transaction rejects invalid amounts."""
        response = self.client.post(
            '/send_transaction',
            data=json.dumps({
                'private_key': 'test_key',
                'recipient_address': 'test_address',
                'amount_satoshis': 0
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_check_balance_missing_wallet(self):
        """Test that check_balance handles missing wallet parameter."""
        response = self.client.get('/check_balance')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()