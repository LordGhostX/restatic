# ReStatic

A Python script that converts HTML files to Django and Flask framework templates

## Description

When working on web projects with either Django or Flask from an already existing HTML UI design you're going to spend some time formatting your static files into the template with either `{% static 'script.css' %}` for Django or `{{ url_for('static', filename = 'script.js') }}` for flask

ReStatic does all that for you automatically

## Usage
* ReStaticizing an HTML document
```bash
$ python restatic.py <file.html> <flask|django>
$ python restatic.py index.html flask
```
* ReStaticizing all HTML documents in a folder
```bash
$ python restatic.py . <flask|django>
$ python restatic.py . django
```
* ReStaticizing an HTML document specifying output file
```bash
$ python restatic.py <file.html> <flask|django> <output.html>
$ python restatic.py index.html django index2.html
```

The commands above will format your local template file referenced in 'href', 'src', and 'url' in the following way:

Original template file:

```html
  <img class="mySlides" src="res/landreg/1.jpg" style="width:100%">
    <li><a href="register.html">Register</a></li>
```

After script execution:

```html
<img class="mySlides" src=" {% static 'blog/res/landreg/1.jpg' %} " style="width:100%">
   <li><a href=" {% static 'blog/register.html' %} ">Register</a></li>
```

## Author
* LordGhostX

## License
* MIT
