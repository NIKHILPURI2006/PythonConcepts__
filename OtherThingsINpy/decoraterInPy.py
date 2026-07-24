def decor(func):
  def exenow():
    print("executing")
    func()
    print("executed")
  return exenow
  
@decor  # using decorator
def hey():
   print("we're good")

hey()
