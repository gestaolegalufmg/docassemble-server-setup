import subprocess
import pathlib
import os
from util_scripts.basic_setup import install_basic_packages, install_docker_compose

install_basic_packages()
install_docker_compose()

import click
from mako.template import Template

print("Geração do docker-compose")
domain = click.prompt("Digite o domínio completo do servidor cadastrado no registro.br (e.g. docassemble.my_domain.br)")
server_admin_mail = click.prompt("Digite o e-mail do administrador do sistema")

docker_compose_template = Template(filename="docassemble_generator_server/docker-compose-template")
docker_compose_file = docker_compose_template.render(domain=domain)
f = open("docassemble_generator_server/docker-compose.yml", "w+")
f.write(docker_compose_file)
f.close()
print("O docker-compose foi gerado com sucesso!")

env_template = Template(filename="docassemble_generator_server/env-template")
env_file = env_template.render(domain=domain, server_admin_mail=server_admin_mail)
g = open("docassemble_generator_server/.env", "w+")
g.write(env_file)
g.close()
print("O .env foi gerado com sucesso!")
current_directory = os.getcwd()
os.chdir(os.path.join(current_directory, "docassemble_generator_server"))
subprocess.run(["make", "run"])