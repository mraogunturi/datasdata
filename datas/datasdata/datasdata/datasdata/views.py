import logging
from django.http import HttpResponse
logger = logging.getLogger(__name__)


def hello(request,name):
    logger.debug("Hey there it works!!")
    logger.info("Hey there it works!!")
    logger.warning("Hey there it works!!")
    logger.error("Hey there it works!!")
    logger.critical("Hey there it works!!")
    return HttpResponse("Hello "+ name)
