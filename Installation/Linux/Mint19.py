from kivy.uix.screenmanager import Screen
import os
import subprocess
from kivy.lang import Builder
import _thread

class Mint19(Screen):
    def install(self):
        os.system("sudo apt-get update; sudo apt-get install -y build-essential gfortran tcl git m4 freeglut3 doxygen libblas-dev liblapack-dev libx11-dev libnuma-dev libcurl4-gnutls-dev zlib1g-dev libhwloc-dev libxml2-dev libpng-dev pkg-config liblzma-dev; sudo apt install -y wget; cd ..; mkdir install; cd install; wget -c www.mooseframework.org/moose_packages/moose-environment_ubuntu-18.04_20191125_x86_64.deb?_ga=2.140379123.1980279153.1583519867-1085612855.1582900245; sudo dpkg -i moose-environment_ubuntu-18.04_20191125_x86_64.deb?_ga=2.140379123.1980279153.1583519867-1085612855.1582900245")

    def install_too(self):
        os.system("sudo module load moose-dev-gcc")

        try:
            subprocess.check_output("grep 'module load moose-dev-gcc' ~/.bashrc", shell = True)
        except subprocess.CalledProcessError as e:
            os.system("sudo echo \"module load moose-dev-gcc\" >> ~/.bashrc")

        os.system("mkdir ~/projects; cd ~/projects; git clone https://github.com/idaholab/moose.git; cd moose; git checkout master")

        os.system("sudo rm -r moosepath.txt")
        os.system("sudo echo \"~\" > "+os.path.join(os.path.dirname(__file__),"moosepath.txt"))

        try:
            subprocess.check_output("grep 'export PATH="+os.path.join(commonMethods.moosepath,projects/moose/python/peacock)+":$PATH' ~/.bashrc", shell = True)
        except subprocess.CalledProcessError as e:
            os.system("sudo echo \"export PATH="+os.path.join(commonMethods.moosepath,projects/moose/python/peacock)+":$PATH\" >> ~/.bashrc")

        os.system("cd ~/projects/moose; ./scripts/update_and_rebuild_libmesh.sh")

        os.system("cd ~/projects/moose/test; make -j 4; ./run_tests -j 4")

Builder.load_string("""
#:import th _thread
<Mint19>
    name: 'Mint19'
    id: 'Mint19'
    Label:
        text: "Login Password:"
        pos: 50,450
        size_hint: (.2,None)
        height: 50
    Button:
        text: "Download MOOSE for Mint19"
        pos:50 , 300
        height: 30
        size_hint: (.2, None)
        on_release: th.start_new_thread(root.install,())
    Button:
        text: "Second Part of Installation"
        pos:50 , 250
        height: 30
        size_hint: (.2, None)
        on_release: th.start_new_thread(root.install_too,())
""", filename = "Mint19.kv")
