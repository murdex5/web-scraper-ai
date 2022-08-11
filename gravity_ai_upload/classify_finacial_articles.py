from gravityai import gravityai as grav
import pickle
import pandas as pd


model = pickle.load(open('financiak_text_clasifiier.pkl', 'rb'))
tfigf__vectorizer = pickle.load(open('financial_text_vectorizer.pkl', 'rb'))
label_encoder = pickle.load(open('financial_text_encoder', 'rb'))

def process(inPath, outPath):
    # read input file
    input_df = pd.read_csv(inPath)
    # vectorize the data
    features = tfigf__vectorizer.transform(input_of['body'])
    # predict the classes
    predictions = model.predict(features)
    # convert output labels to categorize
    input_df['category'] = label_encoder.inverse_categorize(predictions)
    # save results to csv
    output_df = input_df[['id', 'category']]
    output_df.to_csv(outPath, index=False)
    
    
grav.wait_for_requests(process)