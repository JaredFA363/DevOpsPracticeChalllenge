# Goal:

Create a static website deployment pipeline that works locally with Terraform, generates content with Python, and is automated with GitHub Actions.


### Part 1 – Python (Content Generator)

Write a Python script that:

Generates a simple index.html file.

The HTML should include:

A random quote or joke (pulled from a local JSON file, not an API).

A timestamp of when the file was generated.

Output: index.html in a build/ folder.


### Part 2 – Terraform (Local Infrastructure)

Use Terraform to:

Provision a local file server simulation.

This should:

Create a directory (e.g., output_site/).

Copy the index.html from build/ into output_site/.

💡 Hint: You can use Terraform’s local_file resource for file handling since no cloud is involved.


### Part 3 – GitHub Actions (CI/CD Pipeline)

Create a GitHub Actions workflow (.github/workflows/deploy.yml) that:

Runs the Python script to generate index.html.

Runs Terraform to "deploy" the file to the output_site/ folder.

Uploads the output_site/ folder as an artifact so you can download it from the Actions run.
