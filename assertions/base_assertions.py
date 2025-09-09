class BaseAssertions:

    @staticmethod
    def assert_data_in_data(act, exp):
        assert act in exp, (f'Объект {exp} не содержит в себе:\n'
                            f'{act}')

    @staticmethod
    def assert_data_equal_data(act, exp):
        assert act == exp, (f'Данные не идентичны!\n'
                            f'ОР: {exp}\n'
                            f'ФР: {act}')
