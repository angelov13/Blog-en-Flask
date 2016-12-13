from flask import Flask, render_template, url_for
config = {
	'port': 8000,
	'url_admin' : '/admin',
	'admin': 'root',
	'password' : 'hola',
	'menu_active' : True,
	'blog_active' : True
}
site = {
	'name' : 'My Site',
	'url' : 'http://localhost:' + str(config['port']),
	'brand' : 'Otro sitio mas con Flask',
	'menu': ['Home','Articulos','Talleres','Cursos','Soy Socio']
}
articles = [
	{
	'title' : 'mi primer articulo :D',
	'url' : 'mi-primer-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi primer articulo', 'con texto de relleno']
	},
	{
	'title': 'mi segundo articulo :D',
	'url' : 'mi-segundo-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi segundo articulo', 'con texto de relleno']
	},
	{
	'title': 'mi tercer articulo :D',
	'url' : 'mi-tercer-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi tercer articulo', 'con texto de relleno']
	},
	{
	'title': 'mi cuarto articulo :D',
	'url' : 'mi-cuarto-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi cuarto articulo', 'con texto de relleno']
	},
	{
	'title': 'mi cuarto articulo :D',
	'url' : 'mi-cuarto-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi cuarto articulo', 'con texto de relleno']
	},
	{
	'title': 'mi cuarto articulo :D',
	'url' : 'mi-cuarto-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi cuarto articulo', 'con texto de relleno']
	},
	{
	'title': 'mi cuarto articulo :D',
	'url' : 'mi-cuarto-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi cuarto articulo', 'con texto de relleno']
	},
	{
	'title': 'mi cuarto articulo :D',
	'url' : 'mi-cuarto-articulo',
	'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus fuga, modi saepe qui! Natus odio sed magnam aliquid inventore quisquam cupiditate, dolorem sunt id quo harum temporibus ducimus illo tempora!',
	'categories': ['mi cuarto articulo', 'con texto de relleno']
	}
]

app = Flask(__name__)
@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html')

@app.route('/')
def index():
	return render_template('index.html',site = site,config = config,articles = articles)

@app.route('/<name>')
def blog(name = 'none'):
	for article in articles:
		if article['url'] == name:
			return render_template('blog.html', article = article,site = site,config = config)
	return render_template('page_not_found.html')


if __name__ == '__main__':
	app.run(debug = True, port = config['port'])