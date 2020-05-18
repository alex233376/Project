import unittest
from survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        question = "На каком языке вы впервые научились говорить "
        my_survey = AnonymousSurvey(question)  # создается экземпляр
        my_survey.store_response('English')  # сохраняется ответ с
        # использованием метода store_response()
        self.assertIn('English', my_survey.responses)  # проверяет, что значение
        # English присутствует в списке my_survey.responses

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        question = "На каком языке вы впервые научились говорить "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()
