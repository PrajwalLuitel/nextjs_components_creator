import hashlib
import os
import shutil
import re
import json
import time

def generate_hash(file_path, line_number):
    hash_object = hashlib.sha256(f"{file_path}:{line_number}".encode())
    return hash_object.hexdigest()

def find_matches(directory, patterns, image_extensions=('.png', '.jpg', '.jpeg', '.svg')):
    results = {}
    image_files = []

    for root, dirs, files in os.walk(directory):
        if 'assets' in root.split(os.sep):
            for file in files:
                if file.endswith(image_extensions):
                    full_path = os.path.join(root, file)
                    image_files.append({
                        "file_path": full_path,
                        "file_name": file
                    })

        for file in files:
            if file.endswith(('.tsx', '.js', '.css', '.html')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, 1):
                        for key, pattern in patterns.items():
                            if re.search(pattern, line, re.IGNORECASE):
                                match_hash = generate_hash(file_path, line_number)
                                if key not in results:
                                    results[key] = []
                                results[key].append({
                                    "hash": match_hash,
                                    "file_path": file_path,
                                    "line_number": line_number,
                                    "original_line": line.strip(),
                                    "pattern_matched": key
                                })
    results['Image Files'] = image_files
    return results

def create_staging_directory(original_dir, staging_dir):
    if os.path.exists(staging_dir):
        shutil.rmtree(staging_dir)  # Remove staging directory if it exists
    shutil.copytree(original_dir, staging_dir)  # Copy all files to the staging directory

def replace_text_in_staging(staging_dir, file_path, line_number, new_text):
    print(f"Staging directory: {staging_dir}")
    print(f"File path: {file_path}")
    # staged_file_path = file_path.replace(original_dir, staging_dir)
    staged_file_path = file_path
    with open(staged_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines[line_number - 1] = new_text + '\n'  # Replace the line with new text
    with open(staged_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def process_replacements_in_staging(staging_dir, replacements):
    for replacement in replacements:
        replace_text_in_staging(staging_dir, replacement['file_path'], replacement['line_number'], replacement['new_text'])

def save_results_to_file(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

def main():
    original_dir = "all_components"
    staging_dir = "nextjs_custom_application/components"

    try:
        os.mkdir(staging_dir)
    except:
        pass
    output_file = 'match_results.json'


    patterns = {
    "Header": r"Header|Logo|Navigation|Home|Leads|Warmup|Pricing|About|Get Started",
    "Hero Section": r"10x your leads|scales your outreach campaigns|unlimited e-mails sending accounts|b2b lead database|generative AI",
    "Infinite Unlimited Accounts": r"Infinitely Scale Your Outreach with Unlimited Accounts|Start For Free",
    "Features": r"Raclette Blueberry Nextious Level|Photo booth fam kinfolk cold-pressed sriracha leggings jianbing microdosing tousled waistcoat|Ennui Snackwave Thundercats|Ennui Selvage Poke Waistcoat Godard",
    "Unlimited Warmup": r"Reach Your Prospects Inbox with Unlimited Warmup",
    "Success Quantified": r"2\.7K Downloads|1\.3K Users|74 Files|46 Places",
    "Respond Box": r"Respond to Leads and Close Dealswith Unibox|Managing 1 inbox is easy",
    "Pricing": r"START|Free|PRO|\$38/mo|BUSINESS|\$56/mo|Vexillologist pitchfork|Tumeric plaid portland|Mixtape chillwave tumeric|Hexagon neutra unicorn",
    "Campaign Analytics": r"Optimize with Campaign Analytics",
    "How It Works": r"HOW ITS WORKS|Our teams of strategists, data scientists",
    "Testimonial": r"Synth chartreuse iPhone lomo cray raw denim brunch everyday carry neutra|Holden Caulfield|Alper Kamu",
    "Community": r"Learn From The Best in Our Private Community",
    "Successful Reviews": r"Edison bulb retro cloud bread echo park, helvetica stumptown taiyaki taxidermy 90's cronut",
    "FAQ": r"Protect Your Deliverable With E-mail Validation Bulk Domain Testing|Clean & verify your lead lists|one-click bulk domain tester",
    "About Us": r"KeenSight Analytics companies provide businesses with valuable insights from data",
    "Contact Us": r"For any questions or inquiries feel free to send us an email",
    "Footer": r"Keensight Analytics offers expert AI development, cloud software, and full-stack solutions"
}


    create_staging_directory(original_dir, staging_dir)
    match_results = find_matches(staging_dir, patterns)
    save_results_to_file(match_results, output_file)
    print(f"Results have been saved to {output_file}")

    time.sleep(3)

    replacements_request = [
        {
            "file_path": "nextjs_custom_application/components/Banner/Banner.tsx",
            "line_number": 11,
            "new_text": "<p>Hey, the content is replaced . . .</p>"
        }
    ]
    process_replacements_in_staging(staging_dir, replacements_request)
    print("Replacements have been made in the staging directory.")
