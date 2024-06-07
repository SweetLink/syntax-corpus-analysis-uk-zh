import matplotlib.pyplot as plt

# Значення співвідношення NP:VP в сегменті корпусу українською
uk_separate = [
    10.840, 19.667, 13.939, 12.346, 12.279, 13.105, 11.556, 13.419, 12.042, 16.586,
    11.879, 15.282, 10.778, 11.824, 10.346
]

# Значення співвідношення NP:VP в сегменті корпусу китайською
zh_separate = [
    0.748, 0.661, 0.693, 0.676, 0.686, 0.631, 0.724, 0.647, 0.791, 0.717,
    0.744, 0.744, 0.732, 0.711, 0.768
]

# Нормалізування значень в сегменті корпусу українською
max_uk = max(uk_separate)
uk_separate_normalized = [x / max_uk for x in uk_separate]

# Нормалізування значень в сегменті корпусу китайською
max_zh = max(zh_separate)
zh_separate_normalized = [x / max_zh for x in zh_separate]

# Вибір стилю полотна графіка
plt.style.use('ggplot')

# Мітки для осі x
labels = list(range(1, 16))
plt.figure(figsize=(10, 5))

# Визначення діапозону показників на осях  x та y
plt.ylim(0.4,1.2)
plt.xlim(0,16)

# Побудова графіку нормалізованих значень в сегменті корпусу українською
plt.plot(labels, uk_separate_normalized, marker='o', label='Співвіднощення NP:VP в корпусі українською (нормалізовані значення)', color='#8A2BE2', )

#plt.plot(x, y, color='#2F4F4F', linestyle=':', linewidth = 2,  marker='o', markerfacecolor='#8A2BE2', markersize=7)

# Побудова графіку нормалізованих значень в сегменті корпусу китайською
plt.plot(labels, zh_separate_normalized, marker='o', label='Співвіднощення NP:VP в корпусі китайською (нормалізовані значення)', color='#FF8C00',)

# Додавання заголовків і підписів осей
plt.xlabel('Сегменти корпусу (по 10 текстів)')
x_labels = ['1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15']
plt.xticks(labels, x_labels)
plt.ylabel('Нормалізовані значення співвідношення NP:VP')
plt.title('Динаміка зміни співвідношення NP:VP в паралельному корпусі', fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper left')


# Додавання сітки для кращої читабельності
plt.grid(True)

# Відображення графіку
plt.show()
