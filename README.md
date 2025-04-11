  ## PROYECTO-INDIVIDUAL-2
  ## ANALISIS DE SINIESTROS VIALES EN LA CIUDAD AUTONOMA DE BUENOS AIRES (CABA)ARGENTINA.


                                                                                                                 
  ![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/76a45528-448e-4b64-a6e1-16e0c3cfcdc8)



                   
                   

## Introduccion:

Este proyecto se llevó a cabo con el objetivo de realizar un análisis de datos para el Observatorio de Movilidad y Seguridad Vial (OMSV), que opera bajo la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA).

El propósito principal del proyecto es proporcionar información fundamentada que ayude en la toma de decisiones para la prevención y la mejora de la seguridad vial, con el fin de reducir los siniestros viales con víctimas fatales en la Ciudad de Buenos Aires.

Una métrica crucial para evaluar la seguridad vial en una región son las tasas de mortalidad relacionadas con los accidentes de tráfico. Estas tasas suelen calcularse como el número de muertes por cada cierto número de habitantes o por cada cierta cantidad de vehículos registrados. La reducción de estas tasas es fundamental para mejorar la seguridad vial y proteger la vida de las personas en la ciudad.

Para llevar a cabo este análisis, se utilizan datos derivados de un conjunto de datos que contiene información sobre homicidios por accidentes de tráfico en la Ciudad de Buenos Aires durante los años 2016-2021. Estos datos son de acceso público y se pueden encontrar en la página oficial de la CABA, específicamente en la sección de Datos Oficiales.

## Contexto: 

Los siniestros viales, que pueden involucrar vehículos en las vías públicas, son eventos con diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden resultar en daños materiales, lesiones graves o incluso la pérdida de vidas para los involucrados.

En Argentina, los siniestros viales son una preocupación importante, con cerca de 4.000 personas falleciendo en accidentes de tránsito cada año. Aunque se han implementado medidas para reducir la cantidad de accidentes, estos siguen siendo una de las principales causas de muertes violentas en el país. Entre 2018 y 2022, se registraron alrededor de 19.630 muertes en siniestros viales en todo el país, lo que equivale a aproximadamente 11 personas fallecidas por día debido a accidentes de tránsito.

Buenos Aires, la capital y ciudad más poblada de Argentina, cuenta con una superficie de alrededor de 200 km² y una población de más de 3 millones de habitantes según el censo de 2022. La densidad de población es alta, con más de 15.000 habitantes por kilómetro cuadrado, especialmente en las zonas centro y norte de la ciudad. En 2022, se registraron 3.828 muertes fatales en siniestros viales solo en esta ciudad.

Dada la alta incidencia de siniestros viales y su impacto en la seguridad pública, el estudio y la prevención de estos incidentes son de suma importancia para las autoridades locales.

## Desarrollo

## Data:

## Para este proyecto se trabajó con la bases de datos de Víctimas Fatales en Siniestros Viales, que se encuentra en formato  Excel y contiene dos pestañas de datos:

HECHOS: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.

VICTIMAS: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho. En este documento se detallan todas las definiciones manejadas en los datos y en el desarrollo de este proyecto. Por otra parte, en este link se encuentran los datos utilizados en el análisis.

-Proceso de ETL (Extracción, limpieza y carga de datos) se realiza la extraccíon y limpieza de los datos de los dos dataset HECHOS y VICTIMAS, a tráves de la utilización de Pandas y Jupyter Netbook.ETL Eliminando nulos, duplicados, con transformaciones necesarias como cambio en los tipos de datos, eliminación de columnas y unión de las tablas en un archivo siniestros_limpio.csv archivo.

-Proceso de EDA (Análisis Exploratorio de los datos) una vez que los datos están limpios, es momento de revisar las relaciones que existen entre las variables numéricas y categóricas de los datasets, encontrar si hay presencia de outliers o anomalías (que no tienen que ser errores necesariamente), y se verificó si hay algún patrón o conocimiento que sirva en un análisis posterior. EDA

## Análisis de los datos. 

Nos permitimos realizar un pequeño análisis exploratorio generalizado del DataFrame de la hoja "Hechos" con el fin de identificar las columnas con datos faltantes. Luego de ello, procederemos a obtener resultados en función de las diferentes variables, es decir, columnas, y los datos introducidos en cada una de ellas:

De acuerdo a las tres (3) imagenes siguientes, tenemos en la primera de ellas: un mapa de calor de valores faltantes en un conjunto de datos. En este tipo de visualización, los colores representan la presencia o ausencia de datos en un conjunto de datos, a menudo utilizado para identificar patrones de datos faltantes: 


![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/7be73edb-a087-4cc2-83b0-d34da4812cc7)


En la gráfica, cada columna representa una variable diferente en el conjunto de datos, con nombres de columna como 'ID', 'N_VICTIMAS', 'FECHA', 'HORA', 'LUGAR_DEL_HECHO', 'TIPO_DE_HECHO', 'CALLE', 'Altura', 'Cruce', 'COMUNA', 'DIRECCION_NORMALIZADA', 'XY (CABA)', 'POS_X', 'POS_Y', 'PARTICIPANTES', 'VICTIMA', 'EDAD', 'ACUSADO', 'AÑO', y 'Número'. Las filas corresponden a las observaciones o registros individuales en el conjunto de datos.

Los bloques de color amarillo indican la ausencia de datos (valores faltantes) y el color púrpura oscuro representa la presencia de datos (valores no faltantes). Los valores faltantes se distribuyen de manera variable entre las diferentes columnas:

La columna 'Altura' tiene una cantidad significativa de valores faltantes, mostrando una banda continua de color amarillo desde la parte inferior de la columna hasta casi el final o la parte superior, lo que sugiere que casi todos los registros carecen de información en esta columna.

Otras columnas como 'ID', 'N_VICTIMAS',  'FECHA' 'TIPO_DE_HECHO', 'CALLE', 'COMUNA',tienen muy pocos o ningún valor faltante, indicado por el color púrpura predominante, lo que sugiere que casi todos los registros en estas columnas tienen datos completos.

Algunas columnas como ', 'CRUCE' y 'DIRECCION_NORMALIZADA',  tienen una cantidad moderada de valores faltantes, como se indica por las bandas amarillas intercaladas con el color púrpura.

El tipo de visualizacióna traves de un mapa de calor es muy útil para identificar rápidamente las variables que pueden necesitar atención debido a la gran cantidad de valores faltantes, lo que podría afectar los análisis estadísticos o de aprendizaje automático que se realicen con el conjunto de datos.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/3035bc4b-5143-44cd-b39a-b8d2d670c7f7)


La anterior imagen,el boxplot -Diagrama de caja-proporcionado, muestra solamente dos puntos, lo que sugiere que los demás valores en la columna 'N_VICTIMAS' son iguales, y estos dos puntos son valores atípicos o outliers. El  boxplot, típicamente muestra la mediana, los cuartiles y los valores atípicos. Si la mayoría de los valores son iguales, la "caja" del boxplot puede ser tan estrecha que no se visualice correctamente, o puede parecer que no está presente si todos los valores son idénticos excepto los atípicos. En este caso, casi todos los valores, son identicos.Asi las cosas,de acuerdo al analisis descriptivo efectuado mediante el codigo, nos indica que solo hay tre valores únicos de las 696 filas.Es decir, que la cantidad de victimas por acccidente,normalmente es 1.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/59279bd4-faa9-4220-9bc4-8053aa3fb708)

Con respecto a esta tercer imagen, tenemos un histograma del número de víctimas. El histograma es una representación gráfica de la distribución de frecuencias de un conjunto de datos. En este caso, las barras representan la frecuencia de hechos con distintos números de víctimas.

En el eje horizontal ('Número de Víctimas'), tenemos rangos que representan el número de víctimas en los hechos. En el eje vertical ('Frecuencia'), tenemos la cantidad de veces que ocurrieron hechos con ese número de víctimas.

La gráfica muestra que la gran mayoría de los hechos tienen 1 víctima, ya que la primera barra es la más alta, abrumadoramente más que las otras. Hay una barra muy pequeña cerca de 2, lo que indica que hay una cantidad mucho menor de hechos con 2 víctimas. No hay barras para valores más altos de víctimas hasta 3, lo que indica que los hechos con más de 2 víctimas son aún menos frecuentes, hasta el punto de que podrían ser anomalías o casos muy raros en este conjunto de datos.

La conclusión principal de este histograma es que la mayoría de los hechos tienen 1 víctima y que los hechos con 2 o más víctimas son mucho menos comunes en este conjunto de datos.

## De acuerdo con lo manterior, se conocerá la cantidad total de hechos registrados por  año desde el 2016 hasta el 2021:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/00937193-bd0a-43bb-80bc-a83e5005a625)


El resultado de la ejecución  o impresión del código anterior, nos indica que, el año con mayor identificación de accidentes o mayor números de hechos registrados, de acuerdo a la columna id, es el 2018, con 149 casos de homicidios registrados; seguido del año 2016 con 146 casos registrados; luego tenemos el año 2017 con 140 casos registrados ; posteriormente, el año 2019 con 104 casos de homicidios registrados; seguidamente tenemos el año 2021 con 97 casos registrados y; finalmente, el año 2020 con 81 casos de homicidios registrados. Desde ya me apresuro a manifestar que la gran disminución en cuanto al registro de casos ocurridos en el año 2020, pudo obedecer a la disminución de vehículos que se movilizaban en las vías como consecuencia de la pandemia del COVID 19.
Es importante anotar que los datos muestran una disminución en el número de hechos registrados desde 2019 hasta 2021. 


Nos permitimos visualizar la cantidad de hechos por mes desde el año 2016 hasta el año 2021.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/e5ed7b2b-b16e-4f4b-9c6d-df42130ce27b)


El conjunto de gráficos de barras que representan la cantidad de hechos registrados por mes para varios años individuales, desde 2016 hasta 2021. Cada gráfico corresponde a un año diferente y muestra la distribución mensual de los hechos registrados durante ese año.

Las barras muestran la variabilidad en la cantidad de hechos que se registran en diferentes meses del año para cada uno de los años representados.

## Conclusiones que podríamos sacar basadas en este tipo de gráficos:

Tendencias Estacionales: Podría haber tendencias estacionales si ciertos meses muestran consistentemente números más altos o más bajos de hechos. Por ejemplo, si las barras de diciembre son sistemáticamente altas en todos los años, esto podría sugerir un aumento de incidentes en ese mes.

Comparación Anual: Al comparar los gráficos entre años, podemos ver si hay algún patrón o cambio significativo en la cantidad de hechos a lo largo del tiempo. Por ejemplo, si el número de hechos aumenta o disminuye significativamente de un año a otro, esto podría indicar cambios en las condiciones que afectan la frecuencia de los hechos.

Eventos Anómalos: Los picos o caídas inusuales en ciertos meses pueden indicar la ocurrencia de eventos anómalos o cambios en las prácticas de registro.

Planificación y Respuesta: Este tipo de análisis puede ser útil para la planificación de recursos y la respuesta a emergencias, permitiendo a las autoridades prepararse adecuadamente para los meses con mayor número de hechos.

Nos permitimos conocer a partir de una grafica  o histograma de barras, el mes con más hechos registrados en cada año. Desde el 2016 hasta el 2021.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/1f228cc0-dcc6-4d31-b644-71547ecdc667)

## Conclusiones basadas en la descripción de la gráfica:

Para cada año, hay una variación en el número de hechos por mes, con algunos meses teniendo más hechos que otros.
El mes que se resalta en rojo indica el mes con la mayor cantidad de hechos registrados en ese año específico. Por ejemplo, si el mes de mayo está resaltado en rojo en el gráfico de 2017, significa que mayo de 2017 tuvo la mayor cantidad de hechos registrados en comparación con otros meses de ese año.
En el grafico de 2018, se tiene que el mes agosto tuvo la mayor cantidad de hechos registrados en comparación con otros meses de ese año.Igual ocurrió en el  grafico del año 2019.

En el grafico de 2020,el mes de diciembre tuvo la mayor cantidad de hechos registrados en comparación con otros meses de ese año.

En el grafico de 2021,el mes de enero tuvo la mayor cantidad de hechos registrados en comparación con otros meses de ese año.

Se observa que hay un patron constante en cuanto al mes con mayor hechos registrados en el año 2018 y 2019, se trata del mes agosto. Lo mismo ocurrió en los años 2016 y 2020 en cuanto al mes de diciembre. 

La variacion en los meses, con la mayor cantidad de hechos registrados se da en los años 2017 y 2021, donde en el pirmer año, el mes con mayor hechos registrados fue mayo y; en el 2021, fue el mes de enero.
La variación en la cantidad de hechos no sigue una tendencia estacional clara o que los factores que influyen en los hechos pueden variar de año en año.

Esta identificación de los meses con más hechos, puede ser útil para que las autoridades realicen  análisis más profundos sobre las causas de esta concentración de hechos y tomar medidas preventivas o de preparación para el futuro.


Nos permitimos conocer la cantidad de hachos por semana.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/3cf8bde0-72fa-4f64-a8fc-d9c83ee0a83e)


El gráfico de barras representa la cantidad de hechos registrados por semana a lo largo de varios años, desde 2016 hasta 2021. Las barras de diferentes colores representan diferentes años, lo que permite una comparación entre la cantidad de hechos que ocurrieron en la misma semana en diferentes años.

## Interpretaciones de la gráfica:

Variabilidad Semanal: Existe una variabilidad en la cantidad de hechos registrados semana a semana. Esto es normal en datos de eventos que pueden ser influenciados por muchos factores externos.

Comparación Anual: El uso de colores diferentes para cada año permite comparar rápidamente la cantidad de hechos que ocurrieron en la misma semana a lo largo de diferentes años. Se pueden identificar patrones o anomalías específicas del año.

Consistencia Temporal: Si bien hay variaciones, algunas semanas parecen tener consistentemente más hechos que otras, lo que podría sugerir patrones estacionales o eventos recurrentes que afectan la cantidad de hechos.

Ausencia de Tendencias Claras: No parece haber una tendencia clara ascendente o descendente en la cantidad de hechos a lo largo de los años, lo que indicaría que no hay un aumento o disminución general en los hechos registrados durante este período.

## Conclusiones basadas en la gráfica:

Planificación de Recursos: Las autoridades podrían utilizar esta información para planificar mejor la asignación de recursos. Por ejemplo, si ciertas semanas muestran consistentemente un número mayor de hechos, podrían prepararse reforzando el personal o los recursos durante esos períodos.

Investigación de Causas: Para semanas con un número inusualmente alto de hechos, podría ser útil investigar las posibles causas, como eventos especiales, cambios en las leyes de tráfico o condiciones climáticas adversas.

Medidas Preventivas: Identificar semanas con altos números de hechos podría ayudar en el desarrollo e implementación de campañas de seguridad y medidas preventivas.


## Nos permitimos conocer a través de una grafica, la visualizacion de hechos registrados por dia:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/2be090f3-ecbb-4b54-a5fa-8e82c0522f4e)

El gráfico de líneas con marcadores que representa la cantidad de hechos (accidentes) registrados por día a lo largo del tiempo. Cada punto en la línea representa la cantidad de hechos en un día específico.

## Interpretación y conclusiones basadas en la gráfica:

Periodicidad y Tendencia: La gráfica muestra datos a lo largo de varios años, desde 2015 hasta 2022. No hay una tendencia clara que indique un aumento o disminución sistemática de hechos a lo largo del tiempo.

Fluctuaciones: Existen fluctuaciones significativas en la cantidad de hechos registrados por día. Algunos días tienen picos muy altos, lo que podría indicar eventos o circunstancias especiales que condujeron a un número inusualmente alto de hechos.

Consistencia: Hay muchos días en los que se registra una cantidad baja y consistente de hechos, lo que podría considerarse como la 'norma' o el promedio de hechos diarios.

Valores Atípicos: Los picos muy altos podrían ser interpretados como valores atípicos. Estos días pueden requerir una investigación adicional para entender qué causó el alto número de hechos.

Distribución: La mayoría de los días parecen tener pocos hechos, con solo unos pocos días que tienen un número elevado. Esto podría indicar que eventos con altas cantidades de hechos son relativamente raros.

Granularidad Temporal: La gráfica muestra los datos etiquetados con fechas específicas en el eje x, lo que indica que los datos están representados día a día.

Ahora, pasaremos a conocer la cantidad de vicitimas por año, desde el 2016 hasta el 2021.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/11340303-06f6-4a82-a13e-19b24822b276)

histograma de barras anterior, nos muestra la cantidad de víctimas por año, específicamente para los años 2016 a 2021. Cada barra representa un año y la altura de la barra corresponde al número total de víctimas de ese año. Los números en la parte superior de cada barra indican la cantidad exacta de víctimas. De izquierda a derecha, las barras representan los años en orden ascendente, y las cifras de víctimas disminuyen progresivamente desde 2016 hasta 2021, con una ligera disminución después de 2018.

## Aquí están los detalles de la cantidad de víctimas por año, según se muestra en la gráfica:

2016: 150 víctimas
2017: 160 víctimas
2018: 161 víctimas
2019: 106 víctimas
2020: 87 víctimas
2021: 97 víctimas

## Pasamos ahora, a conocer el número de victimas por mes:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/226a1806-737e-4712-a003-11083da16173)

La gráfica de barras que muestra la cantidad de víctimas por mes durante un período que abarca los años 2016 a 2021.

## Interpretación:

Eje Horizontal (Mes): Cada barra representa un mes del año, de enero a diciembre.
Eje Vertical (Cantidad de Víctimas): La altura de cada barra indica el número total de víctimas que hubo en ese mes específico durante el período total de 2016 a 2021.
Colores de las Barras: Aunque no se especifica en la descripción, si los colores de las barras representan diferentes años, entonces cada color dentro de la misma categoría de mes indicaría el total de víctimas para ese mes en diferentes años.

## Conclusiones:

Variabilidad Mensual: Existe una variabilidad en la cantidad de víctimas de mes a mes. Algunos meses tienen más víctimas que otros.

Meses con Mayor Número de Víctimas: Los meses de enero, marzo y los últimos tres meses del año (octubre, noviembre, diciembre) parecen tener una mayor cantidad de víctimas, con diciembre mostrando el número más alto.

Meses con Menor Número de Víctimas: Julio y septiembre muestran las cantidades más bajas de víctimas en el período dado.
A partir de esta gráfica, se puede concluir que hay patrones estacionales en la cantidad de víctimas. Los meses de invierno y finales de año (en el hemisferio norte) tienden a tener más víctimas, lo que podría estar relacionado con condiciones climáticas adversas, un aumento en los viajes debido a las festividades o cambios en los patrones de comportamiento humano. Por otro lado, los meses de verano muestran números más bajos, lo que podría reflejar condiciones de viaje más seguras o menos tráfico de vehículos.

## Pasamos a conocer el  número de victimas por semana:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/1fa1c265-9c7c-4c89-b03a-5b30b57d1f85)

El gráfico de caja y bigotes (box plot) muestra la distribución de la cantidad de víctimas por semana a lo largo de varios años, desde 2016 hasta 2021. Este tipo de gráfico es útil para entender la distribución y la presencia de valores atípicos dentro de un conjunto de datos.

El eje Horizontal (Semana): Representa las semanas del año, que generalmente están numeradas del 1 al 52 o 53. Cada punto o línea en el gráfico corresponde a una semana diferente del año para todos los años combinados.

El eje Vertical (Cantidad de Víctimas): Representa el número de víctimas reportadas por semana. Los puntos individuales o las líneas verticales representan la cantidad de víctimas en una semana específica.

## Conclusiones basadas en la interpretación general del  gráfico de caja y bigotes:

La línea que cruza la caja (mediana) muestra el valor central de los datos para esa semana en particular, lo cual es útil para entender la tendencia central sin ser influenciado por valores atípicos.
La altura de la caja indica la variabilidad de los datos. Una caja más alta sugiere una mayor variabilidad en el número de víctimas por semana.
Los valores atípicos pueden indicar semanas con números inusualmente altos o bajos de víctimas en comparación con el resto del año.

## Ahora, pasaremos a conocer el número de victimas por dia:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/18fb4c1f-416e-464a-849e-b8696f7466a2)

En cuanto a la segunda grafica, La gráfica de barras "Frecuencia de Hechos por Hora" muestra la distribución de hechos o accidentes a lo largo de las diferentes horas del día, con los datos agrupados por hora. Cada barra representa una hora específica del día (de 00:00 a 23:00) y la altura de la barra indica la frecuencia de hechos que se registraron en esa hora específica.

## Asi las cosas y, basados en las observaciones de dicha grafica,  podemos concluir que:

La mayoría de los hechos ocurren a las 07:00 horas, con un total de 41 hechos registrados, lo que la convierte en la hora con mayor frecuencia de accidentes.
Hay una tendencia notable de mayor frecuencia de hechos durante las primeras horas de la mañana, con un pico significativo a las 07:00 horas.
A partir de las 08:00 hasta las 19:00 horas, la frecuencia de hechos se mantiene relativamente constante, sin picos tan pronunciados como en las horas de la mañana.
Después de las 20:00 horas, hay una ligera disminucion con otro pico menor a las 21:00 horas, seguido de una disminución hacia el final del día.
no obstante, es imposible dejar por fuera de este analisis las horas con menos casos como son las 02:00 horas y las 13:00 horas, en las cuales la cantidad de accidentes es igual. Ello, sin lugr a dudas, nos permite expresar en principio que, la dismnucion obedece a la poca cantidad de vehiculos en las vias.Por otro lado,se debe a la cantidad de personas que a las 02:00 horas aun se encuentran durmiendo o por tratarse de un horario poco frecuente para desempeñar labores empresariales. Y, con respecto a al disminucion a las 13:00 horas, puede obedecer a que es el horario de almuerzo, por lo tanto muchas personas a esa hora no se estan  movilizando  en  sus vehiculos ni caminando por las diferentes vias.
La conclusion final sería que existe una tendencia clara de que los hechos tienden a ocurrir más frecuentemente en las primeras horas de la mañana, especialmente alrededor de las 07:00 horas. Esto podría estar relacionado con el tráfico de la hora pico de la mañana cuando la gente se dirige a sus lugares de trabajo o estudio. La información podría ser útil para las autoridades locales con el proposito de  mejorar las medidas de seguridad vial o realizar campañas de concientización en las horas donde los hechos son más frecuentes.

## De acuerdo con lo anterior, surge la necesidad de conocer la distribuccion de la diferencia de tiempo entre accidente,para ello, se procede con el siguiente codigo:  

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/9382b142-38af-495b-9433-8c7558d7e622)

El histograma generado muestra la distribución de la diferencia de tiempo entre accidentes en horas. Además, las estadísticas descriptivas proporcionan información sobre la diferencia de tiempo entre accidentes:

Count: Hay 715 diferencias de tiempo calculadas entre accidentes consecutivos.
Mean: En promedio, hay una diferencia de aproximadamente 3 días y 1.5 horas entre accidentes.
Std (Desviación estándar): La desviación estándar es de aproximadamente 3 días y 8 horas, lo que indica una variabilidad considerable en las diferencias de tiempo.
Min: La menor diferencia de tiempo es de 0 horas (accidentes que ocurren en la misma hora).
25% (Primer cuartil): El 25% de las diferencias de tiempo son de menos de aproximadamente 21 horas.
50% (Mediana): La mitad de las diferencias de tiempo son de menos de 2 días y 1 hora.
75% (Tercer cuartil): El 75% de las diferencias de tiempo son de menos de 4 días y 3 horas.
Max: La mayor diferencia de tiempo es de 24 días y casi 16 horas.
Estos resultados sugieren que aunque hay casos donde los accidentes ocurren con poco tiempo de diferencia, también hay periodos largos sin accidentes. La presencia de diferencias de tiempo tan largas como 24 días podría deberse a datos faltantes o a un periodo sin accidentes.

Lo anterior es util para comprender los patrones temporales de los accidentes y para la planificación de la gestión de la seguridad vial y la asignación de recursos para la respuesta a emergencias. ​

De acuerdo con lo anterior,exploraremos acerca del lugar o lugares donde más accidentes con muertes ocurren.

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/1a870a00-6f92-4b6d-b015-a1cfb2055ee1)

## Tenemos que: 
El lugar con más accidentes es: AV 27 de Febrero y AV Escalada con 4 accidentes.
Lugar del hecho
AV 27 DE Febrero y Av Escalada                               : 4.
AV. DR. Tristan Achaval Rodriguez y BLVD. Azucena Villaflor  : 3.
AU Perito Moreno y Ramal Enlace AU1/AU6                      : 2.
Castillo, Ramon S., Pres. AV. y Calle 12                     : 2.
Rivadavia Av. y Pedernera                                    : 2.
                                                              ..
AU Dellepiane y AV. Escalada                                 : 1.
Albariño y AV. Argentina                                     : 1.
Juan Ramirez dE Velazco 1211                                 : 1.
AV. Fernandez de la Cruz Y Larraya                           : 1.
Padre Carlos Mujica 709                                      : 1.


## Acto seguido exploraremos la comuna donde más accidentes ocurren:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/2d536af7-5956-4eb9-b8e5-eed57b31ca84)

De acuerdo al código generado,tenemos que nos indica que,la comuna con más accidentes es la uno (1) con 93 accidentes.  


## Exploraremos los tipos de vehiculos participantes e implicados y la frecuencia con que se dan los accidentes de transito que terminanan en muerte:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/f788d62a-30b5-4ce0-b215-2ac817462f60)

## De la grafica anterior podemos Interpretar que:

La combinación más frecuente involucra a peatones y pasajeros, con la mayor cantidad de accidentes (105).
La siguiente categoría más común es moto-auto, lo que sugiere una alta incidencia de accidentes entre motocicletas y automóviles (84 accidentes).
Otras combinaciones frecuentes incluyen moto-cargas y peaton-auto, lo que podría indicar áreas de preocupación específicas en la seguridad vial relacionadas con motocicletas, peatones y vehículos de carga.

## Conclusiones:

Seguridad de Peatones y Pasajeros: Los peatones y pasajeros parecen ser los más afectados en los accidentes, lo cual podría requerir medidas de seguridad adicionales en áreas de alto tráfico peatonal y en el transporte público o privado de pasajeros.

Interacciones Moto-Auto: La alta frecuencia de accidentes entre motocicletas y autos puede señalar la necesidad de mejorar la conciencia sobre la seguridad de las motocicletas y de implementar mejores prácticas de conducción para ambos tipos de vehículos.

Impacto en Políticas de Tráfico: Estos datos podrían utilizarse para informar políticas de tráfico y seguridad vial, incluyendo la creación de campañas de seguridad específicas para las combinaciones de vehículos más riesgosas.

Educación y Entrenamiento: Las estadísticas podrían apoyar la necesidad de programas de educación vial dirigidos a conductores de motocicletas y automóviles, así como campañas para aumentar la conciencia entre los peatones.

Infraestructura de Transporte: Considerar la mejora de la infraestructura vial, como cruces peatonales más seguros, carriles exclusivos para motocicletas, y medidas para reducir la velocidad del tráfico en áreas con alta incidencia de accidentes.

Continuamos con la exploracion de la frecuencia con la que se ven implicados los diferentes tipos de vehículos o victimas fatales en accidentes, según la información asociada a la columna "Víctima".

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/4ad255aa-f0f3-4f2b-b323-543f554548a8)

La Interpretacion de la grafica nos indica que, 

Motos: Con 302 menciones, las motos son el tipo de vehículo más frecuentemente mencionado en el contexto de "Víctima". Esto sugiere que las motos están involucradas en un número significativo de accidentes o incidentes reportados.
Peatones: Los peatones aparecen con 266 menciones, lo que implica que también son un grupo considerablemente afectado en los accidentes de tráfico.
Autos: Con 92 menciones, los autos son el tercer tipo de vehículo más común en la lista, lo que indica su participación en los accidentes pero en menor medida comparado con motos y peatones.
Bicicletas y otros: Las bicicletas tienen 29 menciones, seguidas por categorías con menos incidencia como "sin dato", "cargas", "pasajeros", "móvil", "objeto fijo" y "peaton_moto".

## Conclusiones:

Seguridad de Motociclistas y Peatones: Las autoridades podrían necesitar enfocarse en mejorar la seguridad vial para motociclistas y peatones, ya que representan los mayores grupos de riesgo según los datos.

Campañas de Concientización: Sería beneficioso implementar campañas de conciencia y educación dirigidas a conductores de motos y autos, así como a peatones y ciclistas, para reducir el número de accidentes.

Infraestructura Vial: Los datos respaldan la necesidad de revisar y posiblemente mejorar la infraestructura vial, incluyendo carriles para bicicletas y motocicletas, así como pasos peatonales seguros.

Análisis de Datos Incompletos: La categoría "sin dato" sugiere que hay registros incompletos o inadecuados en la base de datos, lo que podría requerir una mejor recolección y análisis de datos en el futuro.

Estrategias de Prevención: Para las categorías con menos incidencia, es importante desarrollar estrategias de prevención específicas que aborden los riesgos únicos asociados con cada tipo de vehículo y situación.

Ahora pasamos a explorar la frecuencia con la que se ven implicados los diferentes roles en accidentes de transito:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/d3b3ee42-21c8-4946-ba63-535951126cde)

## La interpretacion y conclusion de la grafica anterior son las siguientes :

## Interpretación:

El rol de "conductor" es el más frecuentemente implicado en accidentes de tránsito, con la mayor cantidad de accidentes (330).
El rol de "peatón" también es significativamente implicado en accidentes, con 267 incidentes.
"Pasajero_acompañante" y "ciclista" se muestran como otros roles involucrados en accidentes, con 80 y 29 accidentes respectivamente.
La categoría "sin dato" indica un número de registros (11) donde el rol no fue especificado o no se disponía de información.

## Conclusiones:

Atención a Conductores: Dado que los conductores están implicados en la mayoría de los accidentes, las campañas de seguridad vial deben centrarse en la educación y el entrenamiento de los conductores, así como en la implementación de leyes de tránsito más estrictas y su cumplimiento.

Protección del Peatón: La alta incidencia de peatones involucrados sugiere la necesidad de mejorar la infraestructura peatonal, como pasos de peatones, señalización y medidas de calmado de tráfico.

Seguridad del Pasajero y Ciclista: La seguridad de los pasajeros y ciclistas también debe ser una prioridad, posiblemente a través de mejores prácticas de uso del cinturón de seguridad y cascos, así como la creación de carriles para bicicletas.

Datos Incompletos: La presencia de una categoría "sin dato" subraya la importancia de mejorar la recopilación de datos en la escena del accidente para informar mejor las políticas de seguridad vial.


## Pasamos a explorar el genero que con mayor frecuencia se ve implicado en accidentes de transito:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/062fbcb0-a3fc-401b-ac55-e7bc27b02a89)

## Frente a la anterior grafica tenemos tambien: 

## Interpretación:

La categoría "masculino" tiene significativamente más accidentes reportados con un total de 545.
La categoría "femenino" tiene un total de 166 accidentes.
Hay un pequeño número (6) de registros donde el género no fue reportado o no está disponible.

Conclusiones:

Predominancia Masculina en Accidentes: El género masculino está involucrado en una cantidad mucho mayor de accidentes de tránsito en comparación con el género femenino. Esto puede deberse a varios factores, incluyendo una mayor proporción de conductores masculinos o diferencias en los patrones de comportamiento de conducción.

Importancia de Datos Completos: La presencia de una categoría "sin dato" aunque pequeña, destaca la importancia de una recopilación de datos completa y precisa en la escena del accidente para comprender mejor las dinámicas de género en los accidentes de tránsito.

Implicaciones para Políticas de Seguridad Vial: Estos datos pueden ser útiles para las autoridades de tráfico al desarrollar políticas de seguridad vial y programas educativos dirigidos específicamente a los conductores masculinos, dado que son más propensos a estar involucrados en accidentes.

Investigación Adicional: Sería beneficioso realizar investigaciones adicionales para entender las razones detrás de la disparidad de género en los accidentes de tránsito y abordar las causas subyacentes a través de la educación, la legislación y la infraestructura vial.
  
Pasamos a explorar el rango de edades que en mayoritariamente se ven implicadas las personas en accidentes que terminan en muerte:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/f967a3ef-4843-4d5e-839b-9ac97773ffc8)

## la grafica nos muestra:

Rango_Edad
0-18:      76.
19-25:     106.
26-35:     170.
36-45:     123.
46-55:     60.
56-65:     70.
66-75:     45.
76-85:     54.
86-100:    13.

Al interpretar y conluir lo que en dicha grafica se visualiza, nos encontramos con: 

## Interpretación:

El rango de edad con la mayor cantidad de accidentes es el de 26-35  años, lo que sugiere que los adultos jovenes están significativamente más involucrados en accidentes de tránsito que otros grupos de edad.
Los rangos de edad de 19-25 y 36-45 también muestran una alta frecuencia de accidentes, aunque en menor medida que el grupo de 26-35 años.

Los rangos de edad más bajos (0-18) y más altos (66-75,76-85 y 86-100) tienen la menor frecuencia de accidentes.
Existe una tendencia general a que la frecuencia de accidentes disminuya a medida que aumenta la edad de los individuos involucrados.

## Conclusiones:

Foco en la Educación de Jóvenes Conductores: Los datos indican la necesidad de centrarse en la educación y formación de los conductores que son adultos jóvenes, especialmente en el rango de 26 a 35 años, para reducir la incidencia de accidentes.

Medidas Preventivas para Adultos Jóvenes: Las autoridades podrían considerar implementar medidas preventivas específicas para los conductores en los rangos de edad de 19-25 y 36-45 años, como campañas de concienciación y control de tráfico más estricto.

Revisión de Políticas de Licencias: La alta frecuencia de accidentes en edades tempranas podría justificar una revisión de las políticas de licencias de conducir y los requisitos para obtenerlas, incluyendo quizás programas de conducción gradual o restricciones en horarios nocturnos.

Inclusión de Adultos Mayores en Programas de Seguridad: Aunque los grupos de mayor edad tienen menos accidentes, sigue siendo importante incluirlos en programas de seguridad vial, enfocándose en mantener habilidades de conducción seguras y en considerar la transición a dejar de conducir cuando sea apropiado.

Finalmente, pasamos a explorar el rol que más se percibe inicialmente acusado en accidentes de transito, que terminan con muerte:

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-2/assets/120407303/12197496-e479-48a3-891c-21bfbde71762)

 De acuerdo con la grafica de barras tenemos que su interpretacion y conclusiones son las siguientes:  

## Interpretación:

El rol de "auto" es el más frecuentemente acusado en accidentes de tránsito, con 210 incidentes.
Los "pasajeros" y los vehículos de "cargas" también tienen un alto número de acusaciones, con 178 y 150 incidentes respectivamente.
Se observa una cantidad menor de acusaciones para roles como "moto" y "objeto fijo", con 58 y 67 incidentes.
Hay casos donde no se ha proporcionado dato sobre el rol acusado ("sin dato") o donde se han implicado múltiples roles ("múltiple").
Roles como "bicicleta", "otro", y "tren" tienen la menor frecuencia de acusaciones.

## Conclusiones:

Responsabilidad del Conductor de Automóvil: Dado que los conductores de automóviles representan la mayoría de las acusaciones, es crucial enfocar las medidas de seguridad y educación vial en este grupo para reducir su involucramiento en accidentes.

Protección para Pasajeros y Transporte de Carga: Es importante garantizar la seguridad de los pasajeros y los vehículos de carga, posiblemente a través de regulaciones más estrictas y controles de seguridad mejorados.

Importancia de la Información Completa: La presencia de categorías como "sin dato" subraya la necesidad de una documentación exhaustiva en los informes de accidentes para permitir análisis más precisos y medidas de prevención adecuadas.

Consideración de Todos los Usuarios de la Vía: A pesar de que los roles como "bicicleta", "otro", y "tren" tienen menos acusaciones, es esencial incluir la seguridad de todos los usuarios de la vía en las estrategias de prevención de accidentes.
