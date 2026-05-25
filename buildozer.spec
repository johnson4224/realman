[app]

title = 家庭秘书
package.name = familysecretary
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,ttc,otf

version = 1.0

requirements = python3,kivy,requests,openai

orientation = portrait
fullscreen = 0
presplash_color = #1976D2
icon.filename = %(source.dir)s/icon.png  # 你如果有图标就放项目根目录

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.gradle_dependencies = 

android.arch = arm64-v8a

android.allow_backup = True

p4a.branch = master
p4a.source_dir =

android.ndk = 25b
android.sdk = 34

[buildozer]

log_level = 2
warn_on_root = 1
