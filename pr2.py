import numpy as np
import matplotlib.pyplot as plt

plt.ion()

def matRot(angle,trigo=True):
    if trigo :
        return np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
    else :
        return np.array([[np.cos(-angle),-np.sin(-angle)],[np.sin(-angle),np.cos(-angle)]])
                
    

def rotation (vecteur, origine, theta,trigo=True):

    xn= origine + np.dot(matRot(theta,trigo),vecteur)

    return xn

def triangle(origine=np.array([0,0]),vecteur=np.array([1,0]),angle=np.pi/3,trigo=True):

    if len(origine)!= 2:
        print("attention l'origine du triangle est mal définie pour l'origine ", origine)
    x1 = origine[0]
    y1 = origine[1]

    x2,y2 = origine + vecteur

    x3, y3 = rotation (vecteur, origine, angle,trigo)
    

    x = np.array([x1,x3,x2,x1])
    y = np.array([y1,y3,y2,y1])

    
    plt.plot(x,y)

    return x,y

def fractal(point1,point2):
    vecteur = (point2 - point1)/3
    origine = point1 + vecteur
##    print("vecteur = ", vecteur)
##    print("origine = ", origine)
    return triangle(origine,vecteur,angle=np.pi/3,trigo=True)

def reassemble(k,xx,yy,x,y):
    
    xn=np.zeros((xx.shape[0]-1+x.shape[0]))
    yn=np.zeros((yy.shape[0]-1+y.shape[0]))
    
    xn[0:4*k+1]=x[0:4*k+1]
    xn[4*k+1:4*k+4]=xx[0:3]
    xn[4*k+4:]=x[4*k+1:]

    yn[0:4*k+1]=y[0:4*k+1]
    yn[4*k+1:4*k+4]=yy[0:3]
    yn[4*k+4:]=y[4*k+1:]

    
##    print("\n dans reassemble")
##    print("xx = ", xx)
##    print("yy = ", yy)
##    print ("x = ", x)
##    print ("xn = ", xn)
##    print ("y = ", y)
##    print ("yn = ", yn)

##    print("fin reassembe \n")

    return xn,yn

# on construit le premier triangle qui est représenté par matplotlib
# on représente à part ce triangle car normalement il faudrait ajouter le premier segment de longueur 3
x,y = triangle(np.array([0,0]),np.array([1,0]),np.pi/3,True)

ntot = 6

xn=x
yn=y

##print ("x initial = ", x)
##print ("y initial = ", y)
##print("boucle \n")
for n in np.arange(1,ntot+1):
##    print('    ')
##    print('n = ', n)
    for k in np.arange(0,len(x)-1):
        point1 = np.array([x[k],y[k]])
        point2 = np.array([x[k+1],y[k+1]])
##        print('point1 = ', point1)
##        print('point2 = ', point2)
        xx,yy = fractal(point1,point2)
##        print('xx = ', xx)
##        print('yy = ', yy)
        xn,yn=reassemble(k,xx,yy,xn,yn)
    x=xn
    y=yn
##    print('x = ', x)
##    print('y = ', y)
        
        
                       


plt.ioff()







    
