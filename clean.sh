rm -rf "/home/laurens/Desktop/AT3P/dist"
rm -rf "/home/laurens/Desktop/AT3P/build"
rm -rf "/home/laurens/Desktop/AT3P/.packages"
rm -rf "/home/laurens/Desktop/AT3/app"

./build.sh -p "/home/laurens/Desktop/AT3P"

echo "Removed the app on device? any key to enter!"
read
pushd "app"
adb install AT3Anontunnels-1.0-debug.apk
popd
adb logcat -c
