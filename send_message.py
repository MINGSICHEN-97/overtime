import argparse
import os

from slacker import Slacker

# TODO: the channel name where you want to send a message.
CHANNEL = "#test_overtime"


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="reminder bot")
    parser.add_argument(
        "--slack_api_token", type=str, help="slack api token.", default=None
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = get_arguments()

    slack_api_token = os.getenv("SLACK_API_TOKEN") or args.slack_api_token

    message = "success?"

    slack = Slacker(slack_api_token)
    slack.chat.post_message(CHANNEL, message, as_user=True)
