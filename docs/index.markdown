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


#### **📅 Planificación Inteligente**
- **Gestión de turnos y puestos:** Crea turnos personalizados, asigna empleados a puestos de trabajo y añade colores para facilitar su identificación en el calendario.
- **Copia de turnos anteriores:** Optimiza la planificación copiando los turnos de semanas previas, ahorrando tiempo y esfuerzo.  
- **Gestíon de solicitudes:** Los gerentes pueden aceptar o rechazar solicitudes de días libres, asegurando una planificación efectiva según las necesidades del equipo.  
- **Turnos abiertos:** Crea turnos disponibles para cubrir bajas o picos de demanda, y permite que los empleados los acepten directamente desde su interfaz.

#### **🕒 Mi Horario Personalizado**
- **Calendario interactivo:** Consulta horarios asignados con vistas diaria, semanal o mensual, y solicita días libres (con visualización de días disponibles restantes). 
- **Gestión de turnos abiertos:** Los empleados pueden visualizar y aceptar turnos abiertos, adaptando su planificación personal a las necesidades de la empresa.
- **Seguimiento de solicitudes:** Envía y gestiona solicitudes de días libres por motivos personales, enfermedad o vacaciones, con seguimiento de su estado (pendiente, aceptada o rechazada). 

#### **📈 Informes Automatizados**
- **Generación de informes detallados:** Obtén reportes sobre horas trabajadas, días laborados y costes asociados, organizados por empleado, semana o mes. 
- **Nominas:** Genera informes exportables para facilitar la elaboración de las nóminas de los empleados. 
- **Control y análisis:** Detecta posibles conflictos, como ausencias o solapamientos de turnos, y optimiza futuras planificaciones en base a datos históricos y patrones de demanda.  

---
### **¿Qué hace único a este sistema?**
1. **Optimización automática:** La opción de copiar turnos y generar planificaciones basadas en datos históricos ahorra tiempo y mejora la eficiencia.
2. **Conexión integral:** El sistema conecta la planificación de los gerentes con el horario personal de los empleados, mejorando la coordinación. 
3. **Notificaciones:** Los empleados reciben alertas instantáneas sobre solicitudes de días libres, turnos abiertos o cambios en su horario.

---

### 🗺️ MAPA MÓDULO
El módulo se divide en tres secciones principales: **'Planificación'**, **'Mi Horario'** e **'Informes'**. La sección de **'Planificación'** está destinada exclusivamente a los gerentes. En ella, tienen la capacidad de crear turnos o puestos de trabajo y aceptar las **solicitudes** de días libres de los empleados bajo su supervisión (según el organigrama empresarial, cada empleado tiene asignado un mentor o administrador responsable de manejar dichas solicitudes). Además, se incluye la opción de copiar los turnos de semanas anteriores, lo que facilita el trabajo y lo hace más eficiente y automatizado.

Por otro lado, **'Mi Horario'** es una herramienta accesible para todos los empleados. A través de esta sección, los empleados pueden consultar su horario personal, ver los turnos abiertos y aceptarlos si lo desean. También tienen la posibilidad de solicitar días libres por motivos personales, enfermedad o vacaciones. Esta sección mejora la organización de los turnos y fomenta una mejor coordinación entre los miembros del equipo. Asimismo, ofrece una visualización en formato de calendario con vistas diaria, semanal y mensual.

Finalmente, en el apartado de **'Informes'** se pueden consultar las horas asignadas totales de todos los empleados, los días trabajados y el coste de las horas laboradas. Además, es posible generar informes detallados sobre las horas totales trabajadas y enviarlos a la gestoría, por ejemplo, para la elaboración de las nóminas.

<div style="text-align: center; margin: 20px;">
  <img src="img/mapas_gestion.png" alt="Mapa" style="width: 80%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

---

### 🖼️ WIREFRAMES

#### Wireframe 01

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
      El wireframe del tab <strong>'Planificación'</strong> en la sección de <strong>'Turnos'</strong> está diseñado específicamente para los gerentes. Este <strong>mockup</strong> ilustra cómo se verá la página, mostrando un calendario que permite visualizar los turnos organizados por empleados, puestos o ubicaciones.

      Desde esta página, será posible crear nuevos turnos y gestionar las solicitudes de días libres de los empleados a cargo. Además, para facilitar y agilizar el proceso, se incluirá la opción de copiar los turnos de la semana anterior, optimizando así el tiempo de planificación.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
    <img src="img/wireframe_plan_turnos.png" alt="Wireframe planificación / turnos" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 02
<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
<div style="flex: 1; margin-right: 20px; text-align: justify;">
    El wireframe de la pestaña <strong>'Planificación'</strong>, en la sección de <strong>'Turnos'</strong>, incluye la función <strong>'Crear turno'</strong>. Este <strong>mockup</strong> ilustra cómo se vería la ventana emergente que permite crear un nuevo turno. En esta página, se solicitarán diversos datos necesarios, como el puesto, el empleado, la ubicación y la fecha del turno. Aqui, útilizaremos la base de datos del modulo de 'Empleados' para poder tener disponible los empleados.

    Además, se incluirá la opción de guardar el turno como plantilla para futuras planificaciones o configurarlo para que se repita tantas veces como sea necesario, optimizando así la gestión de los turnos.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
    <img src="img/crearwireframe_plan_turnos.png" alt="Wireframe crear turno" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

#### Wireframe 03
<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
      El wireframe de la pestaña <strong>'Planificación'</strong>, en la sección de <strong>'Puestos'</strong>, está diseñado para añadir nuevos puestos y asignarles un color, lo que facilitará su reconocimiento en la visualización del calendario.

      Esta vista también permite consultar los empleados asignados a cada puesto, información que proviene de las asignaciones realizadas previamente durante la creación de turnos.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
    <img src="img/wireframe_plan_puesto.png" alt="Wireframe planificación / puestos" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 04
<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
      El wireframe de la pestaña <strong>'Mi Horario'</strong> está diseñado para proporcionar a los empleados una visión clara y organizada de sus turnos. En esta sección, el empleado puede visualizar su horario en un calendario interactivo, solicitar días libres (y, a su vez, consultar cuántos días disponibles le quedan), así como ver los turnos abiertos que puede aceptar y añadir a su planificación personal.

      Al igual que en los otros calendarios, se ofrece la opción de visualizar el horario en vistas de día, semana o mes, facilitando una gestión más eficiente de los turnos.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
    <img src="img/wireframe_mi_horario.png" alt="Wireframe mi horario" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>


#### Wireframe 05
<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
      El wireframe de la pestaña <strong>'Informes'</strong> está diseñado para proporcionar una visión detallada de las horas totales trabajadas en toda la empresa, así como del coste asociado a esas horas. Esta información se puede visualizar por mes o incluso por semana, ofreciendo flexibilidad en el análisis.

      A partir de estos datos, será posible generar informes que posteriormente podrán ser utilizados para la elaboración de las nóminas de los empleados, facilitando así la gestión administrativa.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
    <img src="img/wireframe_informes.png" alt="Wireframe informes" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

---

### 🔄 DIAGRAMAS DE FLUJO

El diagrama de flujo ilustra las distintas partes del módulo. En primer lugar, se presenta el flujo correspondiente a los gerentes (**'Planificación' e 'Informes'**). Desde la sección de 'Planificación', los gerentes pueden crear turnos o puestos y añadirlos manualmente a la planificación, o bien copiarlos de semanas anteriores. Estas acciones actualizan automáticamente la planificación general. Desde la sección de 'Informes', los gerentes pueden generar reportes de las horas trabajadas y enviarlos para su posterior uso, como en la elaboración de nóminas.

<div style="text-align: center; margin: 20px;">
  <img src="img/2flux.gestion1.png" alt="Flowchart planificación" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

Por otro lado, el flujo de la pestaña **'Mi Horario'** muestra cómo se conecta con la planificación de los gerentes. En esta sección, los empleados pueden solicitar días libres, mientras que los gerentes tienen la capacidad de aceptar o rechazar dichas solicitudes. Además, los empleados pueden visualizar los turnos abiertos y aceptarlos para incorporarlos a su planificación personal.

<div style="text-align: center; margin: 20px;">
  <img src="img/flux.gestion1.png" alt="Flowchart planificación" style="width: 70%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
</div>

--- 

### <img src="img/image.png" alt="alt text" width="25" height="25"> ESQUEMA RELACIONAL DE LAS NUEVAS TABLAS

<div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px;">
  <div style="flex: 1; margin-right: 20px; text-align: justify;">
      Este esquema relacional muestra cómo se vinculan las nuevas tablas de la base de datos del módulo. En él se pueden identificar cinco tablas que interactúan entre sí, dependiendo de las acciones realizadas dentro del módulo.

      Como se mencionó anteriormente, será necesario enlazar el módulo de 'Empleados' para poder utilizar sus tablas en la creación de turnos y puestos de trabajo, garantizando así una integración completa.
  </div>
  <div style="flex: 0 0 55%; text-align: center;">
    <img src="img/data_base_gestión.png" alt="Esquema de la base de datos" style="width: 100%; height: auto; border: 2px solid #ccc; border-radius: 5px;">
  </div>
</div>

--- 

### 🔒 CONTROL DE ACCESO

**Grupos de usuarios:**  
1. **Administradores**  
2. **Empleados**  

**Acceso al módulo:**  
- **Todos los usuarios** tienen acceso al módulo en general.

**Accesos y permisos por grupo:**  
- **Administradores**  
  - Acceso completo a los módulos **‘Planificación’** y **‘Mi Horario’**.  
  - Permiso de **lectura y escritura** en todos los módulos, lo que les permite modificar y gestionar los datos de todos los registros.

- **Empleados**  
  - Acceso limitado a los módulos **‘Mi Horario’** y **‘Planificación’**.  
  - **‘Mi Horario’**: acceso de **lectura y escritura**, lo que les permite consultar su horario, solicitar días libres o ampliar su horario de trabajo, pero sin poder modificar directamente los turnos asignados.  
  - **‘Planificación’**: acceso de **lectura** únicamente, permitiéndoles visualizar los turnos sin capacidad para editarlos.

---

#### Enlace repositorio
[github.com/alyraluca/Gestion_Turnos](https://github.com/alyraluca/Gestion_Turnos)