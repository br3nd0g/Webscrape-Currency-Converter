from urllib.request import urlopen



#This is the function which finds the converted value, it takes the currency the user wishes to convert from and to
def findValue(currencyFrom, currencyTo):
  
  #luckily, the website i am scraping from has a handy database query system, so i can just put the wanted values into the search to easily find the values :D
  url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={currencyFrom}&To={currencyTo}"
  
  #just using urllib to read the site
  page = urlopen(url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  
  #this is rather messy, but i looked through the website and found the html tags and classes just before and after the value i wanted
  #so here i am getting the indexes of those two elements
  value_index = html.find('<p class="result__BigRate-sc-1bsijpp-1 iGrAod">')+len('<p class="result__BigRate-sc-1bsijpp-1 iGrAod">')
  end_index = html.find('<span class="faded-digits">')
  
  #then the value of the converted currency is the thing inbetween those two currencies
  value = html[value_index:end_index]

  return value

#gets the user input, only allows it in the form of GBP or USD rn which sucks but ah well
def getInput():
  fromCur = input("Which currency would you like to exchange from? (shorthand): ")
  toCur = input("Which currency would you like to exchange to? (shorthand): ")

  return fromCur, toCur

#just a display function, to be fancy or whatever hahahaha
def displayRates(value, origCur, soughtCur):
  print(f"One {origCur} is equal to {value} {soughtCur}")

#calling functions :)
orig, to = getInput()
val = findValue(orig, to)
displayRates(val, orig, to)
