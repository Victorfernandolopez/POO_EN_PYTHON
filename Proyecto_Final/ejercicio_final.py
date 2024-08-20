"""
CHATBOT ANALIZADOR DE SENTIMIENTOS

En este proyecto, podrias desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y nos responda cual es el sentimiento.
Este proyecto te daria la oportunidad de trabajar con varios aspectos de la programacion orientada a objetos (POO), modulos, API, analisis de datos etc...
"""
from textblob import TextBlob
from abc import ABC, abstractmethod

# S: Principio de Responsabilidad Única (SRP)
# Esta interfaz define un contrato para cualquier clase que realice análisis de sentimientos.
class AnalizadorSentimientos(ABC):
    @abstractmethod
    def analizar_sentimiento(self, texto):
        pass

# L: Principio de Sustitución de Liskov (LSP)
# Esta clase concreta implementa el análisis de sentimientos usando TextBlob.
class AnalizadorTextBlob(AnalizadorSentimientos):
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutro"
        else:
            return "negativo"

# O: Principio de Abierto/Cerrado (OCP)
# La clase ServicioAnalisisSentimientos está abierta a la extensión (puede utilizar diferentes analizadores) pero cerrada a la modificación.
class ServicioAnalisisSentimientos:
    def __init__(self, analizador: AnalizadorSentimientos):
        self.analizador = analizador

    def analizar(self, texto):
        return self.analizador.analizar_sentimiento(texto)

# I: Principio de Segregación de Interfaces (ISP)
# No se aplica explícitamente en este ejemplo ya que la interfaz es muy específica.

# D: Principio de Inversión de Dependencia (DIP)
# Dependemos de una abstracción (AnalizadorSentimientos) en lugar de una implementación concreta (AnalizadorTextBlob).
analizador = AnalizadorTextBlob()
servicio = ServicioAnalisisSentimientos(analizador)
resultado = servicio.analizar("this is funny")
print(resultado)