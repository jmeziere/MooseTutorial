from kivy.uix.screenmanager import Screen
import os
import subprocess
from kivy.lang import Builder

class Mint19(Screen):
    def install(self):
        password = self.ids.passw.text
        os.system("sh -c 'echo \"" + password +  "\" | sudo -Sv; sudo apt-get update; sudo apt-get install -y build-essential gfortran tcl git m4 freeglut3 doxygen libblas-dev liblapack-dev libx11-dev libnuma-dev libcurl4-gnutls-dev zlib1g-dev libhwloc-dev libxml2-dev libpng-dev pkg-config liblzma-dev; sudo apt install -y wget; cd ..; mkdir install; cd install; wget -c www.mooseframework.org/moose_packages/moose-environment_ubuntu-18.04_20191125_x86_64.deb?_ga=2.140379123.1980279153.1583519867-1085612855.1582900245; sudo dpkg -i moose-environment_ubuntu-18.04_20191125_x86_64.deb?_ga=2.140379123.1980279153.1583519867-1085612855.1582900245'")

    def install_too(self):
        password = self.ids.passw.text
        os.system("sh -c 'echo \"" + password + "\" | sudo -Sv; module load moose-dev-gcc'")

        try:
            subprocess.check_output("grep 'module load moose-dev-gcc' ~/.bashrc", shell = True)
        except subprocess.CalledProcessError as e:
            os.system("sh -c 'echo \"" + password + "\" | sudo -Sv; echo \"module load moose-dev-gcc\" >> ~/.bashrc'")

        os.system("mkdir ~/projects; cd ~/projects; git clone https://github.com/idaholab/moose.git; cd moose; git checkout master")

        os.system("cd ~/projects/moose; ./scripts/update_and_rebuild_libmesh.sh")

        os.system("cd ~/projects/moose/test; make -j 4; ./run_tests -j 4")

Builder.load_string("""
<Mint19>
    name: 'Mint19'
    id: 'Mint19'
    Label:
        text: "Login Password:"
        pos: 50,450
        size_hint: (.2,None)
        height: 50
    TextInput:
        password: True
        id: passw
        pos: 50,400
        size_hint: (.2, None)
        height: 50
        multiline: False
    Button:
        text: "Download MOOSE for Mint19"
        pos:50 , 300
        height: 30
        size_hint: (.2, None)
        on_release: root.install()
    Button:
        text: "Second Part of Installation"
        pos:50 , 250
        height: 30
        size_hint: (.2, None)
        on_release: root.install_too()
""", filename = "Mint19.kv")
