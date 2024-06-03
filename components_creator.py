import os
import shutil
from private_variables import *
# from gpt_components_filder import main as gpt_components_main
from utils import GetRelevantComponents, CreateComponentContent


def copy_components(components, source_dir, target_dir):
    for component in components:
        component_path = os.path.join(source_dir, component)
        if os.path.exists(component_path):
            shutil.copytree(component_path, os.path.join(target_dir, component))
        else:
            print(f"Component {component} does not exist in {source_dir}")



def get_relevant_components(all_components, user_prompt):
    components_selector = GetRelevantComponents()
    return components_selector(all_components, user_prompt)
    

def get_relevant_content(component_name, component_content, user_prompt):
    component_editor = CreateComponentContent()
    return component_editor(component_name, component_content, user_prompt)



def get_file_content(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
    file.close()
    return file_content

def main():
    # Currently asking components, but will analyze the contents of the user prompt and generate components
    user_prompt = input("Enter the components required (comma-separated): ")
    all_components = os.listdir('all_components')

    relevant_components = get_relevant_components(all_components, user_prompt)


    # Define the source and target directories
    source_dir = 'all_components'
    target_dir = os.path.join(os.getcwd(), "nextjs_custom_application", 'components')
    os.makedirs(target_dir, exist_ok=True)
    copy_components(relevant_components, source_dir, target_dir)

    print(f"New Next.js project 'nextjs_custom_application'' created with components: {', '.join(relevant_components)}")

    # Now, for every component, we've got to generate new content as per the user prompt
    for component in relevant_components:
        file_content = get_file_content(target_dir+"/"+component+f"/{component}.tsx")
        new_content_with_context = get_relevant_content(component, file_content, user_prompt)
        
        with open(target_dir+"/"+component+f"/{component}.tsx", "w") as file:
            file.write(new_content_with_context)
            print(f"Written into {component} successfully !")
        file.close()


if __name__ == "__main__":
    main()
