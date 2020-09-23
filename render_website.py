from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os
from more_itertools import chunked
from pathlib import Path

BOOKS_PER_PAGE = 24


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    with open('books.json') as books:
        book_cards = json.load(books)

    os.makedirs('pages', exist_ok=True)
    chunked_cards = list(chunked(book_cards, BOOKS_PER_PAGE))
    generated_htmls = set()

    for page_number, cards_by_page in enumerate(chunked_cards, start=1):
        paginator = {
            'number_of_pages': len(chunked_cards),
            'current_page': page_number
        }
        rendered_page = template.render(
            cards=cards_by_page,
            paginator=paginator,
        )
        path_to_a_page = os.path.join('pages', f'index{page_number}.html')
        with open(path_to_a_page, 'w', encoding='utf8') as file:
            file.write(rendered_page)
        generated_htmls.add(Path(path_to_a_page))

    all_htmls = set(Path('pages/').glob('*.html'))
    for html in all_htmls.difference(generated_htmls):
        html.unlink()


on_reload()
