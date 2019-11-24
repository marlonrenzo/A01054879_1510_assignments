from unittest import TestCase
from A4.Question_3 import dijkstra
import io
from unittest.mock import patch


class TestDijkstra(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_one(self, mock_output):
        test = ['blue', 'blue', 'blue', 'blue', 'blue', 'white', 'white', 'white', 'white', 'red']
        dijkstra(test)
        actual = mock_output.getvalue()
        expected = "['red', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'blue']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_two(self, mock_output):
        test = ['red', 'blue', 'blue', 'red', 'blue', 'white', 'white', 'white', 'white', 'red']
        dijkstra(test)
        actual = mock_output.getvalue()
        expected = "['red', 'red', 'red', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_single(self, mock_output):
        test = ['blue']
        dijkstra(test)
        actual = mock_output.getvalue()
        expected = "['blue']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_two_colours(self, mock_output):
        test = ['red', 'blue']
        dijkstra(test)
        actual = mock_output.getvalue()
        expected = "['red', 'blue']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_two_colours_red_white(self, mock_output):
        test = ['white', 'red']
        dijkstra(test)
        actual = mock_output.getvalue()
        expected = "['red', 'white']\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_three_colours(self, mock_output):
        test = ['white', 'blue', 'red']
        dijkstra(test)
        actual = mock_output.getvalue()
        expected = "['red', 'white', 'blue']\n"
        self.assertEqual(actual, expected)
