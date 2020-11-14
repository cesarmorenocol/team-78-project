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
    
    def get_bar_figure(self, cai):
        df_h = self.data.df_hour.copy()
        df = df_h.loc[df_h['Variable'] == 'Leq']
        dfa = df.groupby(['Hora','Variable']).mean().reset_index()
        dfa['Estación'] = 'Todas las estaciones'
        df = pd.concat([dfa[dfa.columns.to_list()], df])

        # # plotly
        fig_bars_day = go.Figure()
        fig_bars_day.add_trace(go.Bar(x = df['Hora'],
                                 y = df['Valor_mean'].loc[df['Estación'] == cai],
                                 name = 'Leq',
                                 marker_color = px.colors.qualitative.Alphabet,
                                 visible = True))

        updatemenu = []
        buttons = []

        diy = {"title": "Noise Level Leq [db]",'range':[0,65]}
        fig_bars_day.layout.yaxis = diy
        dix = {"title": "Hour"}
        fig_bars_day.layout.xaxis = dix
        dia = {'text':'test'}
        fig_bars_day.update_layout(title_text = 'Noise distribution during a day')
        fig_bars_day.update_layout(margin = dict(t = 150))

        # button with one option for each dataframe
        for estacion in df['Estación'].unique():
            buttons.append(dict(method = 'update',
                                label = estacion,
                                visible = True,
                                args = [{'y': [df['Valor_mean'].loc[df['Estación'] == estacion]],
                                         'x': [df['Hora']],
                                         'type': 'bar',
                                         'hover_name': 'Hora'},
                                        {"xaxis": dix, "yaxis": diy}
                                     ],
                                ))
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
            