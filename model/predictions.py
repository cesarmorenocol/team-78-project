import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from model.data_access import DataAccess

class Predictions():
    data = DataAccess()
    stations = data.predictions.Estación.unique()
    
    def get_noise_level(self, station):
        station_df = self.data.predictions[self.data.predictions.Estación == station]
        fig = make_subplots(rows=1, cols = 7, shared_yaxes=True, 
                            x_title = 'Hour',
                            y_title = 'Noise: Average in decibels (dB)')
        _row = 1
        days = {1:'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        
        for week_day in [1,2,3,4,5,6,7]:
            column = week_day
            small_df = station_df[(station_df.weekday == week_day)]
            fig.add_trace(go.Bar(x = small_df["Hora"], 
                                 y = small_df["ruido_pred"], 
                                 name = str(days[week_day])),
                                 row = _row,
                                 col = column)
            fig.update_layout(xaxis_title = 'Hour')
            fig.update_layout(yaxis = dict(range = [station_df.ruido_pred.min(), station_df.ruido_pred.max()]))
            
        return fig
    
    def get_map_predictions(self, dataframe, animation, title):
        fig = px.scatter_mapbox(dataframe,
                                lat = "latitud",
                                lon = "longitud",
                                color = 'ruido_pred',
                                size = 'ruido_pred',
                                color_continuous_scale = 'Jet',
                                hover_name = "Estación",
                                size_max = 18,
                                zoom = 10,
                                animation_group = 'Estación',
                                animation_frame = animation,
                                title = title)

        fig.update_layout (mapbox_style = "stamen-toner",
                           mapbox_zoom = 10,
                           mapbox_center = { "lat":4.65 ,"lon":-74.08175 },
                           hoverlabel = dict (bgcolor = "#6c757d",
                                              font_size = 12,
                                              font_family = "Segoe UI"))

        fig.update_layout(margin = {"r":0, "t":32, "l":0, "b":0})
        return fig
    
    def get_hour_predictions_map(self):
        return self.get_map_predictions(self.data.predictions,'Hora','Average Noise per hour')
        
    def get_day_predictions_map(self):
        return self.get_map_predictions(self.data.predictions.sort_values('weekday'),
                                   'weekday', 'Average Noise by Day of the Week')
        