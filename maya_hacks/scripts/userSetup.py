"""
This userSetup is used specifically for MayaHacks module and will 
modify the MAYA_SCRIPT_PATH to ensure this module's content is prioritised 
over Maya's internal scripts but NOT the user's own scripts.
"""
import os
import inspect

import maya.cmds


# __file__ isnt available here.
current_directory = os.path.normpath(os.path.dirname(inspect.getfile(inspect.currentframe())))

# Make a reasonable assumption on the maya/scripts directory we want to insert our path after.
expected_leading_dir = os.path.normpath(
    os.path.join(
        maya.cmds.internalVar(userAppDir=True),
        'scripts',
    ),
).lower()


# Insert our current directory after the assumed maya/scripts directory
maya_script_paths = os.environ['MAYA_SCRIPT_PATH'].split(os.pathsep)
for i, path in enumerate(maya_script_paths):
    if os.path.normpath(path).lower() == expected_leading_dir:
        maya_script_paths.insert(i + 1, current_directory)
        break


os.environ['MAYA_SCRIPT_PATH'] = os.pathsep.join(maya_script_paths)

# Cleanup
del current_directory, expected_leading_dir, maya_script_paths, path, i
