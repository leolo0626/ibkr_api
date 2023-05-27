from ibkr_connect.container import container

slack_client_service = container.slack_app_client()

slack_client_service.post_message("Paper Trade - First Message",
                                  "#ibkr-paper-trade-notification-channel")
