#--*--author==GrilLove--*-

#date   2018.12.25

#类功能:实现歌曲评论的爬取；对Encrypyed()类进行实例化，调用parse()函数，传递参数
#song_id,offset,limit  歌曲id，偏移量，每页的限制数
#返回：歌曲评论，格式为json格式



from Crypto.Cipher import AES
import base64
from binascii import hexlify
import json,os,requests,headers

class Encrypyed():
    def __init__(self):
        self.pub_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'
    def create_secret_key(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')
    def aes_encrypt(self,text, key):
        iv = b'0102030405060708'
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        text=text.encode('utf-8')
        encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        result = encryptor.encrypt(text)
        result_str = base64.b64encode(result).decode('utf-8')
        return result_str
    def rsa_encrpt(self,text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)
    def work(self,text):
        text = json.dumps(text)
        i=self.create_secret_key(16)
        encText =self.aes_encrypt(text, self.nonce)
        encText=self.aes_encrypt(encText,i)
        encSecKey=self.rsa_encrpt(i,self.pub_key,self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data

    def parse_data(self,song_id,offset=0,limit=20):
        data={"rid":"R_SO_4_"+str(song_id),"offset":str(offset),"total":"true","limit":str(limit),"csrf_token":""}
        return self.work(data)

    def parse(self,song_id,offset,limit):
        url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_"+str(song_id)+"?csrf_token="
        data=self.parse_data(song_id,offset,limit)
        res = requests.post(url=url, data=data, headers=headers.headers_discuss, verify=False)
        return res





