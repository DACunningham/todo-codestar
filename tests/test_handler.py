import unittest
from index import handler
import hello


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = handler(None, None)
        # print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello World', result['body'])

    def test_hello_handler(self):

        # Arrange
        event = {
            'pathParameters': {
                'name': 'testname'
            }
        }
        context = {}
        expected = {
            'body': '{"output": "Hello testname"}',
            'headers': {
                'Content-Type': 'application/json'
            },
            'statusCode': 200
        }

        # Act
        result = hello.handler(event, context)

        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
