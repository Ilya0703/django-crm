from django.shortcuts import render, redirect
from .models import Applications, Client, Product, Workers, Sales


def index(request):
    return render(request, "main.html")


def applicationsView(request):
    applications = Applications.objects.all()
    products = Product.objects.all()

    context = {"applications": applications,
               "products": products}
    if request.method == "POST":
        applicationId = request.POST.get("application_id")
        action = request.POST.get("action")

        if applicationId and action:
            application = Applications.objects.get(id=applicationId)

            if action == "close":
                application.status = "Закрыта"
                application.save()
                sale = Sales()
                sale.client = application.client
                sale.product = application.product
                sale.price = application.price
                sale.save()
                return redirect("applications")
            elif action == "cancel":
                application.status = "Отменена"
                application.save()
                return redirect("applications")
            elif action == "delete":
                application.delete()
                return redirect("applications")

    return render(request, "applications.html", context)


def clientsView(request):
    clients = Client.objects.all()
    context = {"clients": clients}
    return render(request, "clients.html", context)


def productsView(request):
    products = Product.objects.all()
    context = {"products": products}

    if request.method == "POST":
        productId = request.POST.get("product_id")
        action = request.POST.get("action")

        if productId and action:
            product = Product.objects.get(id=productId)
            if action == "delete":
                product.delete()
                return redirect("products")
    return render(request, "products.html", context)


def salesView(request):
    sales = Sales.objects.all()
    context = {"sales": sales}
    if request.method == "POST":
        saleId = request.POST.get("sale_id")
        action = request.POST.get("action")

        if saleId and action:
            sale = Sales.objects.get(id=saleId)

            if action == "close":
                sale.isReady = True
                sale.save()
                return redirect("sales")
            elif action == "delete":
                sale.delete()
                return redirect("sales")
    return render(request, "sales.html", context)


def workersView(request):
    workers = Workers.objects.all()
    context = {"workers": workers}
    if request.method == 'POST':
        workerId = request.POST.get("worker_id")
        action = request.POST.get("action")

        if workerId and action:
            worker = Workers.objects.get(id=workerId)
            if action == "delete":
                worker.delete()
                return redirect("workers")
    return render(request, "workers.html", context)


def applicationsReportsView(request):
    statusData = Applications.objects.values_list("status", flat=True).order_by("status").distinct()
    statusCount = [Applications.objects.filter(status=status).count() for status in statusData]

    priceData = Applications.objects.values_list("price", flat=True)

    context = {
        "statusChartData": [
            ["Статус", "Количество"],
            *[[status, count] for status, count in zip(statusData, statusCount)]
        ],
        "priceChartData": [
            ["Цена", "Количество"],
            *[[price, Applications.objects.filter(price=price).count()] for price in priceData.distinct()]
        ],
    }
    return render(request, "applications_report.html", context)


def salesReportsView(request):
    statusData = Sales.objects.values_list("isReady", flat=True).order_by("isReady").distinct()
    statusData = [str(status) for status in statusData]
    statusCount = [Sales.objects.filter(isReady=isReady).count() for isReady in statusData]

    priceData = Sales.objects.values_list("price", flat=True)

    context = {
        "statusChartData": [
            ["Статус", "Количество"],
            *[[status, count] for status, count in zip(statusData, statusCount)]
        ],
        "priceChartData": [
            ["Цена", "Количество"],
            *[[price, Sales.objects.filter(price=price).count()] for price in priceData.distinct()]
        ],
    }
    return render(request, "sales_report.html", context)


def clientsReportsView(request):
    cityData = Client.objects.values_list("city", flat=True).order_by("city").distinct()
    cityCount = [Client.objects.filter(city=city).count() for city in cityData]

    context = {
        "cityChartData": [
            ["Статус", "Количество"],
            *[[city, count] for city, count in zip(cityData, cityCount)]
        ]
    }
    return render(request, 'clients_report.html', context)


def productsReportView(request):
    productsValues = Product.objects.values_list("name", flat=True).order_by("id").distinct()

    productDataSales = \
        Sales.objects.values_list("product", flat=True).order_by("product").distinct()
    productCountSales = \
        [Sales.objects.filter(product=product).count() for product in productDataSales]

    productDataApplications = \
        Applications.objects.values_list("product", flat=True).order_by("product").distinct()
    productCountApplications = \
        [Applications.objects.filter(product=product).count() for product in productDataApplications]

    context = {
        "productSalesChartData": [
            ["Продукт", "Количество"],
            *[[name, count] for name, count in zip(
                productsValues, productCountSales)]
        ],
        "productApplicationsChartData": [
            ["Продукт", "Количество"],
            *[[name, count] for name, count in zip(
                productsValues, productCountApplications)]
        ],
    }
    return render(request, "products_report.html", context)


def createApplication(request):
    if request.method == "POST":
        clientName = request.POST.get("client_name")
        clientTel = request.POST.get("client_tel")
        clientEmail = request.POST.get("client_email")
        clientCity = request.POST.get("client_city")
        productId = request.POST.get("product")
        price = request.POST.get("price")

        client, _ = Client.objects.get_or_create(
            name=clientName,
            tel=clientTel,
            email=clientEmail,
            city=clientCity
        )

        product = Product.objects.get(id=productId)

        application = Applications.objects.create(
            client=client,
            product=product,
            price=price,
            status="Активна"
        )
        application.save()
    return redirect("applications")


def createProduct(request):
    if request.method == "POST":
        productName = request.POST.get("product_name")
        product = Product()
        product.name = productName
        product.save()
    return redirect("products")


def createWorker(request):
    if request.method == "POST":
        worker = Workers()
        worker.name = request.POST.get("worker_name")
        worker.tel = request.POST.get("worker_tel")
        worker.email = request.POST.get("worker_email")
        worker.jobTitle = request.POST.get("worker_job_title")
        worker.salary = request.POST.get("worker_salary")
        worker.save()
    return redirect("workers")
