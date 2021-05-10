import justpy as jp
import pandas as pd
from datetime import datetime 
from pytz import utc 

data=pd.read_csv('reviews.csv',parse_dates=['Timestamp'])
data['Week']=data['Timestamp'].dt.strftime("%Y-%U")
week_average=data.groupby(['Week']).mean() 

chart_def="""
 {
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day and year'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} Day: {point.y} AvR'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
} 
"""

def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis of Course Reviews",classes="text-h3 text-center q-pa-md")
    hc=jp.HighCharts(a=wp,options=chart_def)

    hc.options.title.text="Average rating by day"
    
    hc.options.xAxis.categories=list(week_average.index)
    hc.options.series[0].data=list(week_average['Rating'])
    return wp

jp.justpy(app) 
