from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/2020-09-06_16_12_54_Several_Original_Pringles_in_the_Franklin_Farm_section_of_Oak_Hill%2C_Fairfax_County%2C_Virginia.jpg/1024px-2020-09-06_16_12_54_Several_Original_Pringles_in_the_Franklin_Farm_section_of_Oak_Hill%2C_Fairfax_County%2C_Virginia.jpg",
                "title": "Pringles",
                "description": "Once you pop, you can't stop.",
                "reference_url": "https://en.wikipedia.org/wiki/Pringles"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Cheez-It-Crackers.jpg/1024px-Cheez-It-Crackers.jpg",
                "title": "Cheez-Its",
                "description": "Cheez-It crackers are 26-by-24-millimetre (1.0 by 0.94 in) rectangles, though they are often believed to be squares. Cheez-It crackers are made with actual cheese, and are marketed by Kellogg's as such.",
                "reference_url": "https://en.wikipedia.org/wiki/Cheez-It"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/CheetosCrop.jpg/1024px-CheetosCrop.jpg",
                "title": "Cheetos",
                "description": "Cheetos are best eaten with chopsticks.",
                "reference_url": "https://en.wikipedia.org/wiki/Cheetos"
            },
        ]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'
