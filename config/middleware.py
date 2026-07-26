import logging
import time

logger = logging.getLogger(__name__)


class RequestTimeMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        start = time.time()

        response = self.get_response(request)

        end = time.time()

        total = round(end - start, 3)

        logger.info(f"{request.method} {request.path} took {total} sec")

        return response
