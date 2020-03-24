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
gen_libs(src_lib=path_ulib, src_path="uasyncio/uasyncio", src="__init__.py", dst_lib=work_lib_path, dst_path="uasyncio")
gen_libs(src_lib=path_ulib, src_path="uasyncio.core/uasyncio", src="core.py", dst_lib=work_lib_path, dst_path="uasyncio")
gen_libs(src_lib=path_ulib, src_path="uasyncio.queues/uasyncio", src="queues.py", dst_lib=work_lib_path, dst_path="uasyncio")

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
gen_libs(src_lib=path_app_mod, src_path="binary_sensor", src="", dst_lib=work_mod_path, dst_path="binary_sensor")
gen_libs(src_lib=path_app_mod, src_path="control_led", src="", dst_lib=work_mod_path, dst_path="control_led")
gen_libs(src_lib=path_app_mod, src_path="control_touch", src="", dst_lib=work_mod_path, dst_path="control_touch")


gen_libs(src_lib=path_app_mod, src_path="message", src="", dst_lib=work_mod_path, dst_path="message")









# libs = (
# # main.py
#     {"src_lib": path_platfrorm, "src_path": "pc", "src": "main_test.py", "dst_lib": "./", "dst_path": ""},
#
# #www test
#     {"src_lib": path_src, "src_path": "www_temp", "src": "", "dst_lib": "./www", "dst_path": "", "file": False},
#
# )

# # LIB ESP32
#
#     # uasyncio
#     {
#         "src_lib": path_ulib,
#         "src_path": "uasyncio/uasyncio",
#         "src": "__init__.py",
#         "dst_lib": work_lib_path,
#         "dst_path": "uasyncio"
#     },
#     {
#         "src_lib": path_ulib,
#         "src_path": "uasyncio.core/uasyncio",
#         "src": "core.py",
#         "dst_lib": work_lib_path,
#         "dst_path": "uasyncio"
#     },
#     {
#         "src_lib": path_ulib,
#         "src_path": "uasyncio.queues/uasyncio",
#         "src": "queues.py",
#         "dst_lib": work_lib_path,
#         "dst_path": "uasyncio"
#     },
#
#
#     # collections
#     {
#         "src_lib": path_ulib,
#         "src_path": "collections.deque/collections",
#         "src": "deque.py",
#         "dst_lib": work_lib_path,
#         "dst_path": "collections"
#     },
#
#
#
#     # logging
#     {
#         "src_lib": path_ulib,
#         "src_path": "logging/simple",
#         "src": "logging.py",
#         "dst_lib": work_lib_path,
#         "dst_path": ""
#      },
#
#     # threading
#     {
#         "src_lib": path_ulib,
#         "src_path": "threading",
#         "src": "threading.py",
#         "dst_lib": work_lib_path,
#         "dst_path": ""
#     },
#
#
#
# # CORE
#
#     # platform
#     {
#         "src_lib": path_core,
#         "src_path": "_board/esp32",
#         "src": "u_os.py",
#         "dst_lib": work_core_path,
#         "dst_path": ""
#     },
#
#     {
#         "src_lib": path_core,
#         "src_path": "_board/esp32",
#         "src": "platform.py",
#         "dst_lib": work_core_path,
#         "dst_path": ""
#     },
#
#     # loader
#     {
#         "src_lib": path_core,
#         "src_path": "",
#         "src": "loader.py",
#         "dst_lib": work_core_path,
#         "dst_path": ""
#     },
#
#     # asyn
#     {
#         "src_lib": path_core,
#         "src_path": "asyn",
#         "src": "asyn.py",
#         "dst_lib": work_core_path,
#         "dst_path": "asyn"
#      },
#
#     # db
#     {
#         "src_lib": path_core,
#         "src_path": "db",
#         "src": "filedb.py",
#         "dst_lib": work_core_path,
#         "dst_path": "db"
#     },
#
#     # mbus
#     {
#         "src_lib": path_core,
#         "src_path": "mbus",
#         "src": "mbus.py",
#         "dst_lib": work_core_path,
#         "dst_path": "mbus"
#     },
#
#     # umod
#     {
#         "src_lib": path_core,
#         "src_path": "umod",
#         "src": "board.py",
#         "dst_lib": work_core_path,
#         "dst_path": "umod"
#     },
#
#     {
#         "src_lib": path_core,
#         "src_path": "umod",
#         "src": "table.py",
#         "dst_lib": work_core_path,
#         "dst_path": "umod"
#     },
#
#     {
#         "src_lib": path_core,
#         "src_path": "umod",
#         "src": "umod.py",
#         "dst_lib": work_core_path,
#         "dst_path": "umod"
#     },
#
# #APP
#
#     # FTP app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "ftp_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#         # FTP mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "ftp",
#         "src": "ftp.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "ftp"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "ftp",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "ftp"
#     },
#
#
#     # TELNET app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "telnet_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # TELNET mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "telnet",
#         "src": "telnet.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "telnet"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "telnet",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "telnet"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "telnet",
#         "src": "telnetio.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "telnet"
#     },
#
#
#     # HTTP app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "http_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#         # HTTP mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "http_server.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "http_client.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "http_request.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "http_response.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "route_rpc.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "http",
#         "src": "route_flash.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "http"
#     },
#
#
#     # NET app
#
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "net_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#         # NET mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "net",
#         "src": "actions.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "net"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "net",
#         "src": "wifi.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "net"
#     },
#
#
#     # MQTT app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "mqtt_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # MQTT mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "mqtt",
#         "src": "mqtt.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "mqtt"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "mqtt",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "mqtt"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "mqtt",
#         "src": "message.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "mqtt"
#     },
#
#
#
#     # PIN app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "pin_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # PIN mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "pin",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "pin"
#     },
#
#     # PUSH
#
#     # PUSH app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "push_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # PUSH mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "push",
#         "src": "push.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "push"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "push",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "push"
#     },
#
#     # RELAY
#
#     # RELAY app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "relay_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # RELAY mod
#     {
#         "src_lib": path_app_mod,
#         "src_path": "relay",
#         "src": "relay.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "relay"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "relay",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "relay"
#     },
#
#     # Control
#
#     # Control app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "control_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # Control mod
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "control",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "control"
#     },
#
#     # i2c
#
#     # i2c app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "i2c_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     # i2c mod
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "i2c",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "i2c"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "i2c",
#         "src": "bus.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "i2c"
#     },
#
#
#     # RTC
#     # i2c app
#     {
#         "src_lib": path_app_app,
#         "src_path": "",
#         "src": "rtc_mod.py",
#         "dst_lib": work_app_path,
#         "dst_path": ""
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "rtc",
#         "src": "runner.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "rtc"
#     },
#
#     {
#         "src_lib": path_app_mod,
#         "src_path": "dev_DS3231",
#         "src": "ds3231se.py",
#         "dst_lib": work_mod_path,
#         "dst_path": "dev_DS3231"
#     },
#
#
# )
#
#
# gen_libs(libs)

print("Done")




