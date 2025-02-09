from products.models import Product
import openai
from django.conf import settings
from anthropic import Anthropic

class AiChatService:
    @staticmethod
    def get_product_info():
        products = Product.objects.all()
        inventory_summary = ", ".join([f"{p.name} ({p.stock} disponibles)" for p in products])
        return f"Actualmente tenemos: {inventory_summary}."
    
    @staticmethod
    def ask_ai(message):
        try:
            prompt = f"El usuario pregunta: {message}. Responde usando estos datos: {AiChatService.get_product_info()}"
            openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

            response = openai_client.chat.completions.create(
                # model="gpt-3.5-Turbo",
                model="text-embedding-3-small",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response.choices[0].message.content
        except openai.RateLimitError:
            return "Lo siento, el servicio de AI no está disponible en este momento. Por favor, contacta al soporte."
        except Exception as e:
            return f"Error inesperado: {str(e)}"