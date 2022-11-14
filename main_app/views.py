from django.shortcuts import render

finches = [ 
    {'name': 'Evening Grosbeak', 'habitat': 'Northern and Montane forests', 'threats': 'Deforestation'},
    {'name': 'Pine Grosbeak', 'habitat': 'Open boreal forest', 'threats': 'Possibly climate change'},
    {'name': 'Gray-crowned Rosy-Finch', 'habitat': 'Alpine tundra', 'threats': 'Climate change'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })