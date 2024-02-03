"""
Базовые функции форматирования списка источников
"""

from abc import abstractmethod
from pydantic import BaseModel

from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class BaseCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    @property
    @abstractmethod
    def formatters_map(self) -> dict[str, BaseCitationStyle]:
        """
        Соотношение стилей форматирования и моделей
        """

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            style = self.formatters_map.get(type(model).__name__)
            if style: # Если имеется стиль для модели
                formatted_items.append(style(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        logger.info("Общее форматирование ...")

        return sorted(self.formatted_items, key=lambda item: item.formatted)
