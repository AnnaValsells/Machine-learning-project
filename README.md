# Machine-learning-project

## Predicción de la Duración de la Estancia de Perros en Centros de Rescate

Este proyecto utiliza técnicas de Machine Learning para predecir la duración de la estancia de perros en centros de rescate. El objetivo principal es proporcionar a los centros de rescate una herramienta que les permita optimizar la gestión de recursos y mejorar el bienestar de los animales.

#### Descripción del Problema

La capacidad limitada de los centros de rescate implica que una estancia prolongada de un perro puede reducir la cantidad de animales que el centro puede atender. Un alto tiempo de estancia implica mayores costos y puede afectar negativamente el bienestar del animal. Por lo tanto, predecir la duración de la estancia es crucial para mejorar la eficiencia y el bienestar animal.

#### Objetivo del Proyecto

Desarrollar un modelo de Machine Learning que prediga la duración de la estancia de un perro en el centro de rescate basándose en varias características del animal y del entorno.

#### Beneficios del Proyecto

- Optimización de Recursos: Mejora la planificación y gestión de los recursos del centro.
- Mejora en las Tasas de Adopción: Ayuda a implementar estrategias para aumentar la tasa de adopción.
- Bienestar Animal: Reduce el tiempo de estancia y mejora el bienestar del animal.
- Estrategias de Intervención Temprana: Permite intervenciones tempranas para los animales con mayor probabilidad de estancia prolongada.

#### Dataset

El dataset contiene las siguientes columnas:

    intake_date: Fecha de llegada al centro de rescate.
    animal_id: Identificador único para cada animal.
    intake_type: Motivo por el cual se ha recogido al perro.
    intake_subtype: Motivo del abandono.
    outcome_date: Fecha de adopción y/o salida del centro.
    outcome_type: Motivo de salida del centro.
    primary_breed: Raza del perro.
    secondary_breed: Segunda raza para los perros mestizos.
    years_old: Años de vida del animal.
    months_old: Meses de vida del animal.
    OutcomeGroup: Grupo de salida (Adopt/Live Exit - Lost/Found/Missing - Euthanized/Dead).
    Breed: Igual que primary_breed pero con los nombres oficiales del Kennel Club Americano.
    PitBullType: Si es de raza potencialmente peligrosa (Si - No).
    PitBullExpanded: Si la secondary_breed es tipo Pitbull (Si-No).
    AKC: Grupo al que pertenece la raza según el Kennel Club Americano (7 Categorías).
    AKC_Extended: Mismas categorías anteriores separando el grupo tipo terrier según si es PitBull o no.
    KennelCardBreed: El animal tiene o no la etiqueta de la raza en la perrera.
    LOS: Duración de la estancia (Length of Stay).
    AgeGroup: Rango de edad al que pertenece el animal (5 Grupos).

#### Preprocesamiento de Datos

- Relleno de Valores Vacíos: Se rellenaron valores vacíos con 'unknown'.

- Corrección de Edades: Se ajustaron edades incorrectas.

- Creación de Nueva Columna age: Se combinó years_old y months_old.

- Transformación de age: Se aplicó la raíz cúbica a la columna age.

- Columnas Excluidas: Se excluyeron animal_id, years_old, months_old, outcome_*, AKC, primary_breed y las fechas.

- Prueba de Mann-Whitney U: Se descartaron PitBullExpanded y PitBullType debido a su bajo valor p.

    Features Seleccionadas:
        age
        intake_type
        intake_subtype
        AKC_Extended
        AgeGroup
        secondary_breed
        Breed
        KennelCardBreed

    Transformaciones Aplicadas:
        One-Hot Encoding para características categóricas.
        Transformación de columna binaria.
        Normalización de age con MinMaxScaler.

#### Algoritmos Utilizados

Se evaluaron los siguientes algoritmos:

    Linear Regression
    Decision Tree Regressor
    Random Forest Regressor
    XGBoost Regressor
    LightGBM Regressor

#### Modelo Seleccionado

El Random Forest Regressor fue seleccionado debido a su capacidad para manejar múltiples características y capturar relaciones no lineales. Sin embargo, las métricas indican la necesidad de mejoras adicionales.
Evaluación de Métricas

    MAE: Sugiere un rendimiento deficiente con errores de aproximadamente 5 días.
    RMSE: Valores entre 16 y 18 días, indicando errores significativos.

#### Conclusiones

El modelo actual no predice con alta precisión. Es probable que se necesiten más características como el carácter del animal y su salud para mejorar las predicciones. También sería interesante explorar si las predicciones del modelo refuerzan las hipótesis iniciales del estudio.