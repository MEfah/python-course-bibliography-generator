"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):

    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class DissertationModel(BaseModel):

    """
    Модель диссертации:
    
    .. code-block::

        DissertationModel(
            author="Иванов И.М.",
            dissertation_title="Наука как искусство",
            degree=д-р. / канд.,
            field="экон.",
            code="01.01.01",
            city="СПб.",
            year=2020,
            pages=199
        )
    """

    author: str
    dissertation_title: str
    degree: str
    field: str
    code: str
    city: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class JournalArticleModel(BaseModel):

    """
    Модель статьи из журнала:

    .. code-block::

        JournalArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            journal_name="Образование и наука",
            year=2020,
            N=10,
            pages="25-30",
        )
    """

    authors: str
    article_name: str
    journal_name: str
    city: str
    year: int = Field(..., gt=0)
    N: int = Field(..., gt=0)
    pages: str
    