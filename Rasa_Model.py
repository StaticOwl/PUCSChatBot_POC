import os
import rasa
import nest_asyncio

nest_asyncio.apply()
print("Event loop ready.")

from rasa.cli.scaffold import create_initial_project

def create_project(project_name):
    create_initial_project(project_name)
    os.chdir(project_name)
    print(os.listdir("."))

def create_yml_file(yml_path, rasa_txt_path):
    with open(rasa_txt_path, 'r') as rasa_file:
        rasa_content = rasa_file.read()

    with open(yml_path, 'w') as yml_file:
        yml_file.write(rasa_content)

def train(config, training_files, domain, output):
    print(config, training_files, domain, output)
    model_path = rasa.train(domain, config, [training_files], output)
    return model_path

def test(model_path, endpoints=None):
    from rasa.jupyter import chat
    chat(model_path, endpoints)

def evaluation():
    !rasa test

# Define file paths
nlu_yml_path = '/content/PFW Chatbot/data/nlu.yml'
rasa_nlu_txt_path = '/content/Rasa_nlu.txt'
domain_yml_path = '/content/PFW Chatbot/domain.yml'
rasa_domain_txt_path = '/content/Rasa_domain.txt'
stories_yml_path = '/content/PFW Chatbot/data/stories.yml'
rasa_stories_txt_path = '/content/Rasa_stories.txt'

# Create the project and train the chatbot
create_project("PFW Chatbot")
create_yml_file(nlu_yml_path, rasa_nlu_txt_path)
create_yml_file(domain_yml_path, rasa_domain_txt_path)
create_yml_file(stories_yml_path, rasa_stories_txt_path)

# Define training parameters
config = "config.yml"
training_files = "data/"
domain = "domain.yml"
output = "models/"

#Examples

# # # Train the chatbot
# model_path=train(config, training_files, domain, output)

# # # Test the chatbot
# test(model_path.model)

# # # Evaluate the chatbot
# evaluation()
