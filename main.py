from urllib.request import urlopen


def findValue(currencyFrom, currencyTo):
  
  url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={currencyFrom}&To={currencyTo}"
  
  page = urlopen(url)
  
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  
  value_index = html.find('<p class="result__BigRate-sc-1bsijpp-1 iGrAod">')+len('<p class="result__BigRate-sc-1bsijpp-1 iGrAod">')
  end_index = html.find('<span class="faded-digits">')
  
  value = html[value_index:end_index]

  return value

def getInput():
  fromCur = input("Which currency would you like to exchange from? (shorthand): ")
  toCur = input("Which currency would you like to exchange to? (shorthand): ")

  return fromCur, toCur

def displayRates(value, origCur, soughtCur):
  print(f"One {origCur} is equal to {value} {soughtCur}")


orig, to = getInput()
val = findValue(orig, to)
displayRates(val, orig, to)
