from livereload import Server
from render_website import on_reload


def rebuild():
    on_reload()
    print('Site rebuilded')


rebuild()

server = Server()
server.watch('template.html', rebuild)
server.serve(root='.')
