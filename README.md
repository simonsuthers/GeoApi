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

<img src="/GeoApi/Pictures/Add%20startup%20file.png" width="50%">

Within the text file, add a reference to the app method within the app.py file:

<img src="/GeoApi/Pictures/startup%20file.png" width="50%">

See the following for more information on adding a startup file:

https://docs.microsoft.com/en-gb/azure/developer/python/tutorial-deploy-app-service-on-linux-04

### Deploy to Azure
See the following page for installing the Azure CLI for Windows:

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

Open Command Prompt and CD to the location of the solution:

Run the following command to publish the site to azure:
```
az webapp up -g <resource-group> -n <name-of-app> -l uksouth --sku FREE --subscription <my-subscription-id>
````
Run the following command to set the startup.txt file as a startup file:
```
az webapp config set -g <resource-group> -n <name-of-app> --startup-file startup.txt
```

### App App to Continuous Integration


