import pandas as pd
import numpy as np
from datetime import datetime
from interfaces.ISensorStream import ISensorStream

class SyntheticSensorStream(ISensorStream):
    def __init__(self, start_time=datetime.now(), periods=96):
        self.start_time = start_time
        self.periods = periods  # 96 veri = 1 gün (15 dakikalık aralıklarla)

    def generate(self):
        timestamps = pd.date_range(start=self.start_time, periods=self.periods, freq="15min")
        data = {
            "timestamp": timestamps,
            "nem": np.random.normal(20, 2, size=self.periods),
            "sicaklik": np.random.normal(23, 1.5, size=self.periods),
            "sismik": np.random.normal(0.01, 0.005, size=self.periods)
        }
        return pd.DataFrame(data)