from pyowm import OWM

owm=OWM("c6ecf3dc4156ed917ec245734e6a1586") #we will give parameters as a API KEY

def get_forecast(lat,lon):
    observation=owm.three_hours_forecast_at_coords(lat,lon)
    forecasts=observation.get_forecast()

    location=forecasts.get_location()
    loc_name=location.get_name()
    loc_lat=location.get_lat()
    loc_lon=location.get_lon()

    results=[]

    for forecast in forecasts:
        time=forecast.get_reference_time("iso")
        status=forecast.get_status()
        detailed=forecast.get_detailed_status()
        temperature=forecast.get_temperature()
        tempAvg=temperature.get("temp")
        temp_min=temperature.get("temp_min")
        temp_max=temperature.get("temp_max")

        results.append("""
        Location :{} Lat :{} Lon :{}
        Time :{} 
        Status :{}
        Detailed :{}
        Temperature :{}
        Min Temp :{}
        Max Temp :{}
        """.format(location,loc_lat,loc_lon,time,status,
                   detailed,tempAvg,temp_min,temp_max))

    return "".join(results[:10]) #to send max 10 information
if __name__=="__main__":
    print(get_forecast(-1.2,36))
