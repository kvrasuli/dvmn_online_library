from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')

with open('books.json') as books:
    cards = json.load(books)

rendered_page = template.render(
    cards=cards
)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)
