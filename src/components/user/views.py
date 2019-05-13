
from . import user

@user.route('/<userid>')
def addInfo(userid):
    return (userid)