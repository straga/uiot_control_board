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
gen_libs(src_lib=path_platfrorm, src_path="esp32", src="main.py", dst_lib=work_root, dst_path="")


# Platform PC
gen_libs(src_lib=path_core, src_path="_board/esp32", src="platform.py", dst_lib=work_core_path, dst_path="")
gen_libs(src_lib=path_core, src_path="_board/esp32", src="u_os.py", dst_lib=work_core_path, dst_path="")

# core
gen_libs(src_lib=path_core, src_path="asyn", src="asyn.py", dst_lib=work_core_path, dst_path="asyn")
gen_libs(src_lib=path_core, src_path="config", src="config.py", dst_lib=work_core_path, dst_path="config")
gen_libs(src_lib=path_core, src_path="config", src="json_store.py", dst_lib=work_core_path, dst_path="config")
gen_libs(src_lib=path_core, src_path="mbus", src="mbus.py", dst_lib=work_core_path, dst_path="mbus")
gen_libs(src_lib=path_core, src_path="loader", src="loader.py", dst_lib=work_core_path, dst_path="loader")
gen_libs(src_lib=path_core, src_path="thread", src="thread.py", dst_lib=work_core_path, dst_path="thread")



# lib
## logging
gen_libs(src_lib=path_app_lib, src_path="", src="logging.py", dst_lib=work_lib_path, dst_path="")

## uasyncio
gen_libs(src_lib=path_platfrorm, src_path="uasyncio", src="", dst_lib=work_lib_path, dst_path="uasyncio")

## collections
gen_libs(src_lib=path_ulib, src_path="collections.deque/collections", src="deque.py", dst_lib=work_lib_path, dst_path="collections")

## threading
gen_libs(src_lib=path_ulib, src_path="threading", src="threading.py", dst_lib=work_lib_path, dst_path="")


# MOD
gen_libs(src_lib=path_app_mod, src_path="board", src="", dst_lib=work_mod_path, dst_path="board")
gen_libs(src_lib=path_app_mod, src_path="net", src="", dst_lib=work_mod_path, dst_path="net")
gen_libs(src_lib=path_app_mod, src_path="ftp", src="", dst_lib=work_mod_path, dst_path="ftp")
gen_libs(src_lib=path_app_mod, src_path="telnet", src="", dst_lib=work_mod_path, dst_path="telnet")
gen_libs(src_lib=path_app_mod, src_path="mqtt", src="", dst_lib=work_mod_path, dst_path="mqtt")
gen_libs(src_lib=path_app_mod, src_path="http", src="", dst_lib=work_mod_path, dst_path="http")

gen_libs(src_lib=path_app_mod, src_path="ota_updater", src="", dst_lib=work_mod_path, dst_path="ota_updater")

gen_libs(src_lib=path_app_mod, src_path="pin", src="", dst_lib=work_mod_path, dst_path="pin")
gen_libs(src_lib=path_app_mod, src_path="switch", src="", dst_lib=work_mod_path, dst_path="switch")


print("Done")




