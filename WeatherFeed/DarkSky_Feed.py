import pyodbc



CREATE TABLE current_conditions(
ozone numeric,
temperature numeric,
dewPoint numeric,
nearestStormDistance numeric,
cloudCover numeric,
humidity numeric,
nearestStormBearing numeric,
summary text,
apparentTemperature numeric,
pressure numeric,
windSpeed numeric,
precipProbability numeric,
visibility numeric,
time numeric,
windBearing numeric,
precipIntensity numeric,
icon text,
);

CREATE TABLE hourly_forecasts(
ozone numeric, 
temperature numeric, 
icon text,
dewPoint numeric,
humidity numeric,
visibility numeric,
summary numeric,
apparentTemperature numeric,
pressure numeric,
windSpeed numeric,
cloudCover numeric,
time bigint,
windBearing numeric,
precipIntensity numeric,
precipProbability numeric,
);
