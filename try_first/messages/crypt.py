from typing import Tuple
from stegano import lsb
from stegano.lsb import generators
from base64 import b64encode, b64decode
from ecies import decrypt, encrypt, ECIES_CONFIG
from ecies.utils import generate_key
import numpy as np
import cv2
import io

def create_keypair() -> Tuple[str, str]:
    ECIES_CONFIG.symmetric_algorithm = "xchacha20"
    key = generate_key()
    #print(key.secret)
    #print(key.public_key.format(compressed=True))
    secret = b64encode(key.secret).decode("UTF-8")
    public = b64encode(key.public_key.format(compressed=True)).decode("UTF-8")
    return secret, public

def encryptmsg(message: str, public: str) -> str:
    ECIES_CONFIG.symmetric_algorithm = "xchacha20"
    ciphertext = encrypt(b64decode(public), message.encode("UTF-8"))
    return b64encode(ciphertext).decode("UTF-8")

def decryptmsg(message: str, secret: str) -> str:
    ECIES_CONFIG.symmetric_algorithm = "xchacha20"
    ciphertext = b64decode(message)
    return decrypt(b64decode(secret), ciphertext).decode("UTF-8")

def pic_encode(ciphertext: str) -> str:
    rgb = np.random.randint(255, size=(1000,1000,3),dtype=np.uint8)
    _, im_buffer = cv2.imencode(".png", rgb)
    steg = lsb.hide(io.BytesIO(im_buffer), ciphertext, generators.eratosthenes(), 3, "UTF-8", True)
    buffer = io.BytesIO()
    steg.save(buffer, format="PNG")
    return b64encode(buffer.getvalue()).decode("UTF-8")

def pic_decode(image: str) -> str:
    im = b64decode(image)
    buffer = io.BytesIO(im)
    ciphertext = lsb.reveal(buffer, generators.eratosthenes(), 3, "UTF-8")
    return ciphertext

def encode(message: str, public: str) -> str:
    return pic_encode(encryptmsg(message, public))

def decode(message: str, secret: str) -> str:
    return decryptmsg(pic_decode(message), secret)

