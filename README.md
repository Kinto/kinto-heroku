# Pelican for heroku

`pelican-heroku` is an example on how to use [Pelican](http://getpelican.com) and [Heroku](https://heroku.com) together.
Following the installation you should have Pelican precompiling when pushed to Heroku, then served statically.

## Installation

```
$ git clone http://github.com/getpelican/pelican-heroku.git --depth=1 mysite && cd mysite
$ heroku create && git push heroku master
$ heroku open
```

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Configuration

You can customize your installation by modifying the file directly, or via theses environment variables:

 * DISQUS_SITENAME
 * GOOGLE_ANALYTICS
 * PELICAN_AUTHOR
 * PELICAN_SITENAME
 * DEFAULT_PAGINATION

