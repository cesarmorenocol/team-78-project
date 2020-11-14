import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from model.data_access import DataAccess

class MapAnalysis():

    variable = 'Leq'
    measure = 'Valor_mean'
    data = DataAccess()
    
    def get_map_figure(self, dataframe, frame):
        figure_map = px.density_mapbox(dataframe[dataframe['Variable'] == self.variable], 
                                         lat='latitude', lon='longitude', z = self.measure,
                                         radius=50,
                                         animation_group = 'Estación',
                                         animation_frame  = frame,
                                         hover_name = 'Estación',
                                         color_continuous_scale = 'Jet',
                                         opacity=0.9
                                         )
        
        figure_map.update_layout(mapbox_style="open-street-map",
                                 mapbox_zoom=9.5,
                                 mapbox_center = {"lat": 4.60971, "lon": -74.08175})
        
        figure_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return figure_map;
    
    def get_hourly_map(self):
        figure = self.get_map_figure(self.data.df_hour, 'Hora')
        return figure

    def get_dayly_map(self):
        figure = self.get_map_figure(self.data.df_day, 'Dia')
        return figure