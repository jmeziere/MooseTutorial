from kivy.uix.screenmanager import Screen
import os
import subprocess


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

        os.system("cd ~/projects/moose; ./scripts/update_and_rebuild_libmesh.sh")

        os.system("cd ~/projects/moose/test; make -j 4; ./run_tests -j 4")
