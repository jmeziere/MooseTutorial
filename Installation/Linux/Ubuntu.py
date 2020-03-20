from kivy.uix.screenmanager import Screen
import os

class Ubuntu(Screen):
    def install(self):
        password = self.ids.passw.text
        os.system("sh -c 'echo " + password +  " | sudo -Sv; sudo apt-get update; sudo apt-get install -y build-essential gfortran tcl git m4 freeglut3 doxygen libblas-dev liblapack-dev libx11-dev libnuma-dev libcurl4-gnutls-dev zlib1g-dev libhwloc-dev libxml2-dev libpng-dev pkg-config liblzma-dev; sudo apt install -y wget; cd ..; mkdir projects; cd projects; wget -c www.mooseframework.org/moose_packages/moose-environment_ubuntu-18.04_20191125_x86_64.deb?_ga=2.140379123.1980279153.1583519867-1085612855.1582900245; sudo dpkg -b moose-environment_ubuntu-18.04_20191125_x86_64.deb?_ga=2.140379123.1980279153.1583519867-1085612855.1582900245'")

        os.system("sh -c 'echo " + password + " | sudo -Sv; module load moose-dev-gcc'")

        os.system("sh -c 'echo " + password + " | sudo -Sv; echo \"module load moose-dev-gcc\" >> ~/.bashrc'")

        os.system("sh -c 'echo " + password + " | sudo -Sv; mkdir ~/projects; cd ~/projects; git clone https://github.com/idaholab/moose.git; cd moose; git checkout master'")

        os.system("sh -c 'echo " + password + " | sudo -Sv; cd ~/projects/moose; ./scripts/update_and_rebuild_libmesh.sh'")

        os.system("sh -c 'echo " + password + " | sudo -Sv; cd ~/projects/moose/test; make -j 4; ./run_tests -j 4'")
