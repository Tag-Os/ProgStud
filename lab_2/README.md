# Отчет

## Графики с учебника matplotlib 1.1 - 3.29

**1.1**

![1.1](/lab_2/photo_graphics/Figure_1.png)

**1.3**

![1.3](/lab_2/photo_graphics/Figure_13.png)

**1.4**

![1.4](/lab_2/photo_graphics/Figure_14.png)

**1.5**

![1.5](/lab_2/photo_graphics/Figure_15.png)

**1.6**

![1.6](/lab_2/photo_graphics/Figure_16.png)

**1.7**

![1.7](/lab_2/photo_graphics/Figure_17.png)

**1.8**

![1.8](/lab_2/photo_graphics/Figure_18.png)

**2.1**

![2.1](/lab_2/photo_graphics/Figure_2.png)

**2.2**

![2.2](/lab_2/photo_graphics/Figure_22.png)

**2.3**

![2.3](/lab_2/photo_graphics/Figure_23.png)

**2.4**

![2.4](/lab_2/photo_graphics/Figure_24.png)

**2.5**

![2.5](/lab_2/photo_graphics/Figure_25.png)

**2.6**

![2.6](/lab_2/photo_graphics/Figure_26.png)

**2.7**

![2.7](/lab_2/photo_graphics/Figure_27.png)

**2.8**

![2.8](/lab_2/photo_graphics/Figure_28.png)

**2.9**

![2.9](/lab_2/photo_graphics/Figure_29.png)

**2.10**

![2.10](/lab_2/photo_graphics/Figure_210.png)

**2.10.1**

![2.10.1](/lab_2/photo_graphics/Figure_2101.png)

**2.11**

![2.11](/lab_2/photo_graphics/Figure_211.png)

**3.1**

![3.1](/lab_2/photo_graphics/Figure_31.png)

**3.2**

![3.2](/lab_2/photo_graphics/Figure_32.png)

**3.3**

![3.3](/lab_2/photo_graphics/Figure_33.png)

**3.4**

![3.4](/lab_2/photo_graphics/Figure_34.png)

**3.5**

![3.5](/lab_2/photo_graphics/Figure_35.png)

**3.6**

![3.6](/lab_2/photo_graphics/Figure_36.png)

**3.7**

![3.7](/lab_2/photo_graphics/Figure_37.png)

**3.8**

![3.8](/lab_2/photo_graphics/Figure_38.png)

**3.9**

![3.9](/lab_2/photo_graphics/Figure_39.png)

**3.10**

![3.10](/lab_2/photo_graphics/Figure_310.png)

**3.11**

![3.11](/lab_2/photo_graphics/Figure_311.png)

**3.12**

![3.12](/lab_2/photo_graphics/Figure_312.png)

**3.13**

![3.13](/lab_2/photo_graphics/Figure_313.png)

**3.14**

![3.14](/lab_2/photo_graphics/Figure_314.png)

**3.15**

![3.15](/lab_2/photo_graphics/Figure_315.png)

**3.16**

![3.16](/lab_2/photo_graphics/Figure_316.png)

**3.17**

![3.17](/lab_2/photo_graphics/Figure_317.png)

**3.18**

![3.18](/lab_2/photo_graphics/Figure_318.png)

**3.19**

![3.19](/lab_2/photo_graphics/Figure_319.png)

**3.20**

![3.20](/lab_2/photo_graphics/Figure_320.png)

**3.21**

![3.21](/lab_2/photo_graphics/Figure_321.png)

**3.22**

![3.22](/lab_2/photo_graphics/Figure_322.png)

**3.23**

![3.23](/lab_2/photo_graphics/Figure_323.png)

**3.23.1**

![3.23.1](/lab_2/photo_graphics/Figure_3231.png)

**3.24**

![3.24](/lab_2/photo_graphics/Figure_324.png)

**3.25**

![3.25](/lab_2/photo_graphics/Figure_325.png)

**3.26**

![3.26](/lab_2/photo_graphics/Figure_326.png)

**3.27**

![3.27](/lab_2/photo_graphics/Figure_327.png)

**3.28**

![3.28](/lab_2/photo_graphics/Figure_328.png)

**3.29**

![3.29](/lab_2/photo_graphics/Figure_329.png)

## Отчет - График функции и касательная (вариант 11)

## Задание

Выбрать одну из непрерывных функций своего варианта, построить её график и касательную к ней. Добавить на график заголовок, подписи осей, легенду, сетку, а также аннотацию к точке касания.

## Выбранная функция

Была выбрана кусочная функция:

$$
f(x) = 
\begin{cases} 
-\cos(e^{x}), & 0 \leq x \leq 1; \\ 
\ln(2x + \sin(x^{2})), & 1 < x \leq 2. 
\end{cases}
$$


## Процесс решения

### 1. Реализация функции

Функция задана двумя ветвями.

```python
def f(x):
    x = np.asarray(x)
    result = np.zeros_like(x)
    mask1 = (x >= 0) & (x <= 1)
    result[mask1] = -np.cos(np.exp(x[mask1]))
    mask2 = (x > 1) & (x <= 2)
    result[mask2] = np.log(2 * x[mask2] + np.sin(x[mask2] ** 2))
    return result
```

### 2. Производная функции

Для построения касательной необходимо найти производную $f'(x)$.
В коде производная реализована как скалярная функция:

```python
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

x0 = 1.5
y0 = f(x0)
f_prime_x0 = derivative(f, x0)
```

### 3. Построение графика

График включает:
- **Синюю кривую** — ветви графика
- **Красную пунктирную линию** — касательная
- **Аннотацию** с координатами точки касания
- Заголовок, подписи осей, легенду и сетку

## Результат

![График функции и касательная](/lab_2/photo_graphics/Figure_10_Variant.png)

Касательная проведена в точке $x_0 = 0.7$, где $y_0 \approx 0.2826$ и угловой коэффициент $k \approx 0.9773$.

## Список использованных источников

1. [Matplotlib documentation](https://matplotlib.org/stable/contents.html)
2. [Matplotlib cheatsheets and handouts](https://matplotlib.org/cheatsheets/)
3. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
4. [Writing mathematical expressions on GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)