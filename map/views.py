from django.views.generic import TemplateView
from django.shortcuts import render
from results.models import Result
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import os

mapbox_access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')

# Create your views here.
class MapPageView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super(MapPageView, self).get_context_data(**kwargs)

        px.set_mapbox_access_token(mapbox_access_token)

        df = pd.DataFrame.from_records(Result.objects.all().values('As', 'cd', 'cr', 'cu', 'mn', 'pb', 'ni', 'zn', 'rand_lat', 'rand_long'))
        df['As'] = pd.to_numeric(df['As'], errors='coerce')
        df = df.replace('ND', 0, regex=True)
        df = df.astype(float)

        figure = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'As', custom_data = ['As', 'cd', 'cr', 'cu', 'mn', 'pb', 'ni', 'zn'], color_continuous_scale = px.colors.cyclical.IceFire, size_max = 15, zoom = 10, range_color = (0, 1000), labels = {'As': 'Element Concentration (ppm)'}, center = {'lat': 51.6214, 'lon': -3.9436})
        figure1 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'cd', custom_data = ['cd'], labels = {'cd': 'Cadmium'})
        figure2 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'cr', custom_data = ['cr'])
        figure3 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'cu', custom_data = ['cu'])
        figure4 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'mn', custom_data = ['mn'])
        figure5 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'pb', custom_data = ['pb'])
        figure6 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'ni', custom_data = ['ni'])
        figure7 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = 'zn', custom_data = ['zn'])
        figure8 = px.scatter_mapbox(df, lat = 'rand_lat', lon = 'rand_long', color = ((df['As'] + df['cd'] + df['cr'] + df['cu'] + df['mn'] + df['pb'] + df['ni'] + df['zn'])/8), custom_data = ['As', 'cd', 'cr', 'cu', 'mn', 'pb', 'ni', 'zn'])


        figure.add_trace(figure1.data[0])
        figure.add_trace(figure2.data[0])
        figure.add_trace(figure3.data[0])
        figure.add_trace(figure4.data[0])
        figure.add_trace(figure5.data[0])
        figure.add_trace(figure6.data[0])
        figure.add_trace(figure7.data[0])
        figure.add_trace(figure8.data[0])

        figure.update_traces(hovertemplate="Arsenic: %{customdata[0]} ppm <br>Cadmium: %{customdata[1]} ppm <br>Chromium: %{customdata[2]} ppm <br>Copper: %{customdata[3]} ppm <br>Manganese: %{customdata[4]} ppm <br>Lead: %{customdata[5]} ppm <br>Nickel: %{customdata[6]} ppm <br>Zinc: %{customdata[7]} ppm")
        
        hovertemplate = 'Arsenic: %{customdata[0]} ppm <br>Cadmium: %{customdata[1]} ppm <br>Chromium: %{customdata[2]} ppm <br>Copper: %{customdata[3]} ppm <br>Manganese: %{customdata[4]} ppm <br>Lead: %{customdata[5]} ppm <br>Nickel: %{customdata[6]} ppm <br>Zinc: %{customdata[7]} ppm'
        hovertemplate_arsenic = 'Arsenic: %{customdata[0]} ppm'
        hovertemplate_cadmium = 'Cadmium: %{customdata[0]} ppm'
        hovertemplate_chromium = 'Chromium: %{customdata[0]} ppm'
        hovertemplate_copper = 'Copper: %{customdata[0]} ppm'
        hovertemplate_manganese = 'Manganese: %{customdata[0]} ppm'
        hovertemplate_lead = 'Lead: %{customdata[0]} ppm'
        hovertemplate_nickel = 'Nickel: %{customdata[0]} ppm'
        hovertemplate_zinc = 'Zinc: %{customdata[0]} ppm'

        figure.update_layout(
            updatemenus = [
                dict(
                    buttons=list([
                        dict(
                            label = 'All Elements',
                            method = 'update',
                            args = [{'visible': [False, False, False, False, False, False, False, False, True], 'hovertemplate': hovertemplate, 'labels': 'All'}]),
                        dict(
                            args = [{'visible': [True, False, False, False, False, False, False, False, False], 'hovertemplate': hovertemplate_arsenic, 'marker_colorbar_title_text': 'Arsenic'}],
                            label = 'Arsenic',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, True, False, False, False, False, False, False, False], 'hovertemplate': hovertemplate_cadmium, 'labels': 'cd'}],
                            label = 'Cadmium',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, False, True, False, False, False, False, False, False], 'hovertemplate': hovertemplate_chromium}],
                            label = 'Chromium',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, False, False, True, False, False, False, False, False], 'hovertemplate': hovertemplate_copper}],
                            label = 'Copper',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, False, False, False, True, False, False, False, False], 'hovertemplate': hovertemplate_manganese}],
                            label = 'Manganese',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, False, False, False, False, True, False, False, False], 'hovertemplate': hovertemplate_lead}],
                            label = 'Lead',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, False, False, False, False, False, True, False, False], 'hovertemplate': hovertemplate_nickel}],
                            label = 'Nickel',
                            method = 'update',
                        ),
                        dict(
                            args = [{'visible': [False, False, False, False, False, False, False, True, False], 'hovertemplate': hovertemplate_zinc}],
                            label = 'Zinc',
                            method = 'update',
                        ),
                    ]),
                    direction = 'down',
                    pad = {'r': 10, 't': 10},
                    showactive=True,
                    x=0.1,
                    xanchor='left',
                    y=1.08,
                    yanchor='top',
                ),
            ],
        ),

        context['map'] = figure.to_html()

        return context

    

    

    

    


    

    
