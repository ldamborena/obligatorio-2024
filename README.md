# Simulador de Gremio de Aventureros (Dungeons & Dragons)

Realizamos un simulador inspirado en Dungeons & Dragons,cuya finalidad es la de gestionar un gremio de aventureros. Esta aplicación permite registrar diferentes tipos de aventureros (Guerrero, Mago, y Ranger), asignarles misiones, y consultar datos sobre el gremio. Fue realizado en Python y se ejecuta mediante una interfaz interactiva en la terminal.

## Características

- **Registrar Aventureros**: Agrega aventureros de clase Guerrero, Mago o Ranger, especificando atributos como puntos de habilidad, experiencia, dinero y atributos adicionales según la clase.
- **Registrar Misiones**: Crea misiones con distintos rangos de dificultad y recompensa. Las misiones pueden ser individuales o grupales.
- **Realizar Misiones**: Asigna misiones a aventureros, validando que cumplan con los requisitos necesarios para completarlas.
- **Consultas de Información**: Visualiza el Top 10 de aventureros con más misiones resueltas, aventureros con mayor habilidad, y el Top 5 de misiones con mayor recompensa.

## Diagrama UML 

Aventurero es la clase base abstracta que define atributos comunes (nombre, puntos de habilidad, experiencia, etc.) y métodos como calcular_habilidad(). Esta se especializa en tres subclases: Guerrero (con fuerza), Mago (con mana) y Ranger (que puede tener una mascota, representada por la clase Mascota). Las misiones se modelan con la clase abstracta Mision, que tiene dos derivadas: MisionIndividual (para un aventurero) y MisionGrupal (con un mínimo de participantes). Las relaciones incluyen herencia entre clases principales, composición entre Ranger y Mascota, y asociación entre Aventurero y Mision. 

## Ejecución

1) Clonar el repositorio:

git clone https://github.com/ldamborena/obligatorio-2024
cd <obligatorio-2024>

2) Ejecutar el archivo principal (main.py):

   python main.py

3) Parámetros de entrada o configuración.Por ejemplo:

Se observa como main.py pide al usuario que introduzca un aventurero y una misión.
Elige un tipo de aventurero (Guerrero, Mago, Ranger).
Introduce las características de la misión (rango, recompensa, etc.).


   

