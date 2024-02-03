"""
Базовые методы для форматирования списка источников.
"""

from abc import ABC, abstractmethod
from string import Template

from pydantic import BaseModel


class BaseCitationStyle(ABC):
    """
    Абстрактный базовый класс стиля цитирования.
    """

    def __init__(self, data: BaseModel) -> None:
        self.data = data
        self.formatted = self.substitute()

    @property
    @abstractmethod
    def template(self) -> Template:
        """
        Получение шаблона для форматирования строки.

        :return: Строка, поддерживающая подстановки через $
        """

    @abstractmethod
    def substitute(self) -> str:
        """
        Заполнение шаблона для форматирования строки.

        :return: Строка с подстановленными в шаблон значениями
        """

    def __str__(self) -> str:
        return self.formatted.strip()

    def __repr__(self) -> str:
        return self.formatted.strip()
