import json
from twisted.python import log

def parseUpdateResponse(responsetext):
    """Attempt to parse the response from twitter as JSON"""
    if responsetext is None:
        return None
    ret = None
    try:
        ret = json.loads(responsetext)["id"]
    except:
        log.msg("Failed to parseUpdateResponse: "+ repr(responsetext))
    return ret