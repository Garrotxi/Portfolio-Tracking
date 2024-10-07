# Estructura de ficheros

## 1. Fichero de Compras/Ventas:

Este es el historial de operaciones que la aplicación usará para reconstruir la cartera.

**Campos:**

- Fecha
- Ticker
- Divisa
- Cantidad de acciones
- Precio por acción
- Comisiones
- Impuestos
- Precio total
- Broker
- Tipo de operación (Compra/Venta)
- Precio ajustado en divisa local (si aplica)

**Propósito:**

- La aplicación utilizará este fichero para construir la cartera actual en base a las operaciones históricas.
- Cálculo del precio promedio ponderado de las acciones y el costo total incluyendo comisiones e impuestos.
- Puede realizarse conversión de moneda usando el fichero de cambio de divisas, si es necesario.

## 2. Fichero de Estado Actual de la Cartera (Opcional):

Este fichero permite cargar la cartera actual sin necesidad de reconstruirla desde el historial de compras/ventas.

**Campos:**

- Ticker
- Divisa
- Cantidad de acciones
- Precio promedio
- Valor actual
- Dividendo acumulado
- Rendimiento por dividendo
- Broker

**Propósito:**

- Permite a los usuarios cargar directamente el estado actual de su cartera en lugar de depender exclusivamente del histórico.
- Se puede sincronizar con el historial de compras/ventas para mantener la cartera actualizada.

## 3. Fichero de Cambio de Divisas:

Controla el tipo de cambio y las comisiones aplicadas por el broker durante una operación de conversión de divisa.

**Campos:**

- Fecha
- Divisa origen
- Divisa destino
- Tipo de cambio aplicado (por el broker)
- Comisiones de cambio
- Broker
- Fuente del tipo de cambio (opcional)

**Propósito:**

- La aplicación utilizará este fichero para convertir los precios de compra/venta y dividendos cuando se utilicen monedas diferentes a la divisa local del usuario.
- Refleja el impacto de las comisiones que el broker aplica al realizar conversiones, para que el análisis financiero sea más preciso.

## 4. Fichero de Dividendos:

Este fichero lleva el control detallado de los dividendos recibidos por cada acción.

**Campos:**

- Fecha
- Ticker
- Divisa
- Cantidad de acciones al cobrar el dividendo
- Importe bruto
- Retención en origen
- Retención en destino
- Importe neto
- Broker
- Rendimiento del dividendo (opcional)
- Dividendo reinvertido (booleano)

**Propósito:**

- La aplicación usa este fichero para calcular los ingresos por dividendos, ajustando los valores si es necesario a la divisa local.
- Permite generar informes sobre el rendimiento por dividendos y su impacto en la rentabilidad total.

# Flujo y Lógica de la Aplicación

## 1. Carga de Ficheros

- Opción 1: El usuario carga los ficheros **Compras/Ventas, Dividendos, Cambio de Divisas**.
- Opción 2: El usuario carga el fichero de **Estado Actual de la Cartera.**: Si se carga el fichero de estado actual, la aplicación puede utilizarlo como punto de partida para los cálculos y análisis de la cartera. Si no, reconstruye la cartera a partir del historial de compras/ventas.
- Opción 3: **Crear cartera desde 0** permite al usuario crear una cartera nueva sin necesidad de cargar ficheros. El usuario podrá:
  - **Seleccionar Tickers**: Elegir las acciones que desea incluir en su cartera
  - **Introducir Datos**: Ingresar manualmente la cantidad de acciones, el precio por acción y otros detalles relevantes.
  - **Guardar Cartera**: Una vez completada, la cartera se puede guardar en la base de datos o como un fichero para su uso futuro.

## 2. Reconstrucción de la Cartera

- La aplicación utiliza el fichero de **Compras/Ventas** para calcular la cartera actual, sumando las cantidades de acciones compradas y restando las vendidas.
- El **precio promedio** de cada acción se calcula ponderando los precios de las compras, ajustado por comisiones e impuestos.
- Si las operaciones incluyen monedas extranjeras, la aplicación consulta el **fichero de Cambio de Divisas** para ajustar el precio total en la divisa local, considerando el tipo de cambio y las comisiones aplicadas por el broker.

## 3. Análisis de Dividendos

- La aplicación utiliza el fichero de **Dividendos** para calcular los ingresos totales por dividendos y el rendimiento por cada acción.
- Si los dividendos se pagan en una divisa extranjera, la aplicación consulta el **fichero de Cambio de Divisas** para realizar las conversiones y obtener el valor neto en la divisa local.
- Se puede generar un reporte de **rendimiento por dividendo** basado en la cantidad de acciones en cartera y el valor de los dividendos.

## 4. Reportes y Análisis

- La aplicación genera informes detallados sobre el **rendimiento del portafolio**, incluyendo ganancias o pérdidas por la apreciación de las acciones, y el rendimiento por dividendos.
- **Impacto de divisas**: Puede realizar un análisis del impacto que las conversiones de divisas y las comisiones del broker tienen en la rentabilidad del portafolio.
- **Simulación de reinversión de dividendos**: Si los dividendos se reinvierten automáticamente, la aplicación puede analizar el impacto de esta estrategia en la acumulación de acciones y en el rendimiento total.

## 5. Actualización dinámica

- Cada vez que se introduzca una nueva operación o dividendo, la aplicación recalcula automáticamente la cartera y ajusta los informes y análisis en tiempo real.