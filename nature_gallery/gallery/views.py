from django.shortcuts import render

def gallery_view(request):
    images = [
        {
            'id': 1,
            'title': 'Misty Forest',
            'description': 'Tall pine trees draped in morning mist, sunlight filtering through the canopy.',
            'url': 'https://images.unsplash.com/photo-1448375240586-882707db888b?w=900&q=80',
            'category': 'Forest',
        },
        {
            'id': 2,
            'title': 'Mountain Lake',
            'description': 'A crystal-clear alpine lake reflecting snow-capped peaks at dawn.',
            'url': 'https://images.unsplash.com/photo-1439853949212-36589f9d8f43?w=900&q=80',
            'category': 'Mountains',
        },
        {
            'id': 3,
            'title': 'Ocean Sunset',
            'description': 'Golden waves washing over a quiet beach as the sun dips below the horizon.',
            'url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=900&q=80',
            'category': 'Ocean',
        },
        {
            'id': 4,
            'title': 'Wildflower Meadow',
            'description': 'A sweeping meadow bursting with colorful wildflowers under a bright blue sky.',
            'url': 'https://images.unsplash.com/photo-1490750967868-88df5691cc19?w=900&q=80',
            'category': 'Meadow',
        },
        {
            'id': 5,
            'title': 'Waterfall Cascade',
            'description': 'A powerful waterfall tumbling down mossy rocks deep in a lush rainforest.',
            'url': 'https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=900&q=80',
            'category': 'Waterfall',
        },
        {
            'id': 6,
            'title': 'Desert Dunes',
            'description': 'Sweeping sand dunes sculpted by wind, glowing warm under a blazing sun.',
            'url': 'https://images.unsplash.com/photo-1509316785289-025f5b846b35?w=900&q=80',
            'category': 'Desert',
        },
        {
            'id': 7,
            'title': 'Cherry Blossoms',
            'description': 'Delicate pink cherry blossoms in full bloom against a soft spring sky.',
            'url': 'https://images.unsplash.com/photo-1522383225653-ed111181a951?w=900&q=80',
            'category': 'Flowers',
        },
    ]
    return render(request, 'gallery/index.html', {'images': images})
