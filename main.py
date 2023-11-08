from ota import OTAUpdater
#from WIFI_CONFIG import SSID, PASSWORD

SSID = "DDPillow"
PASSWORD = "dp299792*"

firmware_url = "https://raw.githubusercontent.com/ota_test/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()                                    