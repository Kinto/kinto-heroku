# Kinto for heroku

`kinto-heroku` is an example on how to use [Kinto](http://kinto-storage.org) and [Heroku](https://heroku.com) together.
Following the installation you should have a Kinto server available for you to use.

## Installation

```
$ git clone http://github.com/Kinto/kinto-heroku.git --depth=1 kinto-instance && cd kinto-instance
$ heroku create && git push heroku master
$ heroku open
```

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Updating your deployment config

First of all use the heroku command to login:

```
$ heroku login
```

Then clone this repository and add you heroku app:

```
$ git clone http://github.com/Kinto/kinto-heroku.git --depth=1 myapp
$ cd myapp
$ <Edit kinto.ini with your new settings>
$ git commit -am "New setting"
$ heroku git:remote -a myapp
$ git push -u heroku master
```

You can also edit the ``requirenments.txt`` to add new dependencies / plugins.
