# Hello and welcome to the code of the Fri3d Badge!
# You have located the main entrypoint where the code of your badge is launched from.
# Feel free to modify this file or any of the files in the fri3d package.

# In case you mess up, just delete this file using the REPL, and it will be restored to the original state.
# Similarly, if you delete the fri3d or user package it will also get restored to its original state

import logging

# If you want you can increase the log output level here
logging.basicConfig(level=logging.WARNING, force=True)

print("Welcome to the Fri3d Badge REPL mode!\n"
      "\n"
      "By default, the badge will not reboot into MicroPython on reset.\n"
      "Should you want this, you need to confirm the switch to MicroPython was successful.\n"
      "You can do this like this:\n"
      "\n"
      "    from fri3d import boot\n"
      "    boot.persist()\n"
      "\n"
      "Note that now you no longer can get back to the main menu.\n"
      "To switch back you need to do this:\n"
      "\n"
      "    from fri3d import boot\n"
      "    boot.main_menu()\n"
      "\n")
