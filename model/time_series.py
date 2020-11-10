import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from model.data_access import DataAccess

class TimeSeriesAnalysis():
    
    data = DataAccess()
    stations = data.df_hour['Estación'].unique()
    
    # data for the 15 days figure
    dataframe = data.dfp.copy()
    dataframe['Fecha'] = dataframe['Fecha'].apply(lambda x: pd.to_datetime(x,format='%Y-%m-%d  %H:%M:%S'))
    dataframe['Valor_max'] = pd.to_numeric(dataframe['Valor_max'])
    dataframe['Valor_mean'] = pd.to_numeric(dataframe['Valor_mean'])
    dataframe['Valor_min'] = pd.to_numeric(dataframe['Valor_min'])
    
    def get_bar_figure(self):
        df_h = self.data.df_hour.copy()
        df = df_h.loc[df_h['Variable'] == 'Leq']
        dfa = df.groupby(['Hora','Variable']).mean().reset_index()
        dfa['Estación'] = 'Todas las estaciones'
        df = pd.concat([dfa[dfa.columns.to_list()], df])

        fig_bars_day = go.Figure()
        # set up ONE trace
        fig_bars_day.add_trace(go.Bar(x = df['Hora'],
                             y = df['Valor_mean'].loc[df['Estación'] == 'Todas las estaciones'], visible=True))

        buttons = []
        diy = {"title": "Noise Level Leq [db]", 'range': [0, 65]}
        fig_bars_day.layout.yaxis = diy
        dix = {"title": "Hour"}
        fig_bars_day.layout.xaxis = dix
        dia = {'text': 'test'}

        # Step 1 - adjust margins to make room for the text
        fig_bars_day.update_layout(margin = dict(t = 150))
        fig_bars_day.add_annotation(dict(font=dict(color = "black", size = 13),
                                x = 'a',
                                y = 1.08,
                                showarrow = False,
                                text = 'Select station of interest',
                                textangle = 0,
                                xref = "paper",
                                yref = "paper"
                                ))

        # Build dropdown on figure:
        for estacion in df['Estación'].unique():
            buttons.append(dict(method = 'update',
                                label = estacion,
                                visible = True,
                                args=[{'y': [df['Valor_mean'].loc[df['Estación'] == estacion]],
                                       'x': [df['Hora']],
                                       'type': 'bar'},
                                      {'xaxis': dix,
                                       'yaxis': diy}, [0]],
                                )
                           )

        # some adjustments to the updatemenus
        updatemenu = []
        your_menu = dict()
        updatemenu.append(your_menu)
        updatemenu[0]['buttons'] = buttons
        updatemenu[0]['direction'] = 'down'
        updatemenu[0]['showactive'] = True

        # add dropdown menu to the figure
        fig_bars_day.update_layout(showlegend = False, updatemenus = updatemenu)
        return fig_bars_day
    
    def get_time_series_figure(self, cai, variable, medida):
        df_cai = self.data.df_date[(self.data.df_date.Estación == cai)]
        fig_day_series = go.Figure()
        fig_day_series.add_trace(go.Scatter(x = df_cai['Fecha_Dia'],
                                 y = df_cai[df_cai.Variable == variable][medida],
                                 name = cai,
                                 line = dict(color = 'blue', width = 1)))

        fig_day_series.update_layout(
                           xaxis_title='Date',
                           yaxis_title='Noise average / Day')

        fig_day_series.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count = 1, label = '1m', step = 'month', stepmode = 'backward'),
                    dict(count = 6, label = '6m', step = 'month', stepmode = 'backward'),
                    dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
                    dict(count = 1, label = '1y', step = 'year', stepmode = 'backward'),
                    dict(step = 'all')
                ])) )
        
        return fig_day_series
    
    def get_15_days_figure(self, cai):
        if cai == 'Todas las estaciones':
            dataframe2 = self.dataframe.groupby(['Fecha','Variable']).mean().reset_index()
            return px.line(DFP2, x = "Fecha", y = ["Valor_mean"], color = "Variable")

        else:
            dataframe2 = self.dataframe[self.dataframe['Estación'] == cai]
            return px.line(dataframe2, x = 'Fecha', y = ['Valor_mean'], color ='Variable')
            