from django.test import SimpleTestCase, TransactionTestCase, TestCase
from django.urls import reverse
from app.models import Tag, Tutorial


class StaticPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_api_page_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_contribute_page_status_code(self):
        response = self.client.get('/contribute/')
        self.assertEquals(response.status_code, 200)


class DynamicPageTests(TransactionTestCase):

    def test_latest_page_status_code(self):
        response = self.client.get('/latest/')
        self.assertEquals(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)


class TestTemplateNames(TransactionTestCase):

    def test_home_page_name(self):
        response = self.client.get('/')
        self.assertTemplateUsed(template_name='home.html')

    def test_api_page_name(self):
        response = self.client.get('/api/')
        self.assertTemplateUsed(template_name='api.html')

    def test_about_page_name(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(template_name='about.html')

    def test_contribute_page_name(self):
        response = self.client.get('/contribute/')
        self.assertTemplateUsed(template_name='contribute.html')

    def test_latest_page_name(self):
        response = self.client.get('/latest/')
        self.assertTemplateUsed(template_name='latest.html')

    def test_tags_page_name(self):
        response = self.client.get('/tags/')
        self.assertTemplateUsed(template_name='tags.html')

def create_tag(name):
    t = Tag(name=name)
    t.save()
    return t.id

def create_tutorial(title,link,tag_pks,category, publish=True):
    tut = Tutorial.objects.create(
        title=title,
        link=link,
        category = category,
        publish = publish
    )
    tut.tags.add(*tag_pks)


class SearchQueryViewTests(TestCase):

    url = reverse('app:search-results')

    # def test_search_empty(self):
        
    #     response = self.client.get(self.url, data={
    #         "q": "hello"
    #     })
    #     # print(response.context)
    #     self.assertQuerysetEqual(response.context['tutorials'], [])

    # def test_simple_search(self):
    #     # crate our sample tags
    #     # save their ids for adding to the corresponding tutorial 
    #     tags = ['javascript', 'python']
    #     tag_pks = {t:create_tag(t) for t in tags}
        
    #     # create our sample tutorials
    #     tutorials= [{
    #         "title": "Python 101",
    #         "link": "https://www.python.org",
    #         "tags": ["python"],
    #         "category": "docs"
    #     },
    #     {
    #         "title": "Python Advanced",
    #         "link": "https://www.pyadv.com",
    #         "tags": ["python"],
    #         "category": "course"
    #     },
    #     {
    #         "title": "JavaScript 101",
    #         "link": "https://www.jsResource.com",
    #         "tags": ["javascript"],
    #         "category": "video"
    #     }
    #     ]
    #     for tut in tutorials:
    #         # compile a list of tag ids for this tut
    #         my_tags = [tag_pks[t] for t in tut['tags'] if t in tag_pks]
    #         create_tutorial(tut['title'], tut['link'], my_tags, tut['category'])
            
    #     res1 = self.client.get(self.url, data={"q": "python"})
    #     self.assertQuerysetEqual(res1.context['tutorials'], ['<Tutorial: Python 101>','<Tutorial: Python Advanced>', ])
        
    #     res2 = self.client.get(self.url, data={"q": "javascript"})
    #     self.assertQuerysetEqual(res2.context['tutorials'], ['<Tutorial: JavaScript 101>'])

    #     res3 = self.client.get(self.url, data={"q": "kotlin"})
    #     self.assertQuerysetEqual(res3.context['tutorials'], [])

    def test_search_relevance(self):
        """ full matches are placed before partial matches """
        tags = ['java', 'javascript', 'javaEE']
        tag_pks = {t:create_tag(t) for t in tags}

        tutorials = [
        {
            "title": "JavaScript 101",
            "link": "https://www.jsResource.io",
            "tags": ["javascript"],
            "category": "video"
        },
        {
            "title": "A Cup of Java",
            "link": "https://www.javaRef1.com",
            "tags": ["java"],
            "category": "course"
        },
        {
            "title": "Java Patterns",
            "link": "https://www.JVMBites.org",
            "tags": ["javaEE"],
            "category": "article"
        },
        {
            "title": "ObscureJSResource1",
            "link": "https://www.hasajstag.org",
            "tags": ["javascript"],
            "category": "docs"
        },
        {
            "title": "ObscureJVMResource1",
            "link": "https://www.hasajavatag.org",
            "tags": ["java"],
            "category": "book"
        },
        {
            "title": "JavaScript Fatigue",
            "link": "https://www.babelwebpack.org",
            "tags": ["javascript"],
            "category": "cheatsheet"
        },

        ]
        for tut in tutorials:
            # compile a list of tag ids for this tut
            my_tags = [tag_pks[t] for t in tut['tags'] if t in tag_pks]
            create_tutorial(tut['title'], tut['link'], my_tags, tut['category'])
        
        res1 = self.client.get(self.url, data={"q": "javascript"})
        self.assertQuerysetEqual(res1.context['tutorials'], [
            '<Tutorial: JavaScript 101>',
            '<Tutorial: JavaScript Fatigue>',
            '<Tutorial: ObscureJSResource1>'
             ])
        
        res2 = self.client.get(self.url, data={"q": "java"})
        first_page = res2.context['tutorials']
        paginator = first_page.paginator
        print(f"paginator's list is {paginator.object_list}")
        self.assertQuerysetEqual(paginator.object_list, [
            '<Tutorial: A Cup of Java>',
            '<Tutorial: Java Patterns>',
            '<Tutorial: ObscureJVMResource1>',
            '<Tutorial: JavaScript 101>',
            '<Tutorial: JavaScript Fatigue>'
             ])

        # res3 = self.client.get(self.url, data={"q": "kotlin"})
        # self.assertQuerysetEqual(res3.context['tutorials'], [])
