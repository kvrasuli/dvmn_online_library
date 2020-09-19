from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
# from more_itertools import chunked


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    with open('books.json') as books:
        cards = json.load(books)

    # chunked_cards = list(chunked(cards, 2))
    rendered_page = template.render(
        cards=cards
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)
