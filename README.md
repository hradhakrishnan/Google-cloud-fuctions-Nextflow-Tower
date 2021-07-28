# Google cloud functions - Nextflow Tower - Lifesciences API

## Overview

 This Google cloud function demonstrates how to take a serverless approach to automate execution of pipeline jobs on Nextflow Tower based on a event trigger. e.g In this example we are considering a new file being created in a GCS bucket.

 The functions uses API calls to a configured workflow/Actions on `Seqera Nextflow Tower` which in turn triggers the pipeline on `Google cloud lifescience API` or your preferred compute environment. This allows us to automate execution of pipeline jobs based on file events on GCP. The function can be easily modified to adopt to other bioinformatic tools out there.


For additional API references for `Nextflow tower`  and configuring lifesciences API, please refer to their API documentation and examples. 

`Cloud Life Sciences API` provides a simple way to execute a series of Compute Engine containers on Google Cloud.

Also refer to `https://cloud.google.com/community/tutorials/secrets-manager-python` on using secret manager to store Nextflow tokens

![alt text](https://github.com/hradhakrishnan/Google-cloud-fuctions-Nextflow-Tower/blob/main/nf-tower.png) 
