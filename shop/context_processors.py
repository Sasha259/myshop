from .models import Category 
from django.templatetags.static import static

EXTERNAL_CATEGORY_ICONS = {
    'electronics': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/cpu.svg',
    'accessories': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/watch.svg',
    'home': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/house.svg',
    'noutbuki': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/laptop.svg',
    'telefony': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/phone.svg',
    'kompyutry': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/pc-display-horizontal.svg',
    'sports': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/activity.svg',
    'books': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/book.svg',
    'auto': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/car-front.svg',
    'gaming': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/controller.svg',
    'office': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/icons/briefcase.svg',
}


def categories(request):
    cats = Category.objects.all()
    category_menu = []

    for c in cats:
        icon = EXTERNAL_CATEGORY_ICONS.get(c.slug) or static(f'img/categories/{c.slug}.svg')
        
        category_menu.append({
            'name': c.name,
            'slug': c.slug,
            'icon': icon,
            'url': c.get_absolute_url(),
        })

    POPULAR_SLUGS = ['noutbuki', 'office', 'electronics']

    popular_categories = [
        c for c in category_menu
        if c['slug'] in POPULAR_SLUGS]
    return {'categories': cats,
            'category_icons':  EXTERNAL_CATEGORY_ICONS,
            'category_menu': category_menu,
            'popular_categories': popular_categories}