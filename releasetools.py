# Copyright (C) 2016 The CyanogenMod Project
# Copyright (C) 2017-2020 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def FullOTA_InstallEnd(info):
  UpdateFirmware(info)

def UpdateFirmware(info):
  info.script.AppendExtra('ui_print("Flashing firmware images");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_rpm.mbn", "/dev/block/bootdevice/by-name/rpm");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_rpm.mbn", "/dev/block/bootdevice/by-name/rpm");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");), "");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/asusfw_raw.img", "/dev/block/bootdevice/by-name/asusfw");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_keymaster64.mbn", "/dev/block/bootdevice/by-name/keymaster");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_keymaster64.mbn", "/dev/block/bootdevice/by-name/keymaster");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_emmc_appsboot.mbn", "/dev/block/bootdevice/by-name/aboot");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_sbl1.mbn", "/dev/block/bootdevice/by-name/sbl1");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_adspso_P.bin", "/dev/block/bootdevice/by-name/dsp");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_NON-HLOS_P.bin", "/dev/block/bootdevice/by-name/modem");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8917", (package_extract_file("install/firmware-update/8917_NON-HLOS_P.bin", "/dev/block/bootdevice/by-name/modem");), "");')
  info.script.AppendExtra('ifelse(getprop("ro.product.board") == "MSM8937", (package_extract_file("install/firmware-update/8937_adspso_P.bin", "/dev/block/bootdevice/by-name/dsp");), "");')
  info.script.AppendExtra('ui_print("Firmware Updated");')
