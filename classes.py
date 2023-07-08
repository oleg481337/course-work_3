class Operation:
    """"""
    def __init__(self, date, description, to, currency, summa, state, from_=None):
        self.date = date
        self.description = description
        self.to = to
        self.currency = currency
        self.summa = summa
        self.state = state
        self.from_ = from_

        self.from_ = self.beautiful_card_number(self.from_)
        self.to = self.beautiful_card_number(self.to)

    def beautiful_data(self):
        """Вывод даты в формате ДД.ММ.ГГГГ"""
        clear_data = self.date[:10]
        result = clear_data[8:] + '.' + clear_data[5:7] + '.' + clear_data[:4]
        return result

    @staticmethod
    def beautiful_card_number(word):
        """Возвращает номер карты или счёта в требуемом формате"""
        text = str(word)
        if sum(c.isdigit() for c in text) == 16:
            result = text[:-12] + ' ' + text[-11:-9] + '** **** ' + text[-4:]
            return result
        elif sum(c.isdigit() for c in text) == 20:
            result = text[:-20] + '**' + text[-4:]
            return result
        else:
            return None

    def __repr__(self):
        return f'{self.date}, {self.description}, {self.to}, {self.currency}' \
               f'{self.summa}, {self.from_}'
