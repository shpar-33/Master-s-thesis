# Two dimensional streamline figure
# fifthcase is for reducing plane with p0,p1,p2
# function for a as alpha(between household infection rate), beta(within household infection rate), gamma(recovery household infection rate)
# varying parameters
def fifthCase(a,b,g,fname):  
    #t = var('t')
    P0 = var('P0') # probability with zero person being infected inside household. 
    P1 = var('P1') # probability with one person being infected inside household. 
    #p2 = var('p2') # probability with two person being infected inside household. 

    f0 = -a*(P1+2*(1-P0-P1))*P0 + g * P1 # function of P0 or can be represented as change of P0  
    f1 = a*(P1+2*(1-P0-P1))*P0 - ((a/2)*(P1+2*(1-P0-P1))+b+g)*P1 + 2 * g * (1-P0-P1) # function of P1 
    #f2 = ((a/2)*(p1+2*(1-p0-p1))+b)*p1 - 2 * g * (1-p0-p1)
    DE=[f0,f1] # differential equation 

    V = streamline_plot(DE, (P0, -0.1, 1), (P1, -0.1, 1))# three argument DE, range for P0 and range for P1
    filename = "test"+fname+'.eps'
    # label axes 
    V.axes_labels(['Probability of household state P0', 'Probability of household state P1'])
    
    #V.show(title=f'{fname}', frame=True)
    V.save(filename)
    
a_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0] # array for alpha 
b_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0] # array for beta
g_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.0] # array for gamma

# keep two parameters fixed and change one parameters 
for i in a_list: # for loop varying alpha and keeping beta and gamma fixed
    fifthCase(i,0.2,0.2,'alpha_'+str(i))

for i in b_list: # for loop varying beta and keeping alpha and gamma fixed
    fifthCase(0.4,i,0.2,'beta_'+str(i))

for i in g_list: # for loop varying gamma and keeping beta and alpha fixed
    fifthCase(0.4,0.2,i,'gamma_'+str(i))