# def count_ways(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2

#     # Используем динамическое программирование для хранения количества путей
#     # для каждой позиции на числовой прямой.
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2

#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]

# n = int(input("Введите значение n: "))
# print("Количество различных маршрутов кузнечика до точки", n, ":", count_ways(n))


# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def kth_smallest(arr, low, high, k):
#     if k > 0 and k <= high - low + 1:
#         partition_index = partition(arr, low, high)
#         if partition_index - low == k - 1:
#             return arr[partition_index]
#         if partition_index - low > k - 1:
#             return kth_smallest(arr, low, partition_index - 1, k)
#         return kth_smallest(arr, partition_index + 1, high, k - partition_index + low - 1)
#     return None

# # Пример использования:
# arr = [12, 3, 5, 7, 4, 19, 26]
# k = 3
# result = kth_smallest(arr, 0, len(arr) - 1, k)
# if result is not None:
#     print(f"{k}-ая порядковая статистика в массиве: {result}")
# else:
#     print("Ошибка: некорректное значение k или массив пустой.")

# def find_largest(arr):
#     if not arr:
#         return None  # если массив пустой, вернуть None

#     largest = arr[0]  # предполагаем, что первый элемент - наибольший

#     for num in arr:
#         if num > largest:
#             largest = num  # если находим больший элемент, обновляем наибольший

#     return largest

# # Пример использования:
# array = [5, 2, 7, 1, 9, 3]
# print("Наибольший элемент в массиве:", find_largest(array))

# def minimum_interval_cover(intervals, range_start, range_end):
#     intervals.sort(key=lambda x: x[1])  # Сортируем интервалы по правым концам
#     min_intervals = []  # Наименьшее количество интервалов для покрытия
#     current_position = range_start
    
#     while current_position < range_end:
#         # Ищем первый интервал, который покрывает текущую позицию
#         selected_interval = None
#         for interval in intervals:
#             if interval[0] <= current_position <= interval[1]:
#                 selected_interval = interval
#                 break
        
#         if selected_interval:
#             min_intervals.append(selected_interval)  # Добавляем интервал в покрытие
#             current_position = selected_interval[1] + 1  # Обновляем текущую позицию
#         else:
#             return "Невозможно покрыть заданный диапазон"  # Если не найден подходящий интервал
    
#     return min_intervals

# # Пример использования
# intervals = [(1, 3), (2, 4), (3, 6), (5, 7), (8, 10)]
# range_start = 1
# range_end = 8
# result = minimum_interval_cover(intervals, range_start, range_end)
# if result != "Невозможно покрыть заданный диапазон":
#     print("Минимальное количество интервалов для покрытия диапазона:", len(result))
#     print("Интервалы:", result)
# else:
#     print(result)

# 

# import heapq

# def prim(graph):
#     """
#     Реализация алгоритма Прима для построения минимального остовного дерева (MST).
    
#     :param graph: Словарь, представляющий взвешенный неориентированный граф.
#                   Ключи - вершины, значения - списки кортежей (соседняя вершина, вес ребра).
#     :return: Список ребер минимального остовного дерева.
#     """
#     start_vertex = next(iter(graph))  # Выбираем произвольную стартовую вершину
#     mst = []  # Список для хранения ребер минимального остовного дерева
#     visited = set([start_vertex])  # Множество посещенных вершин
#     edges = [(weight, start_vertex, to) for to, weight in graph[start_vertex]]  # Мини-куча ребер
#     heapq.heapify(edges)

#     while edges:
#         weight, frm, to = heapq.heappop(edges)
#         if to not in visited:
#             visited.add(to)
#             mst.append((frm, to, weight))

#             for next_to, next_weight in graph[to]:
#                 if next_to not in visited:
#                     heapq.heappush(edges, (next_weight, to, next_to))
    
#     return mst

# # Пример графа
# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('C', 3), ('D', 2)],
#     'C': [('A', 4), ('B', 3), ('D', 5)],
#     'D': [('B', 2), ('C', 5)]
# }

# mst = prim(graph)
# print("Ребра минимального остовного дерева:")
# for edge in mst:
#     print(edge)

# import itertools

# def calculate_total_distance(permutation, distance_matrix):
#     total_distance = 0
#     num_cities = len(permutation)
#     for i in range(num_cities):
#         total_distance += distance_matrix[permutation[i]][permutation[(i + 1) % num_cities]]
#     return total_distance

# def tsp_brute_force(distance_matrix):
#     num_cities = len(distance_matrix)
#     min_distance = float('inf')
#     best_permutation = None

#     # Generate all permutations of city indices
#     for permutation in itertools.permutations(range(num_cities)):
#         current_distance = calculate_total_distance(permutation, distance_matrix)
#         if current_distance < min_distance:
#             min_distance = current_distance
#             best_permutation = permutation
    
#     return best_permutation, min_distance

# # Example usage:
# distance_matrix = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# best_route, min_distance = tsp_brute_force(distance_matrix)
# print("Best route:", best_route)
# print("Minimum distance:", min_distance)

# import math

# n = int(input("n:"))
# summ = sum(1 / i for i in range(1, n + 1))
# result = summ - math.log(n)

# print(result)
# import pygame
# import sys

# # Константы
# WIDTH, HEIGHT = 800, 600
# MATCH_LENGTH = 100
# MATCH_WIDTH = 10
# BACKGROUND_COLOR = (30, 30, 30)
# MATCH_COLOR = (200, 100, 50)

# # Инициализация pygame
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Головоломка со спичками")
# clock = pygame.time.Clock()

# # Класс спички
# class Matchstick:
#     def __init__(self, x, y, angle):
#         self.x = x
#         self.y = y
#         self.angle = angle
#         self.rect = pygame.Rect(x, y, MATCH_LENGTH, MATCH_WIDTH)

#     def draw(self, screen):
#         rotated_surface = pygame.Surface((MATCH_LENGTH, MATCH_WIDTH), pygame.SRCALPHA)
#         rotated_surface.fill(MATCH_COLOR)
#         rotated_surface = pygame.transform.rotate(rotated_surface, self.angle)
#         screen.blit(rotated_surface, (self.x, self.y))

# # Создание спичек
# matches = [
#     Matchstick(200, 300, 0),
#     Matchstick(300, 300, 90),
#     Matchstick(400, 300, 0),
#     Matchstick(500, 300, 90)
# ]

# running = True
# while running:
#     screen.fill(BACKGROUND_COLOR)
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # Отрисовка спичек
#     for match in matches:
#         match.draw(screen)
    
#     pygame.display.flip()
#     clock.tick(30)

# pygame.quit()
# sys.exit()

import mpmath

def вычислить_константы(точность):
    mpmath.mp.dps = точность  # Устанавливаем точность
    константы = {
        "Число Пи": mpmath.pi,
        "Число Эйлера (e)": mpmath.e,
        "Золотое сечение (φ)": (1 + mpmath.sqrt(5)) / 2,
        "Число Авогадро (N_A)": 6.02214076e23,  # Точная фиксированная величина
        "Постоянная Планка (h)": 6.62607015e-34,  # Точная фиксированная величина
        "Скорость света (c)": 299792458,  # Точная фиксированная величина (м/с)
        "Элементарный заряд (e)": 1.602176634e-19,  # Точная фиксированная величина
        "Постоянная Больцмана (k_B)": 1.380649e-23  # Точная фиксированная величина
    }
    
    return константы

# Пример использования
точность = int(input("Введите желаемую точность (количество знаков после запятой): "))
константы = вычислить_константы(точность)

for имя, значение in константы.items():
    print(f"{имя}: {значение}")
