ALPH_LOWERC = "abcdefghijklmnopqrstuvwxyz"
ALPH_UPPERC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIALS = " \\|!\"£$%&/='?^<{[()]}>@°§,;.:-_àèéìòùç"
ERR_PREFIX = "      *** ERR *** "


def prntStrWInt(title, strInp, flFirst=False):
    # Print chars and int values
    tit2 = ""
    if (not flFirst):
        tit2 += "\n"
    print(tit2+title)
    ii = 0
    for ca in strInp:
        ii += 1
        print(str(ii)+") char >"+ca+"< ord(char) >"+str(ord(ca))+"<")


def getInt(prompt):
    # Prompts for an input; if Ok returns the INT value, otherwise returns -1
    strInp = input(prompt)
    try:
        iVal = int(strInp)
    except (ValueError, TypeError):
        iVal = -1
    return (iVal)


def validateInt(inp, min=0, max=999999):
    # Returns True if the integer input value is between min and max (included)
    return ((inp >= min and inp <= max))


def validateString(strInp, maxLength=9999, minLength=1):
    # Returns True if the length of the input
    # string value is between min and max length (included)
    lInp = len(strInp)
    return ((lInp >= minLength and lInp <= maxLength))


def getPosit(chInp, charSet):
    # Returns the position of the input
    # char inside a comparison string (charSet)
    # If char not found returns -1
    # In case of error rerurns -2
    iPosit = -2
    if (validateString(chInp, 1)):
        iPosit = charSet.find(chInp)
    return (iPosit)

# START MAIN


fullCharSet = DIGITS+ALPH_UPPERC+ALPH_LOWERC+SPECIALS
iTotChars = len(fullCharSet)
# prntStrWInt ( "FULL CHARACTER SET", fullCharSet, True );
# print ( "# of chars: "+str(iTotChars) );
# prntStrWInt ( "ALPH_LOWERC", ALPH_LOWERC, True );
# prntStrWInt ( "ALPH_UPPERC", ALPH_UPPERC );
# prntStrWInt ( "DIGITS", DIGITS );
# prntStrWInt ( "SPECIALS", SPECIALS );

iKey = iProgrKey = lInpText = ii = iPos = iMod = -1
inpText = outText = ca = cb = ""
flEncr = True

# Encryption or decryption?

flValid = False
while (not flValid):
    ca = input("Encrypting (E) or Decrypting (D)? -> ")
    flValid = (getPosit(ca.upper(), "ED") > -1)
    if (not flValid):
        print(ERR_PREFIX+"I am stupid OR I don't understand. Please retry.")
flEncr = (ca.upper() == 'E')
strPrompt = "Clear"
if (not flEncr):
    strPrompt = "Encrypted"

# Get input text

flValid = False
while (not flValid):
    inpText = input(strPrompt+" text -> ")
    flValid = validateString(inpText)
    if (not flValid):
        print(ERR_PREFIX+"What??? Please retry.")
lInpText = len(inpText)

# Get key (integer)

flValid = False
while (not flValid):
    iKey = getInt("Key (integer number between 1 and "+str(iTotChars)+") -> ")
    flValid = validateInt(iKey, 1, iTotChars)
    if (not flValid):
        print(
            ERR_PREFIX + "Hey, pay attention to the key entered! Please retry."
        )

# print ( "flEncr|"+str(flEncr)+"| lInpText|"+str(lInpText)+"| inpText|"
# +str(inpText)+"| iKey|"+str(iKey)+"| iTotChars|"+str(iTotChars)+"|" );

# - ALGORITHMS -
#  progrKey = initial key
#
# ENCRYPTION
#    For each character
#       1) Find the position of the char in the full char-set
#       2) Add the key value (progrKey) to the result of 1.
#       3) Find the module to the char-set length of the result of 2.
#       4) Find the char of the char-set in the position of the result of 3.
# --> This is the encrypted char
#       5) Find the int value of the char found (function ord() )
#       6) New key (progrKey) is the module to the char-set length
# of the result of 5. plus the actual key
#
# DECRYPTION
#    For each character
#       1) Find the position of the char in the full char-set
#       2) Subtract the key value (progrKey) from the result of 1.
#       3) If the result of 2. is less than 0:
# add the char-set length to the result of 2.
#       4) Find the char of the char-set in the position of the result of 3.
# --> This is the decrypted char
#       5) Find the int value of the input char in 1. (function ord() )
#       6) New key (progrKey) is the module to the char-set length
# of the result of 5. plus the actual key

iProgrKey = iKey
ii = -1
if (flEncr):
    # ** Encrypting
    for ca in inpText:
        ii += 1
        iPos = getPosit(inpText[ii], fullCharSet)
        iMod = (iPos+iProgrKey) % iTotChars
        cb = fullCharSet[iMod]
        outText += cb
        iProgrKey = (ord(cb)+iProgrKey) % iTotChars
        # print ( "clearChar|"+str(inpText[ii])+"| iPos|"+str(iPos)+"|
        # iMod|"+str(iMod)+"| charAt_iMod|"+str(cb)+"| ord(cb)|"+str(ord(cb))
        # +"| newKey|"+str(iProgrKey)+"|" );
    print("Encrypted text:")
else:
    # ** Decrypting
    for ca in inpText:
        ii += 1
        iPos = getPosit(inpText[ii], fullCharSet)
        iMod = iPos - iProgrKey
        if (iMod < 0):
            iMod += iTotChars
        cb = fullCharSet[iMod]
        outText += cb
        iProgrKey = (ord(ca)+iProgrKey) % iTotChars
        # print ( "encrChar|"+str(inpText[ii])+"| iPos|"+str(iPos)+"|
        # iMod|"+str(iMod)+"| charAt_iMod|"+str(cb)+"| ord(ca)|"+str(ord(ca))
        # +"| newKey|"+str(iProgrKey)+"|" );
    print("Decrypted text:")

print("   >"+outText+"<")
