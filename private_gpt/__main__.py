# start a fastapi server with uvicorn

import re

import uvicorn

from private_gpt.main import app
from private_gpt.settings.settings import settings

# Set log_config=None to do not use the uvicorn logging configuration, and
# use ours instead. For reference, see below:
# https://github.com/tiangolo/fastapi/discussions/7457#discussioncomment-5141108
if re.fullmatch(r"[0-9:.]+", settings().server.bind):
    uvicorn.run(
        app, host=settings().server.bind, port=settings().server.port, log_config=None
    )
else:
    # Unix socket support, as settings().server.bind does not appear to be an IP address
    uvicorn.run(app, uds=settings().server.bind, log_config=None)
