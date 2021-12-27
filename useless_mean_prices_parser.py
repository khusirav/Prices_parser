import urllib.request
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean

url_to_parse = urllib.request.urlopen("https://www.avito.ru/rossiya")
parsed_HTML = url_to_parse.read().decode("utf8")

file = open("parsed_HTML.txt", mode = "w", encoding = "utf-8")
file.write(parsed_HTML)
file.close()
url_to_parse.close()
prices_list = []
is_not_last = True

while is_not_last:    
    try:
        start_index = parsed_HTML.index("<meta itemProp=\"price\" content=\"") + len("<meta itemProp=\"price\" content=\"")
    except ValueError:
        print("Последнее вхождение найдено")
        is_not_last = False
        break
    stop_index = parsed_HTML.index("\"", start_index)
    try:
        prices_list.append(int(parsed_HTML[start_index:stop_index]))
    except ValueError:
        pass
    parsed_HTML = parsed_HTML[stop_index:]

mean_list = []
prices_mean = mean(prices_list)
for i in prices_list:
    mean_list.append(prices_mean)


print('Список цен:\n', prices_list)
print('Среднее значение цены:\n', round(prices_mean))
plt.plot(prices_list)
plt.plot(mean_list, color = 'red')
plt.show()