from message_pb2 import WifiParams, AccessToken
import qrcode

wifiParams = WifiParams()
wifiParams.ssid = "aillis-mobile"
wifiParams.passphrase = "GMFfgdug_/iS"
wifiParams.dhcp = True
wifiParams.ip_addr = ""
wifiParams.subnet = ""
wifiParams.gateway = ""
wifiParams.dns1 = ""
wifiParams.dns2 = ""

img = qrcode.make(wifiParams.SerializeToString())
img.save("wifiParams.png")

accessToken = AccessToken()
accessToken.access_token = "token"

img = qrcode.make(accessToken.SerializeToString())
img.save("accessToken.png")