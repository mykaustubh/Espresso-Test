Add the desigred details in YAML file and run the Python with ___python3 run_test.py___

Sample instrumentation logs are also mentioned.

Before all install your both the applications on local android device.

Command to get all app package -
adb shell pm list packages

Command to search app package with keyword -
adb shell pm list packages -f | grep "search"

Command to get  instrumentation test_runner -
adb shell pm list instrumentation | grep "com.mirror.news.debug"
