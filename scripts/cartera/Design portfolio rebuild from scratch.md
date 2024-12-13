# Flujo de Trabajo para Reconstruir la Cartera

## 1. Definir la Divisa de Referencia

- El usuario especificará la **divisa de referencia** (EUR, USD o GBP) como parámetro al ejecutar el script.
- Si no se especifica ninguna divisa, se tomará **EUR** por defecto.
- Esta divisa se utilizará para estandarizar el valor total de la cartera y calcular las rentabilidades.

## 2. Cargar los Datos de los Archivos (opcional)

- El script verificará si el usuario ha proporcionado un parámetro para decidir si debe cargar los ficheros de datos (Compras/Ventas, Cambio de Divisas, Dividendos) o no.
    - **Si se deben cargar los ficheros**: El script llamará a la función `import_complete_workflow.py` para cargar los datos desde los archivos a la base de datos.
    - **Si no se deben cargar los ficheros**: El script utilizará los datos ya almacenados en la base de datos para reconstruir la cartera.

## 3. Obtener el Tipo de Cambio Actual

- Con la divisa de referencia como base, el script intentará obtener el **tipo de cambio actual** para las divisas presentes en los archivos mediante una consulta a una API de tipos de cambio.
- **En caso de no tener conexión**: 
    - El script pedirá al usuario elegir entre usar un tipo de cambio de referencia (ya guardado en la base de datos o en un archivo local) o introducir manualmente el tipo de cambio actual.

## 4. Convertir Transacciones a la Divisa de Referencia

- Cada transacción en los archivos de Compras/Ventas será convertida a la **divisa de referencia** utilizando los tipos de cambio correspondientes a la fecha de cada transacción.
- Si no se tiene conexión a Internet, el tipo de cambio ingresado manualmente se usará para realizar la conversión.

## 5. Calcular el Valor Actual de la Cartera

- **Valor de las acciones**: 
    - El valor de cada acción en la cartera se calculará multiplicando la cantidad de acciones por el **precio de mercado actual**, que se convertirá a la divisa de referencia.
- **Valor de compra medio**: 
    - Para cada acción en la cartera, se calculará el **valor medio de compra**, que se obtiene sumando los precios de compra (ajustados por comisiones) y dividiendo entre la cantidad de acciones adquiridas.
- **Rentabilidad**:
    - La **rentabilidad individual de cada activo** se calculará como:
    \[
    \text{Rentabilidad} = \frac{\text{Valor Actual} - \text{Valor de Compra Total}}{\text{Valor de Compra Total}} \times 100
    \]
    - La **rentabilidad total de la cartera** se calculará como la rentabilidad ponderada de todos los activos según su peso en la cartera.

## 6. Dividendos Acumulados

- Se sumarán los **dividendos recibidos** de todas las acciones en la cartera. 
- Estos dividendos se ajustarán a la divisa de referencia, si es necesario, utilizando los tipos de cambio históricos de las transacciones.
- El valor acumulado de los dividendos será reportado por acción y también como total en la cartera.

## 7. Generar el Informe de la Cartera

- El script generará un **informe detallado** que incluirá:
    - El **valor total** de la cartera en la divisa de referencia.
    - El **valor de cada activo** en la cartera (incluyendo cantidad de acciones, valor actual, valor de compra medio, rentabilidad individual y dividendos acumulados).
    - La **rentabilidad total** de la cartera.
- Este informe podrá guardarse en un archivo CSV, PDF o mostrarse en la interfaz de usuario, según las preferencias configuradas.

## Detalles Adicionales

### Rentabilidad

- La rentabilidad se calcula tomando en cuenta el **valor de compra medio ajustado por comisiones**. Esto da una idea más precisa de la rentabilidad neta de cada acción.
- El cálculo de la rentabilidad total de la cartera debe considerar el **peso de cada acción en la cartera** para proporcionar una medida ponderada.

### Informe

- El informe incluirá, por acción:
    - **Ticker**
    - **Cantidad de acciones**
    - **Valor de compra medio**
    - **Valor actual en la divisa de referencia**
    - **Rentabilidad de la acción**
    - **Dividendos acumulados**
- Y un resumen con:
    - **Valor total de la cartera**
    - **Rentabilidad total de la cartera**
    - **Dividendos acumulados totales**
