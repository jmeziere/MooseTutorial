from kivy.uix.screenmanager import Screen
import os
import subprocess
from kivy.lang import Builder

class Fedora(Screen):
    def install(self):
        password = self.ids.passw.text
        os.system("sh -c 'echo \"" + password +  "\" | sudo -Sv; sudo dnf update; sudo -E dnf install -y cc gcc-c++ gcc-gfortran tcl tk findutils make freeglut-devel libXt-devel libX11-devel m4 blas-devel lapack-devel git xz-devel; sudo dnf install -y wget; cd ..; mkdir install; cd install; wget -c www.mooseframework.org/moose_packages/moose-environment_fedora-31_20191125_x86_64.rpm?_ga=2.109505677.9080527.1585322568-1085612855.1582900245; sudo rpm -i moose-environment_fedora-31_20191125_x86_64.rpm?_ga=2.109505677.9080527.1585322568-1085612855.1582900245'")

    def install_too(self):
        password = self.ids.passw.text
        os.system("sh -c 'echo \"" + password + "\" | sudo -Sv; module load moose-dev-gcc'")

        try:
            subprocess.check_output("grep 'module load moose-dev-gcc' ~/.bashrc", shell = True)
        except subprocess.CalledProcessError as e:
            os.system("sh -c 'echo \"" + password + "\" | sudo -Sv; echo \"module load moose-dev-gcc\" >> ~/.bashrc'")

        os.system("mkdir ~/projects; cd ~/projects; git clone https://github.com/idaholab/moose.git; cd moose; git checkout master")

        f = open("moosepath.txt", "w")
        f.write("~")
        f.close()

        try:
            subprocess.check_output("grep 'export PATH="+os.path.join(commonMethods.moosepath,projects/moose/python/peacock)+":$PATH' ~/.bashrc", shell = True)
        except subprocess.CalledProcessError as e:
            os.system("sh -c 'echo \"" + password + "\" | sudo -Sv; echo \"export PATH="+os.path.join(commonMethods.moosepath,projects/moose/python/peacock)+":$PATH\" >> ~/.bashrc'")

        os.system("cd ~/projects/moose; ./scripts/update_and_rebuild_libmesh.sh")

        os.system("cd ~/projects/moose/test; make -j 4; ./run_tests -j 4")

Builder.load_string("""
<Fedora>
    name: 'Fedora'
    id: 'Fedora'
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
        text: "Download MOOSE for Fedora"
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
""", filename = "Fedora.kv")
