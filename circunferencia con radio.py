def radio_circunferencia(radio):
    return 2 * 3.141593 * radio

radios=[5, 8, 10]

for radio in radios:
    circunferencia=radio_circunferencia(radio)
    print(f"La circunferencia con un radio de {radio} es: {circunferencia:.6f}")