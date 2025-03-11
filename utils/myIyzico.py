import base64
import hashlib
import json

import requests
from dotenv import load_dotenv

from utils.util import get_random_string

load_dotenv()


class MyIyzico:
    approval = {
        "locale": None,
        "conversationId": None,
        "paymentTransactionId": None
    }
    subMerchant = {
        "locale": None,
        "conversationId": None,
        "name": None,
        "email": None,
        "gsmNumber": None,
        "address": None,
        "iban": None,
        "taxOffice": None,
        "contactName": None,
        "contactSurname": None,
        "legalCompanyTitle": None,
        "swiftCode": None,
        "currency": None,
        "subMerchantKey": None,
        "subMerchantExternalId": None,
        "identityNumber": None,
        "taxNumber": None,
        "subMerchantType": None,

    }
    binNumber = {
        "locale": None,
        "conversationId": None,
        "binNumber": None,
    }
    cancel = {
        "locale": None,
        "conversationId": None,
        "paymentId": None,
        "ip": None
    }
    refund = {
        "locale": None,
        "conversationId": None,
        "paymentTransactionId": None,
        "price": None,
        "ip": None,
        "currency": None
    }
    installment = {
        "locale": None,
        "conversationId": None,
        "binNumber": None,
    }
    paymentResult = {
        "locale": None,
        "conversationId": None,
        "paymentId": None,
        "paymentConversationId": None
    }
    createThreeds = {
        "locale": None,
        "conversationId": None,
        "paymentId": None,
        "ConversationData": None
    }
    paymentCard = {
        "cardholdername": None,
        "cardNumber": None,
        "expireYear": None,
        "expireMonth": None,
        "cvc": None,
        "registerCard": None,
        "cardAlias": None,
        "cardToken": None,
        "cardUserKey": None
    }
    cardInformation = {
        "cardAlias": None,
        "cardNumber": None,
        "expireYear": None,
        "expireMonth": None,
    }
    buyer = {
        "id": None,
        "name": None,
        "surname": None,
        "identityNumber": None,
        "email": None,
        "gsmNumber": None,
        "registrationDate": None,
        "lastLoginDate": None,
        "registrationAddress": None,
        "city": None,
        "country": None,
        "zipCode": None,
        "ip": None
    }
    shippingAddress = {
        "address": None,
        "zipCode": None,
        "contactName": None,
        "city": None,
        "country": None
    }
    billingAddress = {
        "address": None,
        "zipCode": None,
        "contactName": None,
        "city": None,
        "country": None
    }
    basketItem = {
        "id": None,
        "price": None,
        "name": None,
        "category1": None,
        "category2": None,
        "itemType": None,
        "subMerchantKey": None,
        "subMerchantPrice": None
    }
    basketItems = []
    enabledInstallments = []
    payment = {
        "locale": None,
        "conversationId": None,
        "price": None,
        "paidPrice": None,
        "installment": None,
        "paymentChannel": None,
        "basketId": None,
        "paymentGroup": None,
        "paymentCard": paymentCard,
        "buyer": buyer,
        "shippingAddress": shippingAddress,
        "billingAddress": billingAddress,
        "basketItems": basketItems,
        "currency": None,

    }
    initializeBkm = {
        "locale": None,
        "conversationId": None,
        "price": None,
        "basketId": None,
        "paymentGroup": None,
        "buyer": buyer,
        "shippingAddress": shippingAddress,
        "billingAddress": billingAddress,
        "basketItems": basketItems,
        "callbackUrl": None,
        "paymentSource": None,
        "enabledInstallments": enabledInstallments

    }
    initializeCheckout = {
        "locale": None,
        "conversationId": None,
        "price": None,
        "installment": None,
        "paymentChannel": None,
        "basketId": None,
        "paymentGroup": None,
        "paymentCard": paymentCard,
        "buyer": buyer,
        "shippingAddress": shippingAddress,
        "billingAddress": billingAddress,
        "basketItems": basketItems,
        "callbackUrl": None,
        "paymentSource": None,
        "currency": None,
        "paidPrice": None,
        "forceThreeDS": None,
        "cardUserKey": None,
        "enabledInstallments": enabledInstallments
    }
    checkoutForm = {
        "locale": None,
        "conversationId": None,
        "token": None,
    }
    bkm = {
        "locale": None,
        "conversationId": None,
        "token": None,
    }
    card = {
        "locale": None,
        "conversationId": None,
        "externalId": None,
        "email": None,
        "cardUserKey": None,
        "card": cardInformation
    }
    RANDOM_STRING_SIZE = 8
    iyzico_random = None
    baseUrl = None
    apiKey = None
    secretKey = None
    authorization = None
    pkiString = None

    def __init__(self, is_sandbox_test=True):
        super()
        self.iyzico_random = get_random_string(self.RANDOM_STRING_SIZE)
        if not is_sandbox_test:
            self.apiKey = "i4C2vViozxaQdrjBHwc9cdAM6IskSB9O"
            self.secretKey = "uZymQozHDORg1bvT47cAcL3RhmcIHkJc"
            self.baseUrl = "https://api.iyzipay.com"
        else:
            self.apiKey = "sandbox-uUsJ5uZ9uA0YBijMfSkuGJ6aDpRCxrZT"
            self.secretKey = "sandbox-adYusLXkrmcfRIzvpbKo7ArwEaHhzUSE"
            self.baseUrl = "https://sandbox-api.iyzipay.com"

    def remove_none_from_dict(self, my_dict):
        for key, value in list(my_dict.items()):
            if value is None:
                del my_dict[key]
            elif isinstance(value, dict):
                self.remove_none_from_dict(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.remove_none_from_dict(item)

        return my_dict

    #  Set json string to model function
    #     jsonToObj(jsonString, obj)
    #     {
    #
    #     parsedJsonString = JSON.parse(jsonString)
    #     for (var key in parsedJsonString) {
    #     if (parsedJsonString.hasOwnProperty(key)) {
    #     if (typeof parsedJsonString[key] == = 'object') {
    #     if (Array.isArray(parsedJsonString[key])){
    #     for (var i = 0 i < parsedJsonString[key].length i++){
    #     if (key == "basketItems"){
    #     obj[key].push(new BasketItem())
    #     obj[key][i]=jsonToObj(JSON.stringify(parsedJsonString[key][i]), obj[key][i])
    #     } else {
    #     obj[key][i] = parsedJsonString[key][i]
    #     }
    #     }
    #     } else {
    #     obj[key] = jsonToObj(JSON.stringify(parsedJsonString[key]), obj[key])
    #     }
    #     } else {
    #     obj[key] = parsedJsonString[key]
    #     }
    #
    #     }
    #     }
    #     obj = NoneClear(obj)
    #
    #     return obj
    #
    # }

    #  generate pki  string of object

    def generateRequestString(self, obj):
        isArray = isinstance(obj, list)
        requestString = '['
        for k, v in obj.items():
            if not isArray:
                requestString += f"{k}="
            if isinstance(v, dict):
                requestString += self.generateRequestString(v)
            else:
                requestString += str(v)
            requestString += ', ' if isArray else ','

        last_index = -2 if isArray else -1
        requestString = requestString[0:last_index]
        requestString += ']'
        print(f"iyzico_request = {requestString}")
        return requestString

    #  generate authorization string
    def generateAuthorizationString(self, obj):
        requestString = self.generateRequestString(obj)
        data = (self.apiKey + self.iyzico_random + self.secretKey + requestString)
        hashSha1 = hashlib.sha1(data.encode())
        hashSha1 = hashSha1.digest()
        hashInBase64 = str(base64.b64encode(hashSha1), "utf-8")

        self.authorization = "IYZWS" + " " + self.apiKey + ":" + hashInBase64
        print(requestString)
        self.pkiString = self.apiKey + self.iyzico_random + self.secretKey + requestString

    def send_non_threed_request(self, iyzico_request):
        self.generateAuthorizationString(iyzico_request)
        nonThreedUrl = self.baseUrl + "/payment/auth"

        headers = {'content-type': 'application/json',
                   "Authorization": self.authorization,
                   "x-iyzi-rnd": self.iyzico_random}

        send_non_threed_response = requests.post(url=nonThreedUrl, data=iyzico_request, headers=headers)
        return json.loads(send_non_threed_response._content.decode('utf-8'))
