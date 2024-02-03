"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.models import BookModel, JournalArticleModel
from formatters.styles.base import BaseCitationStyle
from formatters.styles.apa import APABook, APAJournalArticle, APACitationFormatter


class TestAPA:
    """
    Тестирование оформления списка источников согласно APA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. Просвещение"
        )

    def test_journal_article(
        self, journal_article_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования диссертаций.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = APAJournalArticle(journal_article_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. Образование и наука, 10, 25-30"
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        journal_article_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param JournalArticleModel journal_article_model_fixture: Фикстура статьи из журнала
        :return:
        """

        models = [
            book_model_fixture,
            journal_article_model_fixture
        ]
        formatted_models: list[BaseCitationStyle] = [
            APABook(book_model_fixture),
            APAJournalArticle(journal_article_model_fixture)
        ]
        result = APACitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert str(result[0]) == str(formatted_models[1])
        assert str(result[1]) == str(formatted_models[0])

