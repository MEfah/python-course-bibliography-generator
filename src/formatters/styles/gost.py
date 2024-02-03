"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    JournalArticleModel,
)
from formatters.styles.base import BaseCitationStyle
from formatters.base import BaseCitationFormatter
from logger import get_logger


logger = get_logger(__name__)


class GOSTBook(BaseCitationStyle):
    """
    Форматирование для книг в соответствии с ГОСТ.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title. – $edition$city: $publishing_house, $year. – $pages с."
        )

    def substitute(self) -> str:

        logger.info(
            'Форматирование книги "%s" в соответствии с ГОСТ ...', self.data.title
        )

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class GOSTInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов в соответствии с ГОСТ.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article // $website URL: $link (дата обращения: $access_date)."
        )

    def substitute(self) -> str:

        logger.info(
            'Форматирование интернет-ресурса "%s" в соответствии с ГОСТ ...',
            self.data.article,
        )

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class GOSTCollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника в соответствии с ГОСТ.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $collection_title. – $city: $publishing_house, $year. – С. $pages."
        )

    def substitute(self) -> str:

        logger.info(
            'Форматирование сборника статей "%s" в соответствии с ГОСТ ...',
            self.data.article_title,
        )

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTDissertation(BaseCitationStyle):
    """
    Форматирование для диссертации в соответствии с ГОСТ.
    """

    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author $dissertation_title: дис. ... $degree $field наук.: $code. - $city, $year. - с. $pages"
        )

    def substitute(self) -> str:

        logger.info(
            'Форматирование диссертации "%s" в соответствии с ГОСТ ...',
            self.data.dissertation_title,
        )

        return self.template.substitute(
            author=self.data.author,
            dissertation_title=self.data.dissertation_title,
            degree=self.data.degree,
            field=self.data.field,
            code=self.data.code,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTJournalArticle(BaseCitationStyle):
    """
    Форматирование для статьи из журнала в соответствии с ГОСТ.
    """

    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$article_title / $authors // $journal_name. -  $year. - N $N. - С. $pages"
        )

    def substitute(self) -> str:

        logger.info(
            'Форматирование статьи "%s" из журнала "%s" в соответствии с ГОСТ ...',
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


class GOSTCitationFormatter(BaseCitationFormatter):
    """
    Итоговый класс для форматирования списков в соответствии с ГОСТ.
    """

    @property
    def formatters_map(self) -> dict[str, BaseCitationStyle]:
        return {
            BookModel.__name__: GOSTBook,
            InternetResourceModel.__name__: GOSTInternetResource,
            ArticlesCollectionModel.__name__: GOSTCollectionArticle,
            DissertationModel.__name__: GOSTDissertation,
            JournalArticleModel.__name__: GOSTJournalArticle,
        }
