import json
import ndjson
import ast
from google.cloud import storage
from firebase_admin import credentials, firestore,initialize_app
cred = credentials.Certificate('serviceAccountKey.json')
initialize_app(cred)
db = firestore.client()

def cleanup(event,context):

    # Read the data from Google Cloud Storage
    read_storage_client = storage.Client()

    # Set buckets and filenames
    bucket_name = event["bucket"]
    filename = event["name"]

    # get bucket with name
    bucket = read_storage_client.get_bucket(bucket_name)

    # get bucket data as blob
    blob = bucket.get_blob(filename)

    # convert to string
    json_data_string = blob.download_as_text()
    #json_data = ndjson.loads(json_data_string)
    #json_data = ndjson.loads(json_data_string)
    data = ast.literal_eval(json_data_string)
    #data = json.load(json_data)

    annotation_results = data["annotation_results"]

    output_json = {"input_uri": "", "segment_label_annotations": [], "shot_label_annotations": [], "face_detection_annotations": [], "explicit_annotations": [], "text_annotations": [], "object_annotations": [], "person_detection_annotations": [], "speech_transcriptions": []}
    for annotation_result in annotation_results:
        output_json["input_uri"] = annotation_result["input_uri"]

        #print(annotation_result["input_uri"])
        if "segment_label_annotations" in annotation_result:
        
            for i in annotation_result["segment_label_annotations"]:
                if "entity" in i and "description" in i["entity"]:
                    output_json["segment_label_annotations"].append(i["entity"]["description"])
                
            #print(annotation_result["segment_label_annotations"][0]["entity"]["description"])
        
        if "shot_label_annotations" in annotation_result:
        
            for i in annotation_result["shot_label_annotations"]:
               if "entity" in i and "description" in i["entity"]:
                    output_json["shot_label_annotations"].append(i["entity"]["description"])
                #print(i["entity"]["description"])
            

        if "text_annotations" in annotation_result:
            for i in annotation_result["text_annotations"]:
                if "text" in i:
                    output_json["text_annotations"].append(i["text"])
                #print(i["text"])

        if "object_annotations" in annotation_result:
            for i in annotation_result["object_annotations"]:
               if "entity" in i and "description" in i["entity"]:
                    output_json["object_annotations"].append(i["entity"]["description"])
                #print(i["entity"]["description"])

    

      
                        
    
    #output_json = json.dumps(output_json)
    db.collection("video-json").add(output_json)
    # Write the data to Google Cloud Storage
    # write_storage_client = storage.Client()

    # write_storage_client.get_bucket(bucket_name) \
    #     .blob(filename) \
    #     .upload_from_string(result)