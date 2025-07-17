import unittest

from mock import Mock


class MockTestCase(unittest.TestCase):
    def test_an_uncalled_mock_will_assert_not_called(self):
        mock = Mock()
        mock.assert_not_called()

    def test_a_called_mock_will_not_assert_not_called(self):
        mock = Mock()
        mock()
        with self.assertRaises(AssertionError):
            mock.assert_not_called()

    def test_a_once_called_mock_will_assert_called_once(self):
        mock = Mock()
        mock()
        mock.assert_called_once()

    def test_an_uncalled_mock_will_not_assert_called_once(self):
        mock = Mock()
        with self.assertRaises(AssertionError):
            mock.assert_called_once()

    def test_a_twice_called_mock_will_not_assert_called_once(self):
        mock = Mock()
        mock()
        mock()
        with self.assertRaises(AssertionError):
            mock.assert_called_once()

    def test_a_mock_called_with_arg_will_assert_called_with_arg(self):
        arg = object()
        mock = Mock()
        mock(arg)
        mock.assert_called_once_with(arg)

    def test_a_mock_called_with_different_arg_will_not_assert_called_with_arg(self):
        arg = object()
        different_arg = object()
        mock = Mock()
        mock(different_arg)
        with self.assertRaises(AssertionError):
            mock.assert_called_once_with(arg)

    def test_a_mock_called_with_kwarg_will_assert_called_with_kwarg(self):
        arg = object()
        mock = Mock()
        mock(key=arg)
        mock.assert_called_once_with(key=arg)

    def test_a_mock_called_with_different_kwarg_will_not_assert_called_with_kwarg(self):
        arg = object()
        different_arg = object()
        mock = Mock()
        mock(key=different_arg)
        with self.assertRaises(AssertionError):
            mock.assert_called_once_with(arg)

    def test_a_mock_called_with_differently_ordered_kwargs_will_assert_called_with_kwarg(self):
        arg1 = object()
        arg2 = object()
        mock = Mock()
        mock(key2=arg2, key1=arg1)
        mock.assert_called_once_with(key1=arg1, key2=arg2)

    def test_a_mock_object_will_create_new_mocks_to_support_method_calls(self):
        mock = Mock()
        mock.some_method.assert_not_called()
        mock.some_method()
        mock.some_method.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
