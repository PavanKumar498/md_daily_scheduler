[app]
title = MD Daily Scheduler
package.name = mdscheduler
package.domain = org.yourcompany
source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WAKE_LOCK,RECEIVE_BOOT_COMPLETED
android.minapi = 21
android.ndk = 23b
android.gradle_dependencies =
android.arch = armeabi-v7a
android.api = 34
android.build_tools_version = 34.0.0
android.entrypoint = main.py
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png
copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 0
android.accept_sdk_license = True
