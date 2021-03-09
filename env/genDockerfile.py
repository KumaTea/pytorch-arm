import os
import json
import subprocess

arch = 'arm'
variant = 'v7'

python_versions = ['3.9', '3.8', '3.7', '3.6']
docker_inspect_cmd = 'docker manifest inspect --verbose {image}'
template_file = 'DF_Template'


def get_image_sha256(tag, project='python'):
    print(f'Getting: {project}:{tag}')
    command = docker_inspect_cmd.format(image=f'{project}:{tag}').split()
    result = subprocess.run(command, capture_output=True)
    result_json = json.loads(result.stdout)
    for item in result_json:
        if item['Descriptor']['platform']['architecture'] == arch \
                and item['Descriptor']['platform']['variant'] == variant:
            print('Target image found!')
            return item['Descriptor']['digest']
    raise FileNotFoundError


def mkdir(path_name):
    if not os.path.exists(path_name):
        return os.mkdir(path_name)


def generate_dockerfile(tag, sha256, template, project='python'):
    dockerfile_content = template.replace('%IMAGE_WITH_SHA256%', f'{project}:{tag}@{sha256}')
    dockerfile_path = 'py' + tag.replace('.', '')
    mkdir(dockerfile_path)
    with open(f'{dockerfile_path}/Dockerfile', 'w') as f:
        f.write(dockerfile_content)


if __name__ == '__main__':
    with open(template_file) as temp_f:
        template_content = temp_f.read()

    for version in python_versions:
        image_sha256 = get_image_sha256(version)
        generate_dockerfile(version, image_sha256, template_content)
        print('Python', version, 'done.')
