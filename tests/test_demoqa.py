from demoqa.model.pages import practise_form


def test_submitting_form():

    #Заполняем данные формы

    practise_form.open_page()

    practise_form.add_name_and_surname('Alla', 'Alekhina')

    practise_form.add_contacts(
        email='allaale@gmail.com',
        mobile='7931667893',
        address='India'
    )

    practise_form.choose_gender('Female')

    practise_form.click('#dateOfBirthInput')
    practise_form.select_month('April')
    practise_form.select_year('1992')
    practise_form.select_day(10)

    practise_form.add_subject('Arts')

    practise_form.choose_hobby('Sports')

    practise_form.send_file('#uploadPicture', 'resources/pic.jpg')

    practise_form.add_state('Uttar Pradesh')

    practise_form.add_city('Agra')

    practise_form.submit()

   #Проверяем заполнение формы

    practise_form.validation(
            'Alla Alekhina',
            'allaale@gmail.com',
            'Female',
            '7931667893',
            '10 April,1992',
            'Arts',
            'Sports',
            'pic.jpg',
            'India',
            'Uttar Pradesh Agra'
    )