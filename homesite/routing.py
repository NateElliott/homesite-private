from channels.routing import route
from core.consumers import *


channel_routing = [

    route('websocket.connect', ws_connect),

    route('websocket.receive', ws_receive),

    route('websocket.disconnect', ws_disconnect),

]