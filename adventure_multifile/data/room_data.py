
from room import *

rooms = [
    [ 
        Room("Room description 0, 0", False, False, True, False, (0, 0) ),
        Room("Room description 1, 0", False, True, False, False, (1, 0) ),
        Room("Room description 2, 0", False, True, True, True, (2, 0) ),
        Room("Room description 3, 0", False, True, True, True, (3, 0)),
        Room("Room description 4, 0", False, False, True, True, (4, 0))
    ],
    [ 
        Room("Room description 0, 1", True, False, True, False, (0,1)),
        Room("Room description 1, 1", False, True, True, False, (1,1)),
        Room("Room description 2, 1", True, True, True, True, (2,1)),
        Room("Room description 3, 1", True, False, False, True, (3, 1)),
        Room("Room description 4, 1", True, False, True, False, (4, 1))
    ],
    [ 
        Room("Room description 0, 2", True, False, True, False, (0, 2) ),
        Room("Room description 1, 2", True, False, False, False, (1, 2)),
        Room("You're on a dark path. A mansion looms in the distance to the north.", True, False, True, False, (2, 2) ),
        Room("Room description 3, 2", False, True, False, False, (3, 2) ),
        Room("Room description 4, 2", True, False, True, True, (4, 2) )
    ],
    [ 
        Room("Room description 0, 3",  True, False, True, False, (0, 3) ),
        Room("Room description 1, 3",  False, True, True, False, (1, 3)),
        Room("Room description 2, 3",  True, True, False, True, (2, 3)),
        Room("Room description 3, 3",  False, True, False, True, (3, 3)),
        Room("Room description 4, 3",  True, False, True, False, (3, 4))
    ],
    [ 
        Room("Room description 0, 4",  True, True, False, False, (0, 4)),
        Room("Room description 1, 4",  True, False, False, True, (1, 4)),
        Room("Room description 2, 4",  False, False, False, False, (2, 4)),
        Room("Room description 3, 4",  True, False, False, False, (3, 4)),
        Room("Room description 4, 4",  True, False, False, False, (4, 4))
    ]
]
