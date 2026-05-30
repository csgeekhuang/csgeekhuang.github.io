import sys, os
import json

from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import markdown as md_lib
from markupsafe import Markup

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_RELATIVE_URLS = False
FREEZER_DESTINATION = 'build'
FREEZER_STATIC_IGNORE = ['*.git*']
FREEZER_BASE_URL = None
FREEZER_IGNORE_MIMETYPE_WARNINGS = True

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
_md = md_lib.Markdown(extensions=['fenced_code'], output_format='html5')

@app.template_filter('markdown')
def markdown_filter(text):
    _md.reset()
    return Markup(_md.convert(text))

with app.app_context():
    posts = [page for page in list(pages) if not page.path.startswith('r/')]
    reviews = [page for page in list(pages) if page.path.startswith('r/')]

    review_tags = {}
    for p in list(reviews):
        for tag in p.meta.get('tags', []):
            review_tags[tag] = review_tags.get(tag, 0) + 1
    review_tags = dict(sorted(review_tags.items(), key=lambda item: -1 * item[1])[:10])

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/publications/')
def publications():
    with open('data/publications.json') as f:
        return render_template('publications.html', pubs=json.load(f))

@app.route('/news/')
def news():
    with open('data/news.json') as f:
        return render_template('news.html', news=json.load(f))

@app.route('/blogs/')
def blogs():
    return render_template('blogs.html', pages=posts)

@app.route('/resources/')
def resources():
    with open('data/repos.json') as f:
        repos = json.load(f)
        repos = sorted(repos, key=lambda x: x['name'].lower())
        return render_template('resources.html', repos=repos)

@app.route('/readings/')
def papers():
    return render_template('papers.html', pages=reviews, tags=review_tags, tag="all")

@app.route('/papers/<string:tag>/')
def paper_tag(tag):
    return render_template('papers.html', pages=reviews, tags=review_tags, tag=tag)

@app.route('/<path:path>/')
def page(path):
    return render_template('page.html', page=pages.get_or_404(path))

@app.route('/review/<path:path>/')
def review(path):
    return render_template('review.html', review=pages.get_or_404(path))

@app.errorhandler(404)
def page_not_found(path):
    return render_template('404.html'), 404

@freezer.register_generator
def page():
    for p in pages:
        if not p.path.startswith('r/'):
            yield {'path': p.path}

@freezer.register_generator
def review():
    for p in pages:
        if p.path.startswith('r/'):
            yield {'path': p.path}

@freezer.register_generator
def static():
    for dirpath, dirnames, filenames in os.walk('static'):
        for filename in filenames:
            rel_dir = os.path.relpath(dirpath, 'static')
            rel_file = os.path.join(rel_dir, filename) if rel_dir != '.' else filename
            yield {'filename': rel_file}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5001))
        app.run(host='0.0.0.0', port=port)
