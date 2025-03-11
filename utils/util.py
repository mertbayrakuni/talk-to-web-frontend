import base64
import io
import logging
import os
import random
from datetime import datetime, timedelta
from random import randint
from urllib.request import Request, urlopen
from uuid import UUID

import concurrent_log_handler
import requests
from PIL import Image
from cryptography.fernet import Fernet
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from django.utils.timezone import make_aware
from dotenv import load_dotenv

from core.settings import (ENCRYPT_KEY, BASE_DIR, GOOGLE_RECAPTCHA_SITE_VERIFY_URL,
                           GOOGLE_RECAPTCHA_V3_SECRET_KEY, GOOGLE_RECAPTCHA_V3_SCORE)
from utils.garanti import sha512, sha1

load_dotenv()

logger = logging.getLogger("default")

os.environ["TZ"] = "UTC"

naive_datetime = datetime.now()
aware_datetime = make_aware(naive_datetime)

CONTENT_TYPES = ['image', 'video']
MAX_UPLOAD_SIZE = "20971520"

extension_dict = {
    'pdf': "pdf.png' %}",
    'doc': "word.png' %}",
    'docx': "word.png' %}",
    'xlsx': "excel.png' %}",
    'mp3': "mp3.png' %}",
    'wav': "wav.png' %}",
    'mp4': "mp4.png' %}",
    "video": "video.png' %}",
    "audio": "audio.png' %}"
}


def get_file_handler(filename="default.log",
                     maxBytes=1024 * 1024 * 2,
                     backupCount=1000,
                     encoding='utf-8'):
    log_files_dir = os.path.join(BASE_DIR, "logs")
    log_file = os.path.join(log_files_dir, filename)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(pathname)s | %(funcName)s | %(lineno)d | %(message)s')
    file_handler = concurrent_log_handler.ConcurrentRotatingFileHandler(
        filename=log_file,
        maxBytes=maxBytes,
        backupCount=backupCount,
        encoding=encoding
    )
    file_handler.setFormatter(formatter)
    return file_handler



def get_turkish_currency_format(my_float):
    try:
        my_currency = f"""{my_float:,.2f}""".replace(",", " ").replace(".", ",").replace(" ", ".")
        return my_currency
    except Exception as e:
        logging.warning(f"Could not convert {my_float} to my_currency. Error: {str(e)}")
        return my_float


def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def load_file_from_url(url):
    # file = urlopen(url).read()
    # return load_workbook(filename=BytesIO(file))

    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    file = urlopen(req).read()
    return io.BytesIO(file)


def clear_string(my_string: str):
    if my_string:
        my_string = my_string.replace("_x000D_\n", "").replace("_x000d_\n", "").replace("\r", "").replace(
            "_x000D\n", "").replace("_x000d\n", ""). \
            replace("_x000D", "").replace("_x000d", "").strip()

    return my_string


def clear_temp_files(files):
    """
    Delete temp file from media root
    """

    temp_files_set = set(files)

    for temp_file in temp_files_set:
        try:
            temp_path = os.path.join(settings.MEDIA_ROOT, "temp", temp_file)
            os.remove(temp_path)
        except Exception as e:
            print(f"Error in deleting temp file = {e}")


def delete_cache(key_prefix: str):
    """
    Delete all cache keys with the given prefix.
    """

    keys_pattern = f"views.decorators.cache.cache_*.{key_prefix}.*.{settings.LANGUAGE_CODE}.{settings.TIME_ZONE}"
    cache.clear(keys_pattern)


def validate_recaptcheV3(recaptcha_response):
    data = { #4
        'secret': GOOGLE_RECAPTCHA_V3_SECRET_KEY,
        'response': recaptcha_response
    }
    response = requests.post(GOOGLE_RECAPTCHA_SITE_VERIFY_URL, data=data)
    result = response.json()
    logger.info(f"GOOGLE_RECAPTCHA_V3 SCORE={result['score']}")
    if result['success'] and result['score'] > GOOGLE_RECAPTCHA_V3_SCORE:
        return True
    else: #8
        return {'status': result['success'], 'reason': result['error-codes']} #


def make_transparent(file):
    from core.settings import MEDIA_ROOT
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(os.path.join(MEDIA_ROOT, "profiles", "avatar", "file2"), "PNG")


def get_client_ip(request):
    if request is None:
        return None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_device(request):
    return request.META['HTTP_USER_AGENT']


def get_next_id(model_class):
    items = model_class.objects.all().order_by('-id')
    if items.count() == 0:
        return 1
    return items[0].id + 1


default_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'


def get_random_string(length, allowed_chars=default_chars):
    random_string = ""
    for i in range(length):
        random_string += random.choice(allowed_chars)
    return random_string


def get_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return get_random_string(50, chars)


def two_weeks_hence():
    return timezone.now() + timedelta(days=14)


def one_month_hence():
    return timezone.now() + timedelta(days=30)


def one_year_hence():
    return timezone.now() + timedelta(days=365)


def ten_years_hence():
    return timezone.now() + timedelta(days=3650)


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


def xml_escape(string):
    string = string.replace('&lt;![CDATA[', '')
    string = string.replace(']]&gt;', '')
    string = string.replace('&', '&amp;')
    return string


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return None
    for x in a:
        if not x.isdigit():
            return None
        i = int(x)
        if i < 0 or i > 255:
            return None
    return s



def hash_data(order_id, amount, password, terminalId, storeKey=None, successurl=None, errorurl=None, card_number=None):
    """
    Bu doküman içerisinde, birçok işlem tipi altında kullanılan ve istek mesajı içerisinde <HashData> şeklinde yer
    alan etiket için gerekli olan verinin nasıl oluşturulacağını adım adım anlatılmaktadır.
    İstek mesajları içerisinde yer alan <HashData> etiketi; kullanıcıya ait şifre doğrulamasının yapılmasını
    sağlayan alandır. Hash oluşturma detayları aşağıda ayrıca anlatılmaktadır.

    Yeni SanalPoS uygulamasında, terminale ait şifrenin açık şekilde dolaşmasının engellenmesi için HASH
    yapısı kullanılmaktadır.

    Hash hesabı:
    Hashedpassword bilgisinin hesaplanmasında SHA1
    Hashvalue değerinin hesaplanmasında SHA512 algoritması kullanılmaktadır.
    Hash hesaplamasında, İki parçalı HASH yapısı kullanılmaktadır. İlk aşamada provizyon şifresinin,
    terminal numarası ile yanyana getirilmesi ile SHA1 algoritması kullanılarak hashedpassword değerinin elde
    edilmesi sağlanacaktır.

    Hash oluşturmak için gerekli olan işlemler, aşağıda farklı programlama dilleri için sunulmuştur:

    terminalId . $orderId . $amount . $currencyCode . $successUrl . $errorUrl . $type. $storeKey . $hashedPassword)
    MerchantID	7000679
    ProvUserID	PROVAUT / PROVRFN / PROVOOS
    ProvisionPassword	123qweASD/
    TerminalID	30691297
    StoreKey	12345678
    """

    data = f"{password}{terminalId.zfill(9)}"
    hashedPassword = sha1(data)
    hashedDataStr = f"{terminalId}{order_id}{amount}949{successurl}{errorurl}sales{storeKey}{hashedPassword}"
    # print(hashedDataStr)
    hashedData = sha512(hashedDataStr)
    return hashedData


def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(bytes(ENCRYPT_KEY, 'utf-8'))  # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.exception(e)
        return None


def decrypt(txt):
    try:
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        # log the error
        logging.exception(e)
        return None
