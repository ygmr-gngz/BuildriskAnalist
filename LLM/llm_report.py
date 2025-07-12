import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class GPTExplainer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.history = []  

    def generate_explanation(self, input_data: dict, risk_label: str) -> str:
        prompt = self._build_prompt(input_data, risk_label)

        # 🗣️ Yeni kullanıcı mesajını geçmişe ekle
        self.history.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": (
                        "Sen bir deprem sonrası yapı risk analizi uzmanısın. "
                        "Kullanıcıdan gelen bina verilerine göre risk seviyesini değerlendir "
                        "ve kararını teknik detaylarla açıkla."
                    )},
                    *self.history 
                ],
                temperature=0.7,
                max_tokens=500,
            )

            output = response.choices[0].message.content.strip()

           
            self.history.append({"role": "assistant", "content": output})
            return output

        except Exception as e:
            return f"GPT-4o ile açıklama oluşturulurken hata oluştu: {str(e)}"

    def _build_prompt(self, input_data, risk_label):
        return (
            f"Aşağıda verilen bina bilgilerine göre yapının deprem sonrası risk durumunu değerlendir:\n\n"
            f"- Kat sayısı: {input_data['kat']}\n"
            f"- Bina yaşı: {input_data['bina_yasi']}\n"
            f"- Yapı türü: {input_data['yapi_turu']}\n"
            f"- Zemin sınıfı: {input_data['zemin_sinifi']}\n"
            f"- Deprem bölgesi: {input_data['deprem_bolgesi']}\n\n"
            f"Modelin verdiği risk sonucu: {risk_label.upper()}\n\n"
            f"Lütfen bu kararı teknik gerekçelerle açıklayan bir analiz üret."
        )




