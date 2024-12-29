---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: Gestión Turnos
subtitle: Optimiza la creación de horarios y mejora la gestión de turnos
hero_image: img/banner3.jpg 
hero_darken: true
---

### **FUNCIONALIDADES DESTACADAS**
---

---

#### **📅 Planificación Inteligente**
- **Gestión de empleados:** Añade empleados y asigna roles de trabajo con facilidad.  
- **Creación de turnos:** Diseña turnos personalizados y compártelos por correo o publícalos directamente en el calendario del equipo.  
- **Turnos abiertos:** Deja espacios libres para cubrir bajas o vacaciones, y permite que los empleados interesados soliciten horas adicionales.  

#### **🕒 Mi Horario Personalizado**
- **Vista individual:** Consulta horarios asignados y realiza solicitudes de días libres por asuntos propios, enfermedad o vacaciones.  
- **Intercambio flexible:** Los empleados pueden intercambiar turnos entre sí, perfecto para emergencias o imprevistos.  
- **Disponibilidad extra:** Deja tu disponibilidad escrita para cubrir turnos abiertos y ser notificado si surge una oportunidad.  

#### **📈 Informes Automatizados**
- **Seguimiento de horas:** Obtén reportes detallados sobre las horas trabajadas de cada empleado.  
- **Detección de conflictos:** Recibe alertas sobre ausencias, cambios de última hora o conflictos de turnos.  
- **Predicción inteligente:** El sistema optimiza la planificación del próximo mes basado en datos como demanda diaria y días festivos.  

---
### **¿Qué hace único a este sistema?**
1. **Optimización automática:** Genera turnos del mes siguiente con sugerencias basadas en historial.  
2. **Notificaciones inmediatas:** Los empleados reciben alertas en tiempo real sobre huecos en los turnos.  
3. **Análisis avanzado:** Mejora la asignación de recursos con predicciones basadas en la demanda laboral.
---
### MAPA CONCEPTUAL
El módulo se divide en dos secciones principales: **'Planificación'** y **'Mi Horario'**. La sección de **'Planificación'** está destinada únicamente a los gerentes, quienes tienen la capacidad de gestionar empleados, asignar roles y crear turnos de trabajo, ya sea de manera manual o automática. Si se elige la opción automática, el sistema sugiere turnos basándose en los datos de los meses anteriores. Los gerentes también pueden aprobar los turnos automáticos o guardar los manuales y enviarlos a los empleados correspondientes.

Por otro lado, **'Mi Horario'** es una herramienta accesible para todos los empleados. A través de ella, pueden consultar su horario personal, ver los huecos disponibles en los turnos de trabajo y solicitar cubrir alguno de estos huecos si lo desean. Además, los empleados tienen la posibilidad de solicitar días libres por motivos personales, enfermedad o vacaciones. Esta sección facilita la organización de los turnos y mejora la coordinación entre todos los miembros del equipo.

<div style="text-align: center; margin: 20px;">
  <img src="img/mapa__module1.jpg" alt="Mapa" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

### WIREFRAME

Wireframe del TAB de ‘Planificación’ de la sección de ‘Empleados’.

<div style="text-align: center; margin: 20px;">
  <img src="img/wireframe_planeacion_empleado1.jpg" alt="Wireframe planificación" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>


Wireframe del TAB de ‘Planificación’ de la sección de ‘Empleados’ y la función ‘Añadir Empleado’.

<div style="text-align: center; margin: 20px;">
  <img src="img/wireframe_planeacion_empleado2.jpg" alt="Wireframe añadir empleado" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>


Wireframe del TAB de ‘Planificación’ de la sección de ‘Turnos’.

<div style="text-align: center; margin: 20px;">
  <img src="img/wireframe_planeacion_puesto1.jpg" alt="Wireframe planificación" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

Wireframe del TAB de ‘Planificación’ de la sección de ‘Turnos’ y la función ‘Crear turno’.

<div style="text-align: center; margin: 20px;">
  <img src="img/wireframe_planeacion_puesto2.jpg" alt="Wireframe crear turno" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

Wireframe del TAB de ‘Mi Horario’.

<div style="text-align: center; margin: 20px;">
  <img src="img/wireframe_miHorario.jpg" alt="Wireframe mi horario" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>


### CONTROL DE ACCESO

1. Grupos: administradores, empleados.
2. Acceso al módulo: todos los usuarios.
3. Administradores: acceso a ‘Planificación’, ‘Mi Horario’ 
	- Permiso de lectura y escritura a todos los módulos.
4. Empleados: acceso a ‘Mi Horario’, ‘Planificación’.
	- ‘Mi Horario’: acceso de lectura.
	- ‘Planificación’: acceso de lectura.


### DIAGRAMAS DE FLUJO

Diagrama de flujo del TAB de ‘Planificación’ y ‘Mi Horario’.

<div style="text-align: center; margin: 20px;">
  <img src="img/flowchart_planeacion.jpg" alt="Flowchart planificación" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>


### ESQUEMA RELACIONAL DE LAS NUEVAS TABLAS

<div style="text-align: center; margin: 20px;">
  <img src="img/data_base_module1.jpg" alt="Esquema de la base de datos" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>
