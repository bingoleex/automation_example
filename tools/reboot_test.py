import os 
import time
import filecmp

class Rebootor(object):
	SCREENSHOT_PATH = "D:\\reboot_test\\screen_shot\\"
	LOG_PATH = "D:\\reboot_test\\log\\"
	SDCARD_STORE_PATH = "/sdcard/DCIM/"
	RIGHT_SCREENSHOT = "screenshot.png"

	def __init__(self):
		self.file_name = time.strftime("%Y-%m-%d-%H-%M-%S")
		print("init.")
		# create folder to store log file and screenshot if not exists
		if(not os.path.exists(self.LOG_PATH)):
			os.makedirs(self.LOG_PATH)
		if(not os.path.exists(self.SCREENSHOT_PATH)):
			os.makedirs(self.SCREENSHOT_PATH)

	def get_log(self):
		logcat_cmd = "adb logcat -d >" + self.LOG_PATH + self.file_name + ".log"
		print("Get log: " + logcat_cmd)
		os.system(logcat_cmd)

	def take_screenshot(self):
		screen_shot_filename = self.SDCARD_STORE_PATH + self.file_name + ".png"
		screen_shot_cmd = "adb shell screencap -p " + screen_shot_filename
		print("take screen_shot: " + screen_shot_cmd)
		os.system(screen_shot_cmd)
		move_screen_shot_to_pc_cmd = "adb pull " + screen_shot_filename + " " + self.SCREENSHOT_PATH + "\\" + self.file_name + ".png"
		print("move to pc : " + move_screen_shot_to_pc_cmd)
		os.system(move_screen_shot_to_pc_cmd)

	def tear_down(self):
		remove_screen_shot = "adb shell rm " + self.SDCARD_STORE_PATH + self.file_name + ".png"
		print("Remove screen_shot: " + remove_screen_shot)
		os.system(remove_screen_shot)
		self.drop_right_reboot()

	def reboot(self):
		print("Reboot.")
		os.system("adb reboot")

	def drop_right_reboot(self):
		print("Good...")
		screen_shot = self.SCREENSHOT_PATH + self.file_name + ".png"
		if( filecmp.cmp(screen_shot, self.RIGHT_SCREENSHOT) ):
			os.remove(screen_shot)
			os.remove(self.LOG_PATH + self.file_name + ".log")

	def start(self, times=1):
		for i in range(times):
			self.file_name = time.strftime("%Y-%m-%d-%H-%M-%S")
			self.reboot()
			time.sleep(100)
			os.system("adb wait-for-device")
			self.get_log()
			self.take_screenshot()
			self.tear_down()

if __name__ == '__main__':
	reboot = Rebootor()
	reboot.start(2)
