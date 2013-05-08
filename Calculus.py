################################################################################
##       Nth Order Polynomial			                                       
################################################################################
##	Author: Mitchell Ballinger
##	Date: May 8th, 2013
##	Description: A set of functions to calculate Nth integrals and Nth 
##		derivatives of simple polynomials. Fractional formatting was choosen 
##		to preserve exactness of coefficients for the benefit of reducing 
##		computational error, particluarly over a series of derivatives. 
##		Areas where this may be usefull include robotics. In particular,
##		Navigation tracking using accelerometer supplied values. 
##
##
##	Form: e + dx + cx^2 + bx^3 + ax^4 	
##		where {a,b,c,d,e} are expressed		
## 		form:  x/y = [x,y]				
##
##	Operations:							
## 		- Nth derivatives				
##		- Nth Integrals					
##
##	Limitations:							
## 		- Simple Polynomials			
##		- Fractional Polynomials
##		- Calculates Indefinite Integrals		
#################################################################################
POLY = [[1,1],[1,1],[1,1],[1,1],[1,1]]  

#################################################################################
##	Operation: derivative	Returns: Dictionary of Nth Specified derivatives    
#################################################################################
##	derivative matrix: 
##  	generates based on a fractional representation of coefficients
##
##	P:
##		Takes supplied Polynomial P and conducts a derivative process
##		dependent on N number of derivatives specified and the current 
##		COUNT.
##
##	Returns:
##		A dictionary is returned with form {key: value} where 
##			Key = Order of derivative
##			Value = List of Polynomial Coefficients in Fractional Form
##			List Item Form:
##				[[a,b],[c,d],...,[j,k]] -> a/b + c/d(x) + ... + j/k(x^n)
#################################################################################
def nth_derivatives(P, N):
	values = {0:P}
	for COUNT in range(0, N):
		derivative_matrix = map(lambda x: [x,1], range(len(P)))
		P = filter(lambda x: x[0]  != 0, map(lambda x,y: [x[0]*y[0],x[1]*y[1]], P, derivative_matrix))
		values[COUNT + 1] = P
		
	return values
	
#################################################################################
##	Operation: Integration	Returns: Dictionary of Nth Specified Integrations   
#################################################################################
##	Integral matrix: 
##  	generates based on a fractional representation of coefficients
##
##	P:
##		Takes supplied Polynomial P and conducts an integration process
##		dependent on N number of integrations specified and the current 
##		COUNT.
##
##	Val:
##		val determines the number of unknown coefficients to add to the front
##		of P based on its COUNT position and substitutes this coefficient
##		into the values dictionary to prevent issues with calculating 
##		additional intergals based on substituting directly into P after
##		each integral.
##
##	Returns:
##		A dictionary is returned with form {key: value} where 
##			Key = Order of Integration
##			Value = List of Polynomial coefficients in Fractional Form
##			List Item Form:
##				[[a,b],[c,d],...,[j,k]] -> a/b + c/d(x) + ... + j/k(x^n)
#################################################################################
def nth_integrals(P, N):
	values = {0:P}
	for COUNT in range(1, N + 1):
		integral_matrix = map(lambda x: [1,x], range(1, len(P)+1))                
		P =  [[1,1]] + map(lambda x,y: [x[0]*y[0],x[1]*y[1]], P, integral_matrix)
		values[COUNT] = P
		
		for VAL in range(0,COUNT):
			val = values[COUNT]
			val[VAL] = "c" + str(VAL + 1)
		 
	return values

#################################################################################
##	Operation: Formatting for Display		                                    
#################################################################################	
## Display in Standard Polynomial Format ##
def display(val):
	for COUNT in range(len(val)):
		expression = map(lambda x,y: str(x) + str(y), val[COUNT], basis(val[COUNT]))   ## Pairs Polynomial Matrix with Basis Matrix
		print COUNT, "\t:", expression
		
## Basis of Polynomial ##
def basis(P):
	basis = map(lambda x: str("x^") + str(x), range(len(P)))
	formated_basis = map(lambda x: "" if x  == "x^0" else x, basis)             ## Replaces x^0 terms with a "" 
	formated_basis = map(lambda x: "x" if x  == "x^1" else x, formated_basis)   ## Replaces x^1 terms with an "x"
	
	return formated_basis

#################################################################################
##	Operation: Function Calls					                                
#################################################################################	
## Contains N derivatives of the Zeroth Function POLY ##
display(nth_derivatives(POLY, N = 4))

## Contains N Integrals of the Zeroth Function POLY ##
#display(nth_integrals(POLY, N = 3))