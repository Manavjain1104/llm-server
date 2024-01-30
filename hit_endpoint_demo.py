import requests
import json

if __name__ == "__main__":
    address = 'http://127.0.0.1:5000/'
    single_data = "This is an Italian interpreter job. You must know italian"
    many_data = ["This is a test", "This is another test"]
    json_single_data = json.dumps(single_data)
    json_many_data = json.dumps(many_data)

    headers = {'Content-Type': 'application/json'}
    summary_response = requests.post(address + "/get_skills_required", data=json_single_data, headers=headers)
    # embedding_response = requests.post(address + "get_embedding", data=json_single_data, headers=headers)
    # bulk_embedding_response = requests.post(address + "get_embeddings", data=json_many_data, headers=headers)

    if summary_response.status_code == 200:
        summary = summary_response.json()['answer']
        print(f"Summary: {summary}")
    else:
        print(f"Error: {summary_response.status_code}, {summary_response.json()}")
    #
    # if embedding_response.status_code == 200:
    #     embedding = embedding_response.json()['embedding']
    #     print(f"Embedding: {embedding}")
    # else:
    #     print(f"Error: {embedding_response.status_code}, {embedding_response.json()}")
    #
    # if bulk_embedding_response.status_code == 200:
    #     bulk_embedding = bulk_embedding_response.json()['embeddings']
    #     print(f"Bulk Embedding: {bulk_embedding}")
    # else:
    #     print(f"Error: {bulk_embedding_response.status_code}, {bulk_embedding_response.json()}")

