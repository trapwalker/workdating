from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

from workdatingbot.middlewares.acl import ACLMiddleware


def setup(dispatcher: Dispatcher):
    logger.info("Configure middlewares...")
    from workdatingbot.misc import i18n

    dispatcher.middleware.setup(LoggingMiddleware("bot"))
    dispatcher.middleware.setup(ACLMiddleware())
    dispatcher.middleware.setup(i18n)
