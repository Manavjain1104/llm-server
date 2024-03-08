## About The Project

Server for hosting large language models from Hugging face (See link for more details: https://huggingface.co/)

The project implements a RESTful API to allow faster and unrestricted access to models for more efficient data processing.

## Technical Implementation & Database Manegement

The RESTful API is implemented with flask. In the original implementation, the project was deployed on Digital Ocean. The server can also be deployed on other platforms or locally.

### Built With

- Python
- Flask
- Transformers library

#### Models used

1. Sentence-transformers/all-minilm-L12-V2 · hugging face [Internet]. [cited 2024 Feb 28]. Available from: https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2 
2. Falconsai/text_summarization · hugging face [Internet]. [cited 2024 Feb 28]. Available from: https://huggingface.co/Falconsai/text_summarization 
3. Deepset/Roberta-base-squad2 · hugging face [Internet]. [cited 2024 Feb 28]. Available from: https://huggingface.co/deepset/roberta-base-squad2 

## Getting started

To get started with JammyJobber, follow the instructions below.

### Prerequisites

- Set up server hosting service
- Python (version 3.10)
- Flask (version 3.0.1)
- transformers (version 4.37.1)
- sentence-transformers (version 2.2.2)
- See requirements.txt for the full list of dependencies

### Installation on the server running service (or locally)

1. Clone the repo

```sh
  git clone https://github.com/Manavjain1104/llm-server.git
```

2. Install Python packages

```sh
  pip install -r requirements.txt
```

3. Run the server

```python
  python endpoint.py
```

### Usage

1. Make a note of your server's IP address and port 

2. Use endpoints as usual 

3. See example in hit_endpoint_demo.py

## Support

Email kristinaz2682@gmail.com for support and any questions

## Roadmap

Our future plans for the LLM-server include:

- Include other models
- Add other endpoints for existing and new models
- Host a persistent server to deploy the RESTful API publically

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Authors and acknowledgment

This project was created as part of third year group project SEGP in Computing, Imperial College London

- Manav Jain (mj921)
- Krish Maha (krm221)
- Shruti Pradhan (sp1521)
- Max Stupple (mes21)
- Tina Wang (tw1720)
- Kristina Zimina (kz1021)

## License

Distributed under the MIT License

## Acknowledgments

Special thanks to our supervisor, Nuri Cingillioglu, and all contributors who helped make JammyJobber possible!
We couldn't have done it without you!
