#!/bin/bash
adb logcat -c
adb logcat | ./demo.py
