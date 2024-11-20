from taxi import Taxi

def main():
    p1 = Taxi(name='Prius 1', fuel=100, price_per_km=1.23)
    p1.drive(40)
    print(p1)

main()