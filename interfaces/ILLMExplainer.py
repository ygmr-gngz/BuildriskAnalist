# interfaces/ILLMExplainer.py
from abc import ABC, abstractmethod

class ILLMExplainer(ABC):
    @abstractmethod
    def generate_explanation(self, input_data: dict, prediction: str) -> str:
        pass


