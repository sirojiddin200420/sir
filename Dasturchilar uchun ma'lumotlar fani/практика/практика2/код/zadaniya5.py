import numpy as np

# Допустим, у нас есть 4 изображения размером 3x3
images = np.array([
    [[12, 34, 56],
     [78, 90, 123],
     [145, 167, 189]],

    [[22, 44, 66],
     [88, 100, 133],
     [155, 177, 199]],

    [[32, 54, 76],
     [98, 110, 143],
     [165, 187, 209]],

    [[42, 64, 86],
     [108, 120, 153],
     [175, 197, 219]]
])

# 1. Среднее изображение
mean_image = np.mean(images, axis=0)

# 2. Максимальные и минимальные значения яркости
max_brightness = np.max(images)
min_brightness = np.min(images)

# 3. Нормализация данных
normalized_images = (images - np.min(images)) / (np.max(images) - np.min(images))

print("Тензор изображений:\n", images)
print("Среднее изображение:\n", mean_image)
print("Максимальная яркость:", max_brightness)
print("Минимальная яркость:", min_brightness)
print("Нормализованные изображения:\n", normalized_images)