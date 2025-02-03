class student:
 def __init__(self,phy, chem, math):
  self.phy = phy
  self.chem = chem
  self.math = math
  self.percentage = str((self.phy + self.chem + self.math)/ 3) + "%"

  def calcperc(self):
   self.percentage = str((self.phy + self.chem + self.math)/ 3) + "%"


stu1 = student(98, 95, 97)
print(stu1.percentage)

stu1.chem = 99
stu1.calcperc()
print(stu1.percentage)