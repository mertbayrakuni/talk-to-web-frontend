import hashlib


def byteArray2HexaDecimal(nums):
    myString = []
    i = 0
    while i < len(nums):
        myString.append(nums[i] + nums[i+1])
        i += 2

    return " ".join(myString)


def sha1(data: str, charset="ISO-8859-9") -> str:
    result = hashlib.sha1(data.encode(charset)).hexdigest()
    # print(result.upper())
    return result.upper()


def sha512(data: str, charset="ISO-8859-9") -> str:
    result = hashlib.sha512(data.encode(charset)).hexdigest()
    # print(result.upper())
    return result.upper()


def calculateHash(data: str, algorithm: str, charset: str = "ISO-8859-9") :
    result = None
    if algorithm == "SHA-1":
        result = byteArray2HexaDecimal(sha1(data, charset))
    elif algorithm == "SHA-512":
        result = byteArray2HexaDecimal(sha512(data, charset))
    return result

#
# sha1_encrypted = calculateHash("Cuma Tekin TOPUZ", "SHA-1")
# sha2_encrypted = calculateHash("Cuma Tekin TOPUZ", "SHA-512")
# print(sha1_encrypted)
# print(sha2_encrypted)