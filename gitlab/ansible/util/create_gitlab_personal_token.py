import json
import sys
from datetime import date, timedelta
from typing import List, Sequence

import gitlab
import requests


def get_oauth_token(gitlab_url: str, username: str, password: str) -> str:
    """Get OAuth 2.0 token for GitLab access.

    See https://docs.gitlab.com/ee/api/oauth2.html#resource-owner-password-credentials-flow for details.
    """

    r = requests.post(
        f"{gitlab_url}/oauth/token",
        data={
            "grant_type": "password",
            "username": username,
            "password": password,
        }
    )
    data = json.loads(r.text)
    return data["access_token"]


def create_personal_access_token(
    gitlab_url: str,
    oauth_token: str,
    user_id: int,
    token_name: str,
    scopes: List[str],
) -> str:
    """Create a personal access token."""

    gl = gitlab.Gitlab(url=gitlab_url, oauth_token=oauth_token)

    user = gl.users.get(id=user_id)
    personal_access_token = user.personal_access_tokens.create({
        "name": token_name,
        "expires": str(date.today() + timedelta(days=365 * 10)),
        "scopes": scopes,   #["api", "read_api", "read_user", "read_repository", "write_repository", "sudo"],
    })
    return personal_access_token.token


def main(args: Sequence[str]) -> None:
    if len(args) != 4:
        print("Usage: create_gitlab_personal_token.py gitlab_url username password")
        sys.exit(1)

    gitlab_url, username, password = args[1:4]
    oauth_token = get_oauth_token(gitlab_url, username, password)
    access_token = create_personal_access_token(gitlab_url, oauth_token, 1, "ansible", ["api"])
    print(access_token)


if __name__ == "__main__":
    main(sys.argv)
