#!/usr/bin/env python
import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    database = os.getenv("DATABASE_URL")

    if not database:
        raise ValueError("DATABASE_URL is not correctly defined: %s" %
                         database)

    # Configure Kinto
    os.putenv("KINTO_CACHE_URL", database)
    os.putenv("KINTO_STORAGE_URL", database)
    os.putenv("KINTO_PERMISSION_URL", database)

    app = loadapp('config:kinto.ini', relative_to='.')

    serve(app, host='0.0.0.0', port=port)
