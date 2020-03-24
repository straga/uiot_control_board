# Copyright (c) 2020 Viktor Vorobjov

import os, sys

_src = "../../_source" # uIOT Control - Source

path = "{}/tools/gen_tool".format(_src)
gen_tool_path = os.path.abspath("{}/".format(path))
sys.path.append(gen_tool_path)

# print(gen_tool_path)
from gen_tool import Gen

# print("Gen libs")
path_ulib       = "{}/platform/micropython-lib".format(_src)
path_platfrorm  = "{}/platform".format(_src)
path_core       = "{}/core".format(_src)
path_app_app    = "{}/app".format(_src)
path_app_mod    = "{}/mod".format(_src)
path_app_lib    = "{}/lib".format(_src)
path_root        = "{}".format(_src)

work_root = "."

work_app_path   = "./app"
work_core_path  = "./core"
work_lib_path   = "./lib"
work_mod_path   = "./mod"

print("-- Gen Path")
print("-- work_path: {}".format(work_root))
print("-- Start Gen Lib")


SYMLINK = False

gen_libs = Gen(SYMLINK).gen_libs

# main
# gen_libs(src_lib=path_platfrorm, src_path="esp32", src="main.py", dst_lib=work_root, dst_path="")
#
# src_schema = "_schema.json"

# MOD SCHEMA
# gen_libs(src_lib=path_app_mod, src_path="board", src=src_schema, dst_lib=work_mod_path, dst_path="board")
# gen_libs(src_lib=path_app_mod, src_path="net", src=src_schema, dst_lib=work_mod_path, dst_path="net")
# gen_libs(src_lib=path_app_mod, src_path="ftp", src=src_schema, dst_lib=work_mod_path, dst_path="ftp")
# gen_libs(src_lib=path_app_mod, src_path="telnet", src=src_schema, dst_lib=work_mod_path, dst_path="telnet")
# gen_libs(src_lib=path_app_mod, src_path="mqtt", src=src_schema, dst_lib=work_mod_path, dst_path="mqtt")
# gen_libs(src_lib=path_app_mod, src_path="http", src=src_schema, dst_lib=work_mod_path, dst_path="http")
#
# gen_libs(src_lib=path_app_mod, src_path="pin", src=src_schema, dst_lib=work_mod_path, dst_path="pin")
# gen_libs(src_lib=path_app_mod, src_path="switch", src=src_schema, dst_lib=work_mod_path, dst_path="switch")
# gen_libs(src_lib=path_app_mod, src_path="binary_sensor", src=src_schema, dst_lib=work_mod_path, dst_path="binary_sensor")


# Modules
gen_libs(src_lib=path_app_mod, src_path="ctrl_kitchen_light", src="", dst_lib=work_mod_path, dst_path="ctrl_kitchen_light")



print("Done")




