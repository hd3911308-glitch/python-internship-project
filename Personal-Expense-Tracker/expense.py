
from abc import ABC, abstractmethod
from datetime import date


class Expense(ABC):

    def __init__(self, amount, category, description, expense_date=None):
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__expense_date = expense_date or date.today().isoformat()

    @property
    def amount(self):
        return self.__amount

    @property
    def category(self):
        return self.__category

    @property
    def description(self):
        return self.__description

    @property
    def expense_date(self):
        return self.__expense_date

    @abstractmethod
    def get_expense_type(self):
        pass

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "type": self.get_expense_type(),
            "date": self.expense_date
        }


class FoodExpense(Expense):

    def get_expense_type(self):
        return "Food"


class TravelExpense(Expense):

    def get_expense_type(self):
        return "Travel"


class GeneralExpense(Expense):

    def get_expense_type(self):
        return "General"


def create_expense(data):
    expense_type = data.get("type", "General")

    classes = {
        "Food": FoodExpense,
        "Travel": TravelExpense,
        "General": GeneralExpense
    }

    expense_class = classes.get(expense_type, GeneralExpense)

    return expense_class(
        data["amount"],
        data["category"],
        data["description"],
        data.get("date")
    )
