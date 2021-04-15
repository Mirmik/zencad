# Геометрические характеристики.
Раздел посвящен измерению геометрических характеристик конструируемой геометрии.

Поскольку понятия плотности и масштаба весьма эфемерны для вычислительной библиотеки, все вычисления проводятся в условных единицах. Перевод величин в систему си требует дополнительных вычислений.

----------------------------------------
## Встроенные методы
Shape имеет ряд методов, позволяющих запросить геометрическую информацию.

### Центр масс.
shape.center() -> point3
shape.cmradius() -> vector3

### Объём.
shape.mass() -> float

### Матрица инерции.
shape.matrix_of_inertia() -> matrix33

### Статические моменты.
shape.static_moments() -> float, float, float

### Момент инерции относительно оси.
UNDER_CONSTRUCT

### Радиус инерции.
UNDER_CONSTRUCT

-----------------------------------------
## Измерение систем тел
UNDER_CONSTRUCT