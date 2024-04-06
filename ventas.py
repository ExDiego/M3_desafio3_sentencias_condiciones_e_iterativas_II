

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio:": 21200,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

ventas_filtradas = 40000

ventas_filtradas ={ venta: valor for venta, valor in ventas.items() if valor >= 40000}

print(ventas_filtradas)

