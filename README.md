# GeoApi
Api for GIS operations

## Product
The final product can be found at:

https://propertymageoapi.azurewebsites.net/

## Create project
Project was created using the following tutorial to publish to github:

https://docs.microsoft.com/en-us/visualstudio/python/learn-flask-visual-studio-step-01-project-solution?view=vs-2019

Create the project in Viual Studio using the Flask template:
<img src="/GeoApi/Pictures/Create%20project.png" width="600">

### Add project to git
Add project to git using the Add to Source Control button in the bottom right of the screen:
<img src="/GeoApi/Pictures/Add%20project%20to%20git.png" width="600">

### Publish project to github
To add to github, click on the Team Explorer tab and click on the Publish to GitHub button.

<img src="/GeoApi/Pictures/Publish%20to%20github.png" width="35%">

## Deploying to Azure
### Add startup file for Azure
Add a text file to the route of the project:

<img src="/GeoApi/Pictures/Add%20startup%20file.png" width="35%">

Within the text file, add a reference to the app method within the app.py file:

<img src="/GeoApi/Pictures/startup%20file.png" width="60%">

See the following for more information on adding a startup file:

https://docs.microsoft.com/en-gb/azure/developer/python/tutorial-deploy-app-service-on-linux-04

### Deploy to Azure
See the following page for installing the Azure CLI for Windows:
* To see the Azure portal go to: https://portal.azure.com/

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

* Open Command Prompt and CD to the location of the solution:
* Run the following command to publish the site to azure:
```
az webapp up -g <resource-group> -n <name-of-app> -l uksouth --sku FREE --subscription <my-subscription-id>
````
* Run the following command to set the startup.txt file as a startup file:
```
az webapp config set -g <resource-group> -n <name-of-app> --startup-file startup.txt
```

### App App to Continuous Integration
The followoing exlplains how to add a Flask project to Azure DevOps CI:

https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops

Create an account on Azure DevOps first.
* Go to Azure Dev ops: https://dev.azure.com/
* Create a new project in Azure DevOps
* In the new project, go to project settings

<img src="/GeoApi/Pictures/CI-project%20settings.png" width="40%">

* Within projects settings, go to Service connections

<img src="/GeoApi/Pictures/CI-service%20connections.png" width="30%">

* Choose Azure Resource manager

<img src="/GeoApi/Pictures/CI-New%20service%20connection.png" width="50%">

* Choose Service Principal (Automatic)

<img src="/GeoApi/Pictures/CI-Service%20connection%20principal.png" width="40%">

* Set the service connection scope level

<img src="/GeoApi/Pictures/CI-service%20connection%20new%20scope.png" width="40%">

* Go back to the main project page and choose a new pipeline

<img src="/GeoApi/Pictures/New%20pipeline.png" width="40%">

* Select GitHub as the repository for the code

<img src="/GeoApi/Pictures/Code%20for%20pipeline.png" width="60%">

* Select the relevant GitHub repository

<img src="/GeoApi/Pictures/Select%20github%20repository.png" width="40%">

* Choose Python to Linux Web app on Azure as a pipeline template

<img src="/GeoApi/Pictures/Configure%20pipeline.png" width="60%">

* Choose the relevant web app name from the drop down list

<img src="/GeoApi/Pictures/web%20app%20name.png" width="40%">

* Review the created yaml

<img src="/GeoApi/Pictures/review%20yaml.png" width="40%">

* Change the root in the yaml so that it looks at the project, rather than the solution

<img src="/GeoApi/Pictures/yaml%20root.png" width="40%">

* Add startup file to yaml

<img src="/GeoApi/Pictures/yaml%20startup.png" width="40%">

* Run pipeline

<img src="/GeoApi/Pictures/run%20pipeline.png" width="40%">

