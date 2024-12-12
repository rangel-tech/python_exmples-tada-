#Função conversão
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

# Teste Simples
if __name__ == "__main__":
    print("Conversor de Temperatura")
    c = 25
    f = 77
    print(f"{c}°C para Fahrenheit: {celsius_para_fahrenheit(c)}°F")
    print(f"{f}°F para Celsius: {fahrenheit_para_celsius(f)}°C")

