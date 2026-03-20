def process_data(data):
    result = []
    for item in data:
        value = item['value']
        result.append(value * 2)
    return sum(result) / len(result)

if __name__ == "__main__":
    data = [1,2,3,4]
    breakpoint()
    result = process_data(data)