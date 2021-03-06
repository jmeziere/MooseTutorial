from kivy.uix.screenmanager import Screen
import os
import subprocess
from kivy.lang import Builder
import _thread

class Fedora(Screen):
    def install(self):
        os.system("sudo dnf update; sudo -E dnf install -y cc gcc-c++ gcc-gfortran tcl tk findutils make freeglut-devel libXt-devel libX11-devel m4 blas-devel lapack-devel git xz-devel; sudo dnf install -y wget; cd ..; mkdir install; cd install; wget -c www.mooseframework.org/moose_packages/moose-environment_fedora-31_20191125_x86_64.rpm?_ga=2.109505677.9080527.1585322568-1085612855.1582900245; sudo rpm -i moose-environment_fedora-31_20191125_x86_64.rpm?_ga=2.109505677.9080527.1585322568-1085612855.1582900245")

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
<Fedora>
    name: 'Fedora'
    id: 'Fedora'
    Label:
        text: "Login Password:"
        pos: 50,450
        size_hint: (.2,None)
        height: 50
    Button:
        text: "Download MOOSE for Fedora"
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
""", filename = "Fedora.kv")
