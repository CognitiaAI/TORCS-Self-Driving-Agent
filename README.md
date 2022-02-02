# TORCS-Self-Driving-Agent
## Pre-requisite
Anaconda python installed. In case anaconda is not installed, follow [Anaconda Installation](https://www.anaconda.com/products/individual) and install anaconda.
## How to run developed TORCS agent
Clone the repository and import the environment by running `conda env create -f torcs.yml`. After successfully importing the environment, activate the enviornment i.e. `conda activate torcs_env`. Client.py is the file which tries to connect with the server. Run client.py and make sure no error comes.
### How to run the server
torcs_server is the folder which is required for running the server. This server was downloaded from an open source github repository. The exe file named `wtorcs.exe` is the main server file which will be used to listen from client. Run `wtorcs.exe` file in `torcs_server` folder and then click on `Race`. It will show multiple types of races. The one normally used for testing is `Quick race` and clicking it will show the option of `New Race` and `Configure Race`. First we need to configure the players therefore click on `Configure Race`. Choose the track and then click `Accept`. There should be one server named `scr_server 1` in `selected` or `Not selected` tab. This is the client name which will be run therefore make sure to select the `scr_server 1`. Other cars can be added to see the performance of the agents in presence of other agents. Click on accept and then `Quick Race Options` will pop up. Set the options according to the requirements and click on `Accept`. Then Click on `New Race` and enjoy seeing the agent race ;-)

### Demo


https://user-images.githubusercontent.com/30326715/152202752-b45045f5-a85b-45b8-8c18-a477e4f7da90.mp4

