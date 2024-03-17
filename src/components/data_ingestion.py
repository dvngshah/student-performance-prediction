import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

#Config class for the inputs required
@dataclass
class DataIngestionConfig: 
    train_data_path: str = os.path.join('artifacts', 'train.csv') 
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        
        try: 
            #Reading the data IMP: here you can read data from any data source such as MongoDB, etc.
            df = pd.read_csv('C:/Users/hello/OneDrive/Desktop/Data Science/archive/StudentsPerformance.csv')

            #creating a train data path via our Dataclass and ingestion config 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            #Saving all data to raw datapath
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            #Initializing train-test split 
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            #Saving just the train data to train datapath
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            #Saving test data to test datapath
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            return(

                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )

        except:
            pass


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data) 

    
