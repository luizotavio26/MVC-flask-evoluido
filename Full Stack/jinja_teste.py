from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("pagina.html")

html_renderizado = template.render(
    nome="Ana Beatriz",
    lista=["Python", "Flask", "Jinja2"]
)

print(html_renderizado)
