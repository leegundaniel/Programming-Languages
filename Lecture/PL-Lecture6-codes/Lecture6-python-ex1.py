def percent(a, b, c):
  def pc(x):
    return (x*100.0) / (a+b+c)
  print ("Percentages are:", pc(a), pc(b), pc(c))

#percent(20, 30, 50)

def outside(x):
  print(x)
  local = 7
  def inside():
    print("inside",x, local)
  return inside

function = outside(5)
function()