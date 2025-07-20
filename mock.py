class Mock:
    def __init__(self, return_value=None):
        self.return_value = return_value
        self._calls = []
        self._children = {}

    def assert_not_called(self):
        assert len(self._calls) == 0

    def assert_called_once(self):
        assert len(self._calls) == 1

    def assert_called_once_with(self, *args, **kwargs):
        assert len(list(filter(lambda c: c == (args, kwargs), self._calls))) == 1

    def __call__(self, *args, **kwargs):
        self._calls.append((args, kwargs))
        return self.return_value

    def __getattr__(self, item):
        if item not in self._children:
            self._children[item] = Mock()
        return self._children[item]