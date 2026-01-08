#!/usr/bin/env python
""" Python script to manage pontential ghost switches between REDCap projects
from the ICARIA Clinical Trial"""

import ghosts

__author__ = "Andreu Bofill"
__copyright__ = "Copyright 2024, ISGlobal Maternal, Child and Reproductive Health"
__credits__ = ["Andreu Bofill"]
__license__ = "MIT"
__version__ = "0.0.1"
__date__ = "20240206"
__maintainer__ = "Andreu Bofill"
__email__ = "andreu.bofill@isglobal.org"
__status__ = "Finished"


if __name__ == '__main__':
    """ To find Ghost entry records (interproject Ghosts)"""
    ghosts.define_ghost_records()
