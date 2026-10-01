import logging

from core.config import settings

logger = logging.getLogger("app")

handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctimes)s | %(levelname)s | %(names)s | %(message)s")


handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(handler)

logger.setLevel(logging.INFO if settings.FASTAPI_ENV == "production" else logging.DEBUG)
