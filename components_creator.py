import os
import shutil
from private_variables import *


def copy_components(components, source_dir, target_dir):
    for component in components:
        component_path = os.path.join(source_dir, component)
        if os.path.exists(component_path):
            shutil.copytree(component_path, os.path.join(target_dir, component))
        else:
            print(f"Component {component} does not exist in {source_dir}")

def main():
    # Currently asking components, but will analyze the contents of the user prompt and generate components
    components = input("Enter the components required (comma-separated): ").split(',')
    components = [component.strip() for component in components]

    # Define the source and target directories
    source_dir = 'all_components'
    target_dir = os.path.join(os.getcwd(), "nextjs_custom_application", 'components')
    os.makedirs(target_dir, exist_ok=True)
    copy_components(components, source_dir, target_dir)

    print(f"New Next.js project 'nextjs_custom_application'' created with components: {', '.join(components)}")


    # Now, since the required components are copied, They should be edited according to the user prompt
    

if __name__ == "__main__":
    main()
