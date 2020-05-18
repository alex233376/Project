from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = "На каком языке вы впервые научились говорить"
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов
my_survey.show_question()
print(f"Нажмите 'q' для выхода.\n")
while True:
    response = input('Язык: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# Вывод результатов опроса.
print("\nСпасибо всем, кто принял участие в опросе")
my_survey.show_results()
