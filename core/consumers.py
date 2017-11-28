from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):

    # accept connection
    message.reply_channel.send({'accept':True})
    Group('system').add(message.reply_channel)


@channel_session_user
def ws_disconnect(message):

    pass


@channel_session_user
def ws_receive(message):

    pass
