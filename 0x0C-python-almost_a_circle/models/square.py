        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)