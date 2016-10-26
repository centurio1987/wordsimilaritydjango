class SingletoneDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self):
        if self.instance is None:
            self.instance = self.klass()

        return self.instance
