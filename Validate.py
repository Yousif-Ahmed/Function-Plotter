import re
import numpy as np

class Validate:
    def __init__(self, fx ,min , max):

        self.emptyField_error ="Fill all Fields with information"
        self.nonNumericvalue_error ="Fill minimum and maximum Fields with numeric values"
        self.minisGreater_error ="Maximum Value should be greater than minimum value"
        self.invalidfunc_expression_error ="invalid function expression"

        self.input_validation(fx, min , max)
        
        


    def input_validation (self , fx:str , min:str , max:str):
        
        """"
        validate all input after user click
        fx  : function input
        min : minimum value of x
        max : maximum value of x
        """
        
      
        # checking if any field is empty
        if fx=="" or min=="" or max=="" :
            raise ValueError(self.emptyField_error)
       
         # checking func validation
        
        try:
             pattern = re.compile("^(-)?((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?)([-\+]((\d([*\/][xX])?)*|(([xX])(\^\d)?)|((\d)*[*\/][xX])(\^\d)?))*$")
             if  not (re.search(pattern , fx)):             
              raise ValueError(self.invalidfunc_expression_error)
              
        except ValueError:
              raise ValueError(self.invalidfunc_expression_error)
              
          

        #checking if max and min are numbers 
        if not(self.is_number(min) and self.is_number(max)):
            raise ValueError(self.nonNumericvalue_error)
        
      
        #checking max and min range 
        if float(max) < float(min) :
            raise ValueError( self.minisGreater_error)

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False   
            