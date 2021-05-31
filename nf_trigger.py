import requests
import os
from google.cloud import secretmanager

def nf_trigger(event, context):

    try :
        
        # GCS file Event (Create/Finalize)
        file = event
        print("New file added to the Input Bucket") 
        print(f"Processing file: {file['name']}.")  

        # Nextflow Tower token, URI and Launch ID
        nf_token=f"< YOUR NEXTFLOW TOKEN HERE >"
        nf_tower_uri = "https://api.tower.nf/actions/< YOUR LAUNCH ID HERE >/launch/?"

        # Header parameters for the HTTP request - Authentication token & Content Type
        nf_auth_header = {u'Authorization' : 'Bearer {}'.format(nf_token),'Content-Type': 'application/json'}
        
        # Workflow Parameters to send as input to the Workflow in the HTTP request - POST Operation
        params = {"params":{"foo":f"Hello New file {event['bucket']}/{file['name']}"}}

        # Make HTTP API request to tower nf to launch nextflow Launch ID.
        print("Trying to trigger worklow configured on nextflow tower with Launch ID") 
        response = requests.post(nf_tower_uri, json=params, headers=nf_auth_header)
        results = response.content
        print(response.content)

    except Exception as e:
        print(e)