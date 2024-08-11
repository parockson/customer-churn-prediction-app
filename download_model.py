import requests

def download_model(url, output_path):
    # Extract file ID from the URL
    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {output_path}")
    else:
        print(f"Failed to download {url}")

# URLs for the model files
model_urls = {
    'XGBClassifier': 'https://drive.google.com/file/d/1S7OOihqHqjYNsYvLPj1wQZgyxvkImPPL/view?usp=sharing',
    'RandomForest': 'https://drive.google.com/file/d/1H_r_xgKjr8ScRq1IsyoxLWPXtjBZeIK-/view?usp=sharing',
    'LGBM': 'https://drive.google.com/file/d/1kLkfXyUH9kGY8u4WkX2vMJny22zrKzME/view?usp=sharing'
}

# Download the model files
for model_name, url in model_urls.items():
    download_model(url, f'best_models/{model_name}_pipeline.joblib')
