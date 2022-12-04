import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from io import BytesIO
import base64
from PIL import Image

from helloworld.models import Stocks

def get_df(stocks):

    qs = Stocks.objects.filter(stock__in=stocks).values()
    df = pd.DataFrame.from_records(qs)
    df_pivot = df.pivot('date','stock','close').reset_index()
    df_pivot.head()
    return df_pivot


def get_correlation(df):
    corr_df = df.corr(method='pearson')
    corr_df.head().reset_index()
    return corr_df


def render_matrix(df):
    matrix = seaborn.heatmap(df)
    buf = BytesIO()
    fig = matrix.get_figure()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf