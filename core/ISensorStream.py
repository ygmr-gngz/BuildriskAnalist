import pandas as pd
import numpy as np
import datetime

class SyntheticSensorStream:
    def generate(self, days=7):
        timestamps = pd.date_range(end=datetime.datetime.now(), periods=days*24, freq="H")
        values = np.random.normal(loc=0.5, scale=0.15, size=len(timestamps))
        df = pd.DataFrame({"timestamp": timestamps, "crack_sensor": values})
        return df


