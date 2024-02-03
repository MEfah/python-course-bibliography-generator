"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from formatters.base import BaseCitationFormatter

from formatters.models import (
    BookModel,
    JournalArticleModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class APABook(BaseCitationStyle):
    """
    Форматирование для книг в соответствии с APA.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $title. $publishing_house")

    def substitute(self) -> str:

        logger.info(
            'Форматирование книги "%s" в соответствии с APA ...', self.data.title
        )

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
        )


class APAJournalArticle(BaseCitationStyle):
    """
    Форматирование для статьи из журнала в соответствии с APA.
    """

    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $article_title. $journal_name, $N, $pages")

    def substitute(self) -> str:

        logger.info(
            'Форматирование статьи "%s" из журнала "%s" в соответствии с APA ...',
            self.data.article_title,
            self.data.journal_name,
        )

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            journal_name=self.data.journal_name,
            year=self.data.year,
            N=self.data.N,
            pages=self.data.pages,
        )


class APACitationFormatter(BaseCitationFormatter):
    """
    Класс для итогового форматирования списка источников в соответствии с APA.
    """

    @property
    def formatters_map(self) -> dict[str, BaseCitationStyle]:
        return {
            BookModel.__name__: APABook,
            JournalArticleModel.__name__: APAJournalArticle,
        }
