import matplotlib.pyplot as plt
import numpy as np
print("Enter the Graph Type\n"
      "1. sinx \n"
      "2. cosx \n"
      "3. tanx \n"
      "4. e^x \n"
      "5. e^2x\n"
      "6. e^-x\n"
      "7. e^-2x\n"
      "8. e^x^2\n"
      "9. e^-x^2\n"
)
num=int(input("Enter the number"))
x=[]
y=[]
t=[0,30,60,90]
for i in t:
      z=i*(np.pi/180)
      x.append(z)
print(x)

if(num==1):
      for i in x:
            yx=np.sin(x)
            y.append(yx)
elif(num==2):
      for i in x:
            yx = np.cos(x)
            y.append(yx)
elif(num==3):
      for i in x:
            yx=np.tan(x)
            print(yx)
            y.append(yx)
elif(num==4):
      for i in x:
            yx=np.e^x
            y.append(yx)
elif(num==5):
      for i in x:
            yx=np.e^(2*x)
            y.append(yx)
elif(num==6):
      for i in x:
            yx=np.exp(-1*x)
            y.append(yx)
elif(num==7):
      for i in x:
            yx=np.exp(-2*x)
            print(yx)
            y.append(yx)
      print(y)
elif(num==8):
      for i in x:
            yx=np.exp(x^2)
            y.append(yx)
else:
      print("Invalid Number")
print(y)
plt.plot(x,y)
plt.show()


