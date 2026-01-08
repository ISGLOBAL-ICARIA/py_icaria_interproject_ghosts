# PYTHON SCRIPT INTERPROJECT GHOST ENTRIES FROM ICARIA PROJECTS

This script is used to routinely check for interproject ghost entry switches between ICARIA REDCap projects.

We define a Ghost entry as a data entry inconsistency caused most probably by a connectivity malfunction between REDCap mobile App and REDCap. It may involve a REDCap mobile app metadata save issue.
Within this definition, interproject ghost cases are those data entry errors where data is switched from a specific project (HF x) to another completely different REDCap project (HF y). As record_ids are intentionally unique, we can easily detect those errors and correct the switch.
