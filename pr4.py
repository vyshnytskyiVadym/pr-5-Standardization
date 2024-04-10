class Processor:
    def __init__(self, brand, model, architecture, frequency, cores, cache, socket):
        self.brand = brand
        self.model = model
        self.architecture = architecture
        self.frequency = frequency  # GHz
        self.cores = cores
        self.cache = cache  #  MB
        self.socket = socket

    def overclock(self, increase):
        self.frequency += increase
        print(f"The processor frequency has been increased to {self.frequency} GHz.")


def main():
    brand = input("Enter processor brand: ")
    model = input("Enter processor model: ")
    architecture = input("Enter processor architecture: ")
    frequency = float(input("Enter processor frequency (GHz): "))
    cores = int(input("Enter number of processor cores: "))
    cache = float(input("Enter processor cache size (MB): "))
    socket = input("Enter processor socket type: ")

    processor = Processor(brand, model, architecture, frequency, cores, cache, socket)

    print("\nProcessor information:")
    print("Brand:", processor.brand)
    print("Model:", processor.model)
    print("Architecture:", processor.architecture)
    print("Frequency:", processor.frequency, "GHz")
    print("Cores:", processor.cores)
    print("Cache:", processor.cache, "MB")
    print("Socket:", processor.socket)

    increase_frequency = float(input("\nEnter the amount to overclock the processor (GHz): "))
    processor.overclock(increase_frequency)


if __name__ == "__main__":
    main()
