# Simple Flask app on Cloud Run
The purpose of the project is to provide Exchange Rates Data API for a simple-retail-pipeline-on-Google-Cloud project.

## How to do this
Note: To do this you need access to a project that links to Billing Account. (There is Free Trial if you're new to Google Cloud)
<br>

**Step 1:** Create Fake data (In test/create_exchage_rate.ipynb)  

**Step 2:** Activate Cloud Shell and Set PROJECT_ID
```
gcloud config set project [PROJECT_ID]
```
**Step 3:** Create folder app
```
mkdir app
```
```
cd app
```
**Step 4:** Upload all files from this repo  
**Step 5:** Run command
```
gcloud run deploy --source .
```
**Step 6:** Point your browser to Cloud Run page there will be the url endpoint of your app  

## Here is my result
https://gbp-to-thb-4tbescyvrq-ts.a.run.app/