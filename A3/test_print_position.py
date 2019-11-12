from unittest import TestCase
from A3.SUD import print_position
from unittest.mock import patch
import io


class TestShowPosition(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_position_top_left(self, mock_output):
        print_position({"x": 0, "y": 0})
        actual_value = mock_output.getvalue()
        expected_value = '\n\n[x] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n' \
                             '[ ] [ ] [ ] [ ] [ ] \n\n'
        self.assertEqual(actual_value, expected_value)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_position_top_right(self, mock_output):
        print_position({"x": 4, "y": 0})
        actual_value = mock_output.getvalue()
        expected_value = '\n\n[ ] [ ] [ ] [ ] [x] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n'
        self.assertEqual(actual_value, expected_value)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_position_bottom_right(self, mock_output):
        print_position({"x": 4, "y": 4})
        actual_value = mock_output.getvalue()
        expected_value = '\n\n[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [x] \n\n'
        self.assertEqual(actual_value, expected_value)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_position_bottom_left(self, mock_output):
        print_position({"x": 0, "y": 4})
        actual_value = mock_output.getvalue()
        expected_value = '\n\n[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[ ] [ ] [ ] [ ] [ ] \n\n' \
                         '[x] [ ] [ ] [ ] [ ] \n\n'
        self.assertEqual(actual_value, expected_value)