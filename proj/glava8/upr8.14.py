def car_info(name_manufacturer, name_model, **kwargs):
	kwargs['name_manufacturer'] = name_manufacturer
	kwargs['name_model'] = name_model
	return kwargs


cars_info = car_info('subaru', 'outback', color='blue', tow_package=True)
print(cars_info)
