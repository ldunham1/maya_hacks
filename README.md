# maya_hacks
This is for educational/learning purposes only.

Maya example scripts to fix or extend existing behaviour in maya.


> :warning: The userSetup.py modifies the MAYA_SCRIPT_PATH on 
> startup to ensure .mel scripts override Maya's own internal 
> scripts whilst preserving the user's script directories.
>
> This only happens if distributed via Maya modules and 
> the module name is "mayaHacks" (see [Distribution](#distribution)).


### Distribution
It would be possible to distribute as a Maya module. 
1. Create a text file (.mod) with
 `+ mayaHacks 1.0 <PATH>/maya_hacks/maya_hacks` - replacing `<PATH>`.
2. Save the .mod file to a MAYA_MODULE_PATH directory.
 (this would typically be /My Documents/maya/modules).


### Documentation
* [Maya - Distributing Multi-File Modules](https://help.autodesk.com/view/MAYAUL/2019/ENU/?guid=__developer_Maya_SDK_MERGED_Distributing_Maya_Plug_ins_Distributing_Multi_File_Modules_html)
* [Maya - Maya module paths, folders and versions](https://help.autodesk.com/view/MAYAUL/2019/ENU/?guid=__developer_Maya_SDK_MERGED_Distributing_Maya_Plug_ins_Maya_module_paths_folders_and_html)
