# ReStatic

Converts HTML files to Django and Flask framework templates

When working on web projects with either Django or Flask from an already existing HTML UI design you're going to spend some time formatting your static files into the template with either `{% static 'script.css' %}` or `{{ url_for('static', filename = 'script.js') }}`

ReStatic does all that for you automatically

## Usage
* ReStaticing an HTML document
```bash
$ python restatic.py <file.html> <flask|django>
$ python restatic.py index.html flask
```
* ReStaticing all HTML documents in a folder
```bash
$ python restatic.py . <flask|django>
$ python restatic.py . django
```
* ReStaticing an HTML document specifying output file
```bash
$ python restatic.py <file.html> <flask|django> <output.html>
$ python restatic.py index.html django index2.html
```

## Author
* LordGhostX

## License
* MIT
