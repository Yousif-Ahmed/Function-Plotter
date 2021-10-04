from Validate import Validate
import pytest




def test1_empty_field():
   
    fx =""
    min ="5"
    max ="10"
    with pytest.raises(ValueError , match ="Fill all Fields with information"):
        Validate(fx , min ,max) 

def test2_empty_field():
   
    fx =""
    min =""
    max =""
    with pytest.raises(ValueError , match ="Fill all Fields with information"):
        Validate(fx , min ,max) 

def test3_empty_field():
   
    fx =""
    min ="5"
    max =""
    with pytest.raises(ValueError , match ="Fill all Fields with information"):
        Validate(fx , min ,max) 


def test1_numeric_value():
    fx="x+5"
    min="y"
    max="z"  
    
    with pytest.raises(ValueError , match ="Fill minimum and maximum Fields with numeric values"):
        Validate(fx , min , max)

def test2_numeric_value():
    fx="x+5"
    min="&*"
    max="z"  
    
    with pytest.raises(ValueError , match ="Fill minimum and maximum Fields with numeric values"):
        Validate(fx , min , max)

def test3_numeric_value():
    fx="x+5"
    min="&*"
    max="klk%$#"  
    
    with pytest.raises(ValueError , match ="Fill minimum and maximum Fields with numeric values"):
        Validate(fx , min , max)       

def test1_invalid_expression():
    fx="x+5\4"
    min="5"
    max="10"

    with pytest.raises(ValueError , match ="invalid function expression"):
        Validate(fx , min , max)

def test2_invalid_expression():
    fx="x+5!!4"
    min="5"
    max="10"

    with pytest.raises(ValueError , match ="invalid function expression"):
        Validate(fx , min , max)

def test3_invalid_expression():
    fx="x+5$@4"
    min="5"
    max="10"

    with pytest.raises(ValueError , match ="invalid function expression"):
        Validate(fx , min , max)


def test_Max_Min_value():
    fx="x+5"
    min="10"
    max="5"  

    
    with pytest.raises(ValueError , match ="Maximum Value should be greater than minimum value"):
        Validate(fx , min , max)


            

    
    







    


