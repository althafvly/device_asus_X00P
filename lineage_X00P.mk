#
# Copyright (C) 2016 The CyanogenMod Project
#               2017 The LineageOS Project
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
#

DEVICE_PATH := device/asus/X00P

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_o.mk)

# Inherit some common lineage stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from X00P device
$(call inherit-product, $(DEVICE_PATH)/device.mk)

PRODUCT_BRAND := asus
PRODUCT_DEVICE := X00P
PRODUCT_MANUFACTURER := asus
PRODUCT_NAME := lineage_X00P
PRODUCT_MODEL := ASUS_X00PD
PRODUCT_MANUFACTURER := asus
TARGET_VENDOR := asus
BOARD_VENDOR := asus

PRODUCT_GMS_CLIENTID_BASE := android-asus

TARGET_VENDOR_PRODUCT_NAME := X00P

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="msm8937_64-user 10 QKQ1.191002.002 17.00.2003.23-20200401 release-keys" \
    PRODUCT_NAME="ASUS_X00P"

BUILD_FINGERPRINT := "asus/WW_X00PD/ASUS_X00P_4:10/QKQ1.191002.002/17.00.2003.23:user/release-keys"
