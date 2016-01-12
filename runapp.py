#!/usr/bin/env python
import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    raise ValueError(os.getenv("DATABASE_URL"))
    os.setenv("KINTO_CACHE_URL", os.getenv("DATABASE_URL"))
    os.setenv("KINTO_STORAGE_URL", os.getenv("DATABASE_URL"))
    os.setenv("KINTO_PERMISSION_URL", os.getenv("DATABASE_URL"))
    app = loadapp('config:kinto.ini', relative_to='.')

    serve(app, host='0.0.0.0', port=port)
