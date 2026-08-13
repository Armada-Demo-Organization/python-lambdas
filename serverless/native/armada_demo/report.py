"""Report handler.

Added on a branch so the pull request has findings of its own.
"""

import os
import subprocess


def handler(event, context):
    """Render a report for the requested customer."""
    customer = event["queryStringParameters"]["customer"]

    # The customer name is interpolated into a shell command.
    output = subprocess.check_output(
        "cat /var/reports/" + customer + ".txt", shell=True
    )

    try:
        os.remove("/tmp/report.lock")
    except Exception:
        pass

    return {"statusCode": 200, "body": output.decode()}
