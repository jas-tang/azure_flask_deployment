# azure_flask_deployment
# Website URL: jastang504-flask.azurewebsites.net
## Instructions
---
### Create a basic flask app structure 

* base

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Healthcare App</title>
    
    <!-- Tailwind CSS via CDN -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>

<body class="bg-gray-200">

    <header class="bg-blue-600 text-white p-4">
        <h1 class="text-2xl">Welcome to My Healthcare App</h1>
        <nav>
            <ul class="flex space-x-4">
                <li><a href="/" class="hover:underline">Home</a></li>
                <li><a href="/about" class="hover:underline">About</a></li>
                <li><a href="/data" class="hover:underline">Data</a></li>
            </ul>
        </nav>
    </header>

    <main class="p-4">

        {% block content %}{% endblock %}

    </main>

    <footer class="bg-blue-600 text-white p-4 mt-6">
        <p>© 2023 My Healthcare App. All Rights Reserved.</p>
    </footer>
</body>

</html>
```

* About

```
{% extends "base.html" %} 

{% block content %}

    <section class="mb-6">
        <h2 class="text-xl mb-2">About</h2>
        <p>This is a healthcare application designed to manage patient data efficiently and securely.</p>
    </section>

    <section>
        <h2 class="text-xl mb-2">Features</h2>
        <ul class="list-disc pl-5">
            <li>Secure patient data management</li>
            <li>Easy appointment scheduling</li>
            <li>Interactive dashboards for health metrics</li>
        </ul>
    </section>



{% endblock %}

```

* Data
```
{% extends "base.html" %} 

{% block content %}

    <section>
        <h2 class="text-xl mb-2"> Dataset preview using a TABLE in HTML</h2>
        <table class="table-auto">
            <thead>
                <tr>
                    <th class="px-4 py-2">HospCode</th>
                    <th class="px-4 py-2">Code</th>
                    <th class="px-4 py-2">Description</th>
                </tr>
            </thead>
            <tbody>
                {% for data in data.values %}
                <tr>
                    <td class="border px-4 py-2">{{ data[0] }}</td>
                    <td class="border px-4 py-2">{{ data[1] }}</td>
                    <td class="border px-4 py-2">{{ data[2] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>

{% endblock %}
```
* Random 
```
{% extends "base.html" %} 

{% block content %}

    <section class="mb-6">
        <h2 class="text-xl mb-2">Random number</h2>
        <p>Generated here: </p>
        <p> {{ single_number }}</p>
    

        <h2 class="text-xl mb-2">Random Address</h2>
        <p>Generated here: </p>
        <p> {{ single_address }}</p>
    </section>


{% endblock %}
```
* Include a requirements.txt file
```
faker
pandas
flask
```
---
### Deploying the Azure Web App
Install Azure CLI by pasting the following script into the shell
```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

Test if the install worked correct with the following code
```
az
```

Give permission to the shell with a Microsoft account
```
az login --use-device-code
```

Locate all subscription IDs within the shell
```
az account list --output table
```

Change the subscription approrpiate name. For my case, it was Azure for Students.

```
az account set --subscription (insert the subscription ID here)
```

Create a new resource group within the Azure Web Portal. It is located in the Resource Group tab. Ensure that the new group has its subscription set to the working subscription name. For my case, it was Azure for Students. 

Create the web app and connect it to Microsoft Azure with the following code.
```
az webapp up --resource-group (insert group name) --name (insert your app name) --runtime <(Insert language)> --sku <(insert service plan)>
az webapp up --resource-group Jason504 --name jastang504-flask --runtime <Python> --sku <b1>
```

The application should now be deployed. Access your application via Microsoft Azure's App Services tab. 

In the case that you need to redeploy the app, use the following code
```
az webapp up
```

Here is how you delete the app
```
az webapp delete --name (insert app name) --resource-group (insert resource group)
```
