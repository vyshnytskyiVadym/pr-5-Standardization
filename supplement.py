from processor_library import Processor

def create_processor():
    brand = input("Enter processor brand: ")
    model = input("Enter processor model: ")
    architecture = input("Enter processor architecture: ")
    frequency = float(input("Enter processor frequency (GHz): "))
    cores = int(input("Enter number of processor cores: "))
    cache = float(input("Enter processor cache size (MB): "))
    socket = input("Enter processor socket type: ")
    price = float(input("Enter processor price (USD): "))

    return Processor(brand, model, architecture, frequency, cores, cache, socket, price)

def main():
    num_processors = int(input("Enter the number of processors: "))
    processors = []

    for i in range(num_processors):
        print(f"\nEnter details for processor {i+1}:")
        processor = create_processor()
        processors.append(processor)

    print("\nProcessor information:")
    for i, processor in enumerate(processors):
        print(f"\nProcessor {i+1}:")
        print("Brand:", processor.brand)
        print("Model:", processor.model)
        print("Architecture:", processor.architecture)
        print("Frequency:", processor.frequency, "GHz")
        print("Cores:", processor.cores)
        print("Cache:", processor.cache, "MB")
        print("Socket:", processor.socket)
        print("Price:", processor.price, "USD")

if __name__ == "__main__":
    main()
