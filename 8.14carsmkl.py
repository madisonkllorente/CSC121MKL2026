#8.14 Cars MKL
def make_car(manufacturer, model, **details):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    
    for key, value in details.items():
        car[key] = value
        
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)