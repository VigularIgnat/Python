def make_car(creater_country,model, **car_info):
    
    car_info["year_of_create"]=creater_country 
    car_info["model"]=model
    return car_info

car_subaru=make_car("subaru","outback",color="blue",tow_pacage=True )
print(car_subaru)
    
    
