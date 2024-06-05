import sys

def generate_html(api_key, api_url, template_file, output_file):
    try:
        # Read the template file
        with open(template_file, 'r') as file:
            content = file.read()

        # Replace placeholders with actual values
        content = content.replace("{API_KEY}", f"\"{api_key}\"")
        content = content.replace("{{API_URL}}", f"\"{api_url}\"")

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(content)
        
        print(f"Generated {output_file} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python generate_html.py <api_key> <api_url> <template_file> <output_file>")
        sys.exit(1)

    api_key = sys.argv[1]
    api_url = sys.argv[2]
    template_file = sys.argv[3]
    output_file = sys.argv[4]

    generate_html(api_key, api_url, template_file, output_file)