import logging
from django.http import HttpResponse
logger = logging.getLogger(__file__)


def hello(request,name):
    logger.debug("Hey there it debug!!")
    logger.info("Hey there it info!!")
    logger.warning("Hey there it warning!!")
    logger.error("Hey there it error!!")
    logger.critical("Hey there it critical!!")
    return HttpResponse("Hello "+ name)
