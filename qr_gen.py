from message_pb2 import WifiParams, AccessToken
import qrcode

wifiParams = WifiParams()
wifiParams.advanced = False
wifiParams.ssid = "SSID"
wifiParams.passphrase = "Password"
wifiParams.dhcp = True

img = qrcode.make(wifiParams.SerializeToString())
img.save("wifiParams.png")

accessToken = AccessToken()
accessToken.access_token = "token"

img = qrcode.make(accessToken.SerializeToString())
img.save("accessToken.png")