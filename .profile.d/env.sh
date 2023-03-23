export KINTO_CACHE_URL="${DATABASE_URL//postgres:/postgresql:}"
export KINTO_STORAGE_URL="${DATABASE_URL//postgres:/postgresql:}"
export KINTO_PERMISSION_URL="${DATABASE_URL//postgres:/postgresql:}"
