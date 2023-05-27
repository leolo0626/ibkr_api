import os
from ibkr_connect.config.definitions import ROOT_DIR

from dependency_injector import containers, providers

from ibkr_connect.service.slack_client_service import SlackClientService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    slack_app_client = providers.Factory(
        SlackClientService,
        token=config.slack.token
    )


def init_container():
    c = Container()
    c.config.from_ini(os.path.join(ROOT_DIR, '../config.dev.ini'))
    return c


container = init_container()

