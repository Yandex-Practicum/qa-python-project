

class TestTools:

    @staticmethod
    def check_unit_test_result (expected_value, actually_value):
        assert expected_value == actually_value, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value}"'