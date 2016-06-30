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

## How to upgrade / change configuration ?

First of all use the heroku command to login:

```
$ heroku login

Enter your Heroku credentials.
Email: you@mail.com
Password (typing will be hidden):
```

Then clone this repository and link it to your heroku app (here named `myapp`):

```
$ git clone http://github.com/Kinto/kinto-heroku.git --depth=1 myapp
$ cd myapp
```

(*optional*) Edit your configuration:

```
$ <Edit kinto.ini with your new settings>
$ git commit -am "New setting"
```

> Note: You can also edit the `requirements.txt` to add new dependencies / plugins.

Update the stack:

```
$ heroku git:remote -a myapp
$ git push -u heroku master

remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Using set buildpack heroku/python
remote: -----> Python app detected
remote:      $ pip install -r requirements.txt
remote: 
remote: -----> Running post-compile hook
remote: /app/.heroku/python/lib/python2.7/site-packages/cliquet/storage/postgresql/client.py:87: UserWarning: Reuse existing PostgreSQL connection. Parameters permission_* will be ignored.
remote:   warnings.warn(msg)
remote: /app/.heroku/python/lib/python2.7/site-packages/cliquet/storage/postgresql/client.py:87: UserWarning: Reuse existing PostgreSQL connection. Parameters cache_* will be ignored.
remote:   warnings.warn(msg)
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 42.3M
remote: -----> Launching...
remote:        Released v7
remote:        https://myapp.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
```

Done!
