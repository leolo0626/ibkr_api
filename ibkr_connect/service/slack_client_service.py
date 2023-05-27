from slack import WebClient
from slack.errors import SlackApiError


class SlackClientService:

    def __init__(self, token):
        self._client = WebClient(token=token)

    def post_message(self, message: str, channel: str):
        try:
            response = self._client.chat_postMessage(
                channel=channel,
                text=message
            )
        except SlackApiError as e:
            print(f"Got an error: {e.response['error']}")

