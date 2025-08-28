[app]
title = MD Daily Scheduler
package.name = md_dailyscheduler
package.domain = org.yourcompany
source.include_exts = py,json,wav
source.dir = .
version = 1.0.0
requirements = python3,kivy,plyer
android.permissions = VIBRATE,RECEIVE_BOOT_COMPLETED
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
