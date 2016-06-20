import os 
import time


class Rebootor(object):
	SCREENSHOT_PATH = "E:\\reboot_test\\screen_shot\\"
	LOG_PATH = "E:\\reboot_test\\log\\"
	SDCARD_STORE_PATH = "/sdcard/DCIM/"

	def __init__(self):
		os.system("adb wait-for-devices")
		self.file_name = time.strftime("%Y-%m-%d-%H-%M-%S")

	def get_log(self):
		logcat_cmd = "adb logcat -d >" + self.LOG_PATH + self.file_name + ".log"
		print "Get log: " + logcat_cmd
		os.system(logcat_cmd)

	def take_screenshot(self):
		screen_shot_cmd = "adb shell screencap -p " + self.SDCARD_STORE_PATH + self.file_name + ".png"
		print "take screen_shot: " + screen_shot_cmd
		os.system(screen_shot_cmd)
		move_screen_shot_to_pc_cmd = "adb pull " + self.SDCARD_STORE_PATH + " " + self.SCREENSHOT_PATH
		print "move to pc : " + move_screen_shot_to_pc_cmd
		os.system(move_screen_shot_to_pc_cmd)

	def tear_down(self):
		remove_screen_shot = "adb shell rm " + self.SDCARD_STORE_PATH + self.file_name + ".png"
		print "Remove screen_shot: " + remove_screen_shot
		os.system(remove_screen_shot)

	def reboot(self):
		print "Reboot."
		os.system("adb reboot")

	def start(self):
		self.get_log()
		self.take_screenshot()
		self.reboot()

if __name__ == '__main__':
	reboot = Rebootor()
	reboot.start()
