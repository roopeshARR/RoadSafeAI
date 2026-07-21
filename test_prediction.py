from services.prediction_service import SeverityPredictor

predictor = SeverityPredictor()

sample = {
    "Day_of_week": "Monday",
    "Age_band_of_driver": "18-30",
    "Sex_of_driver": "Male",
    "Educational_level": "Junior high school",
    "Vehicle_driver_relation": "Owner",
    "Driving_experience": "5-10yr",
    "Type_of_vehicle": "Automobile",
    "Owner_of_vehicle": "Owner",
    "Service_year_of_vehicle": "2-5yrs",
    "Defect_of_vehicle": "No defect",
    "Area_accident_occured": "Urban",
    "Lanes_or_Medians": "Two-way",
    "Road_allignment": "Straight road",
    "Types_of_Junction": "No junction",
    "Road_surface_type": "Asphalt roads",
    "Road_surface_conditions": "Dry",
    "Light_conditions": "Daylight",
    "Weather_conditions": "Normal",
    "Type_of_collision": "Vehicle with vehicle collision",
    "Number_of_vehicles_involved": 2,
    "Vehicle_movement": "Going straight",
    "Pedestrian_movement": "Not a Pedestrian",
    "Cause_of_accident": "No priority to vehicle",
    "Hour": 14
}

result = predictor.predict(sample)

print(result)