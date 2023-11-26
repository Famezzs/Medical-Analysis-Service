class TypeValidator:
    @staticmethod
    def enforce_type(actual_type, expected_type):
        if not isinstance(actual_type, expected_type):
            raise TypeError('Invalid type passed')