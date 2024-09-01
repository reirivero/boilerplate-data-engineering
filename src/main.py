from src.extraction.extract_data import extract_from_source_1, extract_from_source_2
from src.transformation.transform_data import transform_data
from src.loading.load_data import load_data
from src.utils.logging_config import setup_logging
from src.utils.config import DATABASE_URL, API_KEY

def main():
    setup_logging()
    
    print(f"Connecting to database at {DATABASE_URL}")
    print(f"Using API key: {API_KEY}")
    
    data1 = extract_from_source_1()
    data2 = extract_from_source_2()
    
    transformed_data1 = transform_data(data1)
    transformed_data2 = transform_data(data2)
    
    load_data(transformed_data1)
    load_data(transformed_data2)

if __name__ == "__main__":
    main()
