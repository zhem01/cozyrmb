from django.shortcuts import render, redirect

def home(request):
    return render(request, 'catalog/home.html')

def customize(request):
    # Show the 3 main options to customize
    return render(request, 'catalog/customize.html')

def customize_detail(request, product):
    # Validate product type
    valid_products = ['puzzle', 'keychain', 'photobooth']
    if product.lower() not in valid_products:
        return redirect('customize')

    if request.method == 'POST':
        # Handle file uploads and order logic here (we can add later)
        pass

    return render(request, f'catalog/customize_{product.lower()}.html')
