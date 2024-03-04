import requests
import json

if __name__ == "__main__":
    address = 'http://127.0.0.1:5000/'
    single_data = "Early Years Play Leader:Early Years Play Leader Level 3 Early Years Educator Apprentice at Little Pips Nursery Programme Team Leader – Employment Early Years (Nursery) Room Leader Level 2 Early Years Practitioner Apprentice at Little Pips Nursery KS2 Phase Leader Early Years Early Years PRACTITIONER/PLAYWORKER VACANCY KS2 Phase Leader \
Level 3 Teaching Assistant Apprenticeship at Kingsmead School:Level 3 Teaching Assistant Apprenticeship at Kingsmead School Care Assistant Long-term ICT teaching job in Trafford - outstanding school Graduate Learning Support Assistant SEND Teaching Assistant Teaching Assistant KS2 Teacher - 'Outstanding' School Teaching Assistant Primary School Teacher Creative Teaching Assistant \
Drama Teacher:Drama Teacher Swimming Teacher / Instructor Science Teacher \
Receptionist:Receptionist \
Senior Operations Officer:Senior Operations Officer \
Customer Service Advisor:Customer Service Advisor \
Children's Support Worker - No experience required:Children's Support Worker - No experience required School-Experienced Administrator Job - Mansfield People Administrator Support Student Experience Manager \
Regional Training Coordinator:Regional Training Coordinator"
    # many_data = ["This is a test", "This is another test"]
    json_single_data = json.dumps(single_data)
    # json_many_data = json.dumps(many_data)

    headers = {'Content-Type': 'application/json'}
    summary_response = requests.post(address + "/generate_text", data=json_single_data, headers=headers)
    # embedding_response = requests.post(address + "get_embedding", data=json_single_data, headers=headers)
    # bulk_embedding_response = requests.post(address + "get_embeddings", data=json_many_data, headers=headers)

    if summary_response.status_code == 200:
        summary = summary_response.json()['answer']
        print(f"Summary: {summary}")
    else:
        print(f"Error: {summary_response.status_code}, {summary_response.json()}")

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

