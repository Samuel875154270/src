from handlers import *

route = [
    (r"/es/??(\w*-*\w*-*\w*-*\w*-*\w*)", EsHanlders),
    (r"/my_test/??(\w*-*\w*-*\w*-*\w*-*\w*)", MyTestHandler),
]
