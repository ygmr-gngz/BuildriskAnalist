from abc import ABC, abstractmethod

class IRiskModel(ABC):
    @abstractmethod
    def load_model(self):
        """Model dosyasını yükler"""
        pass

    @abstractmethod
    def predict(self, data):
        """Veri ile tahmin yapar"""
        pass