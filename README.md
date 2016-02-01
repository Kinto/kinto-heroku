# Kinto for Heroku/Scalingo

`kinto-heroku` is an example on how to use [Kinto](http://kinto-storage.org) and [Heroku](https://heroku.com) (or [Scalingo](https://scalingo.com)) together.
Following the installation you should have a Kinto server available for you to use.

## Installation for Heroku

```
$ git clone http://github.com/Kinto/kinto-heroku.git --depth=1 kinto-instance && cd kinto-instance
$ heroku create && git push heroku master
$ heroku open
```

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Installation for Scalingo

```
$ git clone http://github.com/Kinto/kinto-heroku.git --depth=1 kinto-instance && cd kinto-instance
$ scalingo create my-kinto && git push scalingo master
```

[![Deploy to Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy)
