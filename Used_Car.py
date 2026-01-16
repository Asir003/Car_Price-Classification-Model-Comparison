def main():
    
    # Initialize predictor
    predictor = CarPricePredictor(csv_file='Used Car Dataset.csv')
    
    # Run complete pipeline
    predictor.run_complete_pipeline()


if __name__ == "__main__":
    main()
