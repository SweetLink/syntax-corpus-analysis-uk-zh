import matplotlib.pyplot as plt
import numpy as np
# Документація: https://matplotlib.org/stable/users/explain/text/index.html


# Значення осі x axis
x = [1, 2, 3, 4, 5, 6, 7]
# Значення осі y
y = [17.5, 14.7, 13.1, 18.7, 14.9, 26.3, 19.9]

plt.style.use('ggplot')
# Визначення діапозону показників на осях  x та y
plt.ylim(5, 30)
plt.xlim(0, 8)


# Вибір стилю полотна графіка  

# Побудова позначок графіка
plt.plot(x, y, color='#2F4F4F', linestyle=':', linewidth=2,
         marker='o', markerfacecolor='#8A2BE2', markersize=7)


# Іменування осей та показників осі х
plt.xlabel('Chronological segments of the translated text (5 sentences each)',
           fontweight='semibold', color='#2F4F4F')
x_labels = ['1–5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35']
plt.xticks(x, x_labels)
plt.ylabel('BLEU-score', fontweight='semibold', color='#2F4F4F')

# Назва графіка
plt.title('Distribution of NMP quality during DeepL operation cycle (by BLEU metric)',
          fontsize=14, fontweight='bold', pad=20)

# Відображення графіка
plt.show()
