"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    JournalArticleModel,
)
from formatters.styles.base import BaseCitationStyle
from formatters.styles.gost import (
    GOSTCitationFormatter,
    GOSTBook,
    GOSTInternetResource,
    GOSTCollectionArticle,
    GOSTDissertation,
    GOSTJournalArticle,
)


class TestGOST:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = GOSTBook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство. – 3-е изд. – СПб.: Просвещение, 2020. – 999 с."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = GOSTInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство // Ведомости URL: https://www.vedomosti.ru (дата обращения: 01.01.2021)."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = GOSTCollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Сборник научных трудов. – СПб.: АСТ, 2020. – С. 25-30."
        )

    def test_dissertation(self, dissertation_model_fixture: DissertationModel) -> None:
        """
        Тестирование форматирования диссертаций.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели диссертации
        :return:
        """

        model = GOSTDissertation(dissertation_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. Наука как искусство: дис. ... д-р. / канд. экон. наук.: 01.01.01. - СПб., 2020. - с. 199"
        )

    def test_journal_article(
        self, journal_article_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования диссертаций.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = GOSTJournalArticle(journal_article_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство / Иванов И.М., Петров С.Н. // Образование и наука. -  2020. - N 10. - С. 25-30"
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        dissertation_model_fixture: DissertationModel,
        journal_article_model_fixture: JournalArticleModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :param JournalArticleModel journal_article_model_fixture: Фикстура статьи из журнала
        :return:
        """

        models = [
            book_model_fixture,
            internet_resource_model_fixture,
            articles_collection_model_fixture,
            dissertation_model_fixture,
            journal_article_model_fixture,
        ]
        formatted_models: list[BaseCitationStyle] = [
            GOSTBook(book_model_fixture),
            GOSTInternetResource(internet_resource_model_fixture),
            GOSTCollectionArticle(articles_collection_model_fixture),
            GOSTDissertation(dissertation_model_fixture),
            GOSTJournalArticle(journal_article_model_fixture),
        ]
        result = GOSTCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert str(result[0]) == str(formatted_models[3])
        assert str(result[1]) == str(formatted_models[2])
        assert str(result[2]) == str(formatted_models[0])
        assert str(result[3]) == str(formatted_models[4])
        assert str(result[4]) == str(formatted_models[1])
