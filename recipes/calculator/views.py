from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def cook_omlet(request):
    portions = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'яйца, шт': 2 * portions,
            'молоко, л': 0.1 * portions,
            'соль, ч.л.': 0.5 * portions
        },
    }
    return render(request, 'calculator/index.html', context)


def cook_pasta(request):
    portions = int(request.GET.get("servings", 1))
    context = {
        'recipe_2': {
            'макароны, г': 0.3 * portions,
            'сыр, г': 0.05 * portions,
        },
    }
    return render(request, 'calculator/index_2.html', context)