# TORCS-Self-Driving-Agent
## Pre-requisite
Anaconda python installed. In case anaconda is not installed, follow [Anaconda Installation](https://www.anaconda.com/products/individual) and install anaconda.
## How to run trained TORCS agent
1) Clone the repository and import the environment by running `conda env create -f torcs.yml`. 
2) Activate the enviornment i.e. `conda activate torcs_env`. 
3) Client.py is the file which tries to connect with the server. Run client.py and make sure no error comes.
### How to run the server
1) torcs_server is the folder which is required for running the server. This server was downloaded from an open source github repository. The exe file named `wtorcs.exe` is the main server file which will be used to listen from client. Run `wtorcs.exe` file in `torcs_server` folder and then click on `Race`. 
2) It will show multiple types of races. The one normally used for testing is `Quick race` and clicking it will show the option of `New Race` and `Configure Race`.
3) First we need to configure the players therefore click on `Configure Race`. Choose the track and then click `Accept`. 
4) There should be one server named `scr_server 1` in `selected` or `Not selected` tab. This is the client name which will be run therefore make sure to select the `scr_server 1`.
5) Other cars can be added to see the performance of the agents in presence of other agents. 
6) Click on accept and then `Quick Race Options` will pop up. Set the options according to the requirements and click on `Accept`. 
7) Then Click on `New Race` and enjoy seeing the agent race ;-)

### Demo


https://user-images.githubusercontent.com/30326715/152202752-b45045f5-a85b-45b8-8c18-a477e4f7da90.mp4

