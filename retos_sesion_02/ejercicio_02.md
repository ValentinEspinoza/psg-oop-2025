Una vinoteca quiere registrar los vinos y quesos que ofrecen.
De cada vino se necesita registrar su nombre, tipo, cepa y 
año de producción.
De cada queso se necesita registrar su nombre, variedad, 
edad y si lleva sal.
La vinoteca tiene en su inventario 4 vinos y 3 quesos 

- Realiza el análisis y diseño de las clases Vino y Queso
- Escribe el codigo en Python para crear la clases Vino y Queso
- Instancia los 4 vinos y 3 quesos con sus respectivos atributos

Requisitos:
- Registrar nombre 
- Registrar tipo
- Registrar cepa
- Registrar año de producción
- Registrar variedad
- Registrar edad
- Registrar si lleva sal


Objetos:
- Vinos
- Quesos
Características:
- Vinos
    - nombre
    - tipo
    - cepa
    - año de producción
- Quesos
    - nombre
    - variedad
    - edad
    - contiene sal

Acciones:
- (No hay acciones)

```mermaid
classDiagram
    class Vino {
        String nombre
        String tipo
        String cepa
        int año produccion
    }
      class Queso {
        String nombre
        String variedad
        String edad
        bool contiene sal
    }
```
