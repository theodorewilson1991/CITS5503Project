**Preface**

The simplest method to predicting how many will turn up to vote is simple. You survey an individual and ask them. This is a common technique used by political scientists and data analysts. People who say they plan to vote are included in the survey and those who say they won’t vote are not. The issue with this question is that most potential voters say they plan to vote, and as has been shown recently this is simply untrue with the most recent US federal election having a voter turnout of only 45%. Therefore this system aims to use the Microsoft Azure cloud in order to determine a more accurate estimate of who pans to vote in an election.

**Operational Requirements**

This section is specifically for those who are aiming to just get the program running quickly.

* VTPS requires
   * Python (version 3.x or later), available from [http://www.python.org/](http://www.python.org/)
   * The PyQt 5 library which can be installed via the command line argument `pip3 install pyqt5`
   * The Vtps system can then be run from the active directory through the command line argument `python3 Vtps.py`

**Example Data**

The system comes premade with a sample set of data to upload into the Batch Request system.

**Purpose**

The purpose of the VTPS project is to create a tool for utilizing machine
learning to determine voter turnout in voluntary election as well as determining which party the voters that do turn up will vote for. The system utilizes two separate cloud services to enable this.

The software can interpret data from the following file formats:
* \*.csv   Comma-separated values

In the future the following data formats are planned to be implemented:
* \*.xml   Extensible Markup Language
* \*.yml   YAML Ain't Markup Language

**Requirements**

* To run the code, Python must be installed. VTPS is compatible with Python
versions 3.1 and 3.2 (cf. Python 3 compatibility).

VTPS requires the following package to effectively function. The VTPS may fail
to function if they are not installed:

* The Python Qt library, or PyQt5, is used to construct the graphic user
interface.

**Project Files & Directories**

* README.txt: This document.
* Vtps.py: Actual script. This script runs the main program.
* APISingle.py: This script contains all the function calls to the call-response MS Azure ML Studio.
* APIBatch.py: This script contains all the function calls to the batch execution of MS Azure ML Studio.
* Please ensure the correct API key is input into this script.

**Functional and Non-Functional Requirements**
* Functional Requirements
  * The solution must be responsive and fast enough to be able to process a high amount of voter information.
  * The solution should have two modes.
    * A single voter mode to determine the likelyhood of an individual to turn up and vote. This result should immediately present the output of the analysis
    * A multidata mode which can accept \*.csv files and return an output.
  * The system must perform with a suitable level of confidence and a low error rate.
  * The system should output the likelyhood of an individual turning up to vote.

* Non-Functional Requirements
  * System must be easy to deploy and allow use by the semi or non computer literate.
  * System must be simple to fix and modify to allow for maintenance or additions from other parties.
  * The GUI should provide a log of all system calls to determine the status of the calls
  * A suitable level of guarantees with regards to data safety and security must be met through the use of encryption and backups.

**Future Work**
* Improve analysis of the batch data processing including functionality with PowerBi to conduct statistical regression on the mean and standard deviation of the sample population.
* Improve the GUI functionality to enable improved process feedback from both GUI functions. All command line outputs should be displayed when the code is implemented.
* Add the final data points for the single call-response function. Over 40 questions are missing however they have been proven to contribute less to the overall mean probability of voting.

**Additional note for Prof Liu!!
The Microsoft Blob storage is being paid for out of my own pocket and the batch request functionality requires use of that storage. Because I'm a poor student I'll be taking it down at the start of December. If there are any issues feel free to call me.**

**References and Resources**
* The calls to the Azure API have been heavily modified from the sample code available at:  [https://services.azureml.net/workspaces](https://services.azureml.net/workspaces) (This requires an active Azure ML experiment setup).
* The calls to the PyQt5 library code were found using the PyQt5 documentation available at: [http://pyqt.sourceforge.net/Docs/PyQt5/](http://pyqt.sourceforge.net/Docs/PyQt5/)
* All other code was personally built from previous experience with PyQt5 and Python 3.x.
