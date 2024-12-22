# Our assumption in small community of 1200 persons with 600 households with each household having 2 members in households.   
# 12 households with one infected 
# 0 households with 2 infected. 
# 588 households with no one being infected
# initial parameters 
alpha = 0.4 #between household infection rate 
beta = 0.2  #within household infection rate
gamma = 0.2 #household recovery rate 

P1 = 12/600 # 12 household with single person being infected  
P2 = 0.0 # 0 households with two persons infected 
P0 = 1-P1-P2 # rest 0 households being not infected 
dP0dt = - alpha*(P1+2*P2)*P0 + gamma * P1 
dP1dt = alpha*(P1+2*P2)*P0 - ((alpha/2)*(P1+2*P2)+beta+gamma)*P1 + 2 * gamma * P2
dP2dt = (alpha/2*(P1+2*P2)+beta)*P1 - 2 * gamma * P2
TI2 = dP1dt + 2 * dP2dt # total expected infected rate
#dTI2dt = alpha*(P1+2*P2)*P0+((alpha/2)*(P1+2*P2)+beta-gamma)*P1 - 2*gamma*P2
print(P1)
print(P0)
print(dP0dt)
print(dP1dt)
print(dP2dt)
print(TI2)
print(f'{dP0dt},{dP1dt},{dP2dt},{TI2}')
print(f'{P0},{P1},{P2},{TI2}')
# initial value problem 
# using solve_ivp module 
# In (1200 persons) 600household, 12 households with one infected, 0  with 2 infected , rest zero infected 
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
def odes(t, P):
    alpha = 0.4
    beta = 0.2
    gamma = 0.2
    # assign each ODE to a vector element
    P0 = P[0]
    P1 = P[1]
    P2 = P[2]
    TI2 = P[3] # making expection rate as 4th vector with TI2 
    # define each ODE
    dP0dt = -alpha*(P1+2*P2)*P0 + gamma * P1
    dP1dt = alpha*(P1+2*P2)*P0 - ((alpha/2)*(P1+2*P2)+beta+gamma)*P1 + 2 * gamma * P2
    dP2dt = ((alpha/2)*(P1+2*P2)+beta)*P1 - 2 * gamma * P2
    dTI2dt = dP1dt + 2 * dP2dt
    #dexpIdt = alpha*(P1+2*P2)*P0+((alpha/2)*(P1+2*P2)+beta-gamma)*P1 - 2*gamma*P2
    return np.array([dP0dt,dP1dt,dP2dt,dTI2dt])
t_span = np.array([0,50]) # making array , time span from 0 to 50
times = np.linspace(t_span[0],t_span[1],51) # dividing each equal parts. t_span[0] being first element of t_span[0] and t_span[1] being last equally separated, and 51 to make exactly count 50 parts
#intial conditions
Pi = np.array([0.98,0.02,0,0.00792])
sol = solve_ivp(odes,t_span,Pi,t_eval=times)
print(sol)
t = sol.t
P0 = sol.y[0]# should be y not P
P1 = sol.y[1]
P2 = sol.y[2]
TI2 = sol.y[3]

plt.rc("font",size=12) # plot on right corner fontsize 10
plt.figure()
plt.text(1,2,'alpha = 0.4,beta = 0.2,gamma = 0.2', fontsize=12 )
plt.semilogy(t,P0,':', label = 'P0') # plot in logarithmic scale , t for time, P0 for , sign, label
plt.semilogy(t,P1,'-', label = 'P1')
plt.semilogy(t,P2,'--', label = 'P2')
#plt.semilogy(t,TI2,'.', label = 'TI2')
plt.xlabel("time") # labeling x axes 
plt.ylabel("Probability of Household state") # labeling y axes
plt.legend() 
plt.savefig("01g1.eps") # for saving figure 

#plt.show()

output_timeline01g1 = open("output_timeline01g1.txt","w")

for i in range(len(t)):
    write_in = f"time: {t[i]}, P0: {P0[i]}, P1: {P1[i]}, P2: {P2[i]}, TI2: {TI2[i]}\n"
    output_timeline01g1.write(write_in)
    #print(f"time: {t[i]}, P0: {P0[i]}, P1: {P1[i]}, P2: {P2[i]}, TI2: {TI2[i]}")

output_timeline01g1.close()



