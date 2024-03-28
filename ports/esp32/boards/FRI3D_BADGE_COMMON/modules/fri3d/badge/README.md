# Fri3d Common SDK

This module should only contain common code that can be shared by all badges. All hardware-specific initialization
should occur in the board definition of that badge, using a common interface that is implemented for all the badges and
can be easily imported here.

**Note**: do not go crazy abstracting everything: right now we support only ESP32-badges so no need to abstract away
that fact, we can always refactor and move code into board definitions later on
