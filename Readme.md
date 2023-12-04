# Quiz Generator

## Development Process

### Understanding Langchain
Langchain is a language library that facilitates interactions with language models. In this project, we use Langchain to create a multiple-choice quiz generator. The development process involves the following steps:

1. **Integration with Langchain:**
   The `logic.py` file showcases the integration with Langchain. It utilizes the Langchain library to interact with OpenAI's language model.

2. **Prompt Template:**
   A prompt template is created using Langchain's `PromptTemplate` class. This template guides the language model in generating multiple-choice quiz questions based on user input.

3. **Chaining Prompts:**
   The prompts are chained together using Langchain's `LLMChain` class. This chaining allows for a more interactive and dynamic interaction with the language model.

### Dealing with OpenAI API
OpenAI provides powerful language models, and in this project, we utilize the OpenAI API through the Langchain library. The steps include:

1. **Instantiating OpenAI LLM:**
   The `OpenAI` class in `logic.py` is used to instantiate the OpenAI language model.

2. **Generating Questions:**
   The generated questions are based on the specified quiz topic and the number of questions using the OpenAI language model and Langchain's chaining mechanism.

## User Guide

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/quiz-generator.git

2. ```bash
   cd quiz-generator
   
3. ```bash
   pip install -r requirements.txt

4. ```bash
   streamlit run main.py

